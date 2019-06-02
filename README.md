
#Requirements:
 - python 3.6>=
 - elasticsearch 6>= | <7

#Quick Setup

```bash
# start elasticsearch in the background
./elasticsearch &

# activate virtualenv
source activate

# install requirements
pip install -r requirements.txt

#migrate and run
python manage.py migrate
python manage.py runserver
```

# Usecase
This is an aggregator for travel agencies.

# Data collection
Data is automatically pulled when command is run:
```bash
python manage.py update_destinations
```

Command goes trough all agencies and their matching selector from database and
updates destinations. Elasticsearch index is updated automatically.
