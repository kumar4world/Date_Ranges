#Date Ranges Api project

This is a JSON based API that will return a response indicating if two date ranges overlap.

Set up steps:

1) git clone 
2) cd Date_Ranges
3) python3 manage.py runserver 8000


Usage:

Example: curl -X POST -d 'date_1[start_date]=2022-01-01&date_1[end_date]=2022-01-13&date_2[start_date]=2022-01-18&date_2[end_date]=2022-28' http://127.0.0.1:8000/date/
