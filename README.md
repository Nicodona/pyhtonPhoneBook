# mastering python python4dev
- This repo is meant to enrich our selves in open source contribution to projects and how to work on a project as a team

- phonebook console application is a project for python4dev group to help master skills the project contains
- when the program is running user should be able to add, delete, edit and read contacts from contact list. 
- this app is to be built using python using Object Oriented Programming

# Contribution(contrib) guide
### contrib Part1
1. fork this repo
2. clone a local copy using. `git clone <your_forked_repo_url.git`
3. cd into `pyhtonPhoneBook`
4. Add upstream to easily grab updates `git remote add upstream https://github.com/Nicodona/pyhtonPhoneBook`
5. create a branch and checkout- run `git checkout -b <your_branch_name`

# Tools
- OS windows: Download [MySQL Installer](https://dev.mysql.com/downloads/installer/)
    - Open installer and download the following or manually by clicking on each tool below
    - [Connector/Python - 8.0.26](https://dev.mysql.com/downloads/connector/python/) . Make sure to select OS
    - [MySQL server - 8.0.26](https://dev.mysql.com/downloads/mysql/)
    - On successful installation of MySQL server, Setup the server following the below procedure - `## Server configuration on windows`
    - [MySQL Workbench - 8.0.26](https://dev.mysql.com/downloads/workbench/) 
- OS Linux ubuntu - [Steps](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
    - [Connector/Python - 8.0.26](https://dev.mysql.com/downloads/connector/python/). Make sure to select OS
    - Install [MySQL Workbench - 8.0.26](https://dev.mysql.com/downloads/workbench/) 
- OS Linux other - Follow above for Ubuntu and create an issue with the message `Tool configuration failed for <Your_OS_Name>` if it fails.

## Server Configuration on windows
1) file1 type$networking 
2) file2 AuthMethod
3) file3 choose windows service
5) create a simple password e.g `myserver` or `testserver` or `phonebookserver` or any other memorable password. We shall update this value in production 

## Install all requirements
`pip install -r requirements.txt`

## Basic configuration
- `cd` to `pyhtonphonebook`
- create a `.env` file with the following
`
HOST=<YOUR_HOST_NAME>
USER=<DB_USERNAME>
PASSWORD=<USER_PASSWORD>
`
`host` and `user` could be `locahost` and  `root` respectively (in my case ofcourse)
## Running the App
- `cd` to `pyhtonphonebook` 
- OS windows: run `python dbconfig.py`. Don't modify this file. Rather create a descriptive issue if you would want the file to be modified
- OS Linux - ubuntu or other Linux distri: run `python3 dbconfig.py`

### contrib Part2
Reminder: `pyhtonphonebook/delta/matrix.py` is the only file to edit here.
6. start writing your code 😄
7. .......
8. when done run: `git add .`
9. `git commit -m "your commit message"`
10. `git push origin <your_branch_name`
11. navigate to your remote forked copy and create a Pull Request (PR)
