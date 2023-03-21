# Tutorial: How to import CSV file into MySQL

> Why we need to import CSV files into MySQL? 
> This is because some CSV files are too big, for example, 'products', 'order_product' and 'orders' and it doesn't make sense to create large amount of SQL insert statements to insert data into the tables (Think about your time and system resource). 

## Step 1: Insert small size csv files by using insert commands. 
#### 1.1 Please download [insert_statement.sql](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/cd9ed7ce36145741fef642f9475aa88997a38f5b/insert_statement.sql). 

#### 1.2 Open your MySQL Workbench (version 8.0 or above) in local computer and double click the connection you created in our previous tutorials. If you are not sure, please refer to our previous tutorial [here](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/76ef1f02eb3ab7554da441cea9538da7f169885c/tutorial.md).

![image](https://user-images.githubusercontent.com/7371969/226687895-8b3eb417-c14c-4104-a6ab-64a419bc9ba0.png)

#### *Note: Please make sure that you turn on your MySQL RDS database in AWS console. 

#### 1.3 Open insert_statement.sql in MySQL Workbench. Select all query, then click the execution icon. 

![image](https://user-images.githubusercontent.com/7371969/226690133-c058817a-b20a-4c78-9d6d-0795d4d63c12.png)

> use p3project;  -- select database

#### *Error: I find I make small mistake on column 'department' in Departments table. Data type should be vachar(50) and I have update the sql file. 
#### *How to fix: drop the table by 'drop table Departments', then re-execute create table statement for only table 'Departments'.
