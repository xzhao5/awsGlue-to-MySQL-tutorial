# Brain Storm: Discussion about improving the efficiency of data transformation by using data partitioning 

> We have established a successful pathway for ingesting data from a third-party source to S3. However, during data transfer between various components, there is a need for data partitioning. The objective of data partitioning is to break down a large dataset into smaller, more manageable portions that can be processed in parallel across multiple nodes in a distributed computing environment. This approach can accelerate the data transformation process and boost overall efficiency. Currently, I am investigating various methods to improve this functionality.

## Summary of my findings：
### 1. Vetical partitioning: Compared to CSV and JSON formats, column-level partitioning using formats such as Parquet offers the ability to store large amounts of data in a block storage format at the column level. With traditional row storage, searching for a specific row using the query "SELECT department FROM Departments where department='missing' " would require scanning through every row of the table until the result is found. However, with column-level partitioning, the result can be easily located without the need for extensive searching. (picture 1 and picture 2: the table looks small but thinking about there are million of rows over there, where this would make difference)

![image](https://user-images.githubusercontent.com/7371969/228148191-cbd6242b-e234-44b9-9cce-698874ad02c1.png)

Picture 1 - Row Searching...

![image](https://user-images.githubusercontent.com/7371969/228149296-26e6af4a-b9ad-404f-b5ce-330f50789063.png)

Picture 2 - Column Sarching...

### 2. In basic terms, horizontal partitioning involves dividing data into separate files based on time intervals, such as year, month, or day. This approach facilitates file management, reduces input/output operations, and segregates data rows into distinct files. As an illustration, we can employ horizontal partitioning to create separate files named collect_year, collect_month, and collect_day for the Department Table. In the following section, I will elaborate on how AWS Glue can be used to implement this method.

![image](https://user-images.githubusercontent.com/7371969/228172722-b5bbc386-940e-4bee-9d37-d9be0ff778b5.png)

### 3. One potential solution is file-level partitioning, which involves considering two scenarios when transferring data: 1) transferring a small number of large files, and 2) transferring a large number of small files. Processing large files can be I/O-intensive and strain system resources, while dealing with too many small files can be time-consuming. To address these issues, AWS Lake Formation offers file-level partitioning as a means of optimizing data transfer. (Will be introduced in the future).

### 4. Although I have found AWS Glue to be an efficient way to create data partitions, the cost of doing so is significant. As a result, I am actively seeking alternative solutions that may be more cost-effective in the long term.

![image](https://user-images.githubusercontent.com/7371969/228171407-caabd2ac-3148-4f70-9bc7-838cd464edc2.png)

## Testing data partition in column level by using AWS Glue：
### Step 1: I create a S3 buckets and two differnt folders under this new S3 buckets.

![image](https://user-images.githubusercontent.com/7371969/228211465-36b8fc77-a02a-4670-9b6a-bd9d6c738481.png)

### Step 2: Create a Glue job - in my case, this called 'orders-data-partition-test-job': 

![image](https://user-images.githubusercontent.com/7371969/228213530-8404d3a9-3d47-489f-a09b-bea6812d5fd9.png)

### Step 3: Create two block - source 'MySQL' and target 'Amazon S3', click 'MySQL' to change configuration: select 'JDBC connection details' and choose the connection created in previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/e6e7c8675d02684a393ebc67e2ce4567e06cf3a2/tutorial.md):

![image](https://user-images.githubusercontent.com/7371969/228213842-bb31cdbf-ecac-4fde-8bf9-ccf1c498eb79.png)

### Step 3.2: choose the table you create for testing, in my case, that's DepartmentTest, which includes column 'id', 'department', 'collect_year', 'collect_month' and 'collect_day'.

![image](https://user-images.githubusercontent.com/7371969/228214944-de57a11b-f486-4970-a87e-c1c676e292ec.png)

#### The table looks like that:

![image](https://user-images.githubusercontent.com/7371969/228217595-19f71ec2-acc1-4484-8a85-89bbae51d8bd.png)


### Step 4: Click 'Amazon S3' block - > select 'Parquet', 'Snappy' for compression, and S3 bucket I create in Step 1. 

![image](https://user-images.githubusercontent.com/7371969/228215918-56e91aa8-6b30-48fe-a893-765bc0a0e9e5.png)

### Step 4.2: Choose the database you created in previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/e6e7c8675d02684a393ebc67e2ce4567e06cf3a2/tutorial.md):

![image](https://user-images.githubusercontent.com/7371969/228216196-383b08c4-c517-4d7f-927e-23fd7a3df05e.png)

### Step 4.2: Create a new table in category, in my case, called 'departmentsnopartitiontable'. 

![image](https://user-images.githubusercontent.com/7371969/228216494-fc79a231-7860-4fa0-b803-30df08b9ded4.png)

### Step 5: Save the job and run this job. 

![image](https://user-images.githubusercontent.com/7371969/228216774-0597015a-6aba-41c1-909c-94c43fe5b87d.png)

### Now check S3 bucket you created, you will see what it looks like - this is no row level partion but the column level partition. This will be equally 20 files with same size.

![image](https://user-images.githubusercontent.com/7371969/228217168-0b9e6d78-bdbe-4649-8a30-9c59739d3530.png)

## Testing data partition in row level by using AWS Glue：
### Step 1: I will create another Glue job now, that's say, 'departments-data-partition-test-2'. 

![image](https://user-images.githubusercontent.com/7371969/228218032-e5a7d1b9-f7d4-449d-9c5c-2a0cb7b0e251.png)

### Step 2: select 'MySQL' block -> select 'Data Catalog table' -> select database created in previous [tutorial](https://github.com/xzhao5/awsGlue-to-MySQL-tutorial/blob/e6e7c8675d02684a393ebc67e2ce4567e06cf3a2/tutorial.md) -> the table your created in last section. 

![image](https://user-images.githubusercontent.com/7371969/228218241-c3f34360-a9a3-42e0-b99b-dae83e4070aa.png)

### Step 3: select 'Amazon S3' block - > select 'Parquet', 'Snappy' for compression, and S3 bucket I create in Step 1

![image](https://user-images.githubusercontent.com/7371969/228219144-736b6c7c-23ca-4cdc-928d-71fd27a9ac5c.png)

### Step 3.2 create a new table, that's say, 'dapartmentspartitiontable' and then add partition key on 'collect_year', 'collect_month' and 'collect_day'.

![image](https://user-images.githubusercontent.com/7371969/228219252-c68e095d-14d2-449c-8516-bf824f49f965.png)

![image](https://user-images.githubusercontent.com/7371969/228219303-d640f42c-f8b3-41c5-bd67-1c84ecb6ce18.png)

### Step 4 Click 'Save' and then Click 'Run' after the job saved.

![image](https://user-images.githubusercontent.com/7371969/228219714-02cf4c9f-6c61-45f2-8049-7a193558044c.png)

### Step 5 Check S3 bucket you created and you will find the structure: 'Year' folder -- 'Month' folder -- 'Day' folder -- All files. 

![image](https://user-images.githubusercontent.com/7371969/228219988-56f34e76-c1d3-4f81-8cb2-99ed1d334478.png)

![image](https://user-images.githubusercontent.com/7371969/228220029-ca893682-ce3f-4692-ac09-39d5d32d4dbd.png)

![image](https://user-images.githubusercontent.com/7371969/228220066-ad07e4f2-ad18-4ee4-be87-a6e0e00df6b5.png)

![image](https://user-images.githubusercontent.com/7371969/228220104-a5c3f3d6-e2ba-4dc6-8b19-da85f86b78e6.png)

### In this way, we can easily identify when we ingest the data and cannot make anything massive. 


