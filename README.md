# Intro
This is the code for https://blog.michaelyin.info/scrapy-tutorial-series-web-scraping-using-python/

# Setup
Install Python3: `$ brew install python3`
Install MySQL: `$brew install mysql`, which install MySQL without password.
To start MySQL: `mysql.server start` and then connect: `mysql -uroot`
```
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To have launchd start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  mysql.server start
```
# Run
Virtual Env:
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
Install packages: `$ pip3 install -r requirements.txt`, which include scrapy
ipython, SQLAlchemy, mysqlclient

# Debug
Use `scrapy shell` to debug. By default, Python Shell is used, iPython Shell is much more powerful.
for instance, you can use %paste once iPython is installed.
