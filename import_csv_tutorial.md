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

#### Please make sure you select the database, otherwise you won't run the query !!!

> use p3project;  -- select database

#### *Error: I find I make small mistake on column 'department' in Departments table. Data type should be vachar(50) and I have update the sql file. 
#### *How to fix: drop the table by 'drop table Departments', then re-execute create table statement for only table 'Departments'.

#### 1.4 Double check if they have been inserted into the table by the below sql queries:

> SELECT * FROM Aisles;
> Select * from Departments;

#### Now you should get the result as below:

![image](https://user-images.githubusercontent.com/7371969/226696983-4525d724-eb16-435b-9519-c7ea85b29c47.png)

## Step 2: Insert large .csv file by importing via MySQL:
#### 2.1 Open the table: for example, I suppose to import products table. 
#### 2.11 Right click the table on your left pannel and then click 'Select Rows -Limit 1000'.

![image](https://user-images.githubusercontent.com/7371969/226698759-d45fefbf-c4b6-403c-935a-ecebadcd298f.png)

#### 2.12 Click the icon I highlighted with red color. 

![image](https://user-images.githubusercontent.com/7371969/226699029-154692e4-f6da-43e3-b9bc-f503b24e80a8.png)

#### 2.13 

![image](https://user-images.githubusercontent.com/7371969/226699495-5ab0921b-8ef7-4eab-800b-421059d46a9a.png)
