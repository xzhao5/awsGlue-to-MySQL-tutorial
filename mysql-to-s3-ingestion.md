# Tutorial: How to load data from MySQL RDS to S3 using AWS Database Migration Servers (DMS)

> In this scenario, it is assumed that third-party data is stored in a MySQL relational database. In a previous tutorial, an RDS was successfully created. The current objective is to perform data ingestion from the MySQL RDS database to S3, which involves copying data from tables and inserting them into S3 buckets as .csv files. This solution is intended for training and learning purposes, specifically for our P3 team members to test this function and become familiar with this skill.

## Prerequisite：
### 1. a AWS working account
### 2. a IAM role which can access s3 and rds.
### 3. a S3 bucket created for this task

## Step 1: Create IAM role: 
#### 1.1 Go to IAM and click 'Create role':

![image](https://user-images.githubusercontent.com/7371969/227772521-ca6820b8-4255-439d-928c-1fe2e3e0d198.png)

#### 1.2 select 'AWS service' -> 'DMS' -> Click 'Next':

![image](https://user-images.githubusercontent.com/7371969/227772641-f1f9a77f-4156-4c0a-aa09-27343348ce44.png)

#### 1.3 Grant this role with FULL Access with RDS and S3 as below screenshot shows and then click 'Next':

![image](https://user-images.githubusercontent.com/7371969/227772743-965561b2-327b-49f0-ac8d-4b08eade23b4.png)

#### 1.4 Fill up role name, that's say, 'test-dms-role'. Then, click 'Next':

![image](https://user-images.githubusercontent.com/7371969/227772800-0a49a436-4b9f-4ba7-a00d-874612c3971d.png)

![image](https://user-images.githubusercontent.com/7371969/227772834-5d4719fe-e183-4684-8d94-8507eb83379f.png)

## Step 2: Create DMS: 
#### 2.1 Go to DMS webpage and click 'Create replication instance':

![image](https://user-images.githubusercontent.com/7371969/227772927-3d00b70e-e555-47d7-9ab6-e09b629b7ec9.png)


