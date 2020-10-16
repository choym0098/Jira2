# Jira2
build a project management tool like Jira or Trello from scratch using Django, React.ts and PostgreSQL

## Setting up
### 1. set up Python virtual environment using Pyenv
Follow the steps from this [link](https://www.notion.so/Jira2-Project-6c0956b63ccf48ea95a3fb80e0df00af#7a378e70c5944734b023c474807182e5) to set up the virtual environment.

The later steps assume that the virtual environment is activated:
```bash
source "path/to/your/venv/bin/activate"
```

### 2. set up PostgreSQL
install `postgresql` using `brew`
```bash
brew update
brew install postgresql
```

Open the app and initialize the database. Then, log in as `postgres` and run the following command:

```sql
create database jira2;
create user root with password 'password';
ALTER USER root CREATEDB;
alter role root set client_encoding to 'utf-8';
alter role root set timezone to 'Asia/Seoul';
grant all privileges on database jira2 to root;
```

### 3. install Django
install Django
```bash
pip install Django
```
Then, install `psycopg2` package to work with `PostgresSQL`
```bash
pip install --no-binary :all: psycopg2
```

```bash
pip install --upgrade Pillow
```

### 4. install code formatter
```bash
pip install pre-commit
```


## Development

### Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### running server
```bash
python manage.py runserver
```


# Running with Docker
1. First install docker on your laptop or desktop.
https://www.docker.com/?utm_source=google&utm_medium=cpc&utm_campaign=dockerhomepage&utm_content=namer&utm_term=dockerhomepage&utm_budget=growth&gclid=CjwKCAjw5p_8BRBUEiwAPpJO6-p4Z1j76uJmVZVqrb_DUYrGBtCsQa2UXdKMgTEZE-6zpft4XgLatBoCYTYQAvD_BwE

2. Go to app/app/settings.py, and find DATABASES in settings.py. Once found, change it to the following codes:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
    }
}
```

3. To initialize, run
```
docker-compose build
docker-compose run app sh -c "python manage.py makemigrations"
```

4. To run the server, run
```
docker-compose up
```
