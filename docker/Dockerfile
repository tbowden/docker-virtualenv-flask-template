FROM ubuntu:xenial  as dev

RUN echo "deb http://ppa.launchpad.net/ubuntugis/ppa/ubuntu xenial main" > /etc/apt/sources.list.d/ubuntugis-stable.list && \
    echo "deb-src http://ppa.launchpad.net/ubuntugis/ppa/ubuntu xenial main" >> /etc/apt/sources.list.d/ubuntugis-stable.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 089EBE08314DF160

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get install -y \
    --no-install-recommends \
    tzdata nginx gosu locales \
    gcc python3 libpython3.4 python3-dev python3-pip \
    vim git screen curl lynx wget sudo && \
    rm /etc/localtime && ln -s /usr/share/zoneinfo/Australia/Perth /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata 
    
RUN adduser --gecos delivery --uid 2000 --disabled-password delivery && \
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> /etc/bash.bashrc
RUN echo "VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> /etc/environment && \
    echo "WORKON_HOME=$HOME/.virtualenvs" >> /etc/environment && \
    echo "PROJECT_HOME=$HOME/python_proj"  >> /etc/environment && \
    echo "delivery ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/delivery

RUN locale-gen  en_AU.UTF-8
RUN update-locale LC_ALL=en_AU.utf8
ENV LC_ALL=en_AU.UTF-8

ENV VIRTUALENVWRAPPER_PYTHON /usr/bin/python3
ENV WORKON_HOME /home/delivery/.virtualenvs
ENV PROJECT_HOME /home/delivery/python_proj

RUN pip3 install setuptools virtualenvwrapper
WORKDIR /root/
RUN mkdir python_proj .virtualenvs

USER delivery
WORKDIR /home/delivery/

RUN mkdir python_proj .virtualenvs

RUN ["/bin/bash", "-ic", "mkproject sample"]

WORKDIR $PROJECT_HOME/sample
COPY --chown=delivery ./requirements.txt .

RUN ["/bin/bash", "-ic", "workon sample && \
    pip install -r requirements.txt"]
COPY --chown=delivery ./include/ ./

EXPOSE 5000

ENTRYPOINT ["./start"]

# docker build -t sample:latest -t sample:0.1 .
# docker exec -it sample /bin/bash
# without ENTRYPOINT or 'start script' running 'something'
# docker run -d -it --rm -h sample --name sample -p 127.0.0.1:5000:5000 sample:latest /bin/bash
# with ENTRYPOINT running flask (or something)
# docker run -d     --rm -h sample --name sample -p 127.0.0.1:5000:5000 sample:latest
