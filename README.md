## Sensor Data Web App Documentation



### Table of Contents
1.	Introduction
2.	Installation
3.	Usage
•	Starting the Application
•	Accessing the Web App
4.	Features
•	Data Display
•	Data Manipulation
•	Sorting and Filtering
5.	Technologies Used
6.	Contributing
7.	License
 
### 1. Introduction
The Sensor Data Web App is a Python Flask-based web application designed to display and manage sensor data stored in an SQLite database. The app provides a user-friendly interface for viewing sensor data such as temperature, pressure, and humidity, and allows users to add, update, sort, and filter data.


### 2. Installation
To run the web app locally, follow these steps:
1.	Clone the repository:
   ```sh
   git clone https://github.com/falahgithub/safetywhat.git 
   ```

2.	Navigate to the project directory:
```sh
cd your-repo
``` 
3.	Install the required dependencies:
```sh
pip install -r requirements.txt 
```

### 3. Usage
* Starting the Application
  
  To start the application, run the following command from the project root directory: python server.py
  
* Accessing the Web App

  Once the application is running, open a web browser and access the app at http://localhost:5000.


### 4. Features

#### Data Display
*	The app displays sensor data from the SQLite database, including city name, temperature, pressure, and humidity.

#### Data Manipulation
*	Users can add new sensor data by clicking the "Add new data" button and filling out the required information in the form.
*	Existing data can be updated by clicking the "Update any data" button and filling out the required information in the form.

#### Sorting and Filtering
*	Sorting: Users can sort the displayed data by temperature, pressure, or humidity using radio input buttons.
*	Filtering: Users can filter data by city name to display only the data for a specific city.



### 5. Technologies Used
*	Python
*	Flask
*	Flask-SQLAlchemy
*	SQLite
*	Bootstrap (for frontend)


### 6. Contributing
Contributions to the project are welcome. To contribute, follow these steps:

1.	Fork the repository.
2.	Create a new branch for your feature or bug fix.
3.	Make your changes and commit them with clear and concise messages.
4.	Push your branch to your forked repository.
5.	Create a pull request to the original repository.



### 7. License
This project is licensed under the MIT License.
Feel free to add more details, code snippets, or specific instructions based on your project's needs. Documentation is a crucial part of maintaining and sharing a project, so make sure to keep it up to date as your project evolves.

