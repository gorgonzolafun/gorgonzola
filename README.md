# Gorgonzola.fun 
[![Build Status](https://travis-ci.org/gorgonzolafun/gorgonzola.svg?branch=master)](https://travis-ci.org/gorgonzolafun/gorgonzola)

This project is built to know if there is Gorgonzola in the daily menu of the [Portami Via](http://daringfireball.net/projects/markdown/syntax) restaurant in Valencia (Spain).

## Development

```
cd ~
git clone https://github.com/escrichov/gorgonzola
cd gorgonzola
cp gorgonzola/settings_dev.py gorgonzola/settings.py
```

### Create virtualenv
```
virtualenv --python=python3 env
source/env/bin/activate
```

### Copy static files and migrate database
```
python manage.py migrate
python manage.py collecstatic
```

### Run development server
```
python manage.py runserver
```

### Run script
```
python manage.py gorgonzola_status
```

### Run tests
```
python manage.py test
```
