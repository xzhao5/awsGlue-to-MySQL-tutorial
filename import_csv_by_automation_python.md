# Implementation Plan: How to import CSV file into MySQL by Cli Automation 

> Scenario: Basaed on last turtorial:[Tutorial: How to import CSV file into MySQL](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/29850ac9cd86ae7feee4362aef67ee36f8958681/import_csv_tutorial.md), There are two methods available for importing large CSV files into MySQL: using the import wizard in MySQL Workbench or MySQL CLI. However, during the process, it has been discovered that importing large CSV files through the MySQL Workbench GUI is very slow. On the other hand, a disadvantage of using MySQL CLI is that it may not be familiar to some team members who are not accustomed to using Linux commands.
> Are there any steps I can take to enhance my approach? I am currently devising an implementation plan and searching for a technique that can facilitate the automatic import of all CSV files. At present, I am executing the second method, which involves utilizing MySQL CLI.

## Step 1: Download the python code that I wrote, then copy this to Home Directory:  
#### In my example, I use Ubuntu in Windows 10 system. I assume that my python code has been download in the path: 'mnt/c/Users/ggbne/Downloads/'.

![image](https://user-images.githubusercontent.com/7371969/227112438-fbfa38d0-6969-44c6-983f-a095c48c2d2b.png)

#### 1.1 Copy main.py to Home Direcotry: 

![image](https://user-images.githubusercontent.com/7371969/227112655-f2ed9afa-d4d5-4c75-87f6-44d0958a6286.png)

## Step 2: Copy all .csv files to Home Directory: 
#### In my example, I save all raw data in same folder 'imba_data' and you need to unzip 2 .gz file and put into same location

![image](https://user-images.githubusercontent.com/7371969/227112970-41a36558-0c36-4ed1-a6a7-5d429e7f211b.png)

![image](https://user-images.githubusercontent.com/7371969/227113711-48d00577-4583-4f73-89ec-64341149d9c8.png)

#### 2.1 Copy all .csv files to Home Directory:

![image](https://user-images.githubusercontent.com/7371969/227114050-e82d20a4-5fff-49fe-b1c6-206885295e29.png)

![image](https://user-images.githubusercontent.com/7371969/227114108-142c52b8-d59e-404d-9f40-00290a70b3bc.png)

![image](https://user-images.githubusercontent.com/7371969/227114356-6dc649d8-ddea-4b86-a1c7-c7f8dfde4bde.png)

#### 2.12 Go back to Home directory and now we have main.py and all 6 csv files under the Home Directory:

![image](https://user-images.githubusercontent.com/7371969/227114547-91fa532c-b36a-4b96-bf72-17a5ea449a83.png)

## Step 3: Run python code in CLI by using user define syntax:
#### In my example,I have python 3 installed on ubuntu so my syntax will be using python3 as a example. Yours would be python, pip, pip3 etc.

#### 3.1 Introduce the syntax I define: 

> python3 main.py -u username -p password -t table_name -f file_path -d option if trancate table: Y/N -h host -e database_name

#### if you want see the syntax, you can also do this command:

> python3 main.py -o

![image](https://user-images.githubusercontent.com/7371969/227115747-42563823-ca8b-4077-b3ee-46a32404ec31.png)

#### verify if you have python3/python/pip/pip3 install:

> python3 --version

> python --version

> pip --version

> pip3 --version

#### if system returns the version info in CLI, this means you have installed the package:

![image](https://user-images.githubusercontent.com/7371969/227116104-c8bb7760-5996-452c-845a-55bc5c19d05d.png)

#### 3.2 Excuecute below CLI commands one by one, replace **python3** with **your python package: python / pip / pip3**, replace **your_username** with **your username (the default is 'admin' if you do not change anything)**, replcae **'your_password'** with **your password (This should be the master password where you create MySQL RDS database)**, replcae **'your_host'** with **your RDS database endpoints（for example, xxxx.xxu7oe4cqxxx.xxx.rds.amazonaws.com）**: 

> python3 main.py -u "your_username" -p "your_password" -t "Products" -f "~/products.csv" -d "Y" -h "your_host" -e "p3project"

> python3 main.py -u "your_username" -p "your_password" -t "Aisles" -f "~/aisles.csv" -d "Y" -h "your_host" -e "p3project"

> python3 main.py -u "your_username" -p "your_password" -t "Orders" -f "~/orders.csv" -d "Y" -h "your_host" -e "p3project"

> python3 main.py -u "your_username" -p "your_password" -t "Departments" -f "~/departments.csv" -d "Y" -h "your_host" -e "p3project"

> python3 main.py -u "your_username" -p *"your_password"* -t "Order_product" -f "~/order_products__train.csv" -d "N" -h "your_host" -e "p3project"

> python3 main.py -u "your_username" -p "your_password" -t "Order_product" -f "~/order_products__prior.csv" -d "N" -h "your_host" -e "p3project"

#### for example:

> python3 main.py -u "admin" -p "123456" -t "Order_product" -f "~/order_products__prior.csv" -d "N" -h "xxxx.xxu7oe4cqxxx.xxx.rds.amazonaws.com" -e "p3project"

#### Note: 1. You must turn on your remote AWS RDS database first.
####       2. Make sure all 6 csv files and main.py in same folder.
####       3. You must execute python3 commands when main.py in the same folder.

#### if you see the below message, it means you have been successfully insert:

![image](https://user-images.githubusercontent.com/7371969/227118442-47036492-0e07-4f57-b7e3-3881b9b1259e.png)


