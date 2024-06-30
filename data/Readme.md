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
