FROM python:3.6

RUN pip3 install --no-cache-dir \
        datascience \
        nbconvert \
        jupyter_client \
        ipykernel \
        matplotlib \
        pandas \
        ipywidgets \
        scipy \
        git+https://github.com/yuvipanda/fakeokclient.git@3798933

COPY . /srv/repo

WORKDIR /srv/repo
