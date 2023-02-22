FROM python:3.7.13
COPY ./deployment/ /app
WORKDIR /app
RUN wget --header="Host: uc6cf3ca3ef222de285c0b4d54a3.dl.dropboxusercontent.com" --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" --header="Accept-Language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7" --header="Referer: https://www.dropbox.com/" "https://uc6cf3ca3ef222de285c0b4d54a3.dl.dropboxusercontent.com/zip_download_get/BaYzYbtJd6GEqoRHA2_ue7m_PlkD1NT102QYDXiBAOAVCFljn2cF52dThB2wlQJpDUjFJk4yX3fYG-NBXRLD2TfqvpEc-_m2rRjJUvLx1uCEEw?_download_id=967654488633847935407271596866167117380549524966336093431067955&_notify_domain=www.dropbox.com&dl=1" -c -O 'generated_model.zip'
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

