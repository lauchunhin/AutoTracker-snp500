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

Please note that the cron daemon must be running for the cron jobs to work. If it's not already running, you can start it with the command `service cron start`. You may need to use `sudo` if you get a permission error, like so: `sudo service cron start`. 

Also, please note that the Python script must have the necessary permissions to be executed. You can add execute permissions to the script with the command `chmod +x /path/to/your/script.py`. Again, replace `/path/to/your/script.py` with the actual path to your script. 

Lastly, please note that the cron job will run in a minimal environment, so it might not have access to the same paths and variables as your regular terminal session. If your script depends on certain environment variables, you might need to define them in the crontab file or in the script itself. If your script depends on certain modules, you might need to provide the full path to the Python interpreter that has access to those modules. 

If you encounter any issues, you can check the cron logs for any error messages. The location of the cron logs depends on your system. On many systems, the cron logs are located at `/var/log/syslog`. You can view the cron-related lines with the command `grep CRON /var/log/syslog`. If the cron logs are not located at `/var/log/syslog` on your system, you might need to check the `/var/log/cron` file or the `/var/log/messages` file, or use the command `journalctl -u cron`. 
