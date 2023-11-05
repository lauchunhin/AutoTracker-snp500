# S&P 500 Auto Constituent Tracker 

This Python program is designed to update the list of S&P 500 constituents. It works by scraping the S&P 500 constituents from the SlickCharts website and comparing it with the previously stored list. If there are any changes, or if the current date is the third Friday of March, June, September, or December (when the S&P 500 constituents are rebalanced), the program will write the new list to a file.

## Functionality Overview

1. **third_friday(year, month)**: This function calculates the date of the third Friday of a given month.
2. **write_to_file(filename, data)**: This function writes a list of data to a file, with each item on a new line.
3. **Logging Setup**: The program sets up logging to a file named 'logfile.log'.
4. **Browser Setup**: The program sets up a headless Chrome browser using Selenium WebDriver.
5. **Web Scraping**: The program navigates to the SlickCharts website and scrapes the symbols of the S&P 500 constituents.
6. **Symbol Sorting**: The symbols are stored in a list, which is then sorted alphabetically.
7. **Date Checking**: The program checks if the current date is the third Friday of March, June, September, or December.
8. **File Comparison**: The program compares the new list of symbols with the most recent file. If there are changes, or if today is a rebalance date, the new list is written to a file. The changes are also logged.

## Cron Job Setup

To run this program every day at midnight, you can use a cron job. Here are the instructions to set it up:

1. Open the terminal.
2. Type `crontab -e` to edit the crontab file.
3. Add the following line to the file:
   ```
   0 0 * * * /usr/bin/python3 /path/to/your/script.py
   ```
   Replace `/path/to/your/script.py` with the actual path to your Python script.
4. Save and close the file.

This cron job will run the Python script every day at midnight. The `0 0 * * *` syntax represents minutes (0), hours (0), day of the month (*), month (*), and day of the week (*), respectively. The asterisks (*) mean "every". So `0 0 * * *` means "at 0 minutes past 0 hours, every day of the month, every month, and every day of the week", which is equivalent to "every day at midnight". The `/usr/bin/python3` is the path to the Python interpreter. Make sure to replace it with the path to the Python interpreter on your system if it's located elsewhere. The `/path/to/your/script.py` is the path to the Python script that you want to run. Replace it with the actual path to your script. 

## Tracker Log Demonstration
The log file provides a daily record of changes in the S&P 500 constituent list. Each entry in the log file contains the following information:

Timestamp: The date and time when the comparison was made, formatted as MM/DD/YYYY HH:MM:SS AM/PM.
Quarter Update: A boolean value indicating whether the update is a quarterly update. False signifies a non-quarterly update.
List Compared: The filename of the S&P 500 constituent list used for comparison.
Changes to the Constituent List: A boolean value indicating whether there were any changes in the constituent list. Yes signifies that changes were detected.
Added: A set of ticker symbols representing companies added to the S&P 500.
Removed: A set of ticker symbols representing companies removed from the S&P 500.
For example, an entry might look like this:
![log_demonstration](https://github.com/lauchunhin/AutoTracker-snp500/blob/main/cron_log.png)


This log file serves as a concise and clear record of the daily changes in the S&P 500 constituent list, providing valuable insights into the dynamics of the index over time. It is an essential tool for financial programmers and analysts tracking the S&P 500.
