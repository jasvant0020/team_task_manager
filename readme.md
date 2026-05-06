# Team Task Manager

A full-stack Team Task Management Web Application built with Django + Tailwind CSS.

This app allows teams to collaborate by creating projects, assigning tasks, and tracking progress — similar to tools like Trello or Asana.

---

# Features

## Authentication

* User Signup / Login / Logout
* Role-based access (Admin / Member)

## Project Management

* Create projects (Admin only)
* Add / Remove members
* Members can view assigned projects

## Task Management

* Create tasks (Admin only)
* Assign tasks to members
* Update task status (To Do / In Progress / Done)

## Dashboard

* Total tasks
* Tasks by status
* Overdue tasks
* Tasks per user (Admin only)

## Role-Based Access

* Admin → manage projects, members, tasks  
* Member → view and update assigned tasks only  

---

# Demo Credentials

Use the following credentials to test the application:

## Admin
username=admin  
password=temp@123  

## Member 1
username=member1  
password=temp@123  

## Member 2
username=member2  
password=temp@123  

---

# Demo Video

Watch the full demo here:  
https://your-demo-video-link.com

---

# Tech Stack

* Backend: Django  
* Frontend: Tailwind CSS  
* Database: SQLite (dev) / PostgreSQL (prod)  
* Deployment: Railway  

---

# Local Setup

# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/team_task_manager.git
cd team_task_manager

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (optional)
python manage.py createsuperuser

# 7. Run server
python manage.py runserver

---

# Tailwind Setup

python manage.py tailwind install  
python manage.py tailwind start  

---

# Deployment (Railway)

# 1. Initialize git
git init
git add .
git commit -m "Initial commit"

# 2. Connect to GitHub
git remote add origin https://github.com/jasvant0020/team_task_manager.git
git branch -M main
git push -u origin main

---

# Deploy on Railway

# 1. Go to Railway
https://railway.app/

# 2. Create new project → Deploy from GitHub

# 3. Select your repository

# 4. Add environment variables:

DEBUG=False  
SECRET_KEY=your_secret_key  
ALLOWED_HOSTS=*  

# 5. Add PostgreSQL service from Railway dashboard

# 6. Run migrations
python manage.py migrate

# 7. Collect static files
python manage.py collectstatic --noinput

---

# Environment Variables

DEBUG=False  
SECRET_KEY=your_secret_key  
DATABASE_URL=your_postgres_url  
ALLOWED_HOSTS=*  

---

# Notes

* Only Admin can create projects and assign tasks  
* Members can only update their assigned tasks  
* Proper access control implemented across all views  

---

# Author

JASVANT  
https://github.com/jasvant0020
