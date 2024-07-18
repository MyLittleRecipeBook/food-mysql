# MySQL 공식 이미지 사용
FROM mysql:8.0

# # UTF-8 설정을 위한 파일 복사
# COPY ./my.cnf /etc/mysql/conf.d/

# 초기화 SQL 스크립트 복사
COPY ./init.sql /docker-entrypoint-initdb.d/

# 포트 노출
EXPOSE 3306

# 컨테이너 시작 시 실행될 명령어
CMD ["mysqld"]