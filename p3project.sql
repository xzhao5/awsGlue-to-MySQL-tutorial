
# This script made by Tom Zhao. This is use for team project P3.

# check if there is any database.
select database();

# create a database.
create database p3project;

# select the database.
use p3project;

#create the 'order' table
CREATE TABLE `Orders` (
  `order_id` int,
  `user_id` int,
  `eval_set` varchar(10),
  `order_number` int,
  `order_dow` int,
  `order_hour_of_day` int,
  `days_since_prior_order` int,
  PRIMARY KEY (`order_id`)
);

#create the 'order_product' table
CREATE TABLE `Order_product` (
  `order_id` int,
  `product_id` int,
  `add_to_cart_order` int,
  `reordered` int,
  PRIMARY KEY (`order_id`, `product_id`)
);

#create the 'products' table
CREATE TABLE `Products` (
  `product_id` int,
  `product_name` varchar(160),
  `aisle_id` int,
  `department_id` int,
  PRIMARY KEY (`product_id`)
);

# create the 'Departments' table
CREATE TABLE `Departments` (
  `department_id` int,
  `department` varchar(50),
  PRIMARY KEY (`department_id`)
);

# create the 'Aisles' table
CREATE TABLE `Aisles` (
  `aisle_id` int,
  `aisle` varchar(30),
  PRIMARY KEY (`aisle_id`)
);

