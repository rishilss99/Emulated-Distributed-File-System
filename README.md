# Emulated Distributed File System

## Project Description

- This project involves building a distributed file system similar to Hadoop Distributed File System (HDFS) and implementing commands like `mkdir, ls, cat, rm, put, getPartitionLocations, readPartition`.
- Utilizing 2 Databases namely `MongoDB` and `MySQL` to store actual data of the file and the metadata of the file (considered as datanode and namenode) respectively.
- Implementing the partitioning-based `map` and `reduce` for the file stored in the DFS
- Building a `web application` which takes the above commands as input from the user and displays the results on a web page. Also, the web application will have `search and analytics` components.
