FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

RUN apt-get update && \
    apt-get install -y zsh time tzdata tree git curl

RUN chsh -s /bin/zsh

RUN apt-get update && \
    apt-get install -y gcc-9 g++-9 python3.8 python3-pip pypy3 nodejs npm

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 30 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 30 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.8 30 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 30 && \
    update-alternatives --install /usr/bin/pypy pypy /usr/bin/pypy3 30 && \
    update-alternatives --install /usr/bin/node node /usr/bin/nodejs 30

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/atcoder/ac-library.git /lib/ac-library
ENV CPLUS_INCLUDE_PATH /lib/ac-library

RUN pip install git+https://github.com/not522/ac-library-python && \
    pip install git+https://github.com/grantjenks/python-sortedcontainers

RUN pip install online-judge-tools==11.5.1
RUN npm install -g atcoder-cli@2.2.0

RUN acc config-dir && \
    acc config default-template python && \
    acc config default-test-dirname-format test

RUN echo 'alias accs="acc s --skip-filename -- --guess-python-interpreter pypy -w 0 -y"' > ~/.zshrc 

WORKDIR /root/problems
WORKDIR /root/library