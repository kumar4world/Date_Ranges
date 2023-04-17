#Date Ranges Api project - date_overlap

This is a JSON based API that will return a response indicating if two date ranges overlap.

Set up steps:

1) git clone git@github.com:kumar4world/Date_Ranges.git
2) cd Date_Ranges
3) python3 manage.py runserver 8000


Usage:

Example: curl -X POST -d 'date_1[start_date]=2022-01-01&date_1[end_date]=2022-01-13&date_2[start_date]=2022-01-18&date_2[end_date]=2022-28' http://127.0.0.1:8000/date/

Alternatively use postman tool to send your POST requests and add the parameters to the body of the request

CI/CD Pipeline:

1) This code is checked in the github and a Jenkinsfile is present in the repository
2) When a commit is made to the repository, Jenkins kicks off a build and uses this Jenkinsfile which defines the build steps
3) The pipeline, checks out the repository from the github, builds, tests, packages and publishes the results.
4) test_data_overlap.py and test_data_no_overlap.py in the date_overlap/tests folder are the unit tests performed by the test step in the build process.
