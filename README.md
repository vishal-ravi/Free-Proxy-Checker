# Free Proxy Checker

This repository contains a Python script to fetch a list of free proxies from [GeoNode](https://geonode.com/free-proxy-list), check their functionality, and save the working proxies to an Excel file. This script is particularly useful for developers and network administrators who need to verify and use functional proxies for various applications.

## Features

- **Fetch Proxies**: Automatically fetches a list of free proxies from GeoNode.
- **Check Proxies**: Validates each proxy to ensure it is functional.
- **Save Functional Proxies**: Saves the list of working proxies to an Excel file for easy reference and usage.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your system.
- The following Python libraries:
  - `requests`
  - `pandas`
  - `openpyxl`

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:
   ```sh
   git clone https://github.com/vishal-ravi/Free-Proxy-Checker.git
   cd Free-Proxy-Checker
   ```

2. **Install Required Libraries**

   Install the required Python libraries using pip:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script**

   Execute the script using Python:
   ```sh
   python proxy_checker.py
   ```

2. **Script Workflow**

   - The script will fetch the free proxy list from GeoNode.
   - It will check each proxy to determine if it is functional.
   - Functional proxies will be saved to an Excel file named `Functional_Proxy_List.xlsx`.


### requirements.txt

```txt
requests
pandas
openpyxl
```

## How It Works

1. **Fetching Proxy List**: The script sends a request to the GeoNode free proxy list URL and retrieves the proxy data in a tabular format using `pandas.read_html()`.

2. **Checking Proxies**: Each proxy's IP, port, and protocols are extracted. The `check_proxy` function tests the proxy by attempting to send a request to Google. If the request is successful, the proxy is considered functional.

3. **Saving Functional Proxies**: Functional proxies are stored in a list and then saved to an Excel file using `pandas.DataFrame.to_excel()`.

## Contribution

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

