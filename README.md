# Molveno

## Intro
>Molveno is a fictive hotel/restaurant application build in Python/Django by students of the Mastery program 2018.
>It simulates a business scenario where an hotel owner assigns a development team with the task to build a custom apllication based on his wishes.

Introduction and instructions for the Molveno repository goes here:
**Todo**

## Setup the environment
* See [how to install conda](https://conda.io/docs/user-guide/install/index.html) on your OS
* Create and switch to the virtual environment
* Clone the molveno repository
* Migrate any changes to the database

Setup environment.
```sh
$ conda create --name molveno_env django
$ conda activate molveno_env

```

Optionally set the virtual environment interpreter in your IDE.  
Run 'which' to find the interpreter path and executable.

```sh
$ which python
``` 

Clone the repository to your project folder.
```sh
$ cd <project-directory>
$ git clone https://github.com/MichaelAkkermans/molveno.git .
```

Migrate
```sh
cd <project-directory>
python manage.py migrate
```

Development database credentials  
admin  
Password321
