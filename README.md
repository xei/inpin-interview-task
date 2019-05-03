# Task Description
The task is to implement Rest-API for the agency and its listings(ads) management system.

Notes:

* You are free to choose any kind of technology/language that fits you the best.
* You must use the provided database schema in your implementation, however, feel free to add/modify everything as needed.
* Pay attention to the scalability of the API.
* One agency can own one or more other agencies.
     
   Hence, the parent agency should have access to all the child agencies' listings(ads) hierarchically. 
   For example, we got 3 agencies A, B, and C accordingly with 10,5 and 2 listings(ads). 
   Agency B belongs to A and agency C belongs to B. Then we can say that agency A has 17, agency B has 7 and agency C has 2 
   listings(ads) in total.

 
#### The database schema for start point:
    1. Listing (id, name, latitude, longitude, agency_id)
    2. Agency (id, parent_agency_id, name)
 
You should make a git repository (perhaps GitHub will be a good choice) and commit as frequently as you can. Then, as a submission share your code with me mohammad@inpinapp.com.

## Task 1
##### Api should support CRUD for listings(ads) and agencies.

## Task 2
##### Implement endpoint which gets all listings.
 * Within the radius of n kilometers from a point (latitude, longitude) ordered by distance.
 * Including all the children listings(ads) in the tree, for the given agency_id.


## Task 3
##### Write a simple, not fancy interface that will consume your API programmatically.

## Task 4
##### You will get extra 100 points if you will do all with TDD and dockerize :D.

## Database Design: ER Diagram
<p align="center">
  <img src="backend/database_design/ERD.png?raw=true" alt="ER Diagram"/>
</p>
* The datatype decimal(10, 8) is used to store latitide (-180 ~ +180) and the dayatype decimal(11, 8) is used to store longitide (-90 ~ +90) values accurately.
* The website https://app.sqldbm.com is used to design the database.

