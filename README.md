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

### 4. install code formatter
```bash
pip install pre-commit
```
