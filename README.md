# PDF_Web_Report_Extraction
A script to retrieve PDF documents on a webpage then parse and store in a database.  

In this activity, we are going to stretch the super powers you have learned thus far. Use your knowledge of
Python and the Linux command line tools to extract information from a scraped file and add it to an SQLite
database.
The Norman, Oklahoma police department regularly reports of incidents arrests and other activity. This data is
hosted on 
their website
. This data is distributed to the public in the forma of PDF files.
The website has three types of 
arrests
, 
incidents
, and 
case summaries
. Your assignment in
this project is to collect 
just the incidents
. To do so, you need to write code to (1) download the data; (2)
extract the id, number, datetime, location and incident ori; (3) create a SQLite database to 
store the data; (4)
insert the data into the database; (5) return the status of the database.
Below we describe the assignment structure and each required function. To complete the project, you may use
any Python3 library available from pypi.
Your code structure should be in a directory with the following format:
normanpd/
    normanpd/
        normanpd.py
        __init__.py
    README
    setup.py
    requirements.txt
    main.py
Create a 
README
 file that will act a a write-up for your project. You should include drections on how to install
and use the code. You should describe all functions and your approach to develop the database. You should
describe any known bugs and cite any sources or people you used for help. 
Besure to include any
assumptions you make for your solution.
CS 5970 | Activity Police Report Extraction
Due date 2/24/17 (14 days)
Project Descriptions
The 
setup.py
 and 
requirement.txt
 files should be used to describe your code package the code
and describe all external packages, respectively. To test the code, we will install your package, essentially
using the 
pip -e install .
 command. Ensure your code is able to be installed and executed on the
GPEL machines.
The 
main.py
 will be used to execute youre code. Create a function called 
main()
 that imports the your
project and sequentially calls each of the function described. Below is a template main function. Feel free to
combine or optimize functions as long as you code preserves the behavior below.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import
 normanpd
from
 normanpd 
import
 normanpd
def
main
(
)
:
# Download data
    normanpd
.
fetchincidents
(
)
# Extract Data
    incidents 
=
 normanpd
.
extractincidents
(
)
# Create Dataase
    normanpd
.
createdb
(
)
# Insert Data
    normanpd
.
populatedb
(
incidents
)
# Print Status
    normanpd
.
status
(
db
)
if
 __name__ 
==
'__main__'
:
    main
(
)
The your code folder should have a package called 
normanpd/
. In side the folder should be an empty
__init__.py
 file and python file called 
normanpd.py
. The latter is where the majority of your code will
reside. Below are the five main functions this code should perform.
The function 
fetchincidents()
 takes no parameters, it uses the python 
urllib.request
 library to grab all
the insident pdfs for the 
norman police report webpage
.
Download Data
Python