## Database Design: DDL Script
* The following SQL commands are auto-generated from above ER diagram to create database and tables in MySQL.
```sql
CREATE DATABASE inpin_db;
USE inpin_db;

CREATE TABLE `agency` (
	`id` bigint(20) NOT NULL AUTO_INCREMENT,
	`parent_id` bigint(20) DEFAULT NULL,
	`name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
	PRIMARY KEY (`id`),
	KEY `fkIdx_1` (`parent_id`),
	CONSTRAINT `sub_agency` FOREIGN KEY `fkIdx_1` (`parent_id`) REFERENCES `agency` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `ad` (
	`id` bigint(20) NOT NULL AUTO_INCREMENT,
	`agency_id` bigint(20) NOT NULL,
	`name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
	`latitude` DECIMAL(10, 8),
	`longitude` DECIMAL(11, 8),
	PRIMARY KEY (`id`),
	KEY `fkIdx_2` (`agency_id`),
	CONSTRAINT `has` FOREIGN KEY `fkIdx_2` (`agency_id`) REFERENCES `agency` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
```

## Install Dependencies
```bash
pip3 install -r backend/requirements.txt
```
* "Flask" is used as a web micro framework to build RESTful APIs.
* "pymysql" is used to connect to MySQL database from Python code.
* "flask-sqlalchemy" is used as an ORM.
* "flask-marshmallows" is used as a Json serializer/deserializer.
* "marshmallow-sqlalchemy" is used to use Marshmallows to serialized SqlAlchemy query results.

# APIs
Here you can find the contract of all APIs that are developed in this project.
It includes CRUD APIs for Agency and Ad (Task 1), Geographical API (Task 2 Part 1) and Subset listing (Task2 Part 2).
## Create a new agency
### Request
```bash
curl --request POST \
  --url http://127.0.0.1:5000/agency \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form 'name=Agency #2' \
  --form 'parent_id =1'
  ```
  * 'parent_id' should be null for root agencies.
### Response
```json
{
  "status" : true,
  "msg" : "Agency created successfully."
}
```
## Read an existing agency
### Request
```bash
curl --request GET \
  --url http://127.0.0.1:5000/agency/1 \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
### Response
```json
{
    "id": 2,
    "name": "Agency #2",
    "parent_id": 1
}
```
## Read all agencies
### Request
```bash
curl --request GET \
  --url http://127.0.0.1:5000/agency \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
### Response
```json
[
    {
        "id": 1,
        "name": "Agency #1",
        "parent_id": null
    },
    {
        "id": 2,
        "name": "Agency #2",
        "parent_id": 1
    }
]
```
## Update an existing agency
### Request
```bash
curl --request PUT \
  --url http://127.0.0.1:5000/agency/2 \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form 'name=Iran Agency' \
  --form parent_id=4
```
### Response
```json
{
  "status" : true,
  "msg" : "Agency updated successfully."
}
```
## Delete an existing agency
### Request
```bash
curl --request DELETE \
  --url http://127.0.0.1:5000/agency/2 \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
### Response
```json
{
  "status" : true,
  "msg" : "Agency deleted successfully."
}
```
## Create a new ad
### Request
```bash
curl --request POST \
  --url http://127.0.0.1:5000/ad \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form agency_id=2 \
  --form 'name=a modern house' \
  --form latitude=35.7719533 \
  --form longitude=51.424691
```
### Response
```json
{
  "status" : true,
  "msg" : "Ad created successfully."
}
```
## Read an existing ad
### Request
```bash
curl --request GET \
  --url http://127.0.0.1:5000/ad/1 \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
### Response
```json
{
    "agency_id": 2,
    "latitude": 35.7719533,
    "longitude": 51.424691,
    "name": "a modern house"
}
```
## Read all existing ads
### Request
```bash
curl --request GET \
  --url http://127.0.0.1:5000/ad \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
### Response
```json
[
    {
        "agency_id": 2,
        "latitude": 35.789371,
        "longitude": 51.466271,
        "name": "a modern house"
    },
    {
        "agency_id": 2,
        "latitude": 35.789317,
        "longitude": 51.462617,
        "name": "an old house"
    }
]
```
## Read an agency (and it's subsets) ads
### Request
```bash
curl --request GET \
  --url 'http://127.0.0.1:5000/ad?agency=2&sub=true' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
* 'sub=true' argument adds the ads belong to the subsets of an agency. We can ommit that to list exclusive ads. 
### Response
```json
[
    {
        "agency_id": 2,
        "latitude": 35.789371,
        "longitude": 51.466271,
        "name": "a modern house"
    },
    {
        "agency_id": 2,
        "latitude": 35.789317,
        "longitude": 51.462617,
        "name": "an old house"
    }
]
```
* To find all subsets of an agency in the hierarchical tree, a Backtracking algorithm has been implemented like bellow:
```python
all_found_agencies = []
def find_sub_agencies(agency_id):
  '''
  This function implements a Backtracking algorithm
  to find all sub-agencies of an agency.
  ID of all sub-agencies, including the agency itself are stored
  in the list all_found_agencies.
  '''
  try:
    all_found_agencies.append(agency_id)
    for agency in Agency.query.filter_by(parent_id=agency_id).all():
      find_sub_agencies(agency.id)
  except Exception as e:
    print('error while finding sub-agencies: ' + str(e))
    raise Exception('error while finding sub-agencies: ' + str(e))
```
## Read near ads
### Request
```bash
curl --request GET \
  --url 'http://127.0.0.1:5000/ad?lat=35.771949&lon=51.426885&dist=1' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
* This API should list all the ads inside a circle around the location('lat', 'lon') with radius 'dist' Killometer.
### Response
```json
[
    {
        "agency_id": 2,
        "latitude": 35.789371,
        "longitude": 51.466271,
        "name": "a modern house"
    },
    {
        "agency_id": 2,
        "latitude": 35.789317,
        "longitude": 51.462617,
        "name": "an old house"
    }
]
```
* To compare the location with all the ads location in the database, we did not use any GIS database or extension. Instead, SqlAlchemy Hybrid methods are used to query from database directly.
* To approximate the distance between two geographical point, [Great Circle (Orthodromic) distance](https://en.wikipedia.org/wiki/Great-circle_distance) is used as follows:
```python
def orthodromic_distance(lat1, lng1, lat2, lng2, math=math):
  '''
  to compute the exact distance, we need to use some GIS database
  (forexample PostgGIS: http://postgis.refractions.net)
  However, for small distances like local map we can approximate it well
  in minimal computations using Great Circle Distance (Orthodromic Distance).
  '''
    ang = math.acos(math.cos(math.radians(lat1)) *
                    math.cos(math.radians(lat2)) *
                    math.cos(math.radians(lng2) -
                             math.radians(lng1)) +
                    math.sin(math.radians(lat1)) *
                    math.sin(math.radians(lat2)))

    return 6371 * ang
```
## Update an existing ad
### Request
```bash
curl --request PUT \
  --url http://127.0.0.1:5000/ad/2 \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form agency_id=3 \
  --form 'name=Comfortable Room' \
  --form latitude=35.7719533 \
  --form longitude=51.424691
```
### Response
```json
{
  "status" : true,
  "msg" : "Ad updated successfully."
}
```
## Delete an existing ad
### Request
```bash
curl --request DELETE \
  --url http://127.0.0.1:5000/ad/2 \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'cache-control: no-cache'
```
### Response
```json
{
  "status" : true,
  "msg" : "Ad deleted successfully."
}
```
# Run the backend app
In ordedr to start the backend app, run the folowing command
```bash
python3 backend/main.py
```