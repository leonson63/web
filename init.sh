#!bash
# add gunicorn config
# sudo ln -s etc/hello.py /etc/gunicorn.d/hello.py
# add nginx config
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/conf.d/add.conf

# run nginx
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart

# run gunicorn
cd ~/web/ask
gunicorn -c "../gunicorn.conf" ask.wsgi --daemon

. sql.sh
