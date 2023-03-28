# Brain Storm: Discussion about improving the efficiency of data transformation by using data partitioning 

> We have established a successful pathway for ingesting data from a third-party source to S3. However, during data transfer between various components, there is a need for data partitioning. The objective of data partitioning is to break down a large dataset into smaller, more manageable portions that can be processed in parallel across multiple nodes in a distributed computing environment. This approach can accelerate the data transformation process and boost overall efficiency. Currently, I am investigating various methods to improve this functionality.

## Summary of my findings：
### 1. Vetical partitioning: Compared to CSV and JSON formats, column-level partitioning using formats such as Parquet offers the ability to store large amounts of data in a block storage format at the column level. With traditional row storage, searching for a specific row using the query "SELECT department FROM Departments where department='missing' " would require scanning through every row of the table until the result is found. However, with column-level partitioning, the result can be easily located without the need for extensive searching. (picture 1 and picture 2: the table looks small but thinking about there are million of rows over there)

![image](https://user-images.githubusercontent.com/7371969/228148191-cbd6242b-e234-44b9-9cce-698874ad02c1.png)

Picture 1 - Row Searching...

![image](https://user-images.githubusercontent.com/7371969/228149296-26e6af4a-b9ad-404f-b5ce-330f50789063.png)

Picture 2 - Column Sarching...

### 2. In basic terms, horizontal partitioning involves dividing data into separate files based on time intervals, such as year, month, or day. This approach facilitates file management, reduces input/output operations, and segregates data rows into distinct files. As an illustration, we can employ horizontal partitioning to create separate files named collect_year, collect_month, and collect_day for the Department Table. In the following section, I will elaborate on how AWS Glue can be used to implement this method.

### 3. Optimal options: File size leve partitioning. 


