# any_value : choice any name
sudo docker stop `sudo docker ps -f ancestor= any_value:latest -q`$
sudo docker build -t any_value .$
