import requests

def test_date_overlap():
    url = 'http://localhost:8000/date/'
    data = {'date_1[start_date]': '2022-01-01', 'date_1[end_date]': '2022-01-13', 'date_2[start_date]': '2022-01-14', 'date_2[end_date]': '2022-01-28'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200
    assert response.json()['status'] == 'no overlap'

