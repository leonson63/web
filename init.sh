#!bash
# add gunicorn config
# sudo ln -s etc/hello.py /etc/gunicorn.d/hello.py
# add nginx config
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/conf.d/add.conf
sudo ln -sf /home/box/web/gunicorn.conf /etc/gunicorn.d/cfg

# run nginx
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart

# run gunicorn
sudo /etc/init.d/gunicorn restart cfg
#gunicorn -c "../gunicorn.conf" ask.wsgi --daemon

. sql.sh

cd ~/web/ask

