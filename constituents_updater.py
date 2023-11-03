from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime
import logging
import sys
import glob
import calendar
#* Will run automatically through cron at 00:01 

#* The S&P500 constituents are rebalanced on a quarterly basis on the 3rd Friday of March, June, September, December
def third_friday(year, month):
    # Get the matrix representing a month’s calendar
    cal = calendar.monthcalendar(year, month)
    # The third Friday must be in the third or fourth week of the month
    if cal[2][calendar.FRIDAY] != 0:
        return cal[2][calendar.FRIDAY]
    else:
        return cal[3][calendar.FRIDAY]

# write a txt file for the updated constituent list
def write_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(item + '\n')

# Set up logging
logging.basicConfig(
    filename='logfile.log', 
    level=logging.INFO,
    format='%(asctime)s %(message)s',  # Include timestamp in log messages
    datefmt='%m/%d/%Y %I:%M:%S %p'  # Format for the timestamp
)

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service('/Users/lauchunhin/miniforge3/chromedriver-mac-arm64/chromedriver')

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    driver.get('https://www.slickcharts.com/sp500')  # navigate to the S&P 500 

    # get all elements in the second column (Symbol)
    symbols = driver.find_elements(By.XPATH, "//table[contains(@class,'table table-hover')]/tbody[1]/tr/td[3]/a[1]") 

except Exception as e:
    logging.info(f"An error occurred: {e}")
    driver.quit()  # close the browser when done
    sys.exit()  # stop the script

# Create a list to store the symbols
symbol_list = [symbol.text.replace('.', '-') for symbol in symbols]

# Sort the list alphabetically
symbol_list.sort()

# Get the current date
now = datetime.datetime.now()

# Check if today is the third Friday of March, June, September, or December
if now.day == third_friday(now.year, now.month) and now.month in [3, 6, 9, 12]:
    quarter_update = True
else:
    quarter_update = False

# Format the date as a string
timestamp = now.strftime("%Y%m%d")

driver.quit()  # close the browser when done

# Get a list of all files that match the pattern
files = glob.glob('snp_constituent_list_*.txt')

# Sort the list of files so the most recent is first
files.sort(reverse=True)

# Check if there are at least one file (the one just created)
if len(files) >= 1:
    # Open the most recent file
    with open(files[0], 'r') as f_old:
        # Read the entire contents of the file into a list
        contents_old = f_old.read().splitlines()

    # Compare the contents of the new symbols with the most recent file
    if symbol_list == contents_old and not quarter_update:
        # If no changes and today is not a rebalance date
        log_message = f"\nQuarter update: {quarter_update}\nList compared: {files[0]}\nChanges to the constituent list: No"
    else:
        # If there are changes or today is a rebalance date, save the new symbols to a new file
        write_to_file(f'snp_constituent_list_{timestamp}.txt', symbol_list)
        added_symbols = set(symbol_list) - set(contents_old)
        removed_symbols = set(contents_old) - set(symbol_list)
        log_message = f"\nQuarter update: {quarter_update}\nList compared: {files[0]}\nChanges to the constituent list: Yes\nAdded: {added_symbols}\nRemoved: {removed_symbols}"
else:
    logging.info("This is the first file.")
    # If this is the first file, save the symbols
    write_to_file(f'snp_constituent_list_{timestamp}.txt', symbol_list)
    log_message = f"\nQuarter update: {quarter_update}\nList compared: {files[0]}\nChanges to the constituent list: First file"

# logging.info log message to terminal
logging.info(log_message)

# Write log message to log file
#with open('log.txt', 'a') as f_log:
#    f_log.write(log_message + '\n')
#* 1min 29 seconds