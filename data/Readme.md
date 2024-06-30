### docker 띄우기
docker build -t aaa:1  --build-arg MYSQL_ROOT_PASSWORD=test1234   --build-arg MYSQL_DATABASE=mlr-dev-db-tlb   --build-arg MYSQL_USER=test   --build-arg MYSQL_PASSWORD=test1234 .
docker run -d -p 3306:3306 --name aaa aaa:1


### container 외부에서 파일 내부로 옮기기
docker cp recipes_metadata.csv [컨테이너명]:/var/lib/mysql-files/recipes_metadata.csv
docker cp seasonal_process.csv [컨테이너명]:/var/lib/mysql-files/seasonal_process.csv
docker exec -it [컨테이너명] bash

###  container 내부 
mysql -u root -p

USE `mlr-dev-db-tlb`;

LOAD DATA INFILE '/var/lib/mysql-files/recipes_metadata.csv' 
INTO TABLE Recipe
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(recipe_id, recipe_title, recipe_thumbnail, situ_no, cate_no);

LOAD DATA INFILE '/var/lib/mysql-files/seasonal_process.csv'
INTO TABLE Seasonal
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(seasonal_name, seasonal_month, seasonal_image);
