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

#### Give the IAM a name, that's say, 'demo_IAM_Glue_Role', then click 'Create role' in the bottom of this page.

![image](https://user-images.githubusercontent.com/7371969/226457386-6812f310-9ae1-4e26-b2bf-70580fa8ea29.png)

![image](https://user-images.githubusercontent.com/7371969/226457742-714f4bd1-1dae-4ffb-993a-4fae3c17157d.png)

## Step 3: Create Database from local computer:

#### 3.1 Open the 'MySQL Workbeach' - if you do not have one, please download from offical website and version is 8.0 or above.

![image](https://user-images.githubusercontent.com/7371969/226458814-503966f7-a4bc-4858-a6a3-d8c4304f9259.png)

#### 3.2 Create New Connection by click '+' button, edit the configuration windows, then click 'ok'. RDS endpoints you can find under RDS database in your AWS console.  

![image](https://user-images.githubusercontent.com/7371969/226459356-92fe123d-712f-4c38-881c-7ef18d618bd9.png)

#### I assume I have this is all configured, so I double click this one to remote access MySQL on AWS RDS. 

![image](https://user-images.githubusercontent.com/7371969/226459639-07b9e269-3a1b-4694-935e-5ad4bbf04d20.png)

#### 3.3 Download the [p3project.sql](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/514816e9ff03646a4688816628a48da2936e0136/p3project.sql), open this sql file and run the script by each statement to create the database, schema and tables.

![image](https://user-images.githubusercontent.com/7371969/226460252-98be25dd-381b-442e-9c38-02d881872ad2.png)

#### Now, you have all tables on MySQL RDS database.

## Step 4: Set up data conncetion in AWS Glue:
#### 4.1 Search 'glue' in search bar and then click 'AWS Glue'. 

![image](https://user-images.githubusercontent.com/7371969/226461155-3ceb0859-13eb-4b75-9423-029a95481246.png)

#### 4.2 Click 'Data connections' in left pannel, scroll down the web page, and click 'Create connection'.

![image](https://user-images.githubusercontent.com/7371969/226461324-a6d978ac-a269-4715-bc3b-36c4af9e5d48.png)

![image](https://user-images.githubusercontent.com/7371969/226461594-a8933605-7529-4b27-ad57-02d3b9b90d1e.png)

#### 4.3 Give the connection a name, that's say, 'mysql_connection'; choose 'Amazon RDS' and then 'MySQL'. 

![image](https://user-images.githubusercontent.com/7371969/226461844-9342f538-bb29-41d7-9e64-ad8a5bfc753b.png)

#### 4.4 Select your 'instance name', in my case, it's 'database-1', then give a Database name, that's say, 'p3project'; Put your master password as 1.6 mentioned here and click 'Create connection'. 

![image](https://user-images.githubusercontent.com/7371969/226462687-e559efff-91d2-4d14-9c74-2c36928784e0.png)

## Step 5: Set up Crawlers in AWS Glue:
#### 5.1 click 'Crawlers' on left pannel and then click 'Add crawler'.  

![image](https://user-images.githubusercontent.com/7371969/226463252-91c4f7da-222f-46fe-aa3f-7d8700931c37.png)

![image](https://user-images.githubusercontent.com/7371969/226463594-8c35d98a-c8b0-4a16-a708-fe54d7c8d520.png)

#### 5.2 give Crawler a name, that's say, 'mycrawler_mysql', then click 'Next'. 

![image](https://user-images.githubusercontent.com/7371969/226478483-f1929784-ef7e-4eaf-b40e-fd14e8fbb365.png)

#### 5.21 Click 'Add a data source'.

![image](https://user-images.githubusercontent.com/7371969/226477179-d5a65455-6cf4-4d11-9c11-21e3d9dd278b.png)

#### 5.22 In 'Add a data source' window, select 'JDBC' -> select the data connection you create in Step 4 -> Include path 'Your database Name/%', in my case, the database name is 'p3project', 'p3project/%' means all schema and tables under database 'p3project'. All set up, now click 'Add a JDBC data source'.

![image](https://user-images.githubusercontent.com/7371969/226477964-ea58ece5-4b0b-4492-b52d-775afe664e11.png)

#### 5.3 Click 'Next' to continue. 

![image](https://user-images.githubusercontent.com/7371969/226478216-3c7446f3-d92d-4e87-98dd-dc17bcd26a5c.png)

#### 5.4 Select IAM role you create in 2.3 in my case, it's 'demo_IAM_Glue_Role' and then click 'Next'.

![image](https://user-images.githubusercontent.com/7371969/226479279-e4d9f658-9f53-42fb-9972-654c31419716.png)

#### 5.5 Create a new databse by clicking 'Add database'. (I have already create a database there called 'demo_p3project')

![image](https://user-images.githubusercontent.com/7371969/226479454-ddab4e16-03b6-4ce8-932a-837218065c39.png)

#### 5.51 Give database a name, that's say, 'demo_p3project' and then click 'Create database'.

![image](https://user-images.githubusercontent.com/7371969/226479799-a7aad97e-24e6-4665-b6f6-2e545c9ba03e.png)

#### 5.52 Go back to Crawler creation web page, click 'Next'.

![image](https://user-images.githubusercontent.com/7371969/226480316-65ea2c85-da21-4d4a-b55a-3fd7fcbcfa4b.png)

#### 5.6 Review your Crawler configuration and click 'Update'. 

![image](https://user-images.githubusercontent.com/7371969/226480510-56d64aad-cad8-4d82-a875-dfd9f149a509.png)

#### 5.7 Now you have your crawler. select the crawler and click 'Run'. As a result, you should have 5 tables in the new database you created in 5.51.

![image](https://user-images.githubusercontent.com/7371969/226481157-472261c7-f66e-4844-a1ae-8ec3c5abd25f.png)

#### As a result, you have successfully run the crawler job. But how to check if tables is over there ? 

![image](https://user-images.githubusercontent.com/7371969/226481228-b61eb6ee-1e41-48d8-9887-987681723c56.png)

#### Click 'Database' on left pannel and now you can see all tables under this databses. Great job !

![image](https://user-images.githubusercontent.com/7371969/226481503-29f6e888-4fa8-4f39-8899-7bcc9adb82d5.png)







