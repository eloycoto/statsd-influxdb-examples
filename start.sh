#!/bin/bash

start_statsd(){
   result=$(docker run -d\
            -e INFLUXDB_HOST='influxdb' -e INFLUXDB_PORT='8086' \
            -e INFLUXDB_NAME='demo' -e INFLUXDB_USER='root' \
            -e INFLUXDB_PASS='root' \
            --name statsd \
            -p 8125:8125/udp\
             --link influxdb:influxdb\
            eloycoto/statsd-influxdb)
}

start_influxdb(){
   mkdir -p /opt/influxdb
   mkdir -p /opt/log
   result=$(docker run -d\
            -e PRE_CREATE_DB="demo" -e INFLUXDB_INIT_PWD="root"\
            --name influxdb \
            -p 8083:8083 -p 8086:8086 --expose 8090 --expose 8099\
            -v /opt/influxdb/:/data/ \
            -v /opt/log:/var/log \
            tutum/influxdb)
   echo $result

}

start_grafana(){

    mkdir -p /opt/grafana/data
    result=$(docker run -d \
            -p 3000:3000 \
            -v /opt/grafana/data:/opt/grafana/data \
            --name grafana\
            --link influxdb:influxdb\
            grafana/grafana)
}

kill_stop(){
    docker stop $1
    docker rm $1
}

function main(){
    kill_stop influxdb
    start_influxdb
    kill_stop statsd
    start_statsd
    kill_stop grafana
    start_grafana
}

main

