Catalyst Count

Catalyst Count is a Django-based web application that allows users to upload and process CSV files containing company data. The application provides functionalities to upload files, process them, and filter data based on specific criteria.

Table of Contents

	•	Features
	•	Technologies Used
	•	Usage
	•	File Upload and Processing
	•	Filtering Data

Features

	•	Upload CSV files containing company data.
	•	Process and store company data from CSV files.
	•	Filter and display company data based on user input.

Technologies Used

	•	Django
	•	PostgreSQL
	•	django-allauth
	•	django-environ
	•	PyJWT
	•	HTML, CSS, JavaScript (for the frontend)

Installation

Prerequisites

	•	Python 3.x
	•	Pip
	•	PostgreSQL

Create a .env file in the project root and add the following configurations:
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver

* Usage

File Upload and Processing

	1.	Navigate to the Upload Page:
Open your web browser and go to http://localhost:8000/upload.
	2.	Upload a CSV File:
Select your CSV file and click on the “Upload” button. The file will be processed, and the data will be stored in the database.

Filtering Data

	1.	Navigate to the Filter Page:
Open your web browser and go to http://localhost:8000/filter.
	2.	Filter Data:
Enter a filter criterion (e.g., a company name) and click on the “Filter” button to see the filtered results.

Contributing

Contributions are welcome! Please follow these steps to contribute:

	1.	Fork the repository.
	2.	Create a new branch: git checkout -b my-feature-branch
	3.	Make your changes and commit them: git commit -m 'Add some feature'
	4.	Push to the branch: git push origin my-feature-branch
	5.	Submit a pull request.
