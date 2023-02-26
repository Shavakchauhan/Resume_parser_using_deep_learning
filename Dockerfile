FROM python:3.7.13
COPY ./deployment/ /app
WORKDIR /app
RUN wget -O /app/generated_model.zip "https://www.dropbox.com/sh/22yw4b7jfk0edmp/AADsvQ9Gm9p0X0dsLgCQD8Z4a?dl=1"
RUN apt-get update && \
    apt-get install -y wget zip unzip
RUN unzip generated_model.zip -x /
RUN mkdir /app/generated_model
RUN mv -v model-best /app/generated_model/
RUN rm -rf generated_model.zip
RUN rm -rf model-last
# RUN cp app/generated_model/ app/
# RUN rm -rf generated_model/*

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir gunicorn 
RUN apt-get update && \
apt-get install -y --no-install-recommends default-jdk && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir tika
EXPOSE 5000
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]

