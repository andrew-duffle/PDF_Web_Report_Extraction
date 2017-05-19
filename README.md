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

-----------------------The Code------------------
Requirements for the the program.

	Sqllite3
	PyPDF2
	re 
	urllib

General:

The purpose of this program is to return and archive incidents reports from the normanpd 	website. These incident reports are stored in PDF format and can be found at http://	normanpd.normanok.gov/content/daily-activity. One file per day is posted to the 	website.The link to the document is stored in the href of each document link. These 		documents can be identified by the string of 20Daily%20Incident%20Summary.pdf. There are 	~6 files posted at any time for the most recent days. Each document will contain a 		varying number of pages and lines.

Code:

normanpd.py

fetchincidents function:

First we are able to find navigate and read the normanpd website using urllib. I 		selected to store this content in a variable called HTML for easier processing in the 		program. After returning the source code we are interested in finding only the links 		that point to the PDF incident reports. To do so I invoke a regex match based on links 		matching the following string. 	
/filebrowser_download/657/\d\d\d\d-\d\d-\d\d%20Daily%20Incident%20Summary.pdf
These links then become the incident PDF file locations we are interested in and used 		for the other functions.

Extractincidents and populatedb function:

As noted in the assignment doc to feel free to combine functions I found it much more simple to combine the extraction and population into one function. In doing so as I process one document 	I am able to insert the data into the database. In theory this would reduce the likely hold of 	connection failures. In this function we process each href (document) found in the extraction 	function. After we extract a document line by line we find the length of the document and drop 	the first 5 and last 1 values in the dictionary. These dropped lines account for the headers of the document and a final date value that is included at the end of every document. From here we process the dictionary as follows. The rolling first and sixth value in the list should be a 	datetime stamp of the incident. I used a regex match to iterate through the document looking for the first and sixth position to match the requirements. At the point we find a valid line we insert 	the line into the database and iterate to the beginning of the following line. If we do not find a correct format we will iterate one position at a time until we find a series that matches the required format.  This make an assumption that we only care about lines that are 5 columns wide and  start with a datetime field. In other words if there is an address that wraps and the PDF reader reads it as two columns we through it out. The other scenario I found with this is if we are missing values we will through out the line and go to the next valid line to insert. 
	
createdb function:

there is not much to this function we are simply creating a table called incidents. The incidents table has six columns ID, number, date_time, location, nature, ORI. This table is populated with 	the data from the normanpd incident reports.

Status function:

Very simple function that queries against the incidents table. First it will return the max id 	number in the table. This is also the total number of lines by default.  Then it will return a 	random sample of 5 lines in the database. I also include a drop table for the incidents table so you can run the code multiple time without error. Then we close the connection to the database.
	
main.py

This file is the python code used to import the code and iterate through the functions. You will see that the extract and populate functions are combine as noted above.

Run the code:

There is no special requirements to run code. As long as you have the required packages noted 	at the top. If you wanted to direct to another website or files a few minor modifications would need to be made. The modifications would relate to the fetchincidents function and then how we 	parse in the extract function.  






