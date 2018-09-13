# Vue + Django

## Description
The following is a project starter that aims to provide a quick start for all who uses it.

## Introduction

The first approach was to provide a project that can make Django work together with Vue smoothly.
After that, the following steps were:
- Provide SCSS precompilation
- Configure Server-Side Rendering
- Create a sample api using Django-Rest and integrate to the project
- Replicate the api previously mentioned using GraphQL and use it for the whole project dataflow
- Provide a easy approach for creating the project files such as components, filters, routes, etc.

## Overview

The project has the following directory structure:
***/backend***: This folder containts the server related files and the whole django app
***/frontend***: This folder containts the frontend files. This is the place where the app gets prettier and useful
***/dev***: This folder contains an environment activation script
***/static***: This folder contains the files that there generated by the webpack serving process


## Installation

1) First at all, clone this repo! :D
2) Create a virtualEnv by running: `virtualenv env`
3) Install the dependiencies for the whole project by running these commands:
    `npm start` or  `yarn install`
    `pip install -r requirements.txt`
    `pip install -r requirements-dev.txt`
4) At this point, you'll need to provide the database setup, for that purpose, update the *settings.py* file. With the purpose of providing a working project, that file is already set with a functional setup.


### Create DB

sudo -u postgres createuser playground
sudo -u postgres createdb playground

### Enter Postgres

sudo -u postgres psql

### Give privileges

grant all privileges on database to playground

### Set user password

sudo -u postgres psql playground
\password playground
Password
playground


5) Execute the migrations by running: `migrate` (*). It should reflect the django models in database.
6) At this time you must be able to run `serve` and watch your app working. (**)

(\*): The *enter.sh* script has many useful aliases for the most common operations and commands. Here is a list of these:

**serve**: Run the whole webapp
**migrations**: Generate the migrations for the backend django app
**migrationsall**: Generate the migrations for all the django app
**migrateall**: Execute the migrations for all the django app
**migrate**: Execute the migrations for the backend django app
**shell**: Run the shell_plus
**createuser**: Create

(\*\*): The project is already set up for allowing you to use the default django admin. For that purpose you need to create a django superuser, the following line will solve that: `createuser` and the script will ask for the required data.

## Hints
Use the **pygen** command for letting your project grow faster.
You can check its documentation in https://github.com/jdimodugno/py-generator
