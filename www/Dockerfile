FROM python:3.7-buster

RUN apt-get install bash
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --trusted-host paranoid-software.asuscomm.com -i http://paranoid-software.asuscomm.com:7201 paranoid_logy -U
RUN pip install --trusted-host paranoid-software.asuscomm.com -i http://paranoid-software.asuscomm.com:7201 paranoid_zookeeper -U

RUN ln -sf /dev/stdout /var/log/access.log && \
    ln -sf /dev/stderr /var/log/error.log

ADD . /usr/src/app

CMD ["bash", "run.sh"]
