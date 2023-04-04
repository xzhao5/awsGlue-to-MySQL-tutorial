# Implementation Plan: How to load data from MySQL RDS to S3 using AWS Database Migration Servers (DMS) 2 - achieve CDC in DMS

> In previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/361ad204940c12e227b3726854767040a7dfd9b7/mysql-to-s3-ingestion.md), A bridge linking MySQL RDS databases and S3 has been established successfully. However, a job runs daily to transfer data from the database to S3, and there is a concern about how to incorporate changes if a user inserts or updates new information. To address this issue, the option of enabling CDC on DMS is being considered.
> 
## Prerequisite：
### 1. A AWS working account.
### 2. A IAM role which can access s3 and rds.
### 3. A S3 bucket created for this task.
### 4. A RDS database with full data.

## Step 1: Create IAM role: 
#### 1.1 Go to IAM and click 'Create role':

![image](https://user-images.githubusercontent.com/7371969/227772521-ca6820b8-4255-439d-928c-1fe2e3e0d198.png)

#### 1.2 select 'AWS service' -> 'DMS' -> Click 'Next':

GRANT REPLICATION CLIENT ON *.* to admin@'%';
GRANT REPLICATION SLAVE ON *.* to admin@'%';
