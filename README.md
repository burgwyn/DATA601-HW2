# DATA601-HW2

## Overview

This study explores [publicly available salary data API](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w) from the City of Chicago.  Transparency in government is a fundamental trait in a functioning democracy.  The [Open Government](https://en.wikipedia.org/wiki/Open_government) movement seeks to ensure citizens have the right to see documents and other data that pertain to how their government operates, including how budgets are spent.

<img src="https://github.com/burgwyn/DATA601-HW2/blob/main/images/salary_hourly_pie.png" alt="Pie chart of departments" />

## Goals

Explore and examine the nature of the wage information for both salaried and hourly public employees of the City of Chicago through requests against a publicly available RESTful API.

- Who is the highest paid salaried employee?  What is that salary?
- What is the lowest hourly wage?
- Which department is has the highest wage bill?
- Which department is paying the least?
- What job titles are the most lucrative?  Which are the least?

## Motivation & Background

I was drawn to this study because I believe strongly that we as citizens should understand how our governments operate and how they allocate resources.  While I no longer live in Chicago, I did spend 7 memorable years there: I met my wife, made lifelong friendships and ignited my passion for software development.

While there appears to be no existing research on this particular dataset, Chicago's Data Portal [acknowledges this is the most popular dataset](https://digital.chicago.gov/index.php/starting-salary/).

## Table of Contents

- API request code - `data.py`
- Python Notebook - `HW2.ipynb`

The final solution should look like this after executing `data.py`

```shell
├── HW2.ipynb
├── LICENSE
├── README.md
├── data
│   └── chicago_employee_salary_data.json
├── data.py
└── images
    ├── hourly_pie.png
    ├── salary_distribution.png
    ├── salary_hourly_pie.png
    └── salary_pie.png
```

### Getting Started

Run the data script to fetch data from the API
```shell
python data.py
```
Run the included Jupyter Notebook `HW2.ipynb` to review the data analysis

## Software Requirements

This solution requires Conda and Python 3.8.  In addition it uses the following libraries:
- [Requests](https://requests.readthedocs.io/en/master/user/quickstart/#json-response-content) - HTTP request library
- [Pandas](https://pandas.pydata.org/) - Data analysis library
- [JSON](https://docs.python.org/3/library/json.html) - Storing and retrieving JSON dataset

## Data

The final dataset, `chicago_employee_salary_data.json`, resides in the `data` directory/

Data is fetched from the City of Chicago's open data portal - `https://data.cityofchicago.org/resource/xzkq-xp2w.json?$limit=50000`

The url above includes a querystring parameter `$limit` to ensure the full dataset of ~33,000 records is retrieved.  This data is publicly available and not authentication or authorization is required.

The dataset shape is `(32928, 8)` or 8 columns and 32928 rows.

The data dictionary is published along with the [dataset](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w) and reproduced below

| Column Name | Description | Type |
|---|---|---|
| Name | Name of employee | Plain Text |
| Job Titles | Title of employee at the time when the data was updated. | Plain Text |
| Department | Department where employee worked. | Plain Text |
| Full or Part-Time	| Whether the employee was employed full- (F) or part-time (P). | Plain Text |
| Salary or Hourly | Defines whether an employee is paid on an hourly basis or salary basis. Hourly employees are further defined by the number of hours they work in a week. See the "Frequency Description" column. | Plain Text |
| Typical Hours	| Describes the typical amount of work for hourly employees. This data does not apply to salary employees. 40 - Employee paid on an hourly basis; works an 8 hour day; can be either full-time permanent (FT/P) or full-time temporary (FT-T) which is a seasonal employee; 35 - Employee paid on an hourly basis; works a 7 hour day; can be either full-time permanent (FT/P) or full-time temporary (FT-T) which is a seasonal employee; 20 - Employee paid on a part-time, hourly basis; typically works a 4 hour day, 5 days a week; 10 - Employee paid on a part-time, hourly basis; works 10 hours or less in a week. | Number |
| Annual Salary | Annual salary rates. Only applies for employees whose pay frequency is "Salary". Hourly employees rates are only shown in "Hourly Rates" column. | Number |

### Data Cleaning

The data clean up is fairly straightforward, filling default values of '0' for `NaN` columns and casting wage and hour fields to numeric values.

```py
## defualt NaN to 0
df.fillna(0)

## cast salary, hours and rate to numeric
df['annual_salary'] = pd.to_numeric(df['annual_salary'],errors='coerce')
df['typical_hours'] = pd.to_numeric(df['typical_hours'],errors='coerce')
df['hourly_rate'] = pd.to_numeric(df['hourly_rate'],errors='coerce')
```

## Results

### Who is the highest paid salaried employee?  What is that salary?

Jamie Rhee, Commissioner of Aviation is the highest salaried employee.  He is responsible for both Midway and O'Hare, two large metropolition airports.

### What is the lowest hourly wage?

The lowest hourly wage is $3/hour and is paid to two roles - FOSTER GRANDPARENT and SENIOR COMPANION in the FAMILY & SUPPORT department.

### Which department is has the highest wage bill?

The Chicago Police Department is the largest employer of salaried staff has has one of the highest median salaries.

<img src="https://github.com/burgwyn/DATA601-HW2/blob/main/images/salary_pie.png" alt="Pie chart of departments" />

### Which department is paying the least?

The Board of Elections has the lowest median salary.

### What job titles are the most lucrative?  Which are the least?

The highest paid poisitons are department leaders and the mayor:

| Title | Department| Salary |
|---|---|---|
| FIRST DEPUTY FIRE COMMISSIONER | FIRE | 197736.0 |
| MAYOR	| MAYOR'S OFFICE | 216210.0 |
| FIRE COMMISSIONER	FIRE | 217728.0 |
| SUPERINTENDENT OF POLICE | POLICE | 260004.0 | 
| COMMISSIONER OF AVIATION | AVIATION | 275004.0 |

The lowest paid poisiton are almost exlusively in the Board of Elections:

| Title | Department| Salary |
|---|---|---|
| COMMITTEE SECRETARY | CITY COUNCIL | 25848.0	|
| ELECTION EQUIPMENT & SUPPLY SPEC I | BOARD OF ELECTION | 30060.0 |
| POLLING PLACE INVESTIGATOR I | BOARD OF ELECTION	| 30822.0 |
| CLERK - BD OF ELECTIONS | BOARD OF ELECTION | 31584.0	|
| ELECTION EQUIPMENT & SUPPLY SPEC II | BOARD OF ELECTION | 34860.0	|

## Conclusion and Future Analysis

The median salary in Chicago exceeds the national median of $56,516 [as reported by the US Census in 2015](https://www.census.gov/library/publications/2016/demo/p60-256.html)

```
Min: 20400.0
Mean: 89609.2195137762
Median: 90024.0
Max: 275004.0
```

In addition, the City of Chicago recently [raised the minimum wage](https://www.chicago.gov/city/en/depts/bacp/supp_info/minimumwageinformation.html).  It would be worthwhile to revisit this dataset to see if there was any impact.

The dataset lacks some context that may explain why certain salaries set the way they are.  Additional information such as years of service and degrees and professional certifications would be helpful.

Although the dataset includes about 33,000 employees, teachers are not included.  This typically a large block of public sector employees and would be interesting to explore.

## Project Info

Contributors: [Nat Burgwyn](https://github.com/burgwyn)

Languages: Python

Tools: PyCharm, Jupyter Notebook

Libraries: pandas, requests