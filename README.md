Event Management
The project is a Django-based web application with PostgreSQL as the database.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Description
The Event Management App is a comprehensive solution designed to streamline the process of planning, organizing, and managing events. Whether it's a conference, seminar, trade show, or social gathering, this app provides a centralized platform for event organizers to efficiently handle various aspects of event management.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Technologies Used
Django
PostgreSQL
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Features
Post listing
Search listing
Update listing
Search listing Based on Filter
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Posting listing
Posting listing: This operation allows users to post details about a event. Users can provide information such as the date, time, size,and any other relevant details.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Update Your Record
Update Your Record: This operation enables users to update their existing  listings. If there are any changes or updates to the details of a posted listings, users can use this feature to edit and modify their records.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Search listing Based on Filter
Search Property Based on Filter: This operation allows users to search for listings based on specific filters. Users can define their preferences, such as size,  and any other relevant criteria. The bot will then present them with listings that match their specified filters.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Installation
Clone the repo

git clone
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Install Python packages

pip install -r requirements.txt
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Create a .env file in the root directory and add the API token

DB_NAME='Eventmanagement'
USER= 'postgres'
PASSWORD= 'Saurabh123'
HOST= 'localhost'
PORT= '5432'
SECRET_KEY='django-insecure-31rysd5))l%j=l627egpcn$0%5-q#%d6qzg!q5x8@zgm7femt%'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Run this command
python manage.py makemigrations
python manage.py migrat
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Run the file

python manage.py runserver