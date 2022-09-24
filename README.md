# Emulated Distributed File System

## Project Description

* This project involves building a distributed file system similar to Hadoop Distributed File System (HDFS) and implementing commands like `mkdir, ls, cat, rm, put, getPartitionLocations, readPartition`.
* Utilizing 2 Databases namely `MongoDB` and `MySQL` to store actual data of the file and the metadata of the file (considered as datanode and namenode) respectively.
* Implementing the partitioning-based `map` and `reduce` for the file stored in the DFS
*  Building a `web application` which takes the above commands as input from the user and displays the results on a web page. Also, the web application will have `search and analytics` components.

## Project Overview

<br>
<p align="center">
<img src="imgs/implementation.jpg" width="500" height="400"/> 
<br>
Implementation Modules
</p>
<br>

## Implementation Details

* The project would involve python scripts each for the EDFS implementations, search and analytics functions and for the partition-based map reduce implementation.
* The EDFS commands to be implemented would be API calls which would be handled in the python script and when a data is inputted in the EDFS, the metadata (namenode) related to the file would be stored in a MySQL database and the actual data (datanode) would be stored in a MongoDB database.
* Once the partitioning of the data into data blocks is completed, the mapreduce python script will run a EDFS Map reduce on the partitioned data. The input to the map function would be a partition of the data followed by the reduce function which will combine/reduce them further.
* Finally, a web application is developed using Flask that will involve 2 components namely
    * Command Line Input Tab: It’ll consist of form fields where a user can enter the EDFS commands and the web app will return the results on the page.
    * Search and Analytics Tab: The user can carry out search and carry out some defined analytics for the given datasets. The web application will interact with both the Databases and run the search and analytics related functions to return the desired results.

## Project Timeline

|                                      Task                                     	            |     Target Date     	|    Status   	|
|:--------------------------------------------------------------------------------------     	|:-------------------:	|:-----------:	|
| MySQL and MongoDB based emulation of EDFS                                     	            |  15 Oct 2022 	        | In Progress 	|
| Implement partition based map and reduce on the data stored in EDFS           	            |  30 Oct 2022 	        |             	|
| Implement Search and Analytics functions on said datasets                     	            |  15 Nov 2022 	        |             	|
| Develop a web application for searching and analyzing the data stored in EDFS 	            |  30 Nov 2022 	        |             	|







