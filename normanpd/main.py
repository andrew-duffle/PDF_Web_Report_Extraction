#!/usr/bin/env python
#-*- coding: utf-8 -*-

import normanpd
from normanpd import normanpd

def main():
    ##### Createing the database to insert data into 
    normanpd.createdb()

    normanpd.fetchincidents()
    #### I opted to combide the returning data and putting in the databse to one.
    #### the code was so short that breakign it into seperate sections and calling each function
    #### was almost more code than the actual program
    normanpd.extractincidents()
    #### this will return 5 random lines form the database and I also included a table drop to reset
    #### for subsequent runs.
    normanpd.status()
    
if __name__=='__main__':
    main()