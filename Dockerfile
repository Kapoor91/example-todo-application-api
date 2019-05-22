FROM python:3.7-alpine

LABEL maintainer="Thomas TRAN <tran.thomasteddy@gmail.com>"

ENV SERVICE_ACCOUNT=oltho \
    PROJECT_NAME=example_todo_application_api


RUN apk update \
  && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2==2.8.2 \
  && apk del build-deps

# creation of service account and directory for project
RUN addgroup --system ${SERVICE_ACCOUNT} \
  && adduser --system -s /bin/false ${SERVICE_ACCOUNT} -G ${SERVICE_ACCOUNT} \
  && mkdir /home/${SERVICE_ACCOUNT}/${PROJECT_NAME}

# copy application code
WORKDIR /home/${SERVICE_ACCOUNT}/${PROJECT_NAME}
COPY . .
RUN chown -R ${SERVICE_ACCOUNT}:${SERVICE_ACCOUNT} /home/${SERVICE_ACCOUNT}/${PROJECT_NAME} \
    && chmod +x entrypoint.sh

# installation of application dependencies
RUN pip install -r requirements.txt
USER ${SERVICE_ACCOUNT}


EXPOSE 8000
ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "web" ]
