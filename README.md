# docker-python-selenium

## selenium chrome driver 
```
$ docker run -d -p 4444:4444 --name=selenium-chrome selenium/standalone-chrome

$ docker run -it --rm --network=container:selenium-chrome -v /e/project/docker/tools/selenium:/app selenium
```
