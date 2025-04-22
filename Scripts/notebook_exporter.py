import requests
from bs4 import BeautifulSoup
import csv

def download_table_from_url(url, output_csv="table_data.csv"):
    """
    Fetches the first HTML table from the given URL and saves its data to a CSV file.

    :param url: The webpage URL containing the table.
    :param output_csv: Name of the CSV file to save the extracted table data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        print(f"No table found at {url}.")
        return

    rows = table.find_all('tr')
    table_data = []
    for row in rows:
        cells = row.find_all(['th','td'])
        table_data.append([cell.get_text(strip=True) for cell in cells])

    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(table_data)

    print(f"Table saved to {output_csv}")

download_table_from_url(url='https://www.quantconnect.com/project/21565345')
# ------------------- UNIT TEST -------------------
# import unittest
# from unittest.mock import patch, MagicMock
# 
# class TestDownloadTableFromUrl(unittest.TestCase):
#     @patch("requests.get")
#     def test_download_table_from_url(self, mock_get):
#         mock_response = MagicMock()
#         mock_response.text = '''
#         <html><body>
#         <table><tr><th>Header1</th><th>Header2</th></tr>
#                <tr><td>Row1Col1</td><td>Row1Col2</td></tr>
#                <tr><td>Row2Col1</td><td>Row2Col2</td></tr>
#         </table>
#         </body></html>
#         '''
#         mock_get.return_value = mock_response
# 
#         # No exception should be thrown, and CSV is created
#         download_table_from_url("http://fakeurl.com", output_csv="test_table.csv")
# 
#         # Check that requests.get was called
#         mock_get.assert_called_once()
# 
# if __name__ == "__main__":
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)
