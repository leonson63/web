#!bash
# add gunicorn config
sudo ln -s etc/hello.py /etc/gunicorn.d/hello.py
# add nginx config
sudo ln -s etc/nginx.conf /etc/nginx/conf.d/add.conf

# run nginx
sudo /etc/init.d/nginx restart

# run gunicorn
sudo gunicorn -v -с /etc/gunicorn.d/hello.py web/hello:wsgi

