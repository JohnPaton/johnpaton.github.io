<!-- 
.. title: Custom color themes in Matplotlib
.. slug: matplotlib_colors
.. date: 2017-05-011 20:00:00 UTC+01:00
.. tags: python, dataviz, matplotlib
.. category: 
.. link: https://johnpaton.github.io/posts/matplotlib_colors/
.. description: Making custome color schemes available in Matplotlib is super easy
.. type: text
.. author: John Paton
-->

At KPMG, like (I imagine) at most companies, we have a custom color palette that presentation and other materials are supposed to conform to. I actually quite like it when things I produce have a consistent look and feel, so I decided to find out how to make a custom color palette in [matplotlib](https://matplotlib.org/). Turns out that it's super easy.

<!-- TEASER_END -->

The first step is to create a `.mplstyle` file for your color scheme. These can contain a bunch of options, but you can download a sample [here](http://matplotlib.org/_static/matplotlibrc). Save it as `my_style_name.mplstyle`. Way down in line 337 (at the time of writing), you will find the following lines:

```python
#axes.prop_cycle    : cycler('color',
#                            ['1f77b4', 'ff7f0e', '2ca02c', 'd62728',
#                              '9467bd', '8c564b', 'e377c2', '7f7f7f',
#                              'bcbd22', '17becf'])
                                            # color cycle for plot lines
                                            # as list of string colorspecs:
                                            # single letter, long name, or
                                            # web-style hex
```

This setting defines the cycle of colors that matplotlib uses for consecutive elements on plots when you don't specify the colors. Uncomment these lines and swap out the list for a list of your favorite (or corporately imposed) colors. As indicated by the comment, matplotlib will accept [single letter](https://matplotlib.org/api/colors_api.html), [long name](https://www.w3schools.com/colors/colors_names.asp), or hex colors. Use the HTML long name colors for full entertainment value.

![HTML long name colors vizualized](https://s-media-cache-ak0.pinimg.com/originals/1b/37/ec/1b37ec6dd26e4368cf9db7558ea46a4f.gif)




```python
>>> import matplotlib
>>> matplotlib.get_configdir()
'C:\\Users\\johnpaton\\.matplotlib'
```

