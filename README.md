# Arcaea potential caalculator

## Introduction
Manually input Arcaea play scores by the user, record them, and display the user's best 30 on the homepage

## Install
```
git clone https://github.com/weiso131/Arcaea_potential_calculator.git
cd Arcaea_potential_calculator
pip install -r requirements.txt
```

## Migration
```
python manage.py makemigrations
python manage.py migrate
```

## Use crawl to get song data
- open a terminal
```
python manage.py start_crawl
```
- open another terminal
```
python manage.py process_tasks
```

## Run server
```
python manage.py runserver
```

