FROM centos:8

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN dnf install python3 -y && pip3 install -r requirements.txt

CMD ["/usr/sbin/init"]
