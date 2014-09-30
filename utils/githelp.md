# Some help getting git configured in the Data Science Toolbox

## Step 0: If you want to delete and re-clone your git repos, ssh into the vagrant environment, and:
**Be certain that you want to do this-- there is no way to undo this delete!!!**
```
vagrant@data-science-toolbox:~$ cd notebooks
vagrant@data-science-toolbox:~/notebooks$ rm -rf fall_2014_lessons
vagrant@data-science-toolbox:~/notebooks$ rm -rf fall_2014_assignments
```

## Step 1: Initial setup -- (after having ssh'd into the vagrant environment and run the dst setup commands)
## **Clone** the "lessons" repo:
	```
	vagrant@data-science-toolbox:~$ cd notebooks
	vagrant@data-science-toolbox:~/notebooks$ git clone https://github.com/gads14-nyc/fall_2014_lessons.git
	Cloning into 'fall_2014_lessons'...
	remote: Counting objects: 108, done.
	remote: Compressing objects: 100% (80/80), done.
	remote: Total 108 (delta 43), reused 88 (delta 23)
	Receiving objects: 100% (108/108), 805.82 KiB | 0 bytes/s, done.
	Resolving deltas: 100% (43/43), done.
	Checking connectivity... done.

	```
## Step 2: **Fork** the "assignments" repo:
### First fork the repo by navigating to the [repo](https://github.com/gads14-nyc/fall_2014_assignments) and clicking the "fork" button

### Next, clone the forked repo from your own github account into the notebooks directory:
	```
	vagrant@data-science-toolbox:~$ cd notebooks
	vagrant@data-science-toolbox:~/notebooks$ git clone https://github.com/YOUR_USERNAME/fall_2014_assignments.git
	Cloning into 'fall_2014_assignments'...
	remote: Counting objects: 79, done.
	remote: Compressing objects: 100% (57/57), done.
	remote: Total 79 (delta 22), reused 70 (delta 13)
	Unpacking objects: 100% (79/79), done.
	Checking connectivity... done.

	```

## [configure git to fetch changes made to upstream repo](https://help.github.com/articles/configuring-a-remote-for-a-fork)

	```
    vagrant@data-science-toolbox:~/notebooks/fall_2014_assignments$ git remote -v
    # origin  https://github.com/YOUR_USERNAME/fall_2014_assignments.git (fetch)
    # origin  https://github.com/YOUR_USERNAME/fall_2014_assignments.git (push)

    vagrant@data-science-toolbox:~/notebooks/fall_2014_assignments$git remote add upstream https://github.com/gads14-nyc/fall_2014_assignments.git
    ```

## Confirm this worked:
   ```
   vagrant@data-science-toolbox:~/notebooks/fall_2014_assignments$ git remote -v
   # origin  https://github.com/YOUR_USERNAME/fall_2014_assignments.git (fetch)
   # origin  https://github.com/YOUR_USERNAME/fall_2014_assignments.git (push)
   # upstream  https://github.com/gads14-nyc/fall_2014_assignments.git (fetch)
   # upstream  https://github.com/gads14-nyc/fall_2014_assignments.git (push)
   ```
    
## [fetch and merge the latest updates from the upstream master](https://help.github.com/articles/syncing-a-fork)
   
   ```
   cd ~/notebooks/fall_2014_assignments/
   git fetch upstream
   git checkout master
   git merge upstream/master
   ```
