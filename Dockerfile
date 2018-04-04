FROM python:3.6
RUN pip install pipenv
COPY . /src
RUN cd src && pipenv install --system
WORKDIR /src
ENTRYPOINT ["gunicorn", "--config=gconfig.py", "app"]
