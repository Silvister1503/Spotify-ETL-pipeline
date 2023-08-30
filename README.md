# Spotify-ETL-Pipeline-Using-AWS

### Introduction: 
In this project, i have built an ETL Pipeline using Spotify API. The pipeline will retrieve the data from the Spotify API, transform the data into a desired format and then load it into the AWS Data Store called Amazon Athena.

### Data/API:
This API contains the information related to music like albums, artists, songs - [Spotify API](https://developer.spotify.com/documentation/web-api)

### Architecture: 
Description: The Architecture mainly consists of 3 parts: Extract, Transform, Load. Firstly the data is extracted from Spotify API using the python code and stored in Jupyter Notebook. Here starts the real process, i have created a Lambda function to extract the data from the API and the data is continously loaded by setting up a trigger called CloudWatch which supplies data continously based on the time given as input. When the data is getting continously extracted the data needs to stored at some place. So, Amazon S3 comes into picture, where the input data is stored in the form of objects. Intially the data is raw and the stored in raw_data folder. I have created one more Lambda function to transform the data and store it in a different folder. Once the data is available in raw_data folder, with the help of s3 trigger, the data is transformed and moved to transformed_data folder. The next step is to laod the data into Amazon Glue using by creating and running the crawlers. Finally you can write SQL query the data on Amazon Athena. 

### Architecture Diagram: - [Architecture_Diagram](https://github.com/SameerPathaan/Spotify-ETL-Pipeline-using-AWS/blob/main/Architecture.png)

### Utilized Services:
**Jupyter Notebook:** Open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

**Amazon S3:** Scalable cloud storage service that allows you to store and retrieve data from anywhere on the web.

**Amazon Lambda:** Serverless compute service that lets you run code without provisioning or managing servers, and pay only for the compute time consumed.

**Amazon CloudWatch:** Monitoring and observability service that provides metrics, logs, and alarms to monitor AWS resources, applications, and services.

**Amazon Glue:** Fully-managed extract, transform, and load (ETL) service that makes it easy to move data between data stores.

**Amazon Crawler:** A component of Amazon Glue that automatically discovers and classifies metadata about your data and stores it in the AWS Glue Data Catalog.

**Amazon Athena:** Serverless, interactive query service that allows you to analyze data stored in Amazon S3 using standard SQL.

### Installed Packages:
Pandas, Numpy, spotipy, boto3, datetime..

### Project Execution Flow:
Spotify API --> CLoudWatch: Trigger to extract the data every 10 minutes --> Lambda Func: Spotify_ETL_data_extract to Extract the input data from Spotify --> Amazon S3: Store the raw data --> S3 trigger: to move the data to transformed data folder once the data is available in raw data folder --> Amazon S3: to store the transformed data in a folder in a seggregated manner in the form of album data, artist data, songs data --> Crawler: To set up the database, metadata and the path from where the data needs to be laoded --> Amazon Glue: To Create the table structures and load the data  --> To analyze the data by applying SQL Queries on the data stored in S3 

