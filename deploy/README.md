# Deploy

Deployment in ubuntu 16.04 with:

* Nginx
* Supervisord
* Cron

## First setup

### Get respository

```
cd ~
git clone https://github.com/escrichov/gorgonzola
cd gorgonzola
cp gorgonzola/settings_prod.py gorgonzola/settings.py
```

### Generate random key
```
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```
then save it in gorgonzola/settings.py

### Create virtualenv
```
virtualenv --python=python3 env
source/env/bin/activate
```

### Copy static files and migrate database
```
python manage.py migrate
python manage.py collecstatic
cp -r root_files/* staticroot/
```


### Install nginx

```
sudo apt-get install nginx
rm /etc/nginx/sites_enabled/default
cp ~/gorgonzola/deploy/nginx.conf /etc/nginx/sites_available/gorgonzola.fun.conf
ln -s /etc/nginx/sites_available/gorgonzola.fun.conf /etc/nginx/sites_enabled/gorgonzola.fun.conf
```

Edit 'root' and 'server_name' in /etc/nginx/sites_enabled/gorgonzola.fun.conf

```
sudo service nginx restart
```

### Install cron job

```
crontab -e
```

Copy cron.job content and edit root directory


### Install supervisor

```
sudo apt-get install supervisor
cp ~/deploy/supervisor.conf /etc/supervisor/conf.d/gorgonzola.fun.conf
```

Modify root directory in /etc/supervisor/conf.d/gorgonzola.fun.conf

```
sudo service supervisor restart
```


## Upload new changes
```
cd ~/gorgonzola
git pull
python manage.py migrate
python manage.py collecstatic
cp -r root_files/* staticroot/
sudo service supervisor restart
```

