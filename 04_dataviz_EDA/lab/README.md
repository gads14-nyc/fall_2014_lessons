## Exploratory Data Analysis
=============================

### Part 1: *IMDB Dataset*

Explore a list of metadata for the top 10,000 movies according to IMDB ratings made since 1950. 

1. Get the data-- Download the data at http://bit.ly/cs109_imdb

2. Clean the DataFrame such that:

	- Each row describes a single object
	
	- Each column describes a property of that object

	- Columns contain numeric data whenever possible

	- Columns contain atomic properties that cannot be further decomposed

	a. Strip out the year from the *title* column

	b. Fix the *runtime* column so that it stores a numeric datatype

	c. Split up the *genres* column into many columns

3. Explore *global/group properties* (e.g. histograms, scatter plots, aggregation functions to summarize)

	a. Run **describe()** on relevant columns-- 

	b. Make some basic plots:

		- histograms of release year, score, runtime. Notice any trends?

	c. More exploring plots:

		- scatterplots of release year vs. score, # votes vs score

	d. Identify Outliers

		- highest/lowest rated movies overall

		- low-score movies with losts of votes

	e. Basic aggregations:

		- How many movies are in each genre?

		- How many genres does a movie have on average?

### Part 2: 

### Option 1: *Matplotlib tutorial(s)*

### Option 2: *New York Times Ad Impressions Dataset*

([adapted from **Doing Data Science**, Cathy O'Neil and Rachel Schutt, Chapter 2: Statistical Inference, EDA, and Data Science Process](http://shop.oreilly.com/product/0636920028529.do))

1. Get the data:

   Write a python script to download datasets nyt1.csv...nyt31.csv from url endpoint: http://stat.columbia.edu/~rachel/datasets/ into your own local directory

   Each file represents a simulated day's worth of ad impressions and clicks recorded on the **New York Times** home page in May 2012. Each row represents a single user. There are five columns: age, gender, number of impressions, number of clicks, and signed-in

2. For a single day of data:

  a. Create a new variable (column) in your dataframe that puts users into the following categories: ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    - hint use the "apply" method

  b. Plot the distributions of the number of impressions and click-through-rate (CTR = clicks/impressions) for these six age categories

  c. Define a new variable (column) to segment or categorize users based on their click behavior

  d. Make visual and quantitative comparisons across user segments/demographics (e.g., <18 year-old males vs. females or logged-in vs not)

  e. Create metrics tha summarize the data. For example: CTR, quantiles, mean, median, variance, min/max. Think about what you would like to track over time-- what will compress the data but still capture user behavior.

3. Now extend the analysis across days. Visualize some metrics and distributions over time. What are some good ways to show day-to-day trends?

#### Option 3: *Africa Soil Dataset*

1. Sign into Kaggle and get cracking on the full Africa Soil Dataset 

#### 




