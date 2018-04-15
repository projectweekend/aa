#!/usr/bin/env bash
aws ecr get-login --no-include-email --region us-east-1 | bash && \
docker build -t aa-api . && \
docker tag aa-api:latest 421713074241.dkr.ecr.us-east-1.amazonaws.com/aa-api:latest && \
docker push 421713074241.dkr.ecr.us-east-1.amazonaws.com/aa-api:latest
