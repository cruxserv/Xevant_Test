import re
import os
import sys

# Use these libraries to parse and create files
import csv
import openpyxl
import pandas as pd

from os import listdir
from os.path import isfile, join
from zipfile import ZipFile
from datetime import datetime

# File configuration object
from file_config import CONFIG as CONF


def extract_files(zip_file_directory, zip_file_name):
    """
    Purpose:
        Extract a zipped file and return the list of files extracted
    Parameters:
        zip_file_directory (string): directory that contains the zip file
        zip_file_name (string): name of the zip file
    """
    path = zip_file_directory + "/" + zip_file_name
    with ZipFile(path, "r") as unzip:
        unzip.extractall(zip_file_directory)

    file_list = [
        f
        for f in listdir(zip_file_directory)
        if isfile(join(zip_file_directory, f)) and f != path
    ]

    return file_list


def file_timestamp_to_datetime(file_name):
    """
    Purpose:
        Extract the Epoch Unix timestamp from file name and
        convert to date time string
    Parameters:
        file_name (string): name of the file containing a timestamp
    """
    ts = re.search("[0-9]{10}", file_name).group(0)
    date_string = datetime.fromtimestamp(int(ts)).strftime("%Y-%d-%m %H:%M:%S")

    return date_string


def main():
    """
    Refer to the PDF file for instructions.
    Add your code below. You can add any additional functions.
    """
    print("Running main")

    # Extract files from the zip
    file_list = extract_files(CONF["inbound_dir"], CONF["zip_file_name"])

    # Iterate through list of files
    for file_name in file_list:
        file_path = os.path.join(CONF["inbound_dir"], file_name)

        # Create a flag for if a df has been read or not
        read_df = None

        # Check if the file is an Excel file as per the configuration file
        for excel_file_config in CONF["excel_files"]:
            # Make sure the file matches acceptable prefixes
            if file_name.startswith(excel_file_config["prefix"]):
                # Add to DataFrame, using conf values
                read_df = pd.read_excel(
                    file_path, sheet_name=excel_file_config["sheet_name"]
                )
                break  # Break if matched and read

        # If not an Excel file, check if it's a CSV file as per the configuration file
        if read_df is None:
            for csv_file_config in CONF["csv_files"]:
                # Make sure the file matches acceptable prefixes
                if file_name.startswith(csv_file_config["prefix"]):
                    # Add to DataFrame, using encoder info
                    read_df = pd.read_csv(
                        file_path, encoding=csv_file_config["encoding"]
                    )
                    break  # Break if matched and read

        # If the file has been read, add additional columns and save to CSV
        if read_df is not None:

            # Add Columns
            read_df["ROW_NUMBER"] = range(1, len(read_df) + 1)
            read_df["FILE_NAME"] = file_name
            read_df["FILE_DATE"] = file_timestamp_to_datetime(file_name)

            # Adjust output file name to include parsed
            base_file_name = file_name.split(".")[0]
            output_file_name = f"{base_file_name}_parsed.csv"

            # Encapsulate non numerical fields in double quotes
            quoting = csv.QUOTE_NONNUMERIC

            # Save to CSV file,
            output_file_path = os.path.join(CONF["outbound_dir"], output_file_name)
            read_df.to_csv(output_file_path, index=False, quoting=quoting)


if __name__ == "__main__":
    sys.exit(main())