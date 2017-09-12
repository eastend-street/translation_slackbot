# any_value : your any_value that written in build_sample.sh
sudo docker stop `sudo docker ps -f ancestor=any_value:latest -q`$

sudo docker run -it \
        # any_key_value : your api key file
        -e "GOOGLE_APPLICATION_CREDENTIALS=keys/any_key_value" \
        # any_directory : own directory
        -v /home/any_directory/app:/app \
        # 0000:0000 : your port number of Docker
        -p 0000:0000 \
        # any_value : your any_value that written in build_sample.sh
        any_value \
        bash
