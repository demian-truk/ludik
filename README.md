<!-- BACK TO TOP -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
![GitHub top language](https://img.shields.io/github/languages/top/demian-truk/ludik?style=flat)
![GitHub language count](https://img.shields.io/github/languages/count/demian-truk/ludik?style=flat)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/demian-truk/ludik?style=flat)
![GitHub](https://img.shields.io/github/license/demian-truk/ludik?style=flat)


<!-- PROJECT LOGO & TITLE -->
<br />
<div align="center">
  <a href="https://github.com/demian-truk/ludik">
    <img src="LUDIK GAMES.gif" alt="Logo">
  </a>

  <h1 align="center">LUDIK</h1>

  <p align="center">
    <a href="#about-the-project">About the project</a>
    ·
    <a href="#setup">Setup</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
# About the project

There should have been a description of the project here :D


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
