# any_value : choice your any_value that written in build_sample.sh
sudo docker stop `sudo docker ps -f ancestor=any_value:latest -q`$

sudo docker run -it \
        #  any_key_value : choice your api key file
        -e "GOOGLE_APPLICATION_CREDENTIALS=keys/any_key_value" \
        -v /home/BIZOCEAN/junya_yamada/botForSlack20170906/app:/app \
        # 0000:0000 : choice your port number of Docker
        -p 0000:0000 \
        # any_value : choice your any_value that written in build_sample.sh
        any_value \
        bash
