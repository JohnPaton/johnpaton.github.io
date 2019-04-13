title: Propagate time series events with Pandas merge_asof
slug: propagate-time-series-events-pandas
date: 2019-04-13 16:00:00 UTC+01:00
tags: python, data, time series, pandas
category: 
link: 
status:
description:
type: text
author: John Paton
summary: I recently discovered that Pandas has a function to propagate time series events forward (or backward) in time across a DataFrame. Here's how it works.
Imagine the following situation: you have two tables, one with event logs, and the other with status changes. To make this concrete, let's take our events to be purchases by our users, and the status changes to be when the users attained a Gold Membership (wow so shiny). You want to use their membership status _at the time of each purchase_ as a feature for some model, but you only have records of when the status _changed_, so you can't just naively join the tables.

After inheriting some code that was performing this operation manually using `groupby`'s and fancy indexing, I decided to check if Pandas had a built in function for it, and I was pleasantly surprised: [`pandas.merge_asof`](https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.merge_asof.html). Let's check out how it works.


```python
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# https://johnpaton.net/posts/custom-color-schemes-in-matplotlib/
plt.style.use('~/johnpaton.mplstyle')
```

We'll begin by generating some fake sales data. We have three users, Alice, Bob, and Charlie, who made purchases over the last year. Sorry about the verbosity, there doesn't seem to be any easier way to generate random dates in a range. 


```python
n_rows = 15
epoch = datetime.utcfromtimestamp(0)
end = (datetime.now() - epoch).days
start = (datetime.now() - timedelta(days=365) - epoch).days

users = ['alice','bob','charlie']
df_sales = pd.DataFrame(data={
    'timestamp': pd.to_datetime(np.random.randint(start, end, n_rows), unit='D'),
    'user': np.random.choice(users, n_rows),
    'amount': np.random.randint(0,100, n_rows)
}).sort_values('timestamp').reset_index(drop=True)
df_sales
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>user</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-04-14</td>
      <td>charlie</td>
      <td>74</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-05-02</td>
      <td>alice</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-05-17</td>
      <td>charlie</td>
      <td>85</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-06-25</td>
      <td>bob</td>
      <td>71</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-06-30</td>
      <td>alice</td>
      <td>50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018-07-04</td>
      <td>charlie</td>
      <td>40</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018-09-22</td>
      <td>bob</td>
      <td>64</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018-11-02</td>
      <td>alice</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018-11-18</td>
      <td>bob</td>
      <td>57</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018-11-21</td>
      <td>alice</td>
      <td>37</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018-11-27</td>
      <td>charlie</td>
      <td>42</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2019-01-19</td>
      <td>alice</td>
      <td>29</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2019-01-22</td>
      <td>alice</td>
      <td>46</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2019-03-17</td>
      <td>bob</td>
      <td>11</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2019-04-02</td>
      <td>alice</td>
      <td>77</td>
    </tr>
  </tbody>
</table>
</div>



Next up, we need the records of when each of them attained their coveted Gold Membership:


```python
df_flags = pd.DataFrame(data={
    'user': users,
    'timestamp': pd.to_datetime(np.random.randint(start, end, len(users)), unit='D'),
    'status': 'gold_member'
}).sort_values('timestamp').reset_index(drop=True)
df_flags
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>timestamp</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>charlie</td>
      <td>2018-04-18</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bob</td>
      <td>2018-06-09</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>2</th>
      <td>alice</td>
      <td>2018-09-24</td>
      <td>gold_member</td>
    </tr>
  </tbody>
</table>
</div>



Now it's time to do our merge. We call `pd.merge_asof`, specifying the following arguments:

* The `left` and `right` DataFrames
* The column to merge `on` (this is generally a time column or some other ordering field)
* The column(s) to group `by`. The `by` keyword is very nice, as we can use it to make sure that the status changes only get propagated across the correct users' purchases. Otherwise we would have to ensure this manually.


```python
df_merged = pd.merge_asof(
    df_sales,
    df_flags,
    on='timestamp',
    by='user',
)
df_merged
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>user</th>
      <th>amount</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-04-14</td>
      <td>charlie</td>
      <td>74</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-05-02</td>
      <td>alice</td>
      <td>61</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-05-17</td>
      <td>charlie</td>
      <td>85</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-06-25</td>
      <td>bob</td>
      <td>71</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-06-30</td>
      <td>alice</td>
      <td>50</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018-07-04</td>
      <td>charlie</td>
      <td>40</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018-09-22</td>
      <td>bob</td>
      <td>64</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018-11-02</td>
      <td>alice</td>
      <td>7</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018-11-18</td>
      <td>bob</td>
      <td>57</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018-11-21</td>
      <td>alice</td>
      <td>37</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018-11-27</td>
      <td>charlie</td>
      <td>42</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2019-01-19</td>
      <td>alice</td>
      <td>29</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2019-01-22</td>
      <td>alice</td>
      <td>46</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2019-03-17</td>
      <td>bob</td>
      <td>11</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2019-04-02</td>
      <td>alice</td>
      <td>77</td>
      <td>gold_member</td>
    </tr>
  </tbody>
</table>
</div>



The result is kind of like a left join, in that all "matching" rows are filled and unmatched rows are `NaN`. However, unlike in a left join (which looks for an exact match), in this the join applied to case all rows on the left that have a `timestamp` that comes _after_ the paired rows on the right. To ensure that this before/after comparison is possible, the DataFrames must be sorted by the `on` column.

To create our Gold Membership flag, all we do is just replace the name of the event with a `1` and fill the `NaN`s (which are rows that came before the status change) with `0`s.


```python
df_merged['gold_member'] = df_merged['status']\
    .replace('gold_member', 1)\
    .fillna(0)\
    .astype(int)
