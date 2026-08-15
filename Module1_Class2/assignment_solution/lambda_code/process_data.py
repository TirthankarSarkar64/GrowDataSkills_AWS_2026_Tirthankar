import pandas as pd
from exception_handling_utility import try_except_decorator

@try_except_decorator
def read_csv_data_file(file_path):
    data = pd.read_csv(file_path)
    return data

@try_except_decorator
def process_csv_file(df):
    """revenue = quantity * price, there is no column for revenue, so we need to create one"""
    """find revenue per city"""

    df["revenue"] = df["quantity"] * df["price"]
    revenue_per_city = df.groupby("city")["revenue"].sum().reset_index()
    return revenue_per_city

"""How to create layer by packaging this folder?"""
"""First, create a folder named 'python' and place the 'exception_handling_utility.py' file inside it. Then, zip the 'python' folder to create a layer package. Finally, upload the zip file to AWS Lambda as a layer."""
"""For providing pandas library with this package itself using pip install, below is detailed instruction:
1. Create a folder named 'python' and navigate into it.
2. Run the command: pip install pandas -t .
3. After the installation is complete, go back one folder andzip the 'python' folder to create a layer package.
4. Also, include the 'exception_handling_utility.py' and 'process_data.py' files in the 'python' folder before zipping.
4. Upload the zip file to AWS Lambda as a layer."""

r"""How to zip the file on windows and linux using CLI?
1. On Windows, open Command Prompt and navigate to the directory containing the 'python' folder. Run the command:
   powershell Compress-Archive .\* -DestinationPath .\<layer_name>.zip
2. On Linux, open Terminal and navigate to the directory containing the 'python' folder. Run the command:
   zip -r layer.zip python
3. After creating the zip file, you can upload it to AWS Lambda as a layer."""