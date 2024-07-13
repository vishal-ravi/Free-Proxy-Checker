import requests
import pandas as pd
from openpyxl import Workbook

# Function to check if a proxy is functional
def check_proxy(ip, port, protocol):
    proxy = {protocol: f"{protocol}://{ip}:{port}"}
    try:
        response = requests.get("http://www.google.com", proxies=proxy, timeout=5)
        if response.status_code == 200:
            return True
    except:
        return False

# Load the CSV file
file_path = '/Free_Proxy_List (1).csv'
proxy_list = pd.read_csv(file_path)

# List to store functional proxies
functional_proxies = []

# Check each proxy and print the IP being checked
for index, row in proxy_list.iterrows():
    ip = row['ip']
    port = row['port']
    protocols = row['protocols']
    print(f"Checking IP: {ip}:{port}")
    if check_proxy(ip, port, protocols):
        functional_proxies.append(row)

# Save functional proxies to an Excel file
functional_proxies_df = pd.DataFrame(functional_proxies)
output_file_path = 'Functional_Proxy_List.xlsx'
functional_proxies_df.to_excel(output_file_path, index=False)

print(f"Functional proxies saved to {output_file_path}")
