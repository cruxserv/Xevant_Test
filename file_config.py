CONFIG = {
	"inbound_dir" : "/files_inbound",
	"outbound_dir" : "/files_outbound",
	"zip_file_name": "example_client_files.zip",
    "csv_files": [
    	{
    		"prefix": "work_orders_sample_",
    		"encoding": "utf-8"
    	},
    	{
    		"prefix": "employee_data_sample_",
    		"encoding": "latin1"
    	}
    ],
    "excel_files": [
    	{
    		"prefix": "insurance_data_sample_",
    		"sheet_name": "PolicyData"
    	}
    ]
}