df_merged
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>user</th>
      <th>amount</th>
      <th>status</th>
      <th>gold_member</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-04-14</td>
      <td>charlie</td>
      <td>74</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-05-02</td>
      <td>alice</td>
      <td>61</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-05-17</td>
      <td>charlie</td>
      <td>85</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-06-25</td>
      <td>bob</td>
      <td>71</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-06-30</td>
      <td>alice</td>
      <td>50</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018-07-04</td>
      <td>charlie</td>
      <td>40</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018-09-22</td>
      <td>bob</td>
      <td>64</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018-11-02</td>
      <td>alice</td>
      <td>7</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018-11-18</td>
      <td>bob</td>
      <td>57</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018-11-21</td>
      <td>alice</td>
      <td>37</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018-11-27</td>
      <td>charlie</td>
      <td>42</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2019-01-19</td>
      <td>alice</td>
      <td>29</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2019-01-22</td>
      <td>alice</td>
      <td>46</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2019-03-17</td>
      <td>bob</td>
      <td>11</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2019-04-02</td>
      <td>alice</td>
      <td>77</td>
      <td>gold_member</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



To make sure there's no funny business going on, we can also visualize exactly what happened:


```python
fig, ax = plt.subplots(facecolor='white', figsize=(12,5))
for user in users:
    df_tmp = df_merged[df_merged['user'] == user]
    plt.scatter(df_tmp['timestamp'], df_tmp['gold_member'], label=user)
    
for i,row in df_flags.sort_values('user').reset_index().iterrows():
    plt.axvline(row['timestamp'], c=f'C{i}')
    plt.annotate(
        f" {row['user']} gets gold", (row['timestamp'], np.random.uniform(0.25,0.75))
    )
plt.yticks([0,1], ['regular', 'gold'])
plt.ylabel('Membership status')
plt.xlabel('Sale date')
plt.title('Sales by membership status')
plt.legend();
```

![png](/images/propagate_12_1.png)


So now we have a nice feature that can be used in a training set, without any data leakage (no events from the future are visible before they happened in the training set).

This also works for multiple status changes. For example, say Bob got demoted on February 1st back to being a normal user.


```python
df_flags = pd.concat([
    df_flags,
    pd.DataFrame(data={
        'user': ['bob'],
        'status': 'normal',
        'timestamp': pd.to_datetime('2019-02-01')
    })
])
df_flags
```



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>status</th>
      <th>timestamp</th>
      <th>user</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>gold_member</td>
      <td>2018-04-18</td>
      <td>charlie</td>
    </tr>
    <tr>
      <th>1</th>
      <td>gold_member</td>
      <td>2018-06-09</td>
      <td>bob</td>
    </tr>
    <tr>
      <th>2</th>
      <td>gold_member</td>
      <td>2018-09-24</td>
      <td>alice</td>
    </tr>
    <tr>
      <th>0</th>
      <td>normal</td>
      <td>2019-02-01</td>
      <td>bob</td>
    </tr>
  </tbody>
</table>
</div>



If we perform the `merge_asof` again, we see that Bob's status changes twice, just how we would expect:


```python
pd.merge_asof(
    df_sales,
    df_flags,
    on='timestamp',
    by='user',
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>user</th>
      <th>amount</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-04-14</td>
      <td>charlie</td>
      <td>74</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-05-02</td>
      <td>alice</td>
      <td>61</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-05-17</td>
      <td>charlie</td>
      <td>85</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-06-25</td>
      <td>bob</td>
      <td>71</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-06-30</td>
      <td>alice</td>
      <td>50</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018-07-04</td>
      <td>charlie</td>
      <td>40</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018-09-22</td>
      <td>bob</td>
      <td>64</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018-11-02</td>
      <td>alice</td>
      <td>7</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018-11-18</td>
      <td>bob</td>
      <td>57</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018-11-21</td>
      <td>alice</td>
      <td>37</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018-11-27</td>
      <td>charlie</td>
      <td>42</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2019-01-19</td>
      <td>alice</td>
      <td>29</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2019-01-22</td>
      <td>alice</td>
      <td>46</td>
      <td>gold_member</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2019-03-17</td>
      <td>bob</td>
      <td>11</td>
      <td>normal</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2019-04-02</td>
      <td>alice</td>
      <td>77</td>
      <td>gold_member</td>
    </tr>
  </tbody>
</table>
</div>



Finally, these have all been examples of so-called "backwards searches". From the [Pandas docs](https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.merge_asof.html): 
> A "backward" search selects the last row in the right DataFrame whose `on` key is less than or equal to the left's key.

Somewhat counter-intuitively, this causes the status changes to propagate _forward_ in time. This is the default behavior of `merge_asof`. To do the reverse (a _forward_ search, a.k.a. propagate changes _backwards_ in time), you can provide the keyword argument `direction="forward"`. 
