# MySQL 공식 이미지 사용
FROM mysql:lts

# # UTF-8 설정을 위한 파일 복사
# COPY ./my.cnf /etc/mysql/conf.d/

# 초기화 SQL 스크립트 복사
COPY ./init.sql /docker-entrypoint-initdb.d/

# 환경 변수 설정
ARG MYSQL_ROOT_PASSWORD
ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD

ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}

# 포트 노출
EXPOSE 3306

# 컨테이너 시작 시 실행될 명령어
CMD ["mysqld"]
