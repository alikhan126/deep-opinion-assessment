# deepopinion-code-assesment


## Instructions

* Pre-requisite
```
Python 3 (3.9, 3.10, 3.11)
```

* Install virtual environment
```bash
virtualenv venv
```

* Activate virtual envionment
```bash
source venv/bin/activate
```

* Install dependencies
```bash
pip3 install -r requirements.txt
```

* Run code
```bash
python manage.py runserver
```

* Navigate to port 8000 to check the running server
```bash
http://127.0.0.1:8000/api/
```

* Navigate to following url to list or create new data.
```bash
http://127.0.0.1:8000/api/training_data/
```

* Navigate to following url to add a tag to some data
```bash
http://127.0.0.1:8000/api/training_data/{pk}/tag/
```

* Navigate to following url to get the list of aspects
```bash
http://127.0.0.1:8000/api/training_data/aspects/
```

* Navigate to following url to get the list of sentiments
```bash
http://127.0.0.1:8000/api/training_data/sentiments/
```

* Navigate to following url to add upload csv or xlsx file to add data with or without tags
```bash
http://127.0.0.1:8000/api/training_data/upload/
```

* Navigate to following url to download the data
```bash
http://127.0.0.1:8000/api/training_data/download/?format=csv
```