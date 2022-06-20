
# IFarm Application

## Author
# Isaac Kiptoo Kilimo.


## Description
This is a web application written in Django. This is a Neigbourhood Check app application where users can view different posts,neighbourhood,and search other business around neighbourhood. The administrator is in charge of populating the database.

## User Story
1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.


## Behaviour Driven Development (BDD)
1. Register

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| A new user must sign up to be able to post,join neighbourhood,post a business and view other people posts and images will be displayed on user timeline  | firstname,email,Username, Password1,password| User is redirected to the login page where they can login |   


2. Login

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| upon signing up successfully the user will be able to be redirected to home page where he/she be able to post and view other people posts and images | Username, Password| User is redirected to the index page where they can manage post and update their profile  |  

3. update profile

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| upon signing up successfully the user will be able to be redirected to home page where he/she be able to post and view other people posts and images,the user can also update his profile |bio,email,username,fullname, Password| User is redirected to the profile page where they can view their profile and create hood  |  

4. logout

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| upon signing up ang logging in successfully the user will be able to post and view other people posts and images will be displayed on user timeline  and he can be able to logout after navigating to the dropdown | 

5. Search by business by business name 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter a search name on the search form   | searchTerm| names that belong to that category are displayed  | 


6. Admin View

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on Admin on navigation bar | Username, Password| User is redirected to the admin page where they can manage the database  |  

7. Create hood/neighbourhood

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| On profile Click on the create hood  and upload form will available.| hood image, name,location| User is redirected to the viewhood,where he can see the hood created |  

8. View hood/neighbourhood

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the view hood on the navbar to view the hoods available and choose the one to join,the user can change the hood by leaving one and joining the one he/she wants 


## Setup/Installation Requirements
1. clone repository
     
2.  Type code based on the text editor you have and work on it.   

### Database
1. Set up Database,and put your username and password in the code

2. Make migrations
    python3.8 manage.py makemigrations picture

3. Migrate
   python3.8 manage.py migrate 
    
### Running the Application
1. Run main apllication
   * python3 manage.py runserver

2. Run tests    
   * python3.6 manage.py test imagery

###
1. Creating Admin Locally
    python manage.py createsuperuser. Then set username, email & password

2. Creating Django Admin   
     heroku run python manage.py createsuperuser. Then set username, email & password

## Technologies Used
* Python3.8
* Django 4.0
* javaScript
* Bootstrap
* PostgreSQL

## License -Copyright 

MIT License

Copyright © license 2022 ,Isaac kiptoo kilimo, student Moringa school.

## Authors Info/contacts

Github Profile - [Isaac kiptoo kilimo](https://github.com/Isaac-kiptoo-kilimo)

Email Address-[Isaac kiptoo kilimo] (isaac.kiptoo.kilimo@student.moringaschool.com)

Copyright © 2022

# project layout

### Homepage
![Neighbourhood](/static/images/landing.png)

### Register 
![Neighbourhood](/static/images/signup.png)

### Login 
![Neighbourhood](/static/images/login.png)


