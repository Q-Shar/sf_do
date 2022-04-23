FROM python:3.8-slim

ENV WORKDIR="/exporter"
ENV DOWNLOADER="downloader.py"

ENV SITE=""
ENV DEST=""
ENV DEBUG=0

RUN mkdir $WORKDIR
RUN pip install wget

WORKDIR $WORKDIR

ADD ./$DOWNLOADER $WORKDIR

RUN chmod 700 $DOWNLOADER
ENTRYPOINT python $DOWNLOADER --site=${SITE} --dest=${DEST} --debug=${DEBUG}