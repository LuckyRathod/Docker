From ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY app.py /opt/app.py 
CMD ["python3","/opt/app.py"]