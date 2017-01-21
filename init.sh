#!bash
# add gunicorn config
# sudo ln -s etc/hello.py /etc/gunicorn.d/hello.py
# add nginx config
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf etc/nginx.conf /etc/nginx/conf.d/add.conf

# run nginx
sudo /etc/init.d/nginx restart

# run gunicorn
cd ~/web/ask
gunicorn -v -с ../gunicorn.conf ask.wsgi:application

