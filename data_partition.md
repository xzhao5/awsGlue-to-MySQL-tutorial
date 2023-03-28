# Brain Storm: Discussion about improving the efficiency of data transformation by using data partitioning 

> We have established a successful pathway for ingesting data from a third-party source to S3. However, during data transfer between various components, there is a need for data partitioning. The objective of data partitioning is to break down a large dataset into smaller, more manageable portions that can be processed in parallel across multiple nodes in a distributed computing environment. This approach can accelerate the data transformation process and boost overall efficiency. Currently, I am investigating various methods to improve this functionality.

## Summary of my findings：
### 1. Column level partitioning, such as Parquet, compare to csv and json format, it has capability to store large amount of data in a column level block storage. For example, in traditional row storage, if we search a row by 'select * from Departments', this would go for each row of tables until this find the result. However, using column level method, he can easily find the the result without lots of search. 

