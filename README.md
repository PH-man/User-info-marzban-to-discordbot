
# Userinfo-marzban-to-discordbot
Script to collect user data from your Marzban panel and discord-bot send it to your DM

## Features

- #### customizable prefix 
- #### customizable commands
- #### collect users info from marzban panel and sent to requested user


## Requirment
##### ubuntu 20.04+
\
or
##### Windows 10
##### Python 3.11.4+
##### pip 24.0
##### git 2.40.0+

## How to use on LInux
to update your packages
        
    sudo apt update && sudo apt upgrade -y
to install python
    
    sudo apt install python3

then to clone script

```bash 
sudo git clone  https://github.com/PH-man/User-info-marzban-to-discordbot.git

```
```bash
cd Userinfo-marzban-to-discordbot-main
```
to install requirment libraries for script
```bash
 sudo pip install -r  requirments.txt
```
or
    
    sudo pip3 install -r requirments.txt

#### then to stat script in background of ubuntu

    sudo nohup python index.py &

or
    
    sudo nohup python3 index.py &

### to kill the script process

    ps aux | grep index.py

then copy the process id and replce it with process id

    kill -9 -process id-

    

    

## How to use in windows
install python from official [Python site](https://www.python.org/downloads/).

then open cmd type 
```bash 
git clone https://github.com/PH-man/User-info-marzban-to-discordbot.git
```
unzip downloaded file and navigate to it

then to install requirment libraries for script
```bash
pip install -r requirements.txt
```
then to run script 
```bash
python index.py
```
## how to config

in config.py file replace your real panel url and discord Channel id in  Specified place 

like LOGIN_URL = "(Replace your url and port with https://)/api/admin/token" only replace your url and port like this LOGIN_URL = "sarab.google.com:443/api/admin/token"
and other Parameters
## 🔗 Link for contacting with me
#### if you found a bug or suggestion to improve a code I will be happy to contact with me
[![portfolio](https://patrolavia.github.io/telegram-badge/chat.png)](https://ph_man.t.me)
