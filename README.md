# News collector web application
News collab is a web application that parses and collects data from different news platforms to have them all under one website to provide ease of access for a more diverse envirnoment of updated daily news along with several different categories, giving the user the chance to have a comfortable way of surfing different news just from only one website.

## More information
* The web application is made by using Flask framework in Python.
* Database used is SQLite, all the managed tables and data is under the management of SQLite.
* The web application is dockerized. So, it runs using Docker application using traditional ```build``` mechanism. For easier access using docker, ```docker-compose up``` functionality is available, simply run the command and follow the procedure to get it working on local machine.
* Hosting on GKE with an IP Address link is available, will be updated here soon.

## Easy run
* Download the git repository to a folder in the local machine.
* Run ```run.py``` file, which will open command prompt that contains an IP address that looks as the following address ```http://0.0.0.0:8080/```.
* Change that latter address with the following ```http://localhost:8080/``` and paste it to the browser. The web application should run smoothly. Happy surfing!


## To run using an IDE such PyCharm, VS Code and so on..
* Run the ```run.py``` file in the main directory, the running function responisble to locally run the Flask application on the system.
* In the run window terminal on the IDE, copy and paste the following link ```localhost:8080``` and press enter. 
