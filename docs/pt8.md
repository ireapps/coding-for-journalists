#### Cleaning data

No data are ever perfect, but that doesn't mean you're not going to have to tangle with its shortcomings on deadline. Once we assess the issues, we can outsource the tedium of cleaning to a Python script. If we ever receive an updated data set from the same source, we have an automated way to run through out and output something we can use for reporting.

This exercise hits three different kinds of cleaning that are fairly common:

- Data that don't arrive in flat file format, where one row equals one record. We'll work through a very formatted Excel file of candidate filings and convert it to a worksheet we can use.

- Data that are just plain dirty: leading and trailing spaces, misspellings, unnecessary characters and more.

- Parsing out names. We'll scrape some board and commission pages from the city of Chicago's website and use some hints in table to help us split names into title, first, middle, last and suffix.

The files:

- **excel.py**: The script we'll write to turn formatted Excel designed for printing into a flat file we can use for analysis and reporting.

- **fun_with_excel.py**: A tour of the ```openpyxl``` library and how it can read and write Microsoft Excel formats from 2007 and later.

- **clean_csv.py**: We'll write Python in this to process a dirty CSV file.

- **names.py**: The script that will scrape board and commission pages and process the names.

- **Candidates.xlsx**: Our formatted Excel file of campaign filings.

- **Candidates_backup.xlsx**: A backup of the formatted Excel file (in case we mess it up). 

- **rahm_spending.csv**: The problematic CSV file with dirty columns. 

In case of no internet, **boards_backup** contains the files to scrape for **names.py**. Finished versions are in **completed**.