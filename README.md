## Recurse Centre Application

Here are my two small programs for the Recurse Centre application. 

The specification for cracklepop are the following:

Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle instead of the number. If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. You can use any language.


The other program is the famous game of fifteen. I had coded a [solution in C](https://gist.github.com/gsime1/30e2e2a3dc6f2b216f955626182288c9) for a problem set for a computer science course (CS50), which I tackled again in Python, using a functional paradigm. Here's the specs:

Implement the Game of Fifteen, per the below.

$ ./fifteen 3
WELCOME TO GAME OF FIFTEEN

8  7  6

5  4  3

2  1  _

Tile to move:

## Environment and setup

You should not need to install any third party package as we only use python libraries (sys, os, itertools, copy, time and functools). To be on the safe side I tried cloning this repo, created and activated a virtual environment using `virtualenv` with the option `--no-site-packages`, which will not include the packages that are installed globally. I ran the programmes without having to install any package and then used `pip freeze --all > requirements.txt` to create a requirements file. You will find it in this here, to activate a virtual environment and check that all packages are installed follow these steps:

0) (Assuming you have Python 3.x and pip3 installed on your machine)
1) Ensure you have an updated version of `virtualenv`. Run `pip install virtualenv` or update with `pip install --upgrade virtualenv`. Test installation/update with `virtualenv --version`, the latest version is `v16.7.2`. 
2) `cd` to a directory where you want to clone the github repo. Run `mkdir gabriele_RC_application` to create a repo where you'll clone the github repository containing my programs. 
3) Run `git clone https://github.com/gsime1/recurse_centre_application.git` to clone the repo containing my programs. 
4) Run `virtualenv -p python3 venv` to create a isolated virtual environment.
5) Run `source source venv/bin/activate` to activate the enviroment. 
6) At this stage you could already run the programs, but to be sure, let's install the requirements.txt file running `pip3 -r requirements.txt`.
7) Test my programs and enjoy game of fifteen! 
  
