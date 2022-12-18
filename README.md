# django_online_examination_system
This online examination system project focuses on dealing with student’s examinations. Also, the system displays all the available course and their question sets. In addition, the system allows managing question set by entering questions, options, and answers. This project is divided into two categories: Student and Admin Panel. In an overview of this web application, a student can simply register and start using it. Here, the system displays all the exams for the student. And the student can proceed to attend their examinations. All the exams are of MCQ type.
The Online Examination System (OES) is created for taking online exam has following stages:
 	Admin
 	Register
 	Login
 	Exam
 	Results

Specific Purpose:
i.	Enables the Admin to create subjects to be undertaken by students.
ii.	Enables the Admin to register Students.
iii.	Enables the Admin to create papers to be undertaken by students.
iv.	Enables the Admin to create Questions to be undertaken by students.
v.	Enables the Admin to manage exam results.
vi.	Ensures timings of student exam papers.
vii.	Ensures exams are marked correctly.

We have developed this project using the below technology:
	HTML : Page layout has been designed in HTML
	CSS: CSS has been used for all the designing part
	JavaScript : All the validation task, logic and animations has been developed by JavaScript 
	Python : All the backend logic has been implemented in Python 
	SQLite3 :SQLite3 database has been used as database for the project 
	Django : Project has been developed over the Python-based Django Web Framework

     Applications Used:
	Visual Studio Code (Code Editor) : The whole coding of the program is written here.
	DB Browser: To check all the Database tables.

•	Install python3 if not installed in your system 
•	Install pip- Open command prompt and enter following command-

python -m pip install -U pip

•	Install virtual environment- Enter following command in cmd-

pip install virtualenv

•	Create a virtual environment by giving this command in cmd-

virtualenv online_exam_system

•	Change directory to online_exam_system by this command-

cd online_exam_system

•	Go to Script directory inside online_exam_system and activate virtual environment-

cd Scripts\Activate.ps1

•	Install Django- Install django by giving following command-

> pip install django

(online_exam_system) D:\(folder_name)( online_examination_system)> python manage.py mkemigrations
(online_exam_system) D:\(folder_name)( online_examination_system)> python manage.py migrate
(online_exam_system) D:\(folder_name)( online_examination_system)> python manage.py runserver

We can access our server from the local host : http://127.0.0.1:8000/

Then to use the system create superuser using
(online_exam_system) D:\(folder_name)( online_examination_system)> python manage.py createsuperuser
'Enter Registration ID and password twice to make your own admin account'
