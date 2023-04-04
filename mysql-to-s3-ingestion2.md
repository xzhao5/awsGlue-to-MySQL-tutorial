# Implementation Plan: How to load data from MySQL RDS to S3 using AWS Database Migration Servers (DMS) 2 - achieve CDC in DMS

> In previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/361ad204940c12e227b3726854767040a7dfd9b7/mysql-to-s3-ingestion.md), A bridge linking MySQL RDS databases and S3 has been established successfully. However, a job runs daily to transfer data from the database to S3, and there is a concern about how to incorporate changes if a user inserts or updates new information. To address this issue, the option of enabling CDC on DMS is being considered.
> 
## Prerequisite：
### 1. A AWS working account.
### 2. A IAM role which can access s3 and rds.
### 3. A S3 bucket created for this task.
### 4. A RDS database with full data.

## Please refer last [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/361ad204940c12e227b3726854767040a7dfd9b7/mysql-to-s3-ingestion.mdstep) Step 1 to step 3 as same steps.  
## Step 4: Create a new migration job - Full load and ongoing replicaiton
#### 4.1 select your replication instance created in last tutorial:

![image](https://user-images.githubusercontent.com/7371969/229884754-195c4f89-6f1c-47ee-8b6d-d6d3c4bc2581.png)

#### 4.2 in 'Migration tasks', click 'Create task':

![image](https://user-images.githubusercontent.com/7371969/229885205-66b44895-0a19-4f6d-b103-bf5371849fe9.png)

#### 4.3 Give this task a name, that's say, 'my-cdc-plus-task'and follow my setup as screenshot shows:

![image](https://user-images.githubusercontent.com/7371969/229886439-1b13a565-b90f-48be-9e3b-29add3f13b4b.png)

![image](https://user-images.githubusercontent.com/7371969/229886622-62effe1f-0428-4127-94d8-59751d23adc9.png)

![image](https://user-images.githubusercontent.com/7371969/229886699-9a793414-67c6-4aeb-bbf6-1785ea62c080.png)

![image](https://user-images.githubusercontent.com/7371969/229886897-40cf6f0b-d510-4352-9f31-d7186ef39385.png)

![image](https://user-images.githubusercontent.com/7371969/229886939-c1702b1d-4053-40ff-b208-555ea25b0158.png)

![image](https://user-images.githubusercontent.com/7371969/229887063-c54fde2d-44a9-4829-a6a7-14018d0e63bc.png)

#### 4.4 The job may be failed but don't worry, this is because our configuration is not finished yet : )

## Step 5: Create parameters groups for CDC job:
#### 5.1 Enter the RDS window in AWS console -> click 'Parameter group'-> click 'Create parameter group':

![image](https://user-images.githubusercontent.com/7371969/229888126-1529868f-0c7b-49d9-808a-aaa624cdb500.png)

![image](https://user-images.githubusercontent.com/7371969/229888373-a429cfff-ae49-4082-9b98-ca46d7925337.png)

#### 5.2 Fill up parameter and give a name, in my case, it's 'my-default-mysql-8'. 

![image](https://user-images.githubusercontent.com/7371969/229889194-cac7a7ae-be5b-4e95-82af-b9882a0cd1c8.png)

#### 5.3 Edit the parameter Group you just created and change the parameters as below and click 'save changes'.

> binlog_format: ROW
> binlog_checksum:NONE
> binlog_row_image: FULL
> log_slave_updates:True (1)

## Step 6: add this parameters group into your RDS instance: 
#### 6.1 In left pannel, click 'Databases' -> select your RDS instance:

![image](https://user-images.githubusercontent.com/7371969/229891120-d229795b-b013-4dd8-a070-f5ed67c9d0be.png)

#### 6.2 Click 'Modify' on your right connor: 

![image](https://user-images.githubusercontent.com/7371969/229891665-6fb53a82-59ee-44d6-93e1-1c26501171dc.png)

#### 6.3 keep all default but on this option: you need to select the parameter group you created: 

![image](https://user-images.githubusercontent.com/7371969/229892052-63c69e31-ce0f-4228-99a9-b38de86940f6.png)

![image](https://user-images.githubusercontent.com/7371969/229892250-6466e7b1-0a7a-4b80-aa39-eb74ebdcc935.png)

#### 6.4 You need to reboot the RDS instance to make this effect. 

![image](https://user-images.githubusercontent.com/7371969/229892689-90ad123c-2176-425a-b670-362650d8fc67.png)

## Step 7: Run DMS task again and await for a few mins.

![image](https://user-images.githubusercontent.com/7371969/229892945-2566e099-7725-4af0-8f54-3ccc99ee6fb1.png)

## Step 8: Do some insert on your MySQl database and test if this is working.
#### Run similar statement as below by using MySQL WorkBench (Note: don't forget to run 'Commit;' to commit data into RDS database)

> INSERT INTO p3project.DepartmentsTest(department_id,department, collect_year,collect_month,collect_day) VALUES (25, 'other5',year(current_timestamp()), month(current_timestamp()),day(current_timestamp()));
> INSERT INTO p3project.DepartmentsTest(department_id,department, collect_year,collect_month,collect_day) VALUES (24, 'other4',year(current_timestamp()), month(current_timestamp()),day(current_timestamp()));
> commit;

## Step 9: Verify this in your DMS menu, mine dectect these inserts successfully. 

![image](https://user-images.githubusercontent.com/7371969/229882928-51791a65-52dc-4e6e-90bd-3a151be5e580.png)

## Step 10: Verify this in your S3 bucket, mine dectect these inserts columns successfully.

![image](https://user-images.githubusercontent.com/7371969/229884419-f0ef2aef-f097-4b8a-8bb5-fa12cae09f6a.png)

## You do a great job ~ : )

![image](https://user-images.githubusercontent.com/7371969/229894295-9e8ce5d2-acbb-4ff2-a99a-69cafc1d41de.png)
