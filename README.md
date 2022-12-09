<!-- BACK TO TOP -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
![GitHub top language](https://img.shields.io/github/languages/top/demian-truk/ludik?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/demian-truk/ludik?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/demian-truk/ludik?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/demian-truk/ludik?style=for-the-badge)


<!-- PROJECT LOGO & TITLE -->
<br />
<div align="center">
  <a href="https://github.com/demian-truk/ludik">
    <img src="LUDIK GAMES.gif" alt="Logo">
  </a>

  <h1 align="center">LUDIK</h1>

  <p align="center">
    <a href="#about-the-project">About The Project</a>
    ·
    <a href="#built-with">Built With</a>
    ·
    <a href="#setup">Setup</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
# About The Project

The Ludik project is a website for storing and distributing information about games and everything related to them.

<p>Here you can get information about the games you are interested in, find out the latest news of the gaming industry,
view reviews, analyze guides or participate in the discussion of topics of interest.</p>

<p>This project was created in order to consolidate the skills and abilities acquired during the training
course «Python Developer» from the school of programming «TeachMeSkills».</p>

Link to the course: https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-minsk

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- BUILT WITH -->
# Built With

* [![Django][Djangoproject.com]][Djangoproject-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- SETUP -->
# Setup

### Step 1. Clone a repository.

```sh
git clone git@github.com:demian-truk/ludik.git
```

### Step 2. Create a virtual environment for installing dependencies and activate it.

```sh
python3 -m venv venv
source venv/bin/activate
```

### Step 3. Install dependencies.

```sh
pip install -r requirements.txt
```

### Step 4. Create a local database and tables in it.
```sh
python3 manage.py migrate
```

### Step 5. Create a system user.
```sh
python3 manage.py createsuperuser
```

### Step 6. Run the app.
```sh
python3 manage.py runserver
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[Djangoproject.com]: https://img.shields.io/badge/Django-1c6e34?style=for-the-badge&logo=django&logoColor=white
[Djangoproject-url]: https://www.djangoproject.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
