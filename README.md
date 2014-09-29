# General Assembly Data Science Course 14 - Fall 2014

*This repo includes materials for the General Assembly Data Science course in NYC. Navigate the directory structure to find what you're looking for. The `README.md` files are often the most central in a directory, and will display by default when you navigate on github.*


## Upcoming Activity:

* 9/29/14 dataexplor01 due
* 10/1/14 Linear Regression

### Getting Help

**Github Issues**

For general or specific course help, students can get the fastest response by posting an issue, to the [issues page for this repository](https://github.com/gads14-nyc/fall_2014_lessons/issues)

* Jarret or David will review each issue
* Students and other instructors following the repository will also be able to address the issue, improving response time.

**Office Hours**

Jarret and David will hold regular office hours, and Rob will be available by appointment.

Jarret: Sun - 4:00-6:00 PM  jarret.petrillo@gmail.com

David: M,W - 5:30-6:30  davidfmccreary@gmail.com

### Tentative Syllabus

| Date      | Location | Topic | Assignment Due 
|:----------|:--------|:------|:------|:------
| 9/24/2014 | GA East (902 Broadway, 4th Floor) |Intro to Intro to Data Science | Submit first pull request (lab01)
| **9/29/2014** || Intro to Machine Learning | Chicago housing price predictor (*dataexplor01*)
| 10/1/2014  | | Linear Regression | lab02 iPython notebooks
| **10/6/2014** | GA West (10 E. 21st St, 4th Floor) | Data Visualization and EDA | *dataexplor02*
| 10/8/2014  | | Dimensionality Reduction | First submission of **Africa Soil Property Prediction Challenge**
| **10/13/2014**| | **Columbus Day (Holiday/ No class)** | |
| 10/15/2014 | | Model Selection & Regularization | Final submission of **Africa Soil Property Prediction Challenge**
| **10/20/2014** | | Logistic Regression | *dataexplor04*
| 10/22/2014 | | Non-linear Classification | First Submission of **Forest Cover Type Prediction Challenge**
| **10/27/2014** | | Probablility and Bayes Theorem | *dataexplor05*
| 10/29/2014 | | Bayesian Classifiers, Discriminant Analysis | 
| **11/3/2014**  | | Time Series Analysis | *dataexplor06*
| 11/5/2014 | | kNN | 
| **11/10/2014** | | k-means Clustering | *dataexplor07*
| 11/12/2014 | | Review | 
| **11/17/2014** | | Natural Language Processing | *dataexplor08*
| 11/19/2014 | | Bayes Networks | 
| **11/24/2014** | GA East (902 Broadway, 4th Floor) | Decision Trees and Ensemble Methods | *dataexplor09*
| 11/26/2014 | | **(Holiday/ No class)** |
| **12/1/2014** | | Data Engineering: Distributed Computing | *dataexplor10*
| 12/3/2014  | | TBA | 
| **12/8/2014**  | | Review | *dataexplor11*
| 12/10/2014  | |Presentation Workshop | Presentation Slides/Outline
| **12/15/2014** | |Final Presentations | Final Project Due

### Submitting Lab Assignments

We will be using the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull</a> git model for submitting labs and some assignments.

For the first assignment:

1. Fork the assignments repo for the class:

2. clone the repo to your newly created Data Science Toolbox

```sh
vagrant@data-science-toolbox:~$git clone git@github.com:<yourgithubusername>/fall_2014_assignments.git
```

in `<yourgithubusername>/fall_2014_assignments/lab01`, make a directory with your first initial/full last name.

```sh
vagrant@data-science-toolbox:~$export DIR=<"flastname">
vagrant@data-science-toolbox:~$mkdir $DIR; cd <yourgithubusername>/fall_2014_assignments/lab01/$DIR;
```

With a text editor, create and save a markdown file with the following content:

* Your name and what you do
* One liner about your coding and math background
* Any social web you use and don't mind sharing (e.g. linkedin, twitter)
* A data blog post you read recently for sharing with the class
create a branch of the repository with a unique name, and then commit to that repo

```sh
vagrant@data-science-toolbox:~$git checkout -b my_name_class_1
vagrant@data-science-toolbox:~$git add .
vagrant@data-science-toolbox:~$git commit -m 'my first git commit!'
vagrant@data-science-toolbox:~$git push origin my_name_class_1
```

Add a pull request. This is the actual submission of your work. You can do this on github by finding your branch and clicking "Create pull request." Developers, feel free to use some command line tool for this if you prefer it.

Again, a link to github documentation on the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>.


