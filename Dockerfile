FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y gnupg software-properties-common && apt-get update && apt-get install wget && wget -qO - https://qgis.org/downloads/qgis-2021.gpg.key | gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/qgis-archive.gpg --import && chmod a+r /etc/apt/trusted.gpg.d/qgis-archive.gpg && add-apt-repository "deb https://qgis.org/ubuntu $(lsb_release -c -s) main" && apt update && apt install -y qgis qgis-plugin-grass
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN apt-get install python pip -y
RUN pip install python-multipart
RUN pip install fastapi --upgrade
RUN pip install pydantic --upgrade
RUN pip install uvicorn --upgrade
RUN pip install aiofile --upgrade
RUN pip install Jinja2 --upgrade
COPY ./app /code/app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","80"]
