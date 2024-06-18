import sqlite3
import pandas as pd
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='data_ingestion.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Connect to the SQLite database
conn = sqlite3.connect('weatherdb.db')

# Folder containing the text files
folder_path = 'wx_data'

# Specify column Names
columns_dict = {
    0: 'date',
    1: 'max_temperature',
    2: 'min_temperature',
    3: 'precipitation'
}

# Start logging
start_time = datetime.now()
logging.info(f"Data ingestion started.")

# Total records ingested
total_records = 0

# Iterate through all text files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)

        # Read data from text file using pandas
        data = pd.read_csv(file_path, delimiter='\t', engine='python', header=None, on_bad_lines='skip')
        # Update the column Names
        data.rename(columns=columns_dict, inplace=True)
        # Add a new column Station Name as File Name
        data['station_name'] = filename.split('.')[0]

        # Write data to SQLite table, avoiding duplicates
        data.to_sql('weather_data', conn, if_exists='replace', index=False, method='multi', chunksize=1000)
        
        # Count the ingested records
        total_records += len(data)

# Commit the transaction and close the connection
conn.commit()
conn.close()

# End logging
end_time = datetime.now()
logging.info(f"Data ingestion completed. Total records ingested: {total_records}. Duration: {end_time - start_time}")

# End logging
end_time = datetime.now()
logging.info(f"Data ingestion completed. Total records ingested: {total_records}. Duration: {end_time - start_time}")
print(f"Data ingestion completed at: {end_time}")
print(f"Total records ingested: {total_records}")
print(f"Duration: {end_time - start_time}")

print("Data loaded successfully from all text files.")
