-- set up datatbase
CREATE DATABASE IF NOT EXISTS hbnb_dev_db
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'