# ---------------------------------------------------------------------------
# Import Libraries
# ---------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ['Country', 'GDP_USD_millions']
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = '/home/project/Countries_by_GDP.csv'
log_file = "./etl_project_log.txt"

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------
def extract(url, table_attribs):
	''' This function extracts the required
	information from the website and saves it to a dataframe. The
	function returns the dataframe for further processing. '''

	# Loading the entire webpage for Webscraping
	html_page = requests.get(url).text
	# Parse the text in the HTML format using BeautifulSoup
	data = BeautifulSoup(html_page, 'html.parser')
	# Loop to extract data in table (tbody)
	tables = data.find_all('tbody')
	# Select 3rd table
	rows = tables[2].find_all('tr')
	# Create dataframe with table_attribs columns
	df = pd.DataFrame(columns=table_attribs)
	for row in rows:
			col = row.find_all('td')
			if len(col)!=0:
				if col[0].find('a') is not None and '—' not in col[2]:
					data_dict = {table_attribs[0]: col[0].a.contents[0],
								table_attribs[1]: col[2].contents[0]}
					df1 = pd.DataFrame(data_dict, index=[0])
					df = pd.concat([df,df1], ignore_index=True)
	return df

def transform(df):
	''' This function converts the GDP information from Currency
	format to float value, transforms the information of GDP from
	USD (Millions) to USD (Billions) rounding to 2 decimal places.
	The function returns the transformed dataframe.'''
	
	# Remove ","
	df['GDP_USD_millions'] = df['GDP_USD_millions'].astype(str).str.replace(",", "")
	# Change the data type of GDP_USD_millions from object to numeric
	df['GDP_USD_millions'] = pd.to_numeric(df['GDP_USD_millions'], errors="coerce")
	# Change GDP_USD_millions to GDP_USD_billions by dividing ll these values by 1000 and round it to 2 decimal places.
	df['GDP_USD_millions'] = (df['GDP_USD_millions']/1000).round(2)
	# Rename
	df.rename(columns={"GDP_USD_millions":"GDP_USD_billions"}, inplace=True)
	return df

def load_to_csv(df, csv_path):
	''' This function saves the final dataframe as a `CSV` file 
	in the provided path. Function returns nothing.'''
	df.to_csv(csv_path, index=False)

def load_to_db(df, sql_connection, table_name):
	''' This function saves the final dataframe as a database table
	with the provided name. Function returns nothing.'''
	df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
	
def run_query(query_statement, sql_connection):
	''' This function runs the stated query on the database table and
	prints the output on the terminal. Function returns nothing. '''
	df = pd.read_sql(query_statement, sql_connection)
	return df

def log_progress(message):
	''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
	timestamp_format = '%Y-%h-%d-%H:%M:%S'
	now = datetime.now()
	timestamp = now.strftime(timestamp_format)
	with open(log_file, "a") as f:
		f.write(timestamp + ' : ' + message + '\n')

def etl():
	# Log the initialization of the ETL process
	log_progress("ETL Job Started")

	# Log the process of the Extraction process
	log_progress("Extract phase Started")
	
	extracted_df = extract(url, table_attribs)
	
	log_progress("Extract phase Ended")

	# Log the process of the Transformation process
	log_progress("Transform phase Started")
	transformed_df = transform(extracted_df)
	print("Transformed Data")
	print(transformed_df)
	log_progress("Transform phase Ended")

	# Log the process of the Loading process
	log_progress("Load phase Started")
	load_to_csv(transformed_df, csv_path)
	load_to_db(transformed_df, conn, table_name)
	log_progress("Load phase Ended")
	
    # Log the process of the Querying the database table
	query = f"""SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100"""
	result =  run_query(query, conn)
	print(result)

	# Log the completion of the ETL process
	log_progress("ETL Job Ended")

if __name__ == "__main__":
	conn = sqlite3.connect(db_name)
	
	etl()
	
	conn.close()
