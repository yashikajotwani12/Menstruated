<h1 align="center">
             Menstruated :drop_of_blood:
</h1>

## Tech Stack:

<img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/> <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/> <img src ="https://img.shields.io/badge/sqlite-%2307405e.svg?&style=for-the-badge&logo=sqlite&logoColor=white"/>


<p align="center">
    ✨ Welcome to Menstruated ✨ <br />
  
  ![](https://github.com/yashikajotwani12/Menstruated/blob/master/menstruated.gif)
    
</p>
<br />



- **Frontend:** Html,Css
- **Backend:** Django
- **Version Control:** Git and GitHub
- **Hosting:** Heroku
- **Code Editor and tools**: VS Code




# Table of Contents

    - Overview
    - Features
    - Future Prospects
    - Setup Guidelines
    - Contribution Guideline
    

## Overview 🔨
Menstruated is a place where women share their first-period stories, feelings, emotions through blogs. Can track their periods and get notified early through the mail. They should know that they are not alone in the fight against PCOS by-polls which shown in the graph and many other questions. Can know the myths/facts, self-care during periods.

## Features:

- [x] Sign up, Login, Logout
- [x] Write Blog
- [x] Edit Profile
- [x] Polls
- [x] PeriodDate Reminder
- [x] Information about Pcods, Self care
- [x] Frequently asked questions
- [x] Contact section

## Folder Structure  📒
* [Project](https://github.com/yashikajotwani12/Menstruated/tree/master/StainStrong)
* Apps
    - [HomePage](https://github.com/yashikajotwani12/Menstruated/tree/master/Home)
    - [AppBlog](https://github.com/yashikajotwani12/Menstruated/tree/master/App_Blog)
    - [AppLogin](https://github.com/yashikajotwani12/Menstruated/tree/master/App_Login)
    - [Polling App](https://github.com/yashikajotwani12/Poll)
    - [PeriodsDateReminder](https://github.com/yashikajotwani12/PeriodsDateReminder)
    - [Chatting App](https://github.com/yashikajotwani12/LetsChat)
* [Static Files](https://github.com/yashikajotwani12/Menstruated/tree/master/static)
* [Templates](https://github.com/yashikajotwani12/Menstruated/tree/master/templates)


## Future Prospects:

- Location detection and details of nearby gynecologist.
- Adding quiz app which will take inputs about periods and give information of what is right and wrong.


# UI of Website

| ![AboutUs](https://user-images.githubusercontent.com/77020164/124215057-f3bad700-db10-11eb-8f7c-f0d44d1b25b3.png) | ![Explore Blogs](https://user-images.githubusercontent.com/77020164/124214911-a6d70080-db10-11eb-811e-6eac01d9bca1.png) | ![Add data](https://user-images.githubusercontent.com/77020164/124214935-b2c2c280-db10-11eb-992e-109f4311f61c.png) | ![Fields](https://user-images.githubusercontent.com/77020164/124214915-a8a0c400-db10-11eb-845f-0c028258b207.png) | 
|-|-|-|-|
| About Us | Explore Page | Add Data | Fields |
| ![Period date reminder](https://user-images.githubusercontent.com/77020164/124214971-c5d59280-db10-11eb-9aed-2cc00df9d296.png)| ![polls](https://user-images.githubusercontent.com/77020164/124214993-d128be00-db10-11eb-98a8-58264ccc7c17.png) | ![contactsection](https://user-images.githubusercontent.com/77020164/124214900-a2124c80-db10-11eb-8ffb-23fb22e67857.png) | ![Blog List](https://user-images.githubusercontent.com/77020164/124214942-b5bdb300-db10-11eb-90e6-a348769bbb44.png) |
| PeriodDateReminder | Pollstoknow | Contact section | Blog List |

<!-- 
  [![ Explanation YouTube vedio] (![Screenshot (76)](https://user-images.githubusercontent.com/77020164/126889748-df0c72fa-c579-4c23-8b1d-1248dc2c3c5c.png))](https://youtu.be/icB4Uq4orRc) 
 -->
<!-- ![Screenshot (76)](https://user-images.githubusercontent.com/77020164/126889748-df0c72fa-c579-4c23-8b1d-1248dc2c3c5c.png) -->


<!-- 
[![ Explanation YouTube vedio ](![Screenshot (76)](https://user-images.githubusercontent.com/77020164/126889609-224b13d8-2ceb-4309-9e86-07b296aa5fdc.png)
)](https://youtu.be/icB4Uq4orRc) -->
<!-- 
<iframe width="560" height="315" src="https://www.youtube.com/embed/icB4Uq4orRc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->

## YouTube Vedio:
[![ Explanation YouTube vedio ](http://img.youtube.com/vi/icB4Uq4orRc/0.jpg)](https://www.youtube.com/embed/icB4Uq4orRc)


 <details>
  <summary><strong>Setup Steps</strong></summary>
  
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Make migrations using
```
$ python manage.py makemigrations
```
- Migrate Database
```
$ python manage.py migrate
```
- Create a superuser
```
$ python manage.py createsuperuser
```
- Run server using
```
$ python manage.py runserver
``` 
  
</details>

[![Uses Git](https://forthebadge.com/images/badges/uses-git.svg)](https://github.com/yashikajotwani12/Menstruated) [![Uses HTML](https://forthebadge.com/images/badges/uses-html.svg)](https://github.com/yashikajotwani12/Menstruated) [![Uses CSS](https://forthebadge.com/images/badges/uses-css.svg)](https://github.com/yashikajotwani12/Menstruated) 
[![Built with love](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/yashikajotwani12/Menstruated) [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://github.com/yashikajotwani12/Menstruated)

