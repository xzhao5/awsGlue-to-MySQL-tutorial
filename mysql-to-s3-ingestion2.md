# Implementation Plan: How to load data from MySQL RDS to S3 using AWS Database Migration Servers (DMS) 2 - achieve CDC in DMS

> In previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/361ad204940c12e227b3726854767040a7dfd9b7/mysql-to-s3-ingestion.md), A bridge linking MySQL RDS databases and S3 has been established successfully. However, a job runs daily to transfer data from the database to S3, and there is a concern about how to incorporate changes if a user inserts or updates new information. To address this issue, the option of enabling CDC on DMS is being considered.
> 
## Prerequisite：
### 1. A AWS working account.
### 2. A IAM role which can access s3 and rds.
### 3. A S3 bucket created for this task.
### 4. A RDS database with full data.

## Please refer last [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/361ad204940c12e227b3726854767040a7dfd9b7/mysql-to-s3-ingestion.mdstep) 1 to step 3 as same steps.  
## Step 4: Create a new migration job - Full load and ongoing replicaiton
#### 4.1 select your replication instance created in last tutorial:

![image](https://user-images.githubusercontent.com/7371969/229884754-195c4f89-6f1c-47ee-8b6d-d6d3c4bc2581.png)

#### 4.2 in 'Migration tasks', click 'Create task':

![image](https://user-images.githubusercontent.com/7371969/229885205-66b44895-0a19-4f6d-b103-bf5371849fe9.png)

#### 4.3 Give this task a name, that's say, 'my-cdc-plus-task' -> 

![image](https://user-images.githubusercontent.com/7371969/229886439-1b13a565-b90f-48be-9e3b-29add3f13b4b.png)

![image](https://user-images.githubusercontent.com/7371969/229886622-62effe1f-0428-4127-94d8-59751d23adc9.png)

![image](https://user-images.githubusercontent.com/7371969/229886699-9a793414-67c6-4aeb-bbf6-1785ea62c080.png)

![image](https://user-images.githubusercontent.com/7371969/229886897-40cf6f0b-d510-4352-9f31-d7186ef39385.png)

![image](https://user-images.githubusercontent.com/7371969/229886939-c1702b1d-4053-40ff-b208-555ea25b0158.png)

![image](https://user-images.githubusercontent.com/7371969/229887063-c54fde2d-44a9-4829-a6a7-14018d0e63bc.png)

![Uploading image.png…]()



![image](https://user-images.githubusercontent.com/7371969/229882928-51791a65-52dc-4e6e-90bd-3a151be5e580.png)

![image](https://user-images.githubusercontent.com/7371969/229884419-f0ef2aef-f097-4b8a-8bb5-fa12cae09f6a.png)


> INSERT INTO p3project.DepartmentsTest(department_id,department, collect_year,collect_month,collect_day) VALUES (25, 'other5',year(current_timestamp()), month(current_timestamp()),day(current_timestamp()));
> INSERT INTO p3project.DepartmentsTest(department_id,department, collect_year,collect_month,collect_day) VALUES (24, 'other4',year(current_timestamp()), month(current_timestamp()),day(current_timestamp()));
> commit;

#### 1.2 select 'AWS service' -> 'DMS' -> Click 'Next':

GRANT REPLICATION CLIENT ON *.* to admin@'%';
GRANT REPLICATION SLAVE ON *.* to admin@'%';
