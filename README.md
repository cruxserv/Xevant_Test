Xevant Python Code Practice
Purpose
The purpose of this exercise is to test your Python experience with parsing and creating files. Our data platform is responsible for ingesting over a thousand of files each month in order to power our products.
Prerequisites
1. You should already have Docker installed on your computer from which you will be programming
2. Extract the provided zip file – xevant_python_code_practice.zip
3. Write your code in the main function of the file_parser.py file.
4. Review the file_config.py file for useful values
5. See helper commands for docker at the bottom of the document. Note the “-v”
command to map the volume for the file export.
Code Instructions
1) Extract the .zip file called “/files_inbound/example_client_files.zip”
2) Create a new CSV file from the .xlsx file using the second sheet called PolicyData
a) The new file should be named “insurance_data_sample_1667864342_parsed.csv” and written to the “/files_outbound” directory.
b) Add three additional columns with values to the new CSV file.
• ROW_NUMBER - row number value for each row. (1,2,3,4, etc.)
• FILE_NAME – the original file name “insurance_data_sample_1667864342.xlsx”
• FILE_DATE – parse the timestamp from the file name to generate a date time string
value in the following format “2022-11-07 00:00:00”
b) Encapsulate non numerical fields in double quotes
3) Create a new CSV file from the .csv file
a) The new file should be named “work_orders_sample_1667864342_parsed.csv” and written to the “/files_outbound” directory.
b) Add 3 additional columns with values to the new CSV file.
• ROW_NUMBER - row number value for each row. (1,2,3,4, etc.)
• FILE_NAME – the original file name “work_orders_sample_1667864342.csv”
• FILE_DATE – parse the timestamp from the file name to generate a date time string
value in the following format “2022-11-07 00:00:00”
c) Encapsulate non numerical fields in double quotes
4) Repeat step 3 for the file “employee_data_sample_1667864342csv” a) Name the new file after adding columns
“employee_data_sample_1667864342_parsed.csv”
5) Zip up your entire project directory, including the new CSV files, and email it to
