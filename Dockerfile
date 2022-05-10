# Writer: Ha Jeong-Hyun
FROM python:3.9

# update upgrade
RUN apt update -y
RUN apt upgrade -y

# install nessesary tools
RUN apt install -y sudo gcc make
RUN apt install -y python3-dev python3-pip
RUN apt install -y libffi-dev
RUN apt install -y build-essential
RUN apt install -y default-libmysqlclient-dev
RUN apt install -y vim
RUN apt install -y git

# set application location
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
# copy requirements.txt for install package
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
