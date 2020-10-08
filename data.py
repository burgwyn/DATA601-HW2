## import path for saving response
import os.path

## import requests for HTTP requests
import requests

## import json to saving API response
import json

## import pandas for data analysis
import pandas as pd

## fetch data
r = requests.get('https://data.cityofchicago.org/resource/xzkq-xp2w.json?$limit=50000')

## check HTTP response code
print('HTTP Status Code: ' + str(r.status_code))

## the HTTP response contains a few headers that provide additional context
print(r.headers['Last-Modified'])
print(r.headers['X-SODA2-Fields'])
print(r.headers['X-SODA2-Types'])

## make data directory
## catch error is directory already exists
try:
    os.mkdir('./data')
except OSError as error:
    print(error)

## save response to data directory
with open(os.path.join('data', 'chicago_employee_salary_data.json'), 'w') as file:
    json.dump(r.json(), file)

## build DataFrame from JSON response saved to file
with open(os.path.join('data', 'chicago_employee_salary_data.json'), 'r') as file:
    df = pd.DataFrame.from_dict(r.json())