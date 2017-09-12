FROM python:3.6

#インストールするものを書く
RUN pip install --upgrade -q \
pip \
nltk \
slackbot \
google-cloud-translate

COPY app /app
WORKDIR /app

RUN pip install --upgrade google-cloud-language

