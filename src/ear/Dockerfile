FROM python:3.8-slim-buster

ARG user_id=1000
ARG user_name=ear

EXPOSE 5000

RUN groupadd -g $user_id $user_name && \
useradd -u $user_id -g $user_id -d /home/$user_name -m $user_name

WORKDIR /opt

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

USER $user_id

ENV FLASK_APP=/opt/ear.py

ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]
