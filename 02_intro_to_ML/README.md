Intro to Data Science Course:
=======

- Intro to Machine Learning
- Intro to Python Tools for Data Science

## Objectives

* Cover some essential concepts related to Machine Learning
* Establish understanding and comfort with basic Python
* Understand the central functions of the Pandas and Numpy libraries
* Be able to quickly navigate the iPython interface and documentation to find the data you need

## Class Materials

* [Lecture Slides](https://github.com/gads14-nyc/fall_2014_lessons/blob/master/02_intro_to_ML/class02.pdf) (posted after class meets)
* [Intro to iPython](http://nbviewer.ipython.org/github/gads14-nyc/fall_2014_lessons/blob/master/02_intro_to_ML/ipython_intro.ipynb)
* [Numpy and Pandas Introduction](http://nbviewer.ipython.org/github/gads14-nyc/fall_2014_lessons/blob/master/02_intro_to_ML/working_with_data.ipynb)
* [More Numpy and Scipy](http://nbviewer.ipython.org/github/gads14-nyc/fall_2014_lessons/blob/master/02_intro_to_ML/numpy_scipy.ipynb)
* [Lab - Python essentials](http://nbviewer.ipython.org/github/gads14-nyc/fall_2014_lessons/blob/master/02_intro_to_ML/python_lab.ipynb)
* [Lab - Practical Pandas](http://nbviewer.ipython.org/github/gads14-nyc/fall_2014_lessons/blob/master/02_intro_to_ML/pandas_lab.ipynb)
* [Bonus Lab - Advanced Pandas Practice](https://github.com/gads14-nyc/fall_2014_lessons/blob/master/02_intro_to_ML/advanced_lab.md)

## Additional Resources

#### Couple extra handy `python` introductions

* <a href="https://docs.python.org/2.7/">https://docs.python.org/2.7/</a>
* <a href="http://www.learnpython.org/">Interactive Python Training</a>
* <a href="https://docs.python.org/2.7/tutorial/index.html">The Python Tutorial</a>

#### More Numpy & Pandas Goodness

* Watch the 5 minute ["Ipython Notebook Tour"](http://ipython.org/notebook.html)

* Review ["What is NumPy"](http://docs.scipy.org/doc/numpy/user/whatisnumpy.html)

* Watch Wes McKinney's 10 minute [Whirlwind Tour of Pandas](http://wesmckinney.com/blog/?p=647) (even once is ok ;-) )

* Another great resource: Review Chapters 1 to 5 of [Julia Evans Cookbook](https://github.com/jvns/pandas-cookbook)

* Try out the [Official Pandas Tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html): Wes & Company's selection of tutorials and lectures

* Learn the basics of [markdown](http://daringfireball.net/projects/markdown/syntax)

* [Julia Evans Pandas Cookbook](https://github.com/jvns/pandas-cookbook): Great resource with eamples from weather, bikes and 311 calls

* [Learn Pandas Tutorials](https://bitbucket.org/hrojas/learn-pandas): A great series of Pandas tutorials from Dave Rojas

#### Other links

* Those looking for a more intensive read, Hadley Wickham's paper on the [Split-Apply-Combine Strategy](http://www.jstatsoft.org/v40/i01/paper) is a fantastic read, though dense. The code is also in R (Wickham is an R developer), but the methodology still perfectly applies.

* [Research Computing Python Data PYNBs](http://nbviewer.ipython.org/github/ResearchComputing/Meetup-Fall-2013/tree/master/python/): There are a ton of additional data sets and lectures about pandas. Consider going through these to continue practicing your python data manipulation.

#### HW

* Once you have completed the Lab iPython notebooks
* In `fall_2014_assignments/lab02`, make a directory with your first initial/full last name.

```sh
vagrant@data-science-toolbox:~$export DIR=<"flastname">
vagrant@data-science-toolbox:~$mkdir $DIR; cd <yourgithubusername>/fall_2014_assignments/lab02/$DIR;
```

```sh
vagrant@data-science-toolbox:~$git checkout -b my_name_lab02
vagrant@data-science-toolbox:~$git add .
vagrant@data-science-toolbox:~$git commit -m 'lab02 notebooks'
vagrant@data-science-toolbox:~$git push origin my_name_lab02
```

Add a pull request for your branch. This is the actual submission of your work. You can do this on github by finding your branch and clicking "Create pull request." Developers, feel free to use a command line tool for this if you prefer it.

Again, a link to github documentation on the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>.


