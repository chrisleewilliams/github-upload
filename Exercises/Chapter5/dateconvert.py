# Converts a date in form "mm/dd/yyyy" to "month day, year"
# Author: Chris Williams

def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    monthStr = months[int(monthStr) - 1]

    # output result in month day, year format
    print("the converted date is: {} {}, {}".format(monthStr, dayStr, yearStr))

main()