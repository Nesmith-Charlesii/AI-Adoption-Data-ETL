# AI_Adoption_Data_ETL

## Overview

The AI Adoption ETL is a data pipeline that utilizes a dataset of nearly 150,000 records, all pertaining to the implementation of AI tools across various countries and industries. This ETL uses a collection of csv records as input, and then outputs AI Adoption Data into a ZIP folder as csv files, categorized by industry. These csv files can then be used in spreadsheets such as Excel, Numbers, and Google Sheets. Currently, this pipeline extracts and outputs 8 industry groups:

1. Agriculture
2. Education
3. Finance
4. Healthcare
5. Manufacturing
6. Retail
7. Technology
8. Transportation

## How to run the ETL pipeline

### Creating an environment

After cloning this repo, navigate to the root of the folder and run:

`python3 -m venv venv`

This creates a virtual environment, where you will install dependencies and run the script.

### Installing dependencies

After a venv is created, activate your virtual environment.

`source venv/bin/activate`

Install the required dependencies using:

`pip install -r requirements.txt`


### Running the ETL

Once you've created and activated a virtual environment, from the root folder, simply run:

`python3 ai_adoption_etl.py`