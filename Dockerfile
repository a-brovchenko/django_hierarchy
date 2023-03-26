FROM python:3.8.16-alpine3.17
EXPOSE 8000

RUN \
    apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev

WORKDIR /app
COPY requirements.txt ./
RUN \
    pip install --no-cache-dir -r requirements.txt ;\
    apk del .build-deps

COPY . ./

WORKDIR /app
ENTRYPOINT [ "/app/entrypoint.sh" ]
