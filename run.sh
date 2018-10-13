#!/bin/sh

docker run -it --rm --network=container:selenium-chrome -v /e/project/docker/tools/selenium:/app/selenium selenium
