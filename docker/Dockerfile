FROM ubuntu:16.04
RUN apt-get update \
    && apt-get -y install sudo
RUN sudo apt-get -y install \
    curl \
    python-software-properties \
    # Must have this line for "add-apt-repository" to work
    software-properties-common

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN npm install npm@latest

# install python
RUN sudo add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN sudo apt-get -y install python3.6
RUN sudo apt-get -y install python3-pip

# install tensorspacejs
RUN python3.6 -m pip install tensorspacejs
RUN echo "alias python=python3.6" >> ~/.bash_aliases
RUN . ~/.bash_aliases

# initalize tensorspacejs
RUN tensorspacejs_converter -init

WORKDIR /data

CMD ["bash", "/data/converter.sh"]
