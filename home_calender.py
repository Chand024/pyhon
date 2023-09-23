# Program to display calendars for all months of a given year in one row with three months in each row

# Importing calendar module
import calendar

# Input year from the user
yy = int(input("Enter year: "))

# Define the months in each row
months_per_row = 3

# Create a list of month names
month_names = list(calendar.month_name[1:])  # Exclude the empty first element

# Iterate through the months and print them in the desired order
for start_month in range(0, 12, months_per_row):
    end_month = min(start_month + months_per_row, 12)
    row_months = month_names[start_month:end_month]

    # Print the month names for the current row
    for month in row_months:
        print(f"{month} {yy}".center(30), end="")

    print()  # Move to the next line for the calendars

    # Print the calendars for the current row
    for month in row_months:
        month_index = month_names.index(month) + 1
        cal = calendar.month(yy, month_index)
        print(cal, end="")

print()  # Separate rows with a blank line
