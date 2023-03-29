# modesec-log-analyzer
## This is a sinple log analyzer for modsec written in Django.

### Requirements
- Django
- PostgreSQL
- pip3
- pipenv3

## Getting started
- clone the project `git clone https://github.com/efocoder/modesec-log-analyzer.git`
- cd `modsec-log-analyzer`
- `pipenv install`
- copy `env.example` to `.env` and provide the credentials
- `python3 manage.py migrate`
- `python3 manage.py runserver`
- Now access the application in your browser `http://localhost:8000`