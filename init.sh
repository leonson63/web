#!bash
# add gunicorn config
sudo ln -s etc/hello.py /etc/gunicorn.d/hello.py
# add nginx config
sudo ln -s etc/nginx.conf /etc/nginx/conf.d/add.conf

# run gunicorn
#sudo gunicorn -v -с /etc/gunicorn.d/hello.py hello:wsgi
sudo /etc/init.d/gunicorn restart
# run nginx
sudo /etc/init.d/nginx restart
