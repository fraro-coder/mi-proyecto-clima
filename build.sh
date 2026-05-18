#!/bin/bash

cat > Dockerfile <<EOF
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "app_clima.py"]
EOF

docker build -t climaapp .

docker run --name samplerunning \
-e API_KEY_PROYECTO=$API_KEY_PROYECTO \
climaapp
