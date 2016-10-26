# For noprom-python:master-957c410
## RUN
```
docker run -it --name python -h python -v /Users/noprom/Documents/Dev/Python/Pro/scrapy-spiders:/app daocloud.io/noprom/noprom-python:master-957c410 /bin/bash
```
## INSTALL
```
rpm -iUvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.el7.art.noarch.rpm
yum -y install sqlite-devel mysql-devel
pip install scrapy scrapy-redis pysqlite python-mysql
```

# For 