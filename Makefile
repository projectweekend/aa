docker_build_push:
	docker build -t projectweekend/aa . && \
	docker push projectweekend/aa

ecr_build_push:
	aws ecr get-login --no-include-email --region us-east-1 | bash && \
	docker build -t aa-api . && \
	docker tag aa-api:latest 421713074241.dkr.ecr.us-east-1.amazonaws.com/aa-api:latest && \
	docker push 421713074241.dkr.ecr.us-east-1.amazonaws.com/aa-api:latest

pytest:
	pipenv run pytest --cov=aa --cov-report=html

run_docker:
	docker run -p 8000:8000 projectweekend/aa

run_local:
	pipenv run gunicorn --config=gconfig.py --reload aa.app
