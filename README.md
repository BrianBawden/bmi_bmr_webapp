# Overview

For this project I wanted to learn how to use Django to help create a website. I decided to build a website that users can log into, enter some basic information: weight, height, age, and gender. The web app would then calculate the users BMI and their BMR using a mathematical formula. I then wanted the web app to allow the user to track their information in a data base and show them their progress over time as their BMI changed.

First, I learned how to create a virtual environment to work out of and downloaded Django in that virtual environment. I learned a lot here because I had to learn how to navigate in the terminal, activate virtual environments, and run a server on my computer. As for Django I got to see how much was done by entering a few commands in the terminal like: django-admin startproject and python manage.py startapp. At first I struggled to understand it all, but I followed along with several tutorials and was able to get my bearings. 

Once I knew some basics, I took what those tutorials showed me and used that to make my own web app. I learned how to create a base.html file in a templates file and how to let Django know where to find the templates. Then I added the little details for the BMR and BMI web pages separately. 

To see the website, I would go to the terminal to the parent folder that had my virtual environment and type 'source my_venv/bin/activate' and hit enter. Once the virtual environment was activated, I would go into the main file that had my manage.py file and type: 'python3 manage.py runserver' to get the web address to see the website locally. the address was 'http://127.0.0.1:8000/' to see the home page.


{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/PBBnb082ddg)

# Web Pages

The first page I created was just a simple home page with links in the navigation bar to the BMR and BMI pages. All three pages have a similar navbar and basic styling because I used the base.html webpage. In the BMR page it has some boxes to take in information from the user like weight, height, age, gender, and a submit button. After the information is entered and submit is clicked the program runs some basic calculations and shows the user their BMR. BMI is very similar but it only needs weight and height from the user.

# Development Environment

Tools used:

* VScode
* Django
* Virtualenv

Languages Used:

* Python
* HTML
* JavaScript

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [YouTube](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=2151s)
* [YouTube](https://www.youtube.com/watch?v=vkBiEuZSq9s)
* [Udemy](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/learn/lecture/4954484#content)
* [Realpython](https://realpython.com/django-setup/)

# Future Work

* Improve css styling
* Add user login 
* Tracking user data in database
