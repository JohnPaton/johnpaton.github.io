title: Groupby without aggregation in Pandas
slug: groupby-without-aggregation
date: 2017-07-17 20:00:00 UTC+01:00
tags: python, pandas, data, time series
category: 
cover:
description:
type: text
author: John Paton
summary: Pandas has a useful feature that I didn't appreciate enough when I first started using it: `groupby`s without aggregation. What do I mean by that? Let's look at an example.


Pandas has a useful feature that I didn't appreciate enough when I first started using it: `groupby`s without aggregation. What do I mean by that? Let's look at an example.

We'll borrow the data structure from my previous post about [counting the periods since an event](https://johnpaton.github.io/posts/periods-since-time-series-events/): company accident data. We have a list of workplace accidents for some company since 1980, including the time and location of the accident (no it's not real, I generated it, please don't send your lawyers to investigate a data breach): 


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```



```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>location</th>
      <th>severity</th>
    </tr>
    <tr>
      <th>time</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980-02-28 22:05:39</th>
      <td>Birmingham</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1980-03-01 02:12:20</th>
      <td>Birmingham</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1980-03-07 07:30:30</th>
      <td>Amsterdam</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1980-05-15 03:23:01</th>
      <td>Amsterdam</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1980-05-29 21:21:39</th>
      <td>Birmingham</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



Say we want to add the total number of accidents at each location as a column in the dataset. We could start off by doing a regular `groupby` to get the total number of accidents per location:


```python
gb = df.groupby('location').count()
gb
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>severity</th>
    </tr>
    <tr>
      <th>location</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Amsterdam</th>
      <td>129</td>
    </tr>
    <tr>
      <th>Birmingham</th>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>



But now we have to separately add this information to the dataframe.

Instead, we have the option to directly operate on the whole group:


```python
def accident_count(group):
    c = group['severity'].count()
    group['num_accidents'] = c
    
    return group

df = df.groupby('location').apply(accident_count)
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>location</th>
      <th>severity</th>
      <th>num_accidents</th>
    </tr>
    <tr>
      <th>time</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980-02-28 22:05:39</th>
      <td>Birmingham</td>
      <td>1</td>
      <td>121</td>
    </tr>
    <tr>
      <th>1980-03-01 02:12:20</th>
      <td>Birmingham</td>
      <td>3</td>
      <td>121</td>
    </tr>
    <tr>
      <th>1980-03-07 07:30:30</th>
      <td>Amsterdam</td>
      <td>1</td>
      <td>129</td>
    </tr>
    <tr>
      <th>1980-05-15 03:23:01</th>
      <td>Amsterdam</td>
      <td>1</td>
      <td>129</td>
    </tr>
    <tr>
      <th>1980-05-29 21:21:39</th>
      <td>Birmingham</td>
      <td>1</td>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>



Now, in this simple case we could have just performed a left join. However, this kind of `groupby` becomes especially handy when you have more complex operations you want to do within the group, without interference from other groups.

As a more complex example, consider calculating the time between accidents at each location. Our dataframe is already sorted by accident time, so all we have to do is make a series out of the group's index (`time`) and take the difference between the rows to get the time differences between incidents. We insert this information directly into the group as a new column and return it:


```python
def time_difference(group):
    # get the time differences and put them directly into the group
    group['time_since_previous'] = group.index.to_series().diff()

    return group

df.groupby('location').apply(time_difference).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>location</th>
      <th>severity</th>
      <th>num_accidents</th>
      <th>time_since_previous</th>
    </tr>
    <tr>
      <th>time</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980-02-28 22:05:39</th>
      <td>Birmingham</td>
      <td>1</td>
      <td>121</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>1980-03-01 02:12:20</th>
      <td>Birmingham</td>
      <td>3</td>
      <td>121</td>
      <td>1 days 04:06:41</td>
    </tr>
    <tr>
      <th>1980-03-07 07:30:30</th>
      <td>Amsterdam</td>
      <td>1</td>
      <td>129</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>1980-05-15 03:23:01</th>
      <td>Amsterdam</td>
      <td>1</td>
      <td>129</td>
      <td>68 days 19:52:31</td>
    </tr>
    <tr>
      <th>1980-05-29 21:21:39</th>
      <td>Birmingham</td>
      <td>1</td>
      <td>121</td>
      <td>89 days 19:09:19</td>
    </tr>
  </tbody>
</table>
</div>



We see that our dataframe maintains its original structure, but we now have information about each location that was calculated using only other datapoints from that location.
