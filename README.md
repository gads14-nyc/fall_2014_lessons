# General Assembly Data Science Course 14 - Fall 2014

*This repo includes materials for the General Assembly Data Science course in NYC. Navigate the directory structure to find what you're looking for. The `README.md` files are often the most central in a directory, and will display by default when you navigate on github.*


## Upcoming Activity:

* 9/24/14 First Class!
* 10/1/14 dataexplor01 due

### Getting Help

**Github Issues**

For general or specific course help, students can get the fastest response by posting an issue, to the [issues page for this repository](https://github.com/gads14-nyc/fall_2014_lessons/issues)

* Jarret or David will review each issue
* Students and other instructors following the repository will also be able to address the issue, improving response time.

**Office Hours**

Jarret and David will hold regular office hours, and Rob will be available by appointment.

Jarret: Sun - 4:00-6:00 PM

David: M,W - 5:30-6:30

### Submitting Lab Assignments

We will be using the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull</a> git model for submitting labs and some assignments.

For the first assignment:

1. Fork the assignments repo for the class:

2. clone the repo to your newly created Data Science Toolbox
```sh
git clone git@github.com
```

in `gads14-nyc/fall_2014_assignments/lab01`, make a directory with your first initial/full last name.

```sh
DIR='flastname'; cd ~/GADS9-NYC-Spring2014/lab_submissions/lab01/flastname; mkdir $DIR; open $DIR
```

With a text or markdown editor, create and save a markdown file with the following content:

* Your name and what you do
* One liner about your coding and math background
* Any social web you use and don't mind sharing (e.g. linkedin, twitter)
* A data blog post you read recently for sharing with the class

create a branch of the repository with a unique name, and then commit to that repo

```sh
git checkout -b my_name_class_1
git add .
git commit -m 'my first git commit!'
git push origin my_name_class_1
```

Add a pull request. This is the actual submission of your work. You can do this on github by finding your branch and clicking "Create pull request." Developers, feel free to use some command line tool for this if you prefer it.

Again, a link to github documentation on the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>.


