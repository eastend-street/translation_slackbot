FROM python:3.6

#インストールするものを書く
RUN pip install --upgrade -q \
pip \
slackbot \
google-cloud-translate

ENV LOG_LEVEL WARNING


COPY app /app
WORKDIR /app


RUN pip install --upgrade google-cloud-language
