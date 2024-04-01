# Sort and Display Data Application
## Overview:
This application is designed to read data from a file named "Parcels.txt", process the data, and display it in two separate tables on a web interface.
The first table is sorted by street name and number, while the second table is sorted by the first name of the owner.
The application is built using Python's Flask framework for the backend and utilizes HTML/CSS for the frontend.

## File Structure:
* **app.py:** This is the main Python file that contains the Flask application and the backend logic for processing the data.
* **index.html:** This file contains the HTML markup for the web interface. It displays the tables and handles user interaction.
* **index.css:** This file contains the CSS styles for styling the HTML elements.
* **Parcels.txt:** This is the data file from which the application reads the parcel information.

## Dependencies:
* **Flask:** Flask is a micro web framework for Python used to develop web applications.
* **Pandas:** Pandas is a data manipulation library for Python. It is used here to read and manipulate data from the CSV file.
* **re (Regular Expressions):** The re module provides support for working with regular expressions in Python.
It is used for pattern matching in extracting information from addresses and owner names.

## Installation:
1. Ensure you have Python installed on your system.
2. Install Flask and Pandas using pip: `pip install flask pandas`

## Running the Application:
1. Navigate to the directory containing the application files.
2. Run the following command to start the Flask development server: `flask run`
3. Open a web browser and go to <http://localhost:5000/> to view the application.

## Functionality:
* The application reads data from the "Parcels.txt" file, which contains information about parcels including address, owner, market value, sale date, sale price, and link.
* It processes the data to extract relevant information such as street name, number, first name, and last name of the owner.
* The processed data is displayed in two separate tables on the web interface.
* Users can navigate between the tables using the provided buttons.
* The application also provides a link to Google Maps for each record, allowing users to view the location on the map.
