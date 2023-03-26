# Tutorial: How to load data from MySQL RDS to S3 using AWS Database Migration Servers (DMS)

> In this scenario, it is assumed that third-party data is stored in a MySQL relational database. In a previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/d5fcbd4f132794a6c6a26ac4d9f52364ac4dfb89/tutorial.md), an RDS was successfully created. The current objective is to perform data ingestion from the MySQL RDS database to S3, which involves copying data from tables and inserting them into S3 buckets as .csv files. This solution is intended for training and learning purposes, specifically for our P3 team members to test this function and become familiar with this skill.

## Prerequisite：
### 1. A AWS working account.
### 2. A IAM role which can access s3 and rds.
### 3. A S3 bucket created for this task.
### 4. A RDS database with full data.

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

#### 2.2 In the window of 'Create replicaiton instance', give DMS a name, that's say, 'migrate-mysql-to-s3':

![image](https://user-images.githubusercontent.com/7371969/227773093-68e47939-4412-44d1-80c2-7eb276aa4764.png)

#### 2.22 Chosse 'Single-AZ' for testing purpose:

![image](https://user-images.githubusercontent.com/7371969/227773133-c9bcb714-df0e-43bf-8dfc-7abda0d138dc.png)

#### 2.23 Chosse VPC which should be same as RDS. 

![image](https://user-images.githubusercontent.com/7371969/227773226-52217529-befe-40fc-90d6-52591e18bd80.png)

#### 2.24 Keep the rest of configuration as default and click 'Next':

![image](https://user-images.githubusercontent.com/7371969/227773269-ad062e1c-9318-4060-8a7e-5c2464b15c36.png)

![image](https://user-images.githubusercontent.com/7371969/227773291-b14e4019-f1a2-4c65-af53-22c65113fc46.png)

#### Next, you just take a break and come back in a few mins. Now, DMS has been created successfully:

![image](https://user-images.githubusercontent.com/7371969/227773358-0a5d76fb-e009-4df8-ae16-aabe2d4dea3d.png)

## Step 3: Create endpoints for both source (RDS) and target (S3):
#### 3.1 Click 'Endpoints' on your left pannel:

![image](https://user-images.githubusercontent.com/7371969/227773440-73efcf38-d4f9-4549-bca2-63efad6cd444.png)

#### 3.2 Click 'Create endpoint': 

![image](https://user-images.githubusercontent.com/7371969/227773492-71785706-2f46-4c0e-8be0-bd8a6a766da1.png)

#### 3.3 Create endpoints for resource - RDS:
##### 3.31 tick 'Select RDS DB instance' and select MySQL instance you created in previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/d5fcbd4f132794a6c6a26ac4d9f52364ac4dfb89/tutorial.md), in my case, it's database-1:

![image](https://user-images.githubusercontent.com/7371969/227773585-e0459f4e-4149-4995-8336-e8447134488a.png)

##### 3.32 Select 'Provide accesss information manually' and fill up the password which you create MySQL RDS database:

![image](https://user-images.githubusercontent.com/7371969/227773766-d68f5877-1df8-4339-b731-2f7859344785.png)

##### 3.33 Choose VPN as same as DMS, click 'Run test' to test if this is working (if all good, its status would be 'Successfuly'), then click 'Create endpoint':

![image](https://user-images.githubusercontent.com/7371969/227773843-f4c6c8d8-9846-4b9c-b89c-01dc75e870c5.png)

#### 3.4 Create endpoints for target - S3:
##### 3.41 Click 'Create endpoint' -> select 'Target endpoint' -> give endpoint a name, that's say, 's3 target' -> select 'Amazon S3' as Target engine:

![image](https://user-images.githubusercontent.com/7371969/227774047-84d9c112-d069-4c78-bb04-ddfd0a1bf338.png)

![image](https://user-images.githubusercontent.com/7371969/227774102-339ed687-2eef-45f6-9fde-a1dcbef3d901.png)

##### 3.42 fill up role ARN - this is role which I created in step 1 and Bucket Name should be the bucket you created in your S3, in my case, my S3 bucket is 'raw-data-mysql-to-s3': 

![image](https://user-images.githubusercontent.com/7371969/227774338-2f9a98aa-2202-42a5-b1cd-36c8f9e12e32.png)

![image](https://user-images.githubusercontent.com/7371969/227774440-1306b5e6-6c63-4dc3-a717-41e275157648.png)

##### 3.43 Expand 'Endpoint settins', click 'add new setting' and enter a new one: AddColumnName:true: 

![image](https://user-images.githubusercontent.com/7371969/227774498-8714ed04-d0a0-4d7d-a878-c4fb286f7d74.png)

##### Note: Why do this step? This is because you would receive the .csv file without column name. 

##### 3.44 Choose VPN as same as DMS, click 'Run test' to test if this is working (if all good, its status would be 'Successfuly'), then click 'Create endpoint': 

![image](https://user-images.githubusercontent.com/7371969/227774659-a1ae3622-3163-4681-8347-f8ed95f4a9a0.png)

## Step 4: Create Database migration task:
### 4.1 Open the menu of DMS, then click DMS's Name: 

![image](https://user-images.githubusercontent.com/7371969/227774781-5e34b8b8-668b-420e-9251-c84c6c95083f.png)

### 4.2 Click tab 'Migration tasks' and then click 'Create task': 

![image](https://user-images.githubusercontent.com/7371969/227774860-84220631-775e-40be-91a8-670c44fe9730.png)

### 4.3 Give task a name, that's say, 'dms-task-from-mysql-to-s3' -> pick up the replication instance (DMS), source endpoint, target source which we created before:

![image](https://user-images.githubusercontent.com/7371969/227775029-645f282f-ab50-4627-8bbf-3dede64cd6a3.png)

### 4.4 Leave the rest of configration as default but 'migration task startup configuration' change into 'Manually later'.Then, click 'Create task':

![image](https://user-images.githubusercontent.com/7371969/227775134-560add38-7696-4a23-b986-b122c549b877.png)

![image](https://user-images.githubusercontent.com/7371969/227775156-507c3189-6aa9-47d6-a139-b04e12f5d186.png)

## Step 5: Run the migration task.
### 5.1 Tick the migration task 'dms-task-from-mysql-to-s3' which you created in step 4 -> click 'Actions' -> Click 'Restart/Resume' to start this task:

![image](https://user-images.githubusercontent.com/7371969/227775304-ea10ba96-662b-4428-a573-edcecac35afe.png)

### 5.2 Once the task completed, it shows 'load complete' as below:

![image](https://user-images.githubusercontent.com/7371969/227775399-7a40edff-42ce-4e70-b1af-05d3ba8d4889.png)

## Step 6: Verfiy .csv file:
### 6.1 Download any csv under S3 bucket you created and this looks good for me:

![image](https://user-images.githubusercontent.com/7371969/227775493-0f0e56fb-263e-4511-9e87-7fa32333cc8e.png)

### Great! You do well, my friends ~!

![image](https://user-images.githubusercontent.com/7371969/227775573-c214b336-6206-4f23-8485-73d81ea46c9c.png)
