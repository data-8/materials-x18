FROM python:3.6

RUN pip3 install --no-cache-dir \
        datascience \
        nbconvert \
        jupyter_client \
        ipykernel \
        matplotlib \
        pandas \
        scipy \
        fakeokpy \
        ipywidgets

COPY . /srv/repo

WORKDIR /srv/repo
