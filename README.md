# learn-airflow
Learn Airflow


## Setup Locally
> Ref: https://medium.com/orchestras-data-release-pipeline-blog/installing-and-configuring-apache-airflow-a-step-by-step-guide-5ff602c47a36

* Create Virtual Env
```
python -m venv py_env
```
* Install Airflow
```
pip3 install apache-airflow
```

### Start Airflow Standalone
```
airflow db init
airflow standalone
```

### Start Airflow
* Initialise db
```
airflow db init
```
* Create users
```
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
```
* Webserver
```
airflow webserver -p 8080
```
* Scheduler
```
airflow scheduler
```