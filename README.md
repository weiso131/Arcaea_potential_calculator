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
- change the Arcaea_score/Arcaea_score/settings.py log filename
```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'your path of task.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}
```

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

## demo
### home page of user
![image](https://github.com/user-attachments/assets/99655d69-f61b-4188-a0ab-963e577f4357)

### edit playing history
![image](https://github.com/user-attachments/assets/98a39fc7-de1c-4eeb-8601-1ca5b52b7124)

