FROM python:3.8.13-alpine3.15

RUN pip install psycopg2-binary==2.9.3 \
    flask==2.1.1 \
    configparser==5.1.0

EXPOSE 80

ENV WORKDIR="/srv/app"
ENV APP="web.py"

RUN mkdir $WORKDIR && mkdir $WORKDIR/conf

WORKDIR $WORKDIR

ADD ./app/$APP $WORKDIR
ADD ./app/conf/web.conf $WORKDIR/conf

RUN chmod 700 $APP

VOLUME $WORKDIR:$WORKDIR

ENTRYPOINT python $APP