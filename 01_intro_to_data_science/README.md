# Computer Setup and Data Handling

For this course, we will be using the [**Data Science Toolbox**](http://datasciencetoolbox.org/), which is a virtual environment based on Ubuntu Linux that is specifically suited for doing data science.

### Step 1: Download and install VirtualBox

- Go to the [Virtualbox download page](https://www.virtualbox.org/wiki/Downloads) and download the appropriate binary. Open the binary and follow the installations instructions.

### Step 2: Download and install Vagrant

- Go the [Vagrant download page](http://www.vagrantup.com/downloads.html) and download the appropriate binary. Open the binary and follow the installations instructions.

### Step 3: Download and start the Data Science Toolbox

- Open a terminal (also known as the command prompt in Microsoft Windows). Create a directory, for example "gadatasciencetoolbox", and navigate to it:

```
$ mkdir MyDataScienceToolbox
$ cd MyDataScienceToolbox
```

- Next, run the following commands:
```
$ vagrant init data-science-toolbox/dst
$ vagrant up
```

### Step 4: Log in (on Mac OS X and Linux)

- If you are running Mac OS X or some other UNIX-like operating system, you can log in to the Data Science Toolbox by simply running the following command in a terminal:

```
vagrant ssh
```

### Step 4: Log in (Windows)

- If you are running Microsoft Windows, you need to use a third-party application in order to log in to the Data Science Toolbox. We recommend **Putty** for this. Go to its [download page](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) and download `putty.exe`. Run `putty.exe` and enter the following values:

```
Host Name (or IP address): 127.0.0.1
Port: 2222
Connection type: SSH
```
(If you want, you can save these values as a session by clicking the "Save" button, so that you do not need to enter these values again.)

Next, click the "Open" button and enter "vagrant" for both the username and the password.

### Step 5: Install GA Data Science Bundle

- Run the following commands:

```
vagrant@data-science-toolbox:~$ dst update
vagrant@data-science-toolbox:~$ dst add gads
```
(Note that `vagrant@data-science-toolbox:~` indicates that this command should be run on the Data Science Toolbox.)

### Step 6: Set up IPython Notebook

Now that you are logged into your new virtual machine, invoke the following command to create a password-protected profile:

```
vagrant@data-science-toolbox:~$ dst setup base
```

Next, `$ exit` out of the virtual machine and use your favorite text editor to open up the `Vagrantfile` in the `MyDataScienceToolbox` directory. Uncomment and edit the line somewhere around line 22 to the following:

```
config.vm.network "forwarded_port", guest: 8888, host: 8888
```

This line instructs Vagrant to open up port 8888 so that the IPython Notebook server is accessible from your browser. Restart the Data Science Toolbox and log in again so that the changes take effect:

```
$ vagrant reload
$ vagrant ssh
```

To start the IPython Notebook server, run:

```sh
vagrant@data-science-toolbox:~$ sudo ipython notebook --profile=dst
```

- You can now access the IPython Notebook server at https://localhost:8888. Because the SSL certificate is self-signed, you may get a warning message from your browser. The image below shows how Chrome complains about this. Because you know what's on the server-side, you can just click on the "Proceed anyway" button.


#### Fork the assignments repo:
Once you've setup the Data Science Toolbox, clone your fork of the class repository. We'll be using the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>. You will be pushing changes to your forked repository, and submitting pull requests to the class repository.

From the github help page:
> The Fork & Pull Model lets anyone fork an existing repository and push changes to their personal fork without requiring access be granted to the source repository. The changes must then be pulled into the source repository by the project maintainer.

For example, from the home directory:
```sh
vagrant@data-science-toolbox:~$ cd ~/; git clone git@github.com/<my git handle>/fall_2014_assignments.git
```

## Lab Submissions

Make a directory with your first name and last name in `~/fall_2014_assignments/lab01`.

```sh
vagrant@data-science-toolbox:~$ cd fall_2014_assignments/lab01
vagrant@data-science-toolbox:~/fall_2014_assignments/lab01$ mkdir '~/fall_2014_assignments/lab01/<firstname>_<lastname>'
```

With a text or markdown editor, create and save a markdown file with the following content:

* Your name and what you do
* One liner about your coding and math background
* Any social web you use and don't mind sharing (e.g. twitter, linkedin)
* A link to a data scince related blog post you read recently for sharing with the class

create a branch of the repository with a unique name, and then commit to that repo

```sh
vagrant@data-science-toolbox:~/fall_2014_assignments/lab01$ git checkout -b my_name_class_1
vagrant@data-science-toolbox:~/fall_2014_assignments/lab01$ git add .
vagrant@data-science-toolbox:~/fall_2014_assignments/lab01$ git commit -m 'my first git commit!'
vagrant@data-science-toolbox:~/fall_2014_assignments/lab01$ git push origin my_name_class_1
```

Add a pull request. This is the actual submission of your work. You can do this on github by finding your branch and clicking "Create pull request." Developers, feel free to use some command line tool for this if you prefer it.

Again, a link to github documentation on the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>.

## Next Steps

We will always recommend 4 or 5 readings or other support materials for every class, either to supplement the current material, prep for the next class, or covering previous material that students still have questions on.

**Reading and other Materials**

* <a href="http://www.quora.com/Data-Science/What-is-it-like-to-be-a-data-scientist">Quora: What is it like to be a data scientist?</a>
* <a href="http://www.youtube.com/watch?v=h9vQIPfe2uU"> Josh Wills: The Life of a Data Scientist</a>
* <a href="http://www.p-value.info/"> P-Value.info, Carl Anderson's blog (Director of Data at Warby Parker)</a>
* <a href="http://blog.okcupid.com/"> A look at OKCupid and their detailed work in trends</a>
* <a href="http://radar.oreilly.com/2011/09/building-data-science-teams.html">DJ Patil, Building Data Science Teams</a>
* <a href="http://benfry.com/phd/">Ben Fry's Dissertation: Computational Information Design </a>
