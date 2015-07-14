#!/bin/bash

export PATH=$PATH:/usr/local/mysql/bin
mysql --user="root" --execute="CREATE USER 'graybeards'@'localhost'; GRANT ALL PRIVILEGES ON *.* TO 'graybeards'@'localhost';"
mysql --user="graybeards" --execute="CREATE DATABASE cfdb_flask;"
mysql --user="graybeards" --execute="set GLOBAL innodb_large_prefix=ON;"