#!/bin/bash

docker build -t climaapp .

docker rm -f samplerunning || true

docker run --name samplerunning \
-e API_KEY_PROYECTO=$API_KEY_PROYECTO \
climaapp
