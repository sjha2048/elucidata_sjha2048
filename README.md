# Assignment for Elucidata 

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

### ```/<file_name>/api2

performs task2 and task3 and returns the zip with two files respectively 

example - http://127.0.0.1:8000/data/api2





