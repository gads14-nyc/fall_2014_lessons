Intro to Data Science Class07: *Classification and Logistic Regression*
=======

- Announcements/Questions
- Intro to Classification Problems
- Review Dataexplor04
- Logistic Regression

## Objectives

* Know how to evaluate classification models
* Understand theory behind LogisticRegression
* Know how to use sklearn's LogisticRegression class

## Lab/Practice

#### Three options:

1. Work on Dataexplor04
2. Extend the model in the Challenger O-ring case to include the "severity index"-- does it improve the model's predictive ability?
3. Three Class Prediction:
  - Use the famous iris dataset to train a MultiClass LogisticRegression model
  - Produce crosstab/confusion matrixes to evaluate your model
  - Use cross-validation to optimize for the best "C" tuning param
```
from sklearn import linear_model, datasets
iris = datasets.load_iris()
# Use first two columns (Sepal Width and Length) as preditors
X = iris.data[:,0:2]
y = iris.target
```

## Homework

* *Term Project*
  Create a text file/markdown/pdf/etc. and answer the following questions:
  1. What is your topic? Can you phrase your topic in the form of a question that you hope to answer?
  2. What do you plan to use as your source of data? Do you have a sense for how large your dataset is? Any other characteristics you know of?
  3. What tools or topics do you hope to learn and demonstrate by the end? In other words, what are your learning objectives?

## Class Materials

* [Lecture Slides](https://github.com/gads14-nyc/fall_2014_lessons/blob/master/07_classification/class07.pdf) (posted after class meets)
* [Logistic Regression Demo](http://nbviewer.ipython.org/github/gads14-nyc/fall_2014_lessons/blob/master/07_classification/lab/logistic_regression.ipynb)

## Additional Resources/Links

* Nice example of classification with sklearn from [DataRobot](http://www.datarobot.com/blog/classification-with-scikit-learn/)
* New version of [Pandas](http://pandas.pydata.org/pandas-docs/version/0.15.0/whatsnew.html)!

## Meetups!

* New York Open Statistical Programming Meetup, Oct. 23 [Hedge Funds’ Use of Alternative, Unstructured Data to Generate Returns](http://www.meetup.com/nyhackr/events/211210392/)
* New York Python Meetup Group, Weekend Study Groups: 
  - [Saturday Study Group](http://www.meetup.com/nycpython/events/210214592/)
  - [Sunday Study Group](http://www.meetup.com/nycpython/events/213665332/)
 

### Next class: *Bayes!*

#### Optional Reading

* Frequentism and Bayesianism: A Practical Introduction, [Part 1](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/)
* Paul Graham's, [A Plan for Spam](http://www.paulgraham.com/spam.html)
* [Probabilistic Programming and Bayesian Methods for Hackers](http://nbviewer.ipython.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/tree/master/Chapter1_Introduction/) (long book, bookmark for future reference)