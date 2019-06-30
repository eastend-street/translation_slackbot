# Translation Slack Bot

Translation Slack Bot is a multilingual translation bot on Slack using Google Cloud Translation API. 
You can translate English to Japanese, Japanese to English, Other languages to English. It automatically detects the language and translates it.

## Requirement
Docker, Python3, Google Cloud Translation AP

## Usage

### 1. Download

```
git clone https://github.com/eastend-street/translation_slackbot.git
```

### 2. Make build.sh like build.sh.sample

You don't have to change this code, just copy. If you want to change docker image tag name, edit it. Default name is "translation_slack_bot".

```
sudo docker stop `sudo docker ps -f ancestor= translation_slack_bot:latest -q`$
sudo docker build -t translation_slack_bot .$
```

### 3. Make run.sh like run.sh.sample

Write your Google Cloud Translation API Key and directory in run.sh

```
sudo docker stop `sudo docker ps -f ancestor=translation_slack_bot:latest -q`$

sudo docker run -it \
        -e "GOOGLE_APPLICATION_CREDENTIALS=keys/your_goolgle_translate_api_key" \
        -v /home/path/to/your/directory/app:/app \
        translation_slack_bot \
        bash
```
### 4. Create Slack app
https://api.slack.com/apps?new_app=1

### 5. Build & Run

Build
```
./build.sh
```

Run
```
./run.sh
```