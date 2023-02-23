# Import the SQLite module
import sqlite3
import random
import time
import csv

from datetime import datetime
from time import sleep # delays between measurements

new_experiment = True
close_experiment = False
species = "NULL"
collection_date = "NULL"
email = "NULL"


def main():
	count = 0
	cont = True
	decision = "NO"
	while decision != "YES":
		decision = input("Do you want to start the experiment? (YES/NO): ")
		if (decision == "YES"):
			if (count == 1):
				delete_table()
			batch_number = input("Enter the batch number: ")
			species = input("Enter the species name: ")
			collection_date = input("Enter the collection date (dd/mm/yy): ")
			email = input("Enter a valid email id: ")
			if (count == 1):
				delete_table()
				count = 0
			create_table()
			count = 1
			while cont:
				insert_values(batch_number,species,collection_date,email)
				print
				time.sleep(2)


def get_temp():
	return round(random.uniform(10.00,50.00),3)
	
def get_humidity():
	return round(random.uniform(0.00,100.00),2)

def get_frequency():
	return round(random.uniform(870.00,1084.00),2)
	
def get_displacement():
	return round(random.uniform(1.00,100.00),2)
	
def create_database():
	conn = sqlite3.connect('OralDemo.db')
	conn.close()	
	
def create_table():
	conn = sqlite3.connect('OralDemo.db')
	curs = conn.cursor()
	start_time = datetime.now()
	
	
	conn.execute(f'''CREATE TABLE Experiment
	 (	"Batch number"	TEXT,
		"Species"	TEXT,
		"Collection Date"	TEXT,
		"Displacement"	REAL,
		"Frequency"	REAL,
		"Temperature (C)"	REAL,
		"Humidity (%)"	REAL,
		"Email id" REAL,
		"Captured Time"	TEXT
		)''')
	
	conn.commit()
	conn.close()
	
def delete_table():
	conn = sqlite3.connect('OralDemo.db')
	curs = conn.cursor()
	curs.execute("DROP TABLE IF EXISTS" + Experiment)
	conn.commit()
	conn.close()

def insert_values(batch_number,species,collection_date,email):
	conn = sqlite3.connect('OralDemo.db')
	curs = conn.cursor()
	current_time = datetime.now()
	curs.execute('''INSERT INTO Experiment VALUES
			(?,?,?,?,?,?,?,?,?)''',(batch_number, species, collection_date, 
			get_displacement(), get_frequency(), get_temp(), 
			get_humidity(),email,current_time))
			
	conn.commit()
	conn.close()

# if user presses cancel on the touchscreen,
# stop inserting data into the table,
# export data via email to the provided email address,
# delete the table 'Experiment'.
# def cancel_experiment():


if __name__ == "__main__":
	main()

