Airflow Tutorial
--------------

* ref: https://youtu.be/K9AnJ9_ZAXE?feature=shared


* Quick Start: https://airflow.apache.org/docs/apache-airflow/stable/start.html

## Standardalone
* Prep linux
```
sudo apt-get update
sudo apt-get install build-essential 
sudo apt-get install libssl-dev
sudo apt-get install -y python3 python3-pip python3-dev python3-venv

```

* Prep .gitignore
```
py_env/
logs/*
airflow.db
airflow.db*
airflow.cfg
simple_auth_manager_passwords.json.generated
```

* Start
```
python3 -m venv py_env
source py_env/bin/activate
pip3 install --upgrade pip setuptools
pip3 install apache-airflow
pip3 install apache-airflow-providers-sqlite
#export AIRFLOW_HOME=~/airflow
export AIRFLOW_HOME=$(pwd)
echo $AIRFLOW_HOME
rm airflow.cfg
rm airflow.db
airflow db migrate
airflow standalone
```

## Setup Airflow Locally

* Install
```
AIRFLOW_VERSION=2.10.3
AIRFLOW_VERSION=3.0.6
# See above for supported versions.
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

* Start
```
export AIRFLOW_HOME=~/airflow
airflow db init
airflow db migrate

airflow users create \
    --username admin \
    --password admin \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email admin@example.com

airflow webserver --port 8080

airflow scheduler
```