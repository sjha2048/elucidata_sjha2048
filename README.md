[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![ViewCount](https://views.whatilearened.today/views/github/sjha2048/elucidata_sjha2048.svg)




# Assignment for Elucidata 
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://elucidata-sjha2048.herokuapp.com/upload)


## Tasks 

 - Write a flask/Django server where a user uploads the dataset 
 - In third column “Accepted Compound ID”, you need to filter   out all the data for metabolite ids ending with:
‘PC’, ‘LPC’ and ‘plasmalogen’, and create 3 child datasets (1 for each compound id) from the data in input file.
 - Add a new column in the parent dataset with the name “Retention Time Roundoff (in mins)”. This column
should have rounded-off values of the corresponding retention time. Retention time should be rounded-off to
the nearest natural number.
 - you should find the mean of all the metabolites which have same "Retention Time Roundoff"
across all the samples. The resultant of above operation should be a new data-frame where you have to
include the "Retention Time Roundoff" column and all samples. You don't have to include columns like m/z,
Accepted Compound Id and Retention time.

## Run Locally 
Clone Repository

``` git clone https://github.com/sjha2048/elucidata_sjha2048.git```

Install the requirements

```pip3 install -r requirements.txt```

Apply Migrations

```python3 manage.py migrate```

Run the server 

```python3 manage.py runserver```

## API endpoints

### ```/upload```

uploads the file to the server 

example - http://127.0.0.1:8000/upload/

### ```/<file_name>/api1```

performs task1 and returns the zip with three child datasets

example - http://127.0.0.1:8000/data/api1

### ```/<file_name>/api2```

performs task2 and task3 and returns the zip with two files respectively 

example - http://127.0.0.1:8000/data/api2


## Live Demo

### for uploading the data:

https://elucidata-sjha2048.herokuapp.com/upload/

ps: the upload can be extremely slow due to heroku free tier limits 

### Task 1

for demo purpose I have already uploaded the dataset and the processed output can be obtained at:

https://elucidata-sjha2048.herokuapp.com/data/api1

if you wish to upload your own data then change the url as below

https://elucidata-sjha2048.herokuapp.com/<file_name>/api1

zipfile containing the processed output will be downloaded 

### Task 2 & 3

processed output can be obtained at:

https://elucidata-sjha2048.herokuapp.com/data/api2

if you wish to upload your own data then change the url as below
https://elucidata-sjha2048.herokuapp.com/<file_name>/api2

#### Code for these endpoints can be found at [views.py](https://github.com/sjha2048/elucidata_sjha2048/blob/master/uploadprocess/views.py)


## Todo

- [x] API for uploading file
- [x] API for TASK 1
- [x] API for TASK 2
- [x] Documentation 
- [x] Heroku Deployment 
- [ ] Functional Tests







