FROM python:3.7-alpine

LABEL maintainer="Thomas TRAN <tran.thomasteddy@gmail.com>"

RUN addgroup --system oltho && adduser --system -s /bin/false oltho -g oltho

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN chown -R oltho:oltho /app

USER oltho

EXPOSE 8000

CMD python api.py
