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