### Django Python MySQL Project

## Introduction
 This project demonstrates connecting a Django application to a MySQL database and displaying all records from the `traffic_volumes` table on a web page.
My first python app beginner project lol 

![image](https://github.com/freda1874/DjangoPythonProject_Beginner/assets/85437054/7f94e565-6941-4c54-bf94-c8bd31bd8bfe)

## Features

- Connects to a MySQL database.
- Retrieves and displays all records from the `traffic_volumes` table using Django framework
  ![image](https://github.com/freda1874/DjangoPythonProject_Beginner/assets/85437054/b7053a25-ec58-46a7-9a6c-7774456572ff)

![image](https://github.com/freda1874/DjangoPythonProject_Beginner/assets/85437054/a8cee3f8-5068-4660-9ce6-558333fcf631)

## Prerequisites
- Python 3.x
- Visual Studio Code
- Django 3.x or later
- MySQL server
- MySQL client library (`mysqlclient`)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   # or
   source myenv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install django mysqlclient
   ```

## Database Setup

1. **Configure `settings.py`:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

2. **Create the `traffic_volumes` table in MySQL:**
   ```sql
   CREATE TABLE traffic_volumes (
       SECTION_ID INT PRIMARY KEY,
       HIGHWAY INT,
       SECTION INT,
       SECTION_LENGTH DOUBLE,
       SECTION_DESCRIPTION TEXT,
       Date TEXT,
       DESCRIPTION TEXT,
       GROUP TEXT,
       TYPE TEXT,
       COUNTY TEXT,
       PTRUCKS TEXT,
       ADT INT,
       AADT INT,
       DIRECTION TEXT,
       PCT85 TEXT,
       PRIORITY_POINTS TEXT
   );
   ```

## Django Setup

1. **Create a Django app:**
   ```bash
   python manage.py startapp traffic
   ```

2. **Add `traffic` to `INSTALLED_APPS` in `settings.py`.

3. **Define the `TrafficVolume` model in `models.py`:**


4. **Make and apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Views and Templates

1. **Create a view in `views.py` to fetch and display data:**
   ```python
   from django.shortcuts import render
   from .models import TrafficVolume

   def traffic_data(request):
       data = TrafficVolume.objects.all()
       return render(request, 'traffic/traffic_data.html', {'data': data, 'author': 'Your Name'})
   ```

2. **Configure URLs in `urls.py`:**
   ```python
   from django.urls import path
   from .views import traffic_data

   urlpatterns = [
       path('traffic/', traffic_data, name='traffic_data'),
   ]
   ```

3. **Include the app URLs in the project's `urls.py`:**
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('traffic.urls')),
   ]
   ```

4. **Create the `traffic_data.html` template:**
  

## Running the Project

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/traffic/` to see all records displayed on the web page.

