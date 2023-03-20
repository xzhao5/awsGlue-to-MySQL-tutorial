# Tutorial: How to load data from S3 to mysql by using AWS Glue

## Step 1: Create RDS database
### 1.1 Login into your AWS console and search 'RDS' on your search bar.

![image](https://user-images.githubusercontent.com/7371969/226431514-98523344-f4ec-4515-abfe-dcd4cc9614ea.png)

### 1.2 Click 'Databases' on your left panel or click 'Create Database' to create a new RDS database. 

![image](https://user-images.githubusercontent.com/7371969/226432149-d6f68eaa-d656-43de-910d-df0098f54426.png)

### 1.3 select 'Standard Create' -> MySQL 
 
![image](https://user-images.githubusercontent.com/7371969/226432450-fd10d374-8417-4dbe-8ee6-296828fbace0.png)

### 1.4 -> Engine Version 'MySQL 8.0.23' Note*: if you choose the version after this and AWS Glue would be not working properly. 

![image](https://user-images.githubusercontent.com/7371969/226432539-e7c2fc0f-bbe8-494e-bf77-74db76f6ea43.png)

### 1.5 -> 'Free tier' 

![image](https://user-images.githubusercontent.com/7371969/226432889-1f68b3fa-2e62-4b7f-8226-063dca1511eb.png)

### 1.6 -> enter your 'DB instance name', your 'username' (default: admin), and your 'master password' (This should be remember!!!)

![image](https://user-images.githubusercontent.com/7371969/226433310-462e0a11-9382-4705-8f75-306e484559f0.png)

### 1.7-> 'db.t2.micro' and storage as default

![image](https://user-images.githubusercontent.com/7371969/226433975-e60b683b-fc51-4ecf-9644-6ff15b542be9.png)

### 1.8 -> select 'default VPC' Note*:please remember this VPC (yours may be differ from mine) because you will use later.

![image](https://user-images.githubusercontent.com/7371969/226434159-b513c61e-81ff-411b-ac06-c628dcf22152.png)

### 1.9 -> Here I create a new security group call 'Glue-RDS-MySQL' and I will explain on 2.1.  

![image](https://user-images.githubusercontent.com/7371969/226435239-ff66039e-62ac-43bb-89ad-1cce903693e8.png)

### Done -> Now click 'Create Database' to get new RDS DB and this will take a few mins. 

![image](https://user-images.githubusercontent.com/7371969/226435701-87462670-c468-488c-8f93-194ae85283a1.png)

## Step 2: prerequisite configuration:

### 2.1 Set up VPC secuirty groups:
#### In serach bar, serach 'security groups' and click VPC one. 

![image](https://user-images.githubusercontent.com/7371969/226436639-88be4797-68af-41f3-905e-67a29d4cdb99.png)

#### You are now in security groups windows, click 'Create security group'. 

![image](https://user-images.githubusercontent.com/7371969/226437315-4e39e714-550f-47ec-b1f0-f87160de33f7.png)

#### Give the secuity group a name, that's say, 'Glue-RDS-MySQL'; Use same VPC as 1.8 mentioned, if you are not in same VPC, this won't be work. 

![image](https://user-images.githubusercontent.com/7371969/226437683-ccf035a4-47c3-4bed-8406-5f2b614f1e0e.png)

#### create 'Inbound rules' as screenshot shows. sg-XXXXXX is this Security group ID, you can achieve this after create this security group. so you can create 'All traffic - 0.0.0.0/0' as inbound rule first and edit this later. 

![image](https://user-images.githubusercontent.com/7371969/226438485-38650aad-88ea-41fd-8f94-7aa88231b1d4.png) 

#### create 'Outbound rules' as screenshot shows.

![image](https://user-images.githubusercontent.com/7371969/226439287-ea27da24-551d-448b-bad5-55ea326f8be5.png)

#### Option: You can create tag for easy search the security group. Then, click 'Create Security Group'.

![image](https://user-images.githubusercontent.com/7371969/226439609-dd7bbe13-4e8d-47f4-8c67-963598d6788e.png)

### 2.2 Create VPC Endpoints: use for AWS glue to connect to S3.
#### In serach bar, serach 'security groups' and click VPC one. 

![image](https://user-images.githubusercontent.com/7371969/226440067-4dd5570f-5057-43e7-bdd4-002bfe382c79.png)

#### On left panel, click 'Endpoints' then click 'Create endpoint'. 

![image](https://user-images.githubusercontent.com/7371969/226440363-076bbd3d-b72c-4a34-975c-9b291f377adf.png)

#### Give the secuity group a name, that's say, 'Glue-RDS-MySQL', then select 'AWS services'. 

![image](https://user-images.githubusercontent.com/7371969/226454460-226d95e1-5790-4d8a-b135-4a5c24016497.png)

#### search 's3' in 'Service' block and select s3 endpoints as screenscreen shows, and the type is 'Gateway'.

![image](https://user-images.githubusercontent.com/7371969/226454954-a12932ef-f908-4f12-951b-6fc3578432db.png)

#### select same VPC as 1.8 mentioned and other configuration can be default.

![image](https://user-images.githubusercontent.com/7371969/226455159-0c12c195-36c2-49c0-bcae-9fd2d9213b78.png)

#### click 'Create endpoint' and successfully create endpoints now. 

![image](https://user-images.githubusercontent.com/7371969/226455330-f496da53-603a-44c4-9623-b9f0abf2fdbc.png)

### 2.3 IAM roles set up for AWS Glue operate and connection. 
#### In serach bar, serach 'IAM' and click 'IAM'.

![image](https://user-images.githubusercontent.com/7371969/226455733-1f533ded-cad8-4be8-b557-f53e5e71e1e1.png)

#### Click 'Roles' on left panel, then click 'Create role'. 

![image](https://user-images.githubusercontent.com/7371969/226456026-e117bfb8-b3b3-46ba-9a6a-1cad6dbe98ff.png)

#### Select 'AWS Service'; Search Glue in below search bar, select 'Glue' and then click 'Next'. 

![image](https://user-images.githubusercontent.com/7371969/226456311-27098634-f203-4034-9fa4-8ef6eaf6054e.png)

![image](https://user-images.githubusercontent.com/7371969/226456490-efa9cbb8-0577-4e87-9bf6-e6777a010b86.png)

![image](https://user-images.githubusercontent.com/7371969/226456745-ff435beb-9c7c-443f-a66d-9ec02977a79b.png)

#### Please grant the below policies as screenshot shows and click 'Next'. 

![image](https://user-images.githubusercontent.com/7371969/226456915-465167f8-b158-4b35-979f-c0aeed303afd.png)

#### Give the secuity group a name, that's say, 'demo_IAM_Glue_Role', then click 'Create role' in the bottom of this page.

![image](https://user-images.githubusercontent.com/7371969/226457386-6812f310-9ae1-4e26-b2bf-70580fa8ea29.png)

![image](https://user-images.githubusercontent.com/7371969/226457742-714f4bd1-1dae-4ffb-993a-4fae3c17157d.png)

## Step 3: Create Database from local computer:

#### 3.1 Open the 'MySQL Workbeach' - if you do not have one, please download from offical website and version is 8.0 or above.

![image](https://user-images.githubusercontent.com/7371969/226458814-503966f7-a4bc-4858-a6a3-d8c4304f9259.png)

#### 3.2 Create New Connection by click '+' button, edit the configuration windows, then click 'ok'. RDS endpoints you can find under RDS database in your AWS console.  

![image](https://user-images.githubusercontent.com/7371969/226459356-92fe123d-712f-4c38-881c-7ef18d618bd9.png)

#### I assume I have this is all configured, so I double click this one to remote access MySQL on AWS RDS. 

![image](https://user-images.githubusercontent.com/7371969/226459639-07b9e269-3a1b-4694-935e-5ad4bbf04d20.png)

#### 3.3 Download the p3project.sql, open this sql file and run the script by each statement to create the database, schema and tables.

![image](https://user-images.githubusercontent.com/7371969/226460252-98be25dd-381b-442e-9c38-02d881872ad2.png)

#### Now, you have all tables on MySQL RDS database.






