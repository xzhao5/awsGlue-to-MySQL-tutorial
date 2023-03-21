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
#### 2.1 Open the table: for example, I suppose to import 'products' table. 
#### 2.11 Right click the table on your left pannel and then click 'Select Rows -Limit 1000'.

![image](https://user-images.githubusercontent.com/7371969/226698759-d45fefbf-c4b6-403c-935a-ecebadcd298f.png)

#### 2.12 Click the icon I highlighted with red color. 

![image](https://user-images.githubusercontent.com/7371969/226699029-154692e4-f6da-43e3-b9bc-f503b24e80a8.png)

#### 2.13 Select 'products.csv' and click 'Next'.

![image](https://user-images.githubusercontent.com/7371969/226699495-5ab0921b-8ef7-4eab-800b-421059d46a9a.png)

#### 2.14 Select 'Using existing table:' with the matching table, then click 'Next'.

![image](https://user-images.githubusercontent.com/7371969/226703081-d508dc28-fa94-4b56-9ee8-dfc80cc19420.png)

#### 2.15 Check if all columns are correct, then click 'Next'.  

![image](https://user-images.githubusercontent.com/7371969/226703522-f5c2ab37-b226-479d-8a48-2300c7d18d3a.png)

#### 2.16 Click 'Next'.  

![image](https://user-images.githubusercontent.com/7371969/226703831-a20657fb-4593-48e9-8bcf-a59e707d8c98.png)

#### 2.17 Wait for a few mins to import .csv file into the table. 

![image](https://user-images.githubusercontent.com/7371969/226704106-74e018c4-7cc5-4e76-ae5e-af9ba0eb258e.png)

#### 2.2 Verify if data has been loaded into table:

> SELECT * FROM p3project.Products;

![image](https://user-images.githubusercontent.com/7371969/226709942-9f9d3c31-20e2-44b8-a0a3-c34e3903744d.png)

## Step 3: Another Method to import .csv file into tables:
### if you feel the process is too slow and then try this method by using mysql command line.
#### 3.1 Install mysql on your command line (My example is using ubunto command line in windows system).

#### verify if you has mysql in ubunto command line:

> mysql

#### I do not have mysql client there so I type this command line:

> sudo apt install mysql-client-core-8.0

![image](https://user-images.githubusercontent.com/7371969/226710862-11f3e179-94a8-4f5c-926d-e89503f0087f.png)

#### check the version of mysql client:

> mysql --version

![image](https://user-images.githubusercontent.com/7371969/226711238-cfa6cb22-54b4-4370-8ba0-ac84c5209725.png)

#### 3.1 copy the .csv file from other place into Home directory:

#### My csv file is under the folder: /mnt/c/Users/JR studying PC/Downloads/imba_data. What I do is go into the folder, execute 'cp product.csv ~/' to copy from that location to home directly. (The command means -> cp 'your folder' 'Home Directory')

![image](https://user-images.githubusercontent.com/7371969/226712788-ab2e4a2d-deb4-4b0a-a7a2-82357a6cd8a7.png)

#### 3.2 Go to Home directory, then we now log in MySQL from local computer:

> cd ~/

>  mysql -h your_RDS_endpoints -P 3306 -u admin -p

![image](https://user-images.githubusercontent.com/7371969/226713660-f15911a9-c229-483d-b6c2-ee2e2993d6e8.png)

#### 3.3 


