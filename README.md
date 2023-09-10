
# Django-RestFramework-UAV-Rental-System

UAV Rental Project with Django




 


## Technologies Used

- Python
- Django
- Postgresql
- Rest Framework
- PgAdmin4


  
## Features

- Membership and Login Screens
- CRUD operations for UAV (Unmanned Aerial Vehicle) rental, including Add, Delete, Update, List, and Rent operations
- UAV Specifications: Brand, Model, Weight, Category, etc.
- Recording of UAV rental transactions by members
- CRUD operations for rented UAVs, including Delete, Update, and List operations
- Rental Details: UAV, Date and Time Intervals, Renter, etc.
- Filtering and search functionality for all listing pages
- Admin page for system management
- Login is mandatory
- User permissions are implemented; regular users cannot access admin pages
  
## Running the Project on Your Computer
Clone the project (Windows)

```bash
git clone https://github.com/onlinEngineer/Django-RestFramework-UAV-Rental-System.git
cd Django-RestFramework-UAV-Rental-System/ihaapp
python -m venv myenv
.\myenv\Scripts\activate
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install psycopg2
cd ApiProject

```
Clone the project (Linux)

```bash
git clone https://github.com/onlinEngineer/Django-RestFramework-UAV-Rental-System.git
cd Django-RestFramework-UAV-Rental-System/ihaapp
python3 -m venv myenv
source myenv/bin/activate
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install psycopg2-binary
cd ApiProject

```

Start the project

```bash
#Windows
python manage.py runserver

#Linux
python3 manage.py runserver
```

After importing ihakiralama.sql into pgAdmin4, you can log in with the following admin credentials to access the admin page.

```bash

Admin username: admin
Password: admin123

```


API Links
```bash
http://127.0.0.1:8000/api/iha/
http://127.0.0.1:8000/api/kirala/
http://127.0.0.1:8000/api/users/

```




Sayfa Links
```bash
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/register/
http://127.0.0.1:8000/login/
http://127.0.0.1:8000/home/
http://127.0.0.1:8000/iha-list/
http://127.0.0.1:8000/kira-list/
http://127.0.0.1:8000/user-list/
http://127.0.0.1:8000/user-kiralama/
```

Database Configuration
```bash

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ihakiralama',
        'USER':'postgres',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'5432'
    }
}

```


## Screenshots
### Register Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/603a24ca-b858-4811-8101-78b4f5ae73aa">

### Login Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/287df9d0-3ed3-4d73-96f6-15c125bd284b">

### Admin User Management
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/afeccfcd-fef0-43b8-bbc7-23973732dc2f">

### Admin Home Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/8ec47096-d967-4a71-8f11-ff7f584e2827">

### Admin UAV CRUD Management
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/8d2f7b47-427c-4a93-b0d9-ac00cb1466fa">

### Admin Rental CRUD Management
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/5358b2d8-5acb-4274-ab90-0cebda32d84d">

### Admin Rental Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/278faa79-c167-42c2-af5e-6f2af03b7228">

### Admin Users Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/763415df-9b36-4494-bebf-92b31ddd6df1">

### User Home Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/67aa4611-807c-40ef-bb8e-bb36fffe1ac3">

### User Rental Page
<img src="https://github.com/onlinEngineer/Django-RestFramework-IHA-Kiralama-Sistemi/assets/70773825/d246727d-48d9-45d2-896f-ecb2fa7abf5c">

  
## Additions

- Datatables are used for listing pages
- Relational tables are kept separate
- Extra libraries are used for Django
- Bootstrap, Jquery, Ajax, etc. are used for the front-end
