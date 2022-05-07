FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y tzdata
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install qgis -y
RUN apt-get install python3-pyqt5 -y
RUN apt-get install pyqt5-dev-tools -y
RUN apt-get install qttools5-dev-tools -y
RUN apt-get install -y x11-apps
RUN mkdir -p /run/user/1000
RUN chmod 0700 /run/user/1000
CMD ["/usr/bin/xeyes"]
ENV QT_DEBUG_PLUGINS=1
COPY . ./__main__.py
COPY . ./example.py
ENTRYPOINT ["python3", "example.py", "print_points","addasd"]