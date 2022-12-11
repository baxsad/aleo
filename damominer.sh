#!/bin/bash
export LANG=en_US.UTF-8
killall damominer
nohup ./damominer --address $1 --proxy aleo3.damominer.hk:9090 >> aleo.log 2>&1 &