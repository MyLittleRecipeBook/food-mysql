-- 0. 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS `mlr-dev-db-tlb`;

-- 1. 데이터베이스 사용
USE `mlr-dev-db-tlb`;

-- 사용자 생성 및 권한 부여
CREATE USER IF NOT EXISTS 'test'@'%' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON `mlr-dev-db-tlb`.* TO 'test'@'%';
FLUSH PRIVILEGES;

-- 2-1. User 테이블 생성
CREATE TABLE IF NOT EXISTS User (
    user_id VARCHAR(255) ,
    user_email VARCHAR(255),
    user_provider ENUM('kakao', 'naver', 'google') ,
    PRIMARY KEY (user_id)
);

-- 2-2. Session 테이블 생성
CREATE TABLE IF NOT EXISTS Session(
  user_id VARCHAR(255) ,
  access_token VARCHAR(255) ,
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- 2-3. MyPage 테이블 생성
CREATE TABLE IF NOT EXISTS MyPage(
  user_id VARCHAR(255),
  user_nickname VARCHAR(255),
  user_subscription BOOLEAN,
  cate_no INT,
  situ_no INT,
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- 2-4. Recipe 테이블 생성
CREATE TABLE IF NOT EXISTS Recipe(
  recipe_id INT ,
  recipe_title VARCHAR(255),
  recipe_thumbnail VARCHAR(255),
  situ_no INT,
  cate_no INT,
  PRIMARY KEY (recipe_id)
);

-- 2-5. Bookmark 테이블 생성
CREATE TABLE IF NOT EXISTS Bookmark (
  user_id VARCHAR(255),
  recipe_id INT,
  PRIMARY KEY (user_id, recipe_id),
  FOREIGN KEY (user_id) REFERENCES User(user_id),
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id)
);

-- 2-6. Ingredient 테이블 생성
CREATE TABLE IF NOT EXISTS Ingredient (
  ingredient_id INT AUTO_INCREMENT,
  ingredient_name VARCHAR(255),
  PRIMARY KEY (ingredient_id)
);

-- 2-7. Ingredient Search 테이블 생성
CREATE TABLE IF NOT EXISTS IngredientSearch (
  recipe_id INT,
  ingredient_id INT,
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
);

-- 2-8. SearchFilter 테이블 생성
CREATE TABLE IF NOT EXISTS SearchFilter (
  user_id VARCHAR(255),
  ingredient_id INT,
  PRIMARY KEY (user_id, ingredient_id),
  FOREIGN KEY (user_id) REFERENCES User(user_id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
);

-- 2-9. Refrigerator 테이블 생성
CREATE TABLE IF NOT EXISTS Refrigerator (
  refrigerator_id INT AUTO_INCREMENT,
  refrigerator_name VARCHAR(255),
  refrigerator_type INT,
  user_id VARCHAR(255),
  PRIMARY KEY (refrigerator_id),
  FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- 2-10. RefrigeratorIngredients 테이블 생성
CREATE TABLE IF NOT EXISTS RefrigeratorIngredients (
  refrigerator_ing_id INT AUTO_INCREMENT,
  refrigerator_id INT,
  refrigerator_ing_name VARCHAR(255),
  expired_date VARCHAR(255),
  enter_date VARCHAR(255),
  color VARCHAR(255),
  PRIMARY KEY (refrigerator_ing_id),
  FOREIGN KEY (refrigerator_id) REFERENCES Refrigerator(refrigerator_id)
);

-- 2-11. Seasonal 테이블 생성
CREATE TABLE IF NOT EXISTS Seasonal (
  seasonal_id INT AUTO_INCREMENT,
  seasonal_name VARCHAR(255),
  seasonal_month INT,
  seasonal_image VARCHAR(255),
  PRIMARY KEY (seasonal_id)
);

-- 2-12. Subscription 테이블 생성
CREATE TABLE IF NOT EXISTS Subscription (
  user_id VARCHAR(255),
  user_email VARCHAR(255),
  user_nickname VARCHAR(255),
  cate_no INT,
  situ_no INT,
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES User(user_id)  
);
