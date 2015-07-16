#!/bin/bash

export PATH=$PATH:/usr/local/mysql/bin
mysql --user="root" --execute="CREATE USER 'graybeard'@'localhost'; GRANT ALL PRIVILEGES ON *.* TO 'graybeard'@'localhost';"
mysql --user="graybeard" --execute="CREATE DATABASE cfdb_flask;"
mysql --user="graybeard" --execute="set GLOBAL innodb_large_prefix=ON;"
