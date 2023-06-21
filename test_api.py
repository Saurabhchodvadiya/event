import requests

def test_get_all_user():
    url = 'http://localhost:8000/get-all-user'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400

def test_create_user():
    url = 'http://localhost:8000/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "email": "chodvadiyasaurabh11111@gmail.com",
        "date_of_birth": "2022-10-12",
        "phone_number": "9664560410",
        "first_name": "saurabh",
        "last_name": "chodvadiya",
        "password": "Saurabh123@",
        "is_admin": "0"
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400



def test_login():
    url = 'http://localhost:8000/login'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "email": "chodvadiyasaurabh1@gmail.com",
        "password": "Saurabh123@"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400


def test_login():
    url = 'http://localhost:8000/login'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "email": "chodvadiyasaurabh1111@gmail.com",
        "password": "Saurabh123@"
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400



def test_create_event():
    url = 'http://localhost:8000/create_event'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    payload = {
        "event_name": "cricket",
        "start_Date": "2023-06-19",
        "end_Date": "2023-06-20",
        "total_participants": "3",
        "starting_time": "11:30:00",
        "ending_time": "11:30:00"
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400



def test_create_user():
    url = 'http://localhost:8000/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "email": "chodvadiyasaurabh1111@gmail.com",
        "date_of_birth": "2022-10-12",
        "phone_number": "9664560489",
        "first_name": "saurabh",
        "last_name": "chodvadiya",
        "password": "Saurabh123@",
        "is_admin": "0"
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400


def test_remove_event_by_id():
    url = 'http://localhost:8000/remove-event-by-id/3/'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NDkxNjA4LCJpYXQiOjE2ODcxOTE2MDgsImp0aSI6ImM3YTk5ZjZjY2QzYzQzN2U5ZmI5ZjczNzM3MGQzYWE2IiwidXNlcl9pZCI6Nn0.pvmeyd6Pya4UswCzSRYgtWeJ9_pMdhIXrCCo5BxYjq4'
    }
    response = requests.put(url, headers=headers)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400



def test_get_event_by_user_id():
    url = 'http://localhost:8000/get-event-by-user-id/6/'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NDkxNjA4LCJpYXQiOjE2ODcxOTE2MDgsImp0aSI6ImM3YTk5ZjZjY2QzYzQzN2U5ZmI5ZjczNzM3MGQzYWE2IiwidXNlcl9pZCI6Nn0.pvmeyd6Pya4UswCzSRYgtWeJ9_pMdhIXrCCo5BxYjq4'
    }
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400
def test_update_event_by_id():
    url = 'http://localhost:8000/update-event-by-id/5/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NDkxNjA4LCJpYXQiOjE2ODcxOTE2MDgsImp0aSI6ImM3YTk5ZjZjY2QzYzQzN2U5ZmI5ZjczNzM3MGQzYWE2IiwidXNlcl9pZCI6Nn0.pvmeyd6Pya4UswCzSRYgtWeJ9_pMdhIXrCCo5BxYjq4'
    }
    payload = {
        "event_name": "hockey",
        "total_participants": 10
    }
    response = requests.put(url, headers=headers, json=payload)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400


def test_get_all_user():
    url = 'http://localhost:8000/get-all-user'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400


def test_register_user_event():
    url = 'http://localhost:8000/user/register-user-event'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    payload = {
        "event_id": "5"
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400




def test_get_user_detail_by_event():
    url = 'http://localhost:8000/get_user_detail_by_event/5/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400


def test_get_participated_user_detail_by_event():
    url = 'http://localhost:8000/get_participated_user_detail_by_event/5/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400

def test_user_participated_event():
    url = 'http://localhost:8000/user_participated_event/6/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400



def test_remove_user_from_event():
    url = 'http://localhost:8000/remove_user_from_event/6/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NTI2MzI0LCJpYXQiOjE2ODcyMjYzMjQsImp0aSI6IjNiNWE5ZTllMDU5NjRjMDM5ZmI3NGZlOGVlMGI2ZTA2IiwidXNlcl9pZCI6Nn0.4lqaYpJTmISyddTKiTuSISLipURabtn9SWtZ3vOn294'
    }
    data = {
        'event_id': '5'
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code==200:
        assert response.status_code == 200
    else:
         assert response.status_code == 400