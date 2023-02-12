# Building a Data Science Salary Estimator 

## overview

The project in question consists of :
* Scraping data from glassdoor 
* Cleaning data
* Exploratory data analysis
* Feature engineering
* Building machine learning model
* Built a client facing API using flask


## prerequisites

* Python version 3.*
* pandas
* numpy
* seaborn
* matplotlib
* scikit-learn
* wordcloud
* flask


## project stages

### Web Scraping

Scraping glassdoor website https://www.glassdoor.com/Job/san-francisco-data-scientist-jobs-SRCH_IL.0,13_IC1147401_KO14,28_IP1.htm?  and extracting:

* Job Title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue

### Data Cleaning

after Scraping the data , we cleaned it and for that we made the following variables:

* cleaning Salary_estimate column (removing $ and 'k') and add 'max'-'min' salary columns
* made new columns for 'hourly' wages and 'employer provided'
* remowing rows with missing values in salary (in our case rows with -1)
* parsing 'Company_name' column
* adding new column of 'State'
* mading a new column of company 'age' from the 'Founded' column
* parsing job description and adding column for 
        * python
        * excel 
        * rstudio
        * spark 
        * aws
       (1 if they are in job description else we put 0)
* Column for simplified job title and Seniority
* Column for description length

### Exploratory Data Analysis

Exploring the distributions of the data and creating boxplots to get summary information
and some pivot tables for categorical values:
![image](https://user-images.githubusercontent.com/89319105/218305444-205b8937-e9db-496d-bceb-5880ef91cbed.png)
![image](https://user-images.githubusercontent.com/89319105/218305458-e232e4b5-ad24-4e67-b82c-6a1488e1b927.png)
![image](https://user-images.githubusercontent.com/89319105/218305468-de70d4bf-52c2-44e5-8402-16e0e2407654.png)
![image](https://user-images.githubusercontent.com/89319105/218305480-a9caa527-b448-4f93-8fdd-dd9a9f9ba41c.png)
![image](https://user-images.githubusercontent.com/89319105/218305492-8f90556a-b00d-4f42-9aac-9366f1347f0e.png)
![image](https://user-images.githubusercontent.com/89319105/218305529-1651c396-9ae3-4d9e-bc24-ca436449f663.png)


### Model Building
To build the machine learning model :
* Transforming Categorical variables into dummy variablees
* Splitting Data into Train and test data

we tried different models:
* Multiple Linear regression using statsmodels
* Linear Regression with Sklearn
* Lasso regression
* Random Forest

### Productionization
I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.






