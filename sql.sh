#! /bin/bash
mysql -uroot -e "create database qadb"
mysql -uroot -e "create user 'box' IDENTIFIED BY 'boxpass'"
mysql -uroot -e "GRANT ALL ON *.* TO 'box'"
