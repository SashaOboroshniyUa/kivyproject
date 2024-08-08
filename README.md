![taxi-service logo](readme.images/home.png)

# taxi-service
***
This is a simple application made for educational and demonstration purposes. Implements 
authentication by filters based on session. Logs some Authentication information and create/update/delete database operations to console and ```.log``` file. Registration of new drivers, managing the relations between cars, drivers and manufacturers and other CRUD operations.  
Program has following functionalities:
- create new Manufacturer
- display all Manufacturers
- create new Driver
- display all Drivers
- create new Car
- display all Cars
- add driver to car
- list all cars by driver

You can access all of them from the main ```/index``` page  
after registering as a new driver at ```/drivers/add``` page  
and signing in at ```/drivers/login``` page (to which you will be redirected if you will try to access pages that are not allowed for unsigned drivers).  
After that you will have access to all the pages and functionality.

## Screenshots
![screenshot1](readme.images/screenshots/1.png)
![screenshot2](readme.images/screenshots/2.png)
![screenshot3](readme.images/screenshots/3.png)

---
## Architecture
1. DAO - Data access layer
2. Service - Application logic layer
3. Controllers - Presentation layer
---
## Technologies
- Java 11
- Apache Maven
- Apache TomCat
- Apache Log4j2
- MySQL
- JDBC
- Http Servlet
- JSTL
- JSP
- HTML, CSS, XML, Bootstrap

---
## How to run a project
*WARNING* Installed TomCat and MySQL is compulsory for this project.
1. Add a tomcat local configuration in IntelliJ (Tomcat server - local, deployment - war 
exploded, application context: /)
2. Run SQL script located in ```src/main/resources/init_db.sql``` to set up a database for this project.
3. Configure ```src/main/java/taxi/util/ConnectionUtil.java``` with your ```URL```, ```USERNAME```, ```PASSWORD``` and ```JDBC_DRIVER```.
4. In the ```src/main/resources/log4j2.xml``` at line 7 you also need to set ```ABSOLUTE_PATH``` to your ```.log``` file.
5. Import Maven dependency from pom.xml.


---
## Demo
https://salty-citadel-80806.herokuapp.com/

Login: root

Password: 1234

---
## Your database should look like this

![shema DB](readme.images/taxi-database-image.png?raw=true "Database")

---
## Contacts
My [LinkedIn](https://www.linkedin.com/)  
