FROM python:latest

WORKDIR /flask-app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . . 

EXPOSE 5000

CMD [ "python","main.py" ]