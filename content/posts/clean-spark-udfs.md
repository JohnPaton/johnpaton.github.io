title: Cleaner Spark UDF definitions with a little decorator
slug: clean-spark-udfs
date: 2017-11-16 19:48:11 UTC+01:00
tags: spark, python, data, snippets
category: 
link: 
status:
description:
type: text
author: John Paton
summary: One of the handy features that makes (Py)Spark more flexible than database tools like Hive even for just transforming tabular data is the ease of creating User Defined Functions (UDFs). However, one thing that still remains a little annoying is that you have to separately define a function and declare it as a UDF. With four lines of code you can clean those definitions right up.

Alternate title: *Clean up your Spark jobs with this one weird trick! Apache will hate you!*

One of the handy features that makes (Py)Spark more flexible than database tools like Hive even for just transforming tabular data is the ease of creating User Defined Functions (UDFs). Although this is [also possible in Hive directly](https://community.hortonworks.com/articles/72414/how-to-create-a-custom-udf-for-hive-using-python.html), the ability to define and call UDFs directly in the Python code of your job makes life a lot easier and provides context to what you're doing. However, one thing that still remains a little annoying is separately defining a Python function and then having to declare it as a Spark UDF.

Consider the trivial example of incrementing all the values in a Spark DataFrame column by 1. We begin by writing the function, and then make a "UDF-ified" version that we can actually use in Spark.

```python
import pyspark.sql.functions as f

# define the function
def increment(x):
    return x + 1

# make the udf version
increment_udf = f.udf(increment)
```

By registering our function as a UDF, we tell Spark that this function should be applied to every value in whatever DataFrame column it is applied to, and Spark takes care of distributing the execution across the cluster when we submit our job. We can now use our newly declared `increment_udf` to increment all the values in a column:

```python
# increment column 'col' by 1
df = df.withColumn('col_plus_1', increment_udf('col'))
```

"Hold up," you say, "you're making it unnecessarily difficult for yourself. Just use the `f.udf` as a [decorator](https://www.python.org/dev/peps/pep-0318/)!" That is indeed an attractive option. The code then condenses to:

```python
@f.udf
def increment(x):
    return x + 1

df = df.withColumn('col_plus_1', increment('col'))
```

This is a lot better looking, but it comes at the cost of flexibility. The function `f.udf` optionally takes as a second argument the type of the UDF's output (in terms of the `pyspark.sql.types` [types](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.types)). Spark will by default convert UDF outputs to strings, which can be a hassle, especially for complex data types (like arrays), or when the precision is important (float vs. double). To avoid this stringy fate, we have to return to our old pattern:

```python
import pyspark.sql.types as t

# define the function
def increment(x):
    return x + 1

# make a typed udf version
increment_udf = f.udf(increment, t.IntegerType())
```

To get back to our nice, clean decorator syntax, we can write a tiny but useful function to generate a UDF decorator that will cast the output to the appropriate type:

```python
def typed_udf(return_type):
    def _typed_udf_wrapper(func):
        return f.udf(func, return_type)
    return _typed_udf_wrapper
```

The function `typed_udf` returns a new UDF decorator with the specified return type. We can think of it as a decorator that accepts an argument. For a more in depth overview of this pattern and decorators in general, see [this blog post from The Code Ship](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/). 

Now we once again have the nice, clean version of the code, with the added legibility bonus of the UDF's return type being visible right beside its definition:

```python
@typed_udf(t.IntegerType())
def increment(x):
    return x + 1

df = df.withColumn('col_plus_1', increment('col'))
```

Using a decorator instead of making two versions of every function isn't really necessary in this simple example, but if you are defining 20 UDFs your namespace will get awfully cluttered and it'll become harder to track what's going on. With four lines of code you can bring sanity back to your function naming scheme.

Finally, the code for DIY decorators is notoriously difficult to read, so if you're going to copy-paste, here is the snippet with a docstring (and a shameless plug):

```python
import pyspark.sql.functions as f

def typed_udf(return_type):
    """Make a UDF decorator with the given return type.

    Example usage:

    >>> @typed_udf(t.IntegerType())
    ... def increment(x):
    ...     return x + 1
    ...
    >>> df = df.withColumn('col_plus_1', increment('col'))

    See http://johnpaton.net/posts/clean-spark-udfs for more detail.

    Args:
        return_type (pyspark.sql.types type): the type that will be
            output by the function being decorated

    Returns:
        function: Typed UDF decorator

    """
    def _typed_udf_wrapper(func):
        return f.udf(func, return_type)

    return _typed_udf_wrapper
```
