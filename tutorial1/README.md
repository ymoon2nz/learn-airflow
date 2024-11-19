Airflow Tutorial
--------------

* ref: https://youtu.be/K9AnJ9_ZAXE?feature=shared


* Quick Start: https://airflow.apache.org/docs/apache-airflow/stable/start.html

## Setup Airflow Locally
* Install
```
AIRFLOW_VERSION=2.10.3
# See above for supported versions.
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

* Start
```
airflow db migrate

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

airflow webserver --port 8080

airflow scheduler
```