import os
from dotenv import load_dotenv
import calendar
from datetime import datetime, timedelta

load_dotenv()

def env(key):
    return os.getenv(key)

def generate_full_weeks_array(year=None, month=None):
    year = datetime.now().year if year==None else year
    month = datetime.now().month if month==None else month

    # Find the first day of the month
    first_day = datetime(year, month, 1)

    # Find the weekday index of the first day (0 = Monday, 6 = Sunday)
    start_weekday = first_day.weekday()

    # Calculate the number of days in the previous month to include
    days_from_previous_month = start_weekday

    # Calculate the number of days in the current month
    _, last_day_of_month = calendar.monthrange(year, month)
    days_in_current_month = last_day_of_month

    # Calculate the number of days in the next month to include
    days_from_next_month = (7 - ((days_from_previous_month + days_in_current_month) % 7)) % 7

    # Calculate the start and end dates for the array
    start_date = first_day - timedelta(days=days_from_previous_month)
    end_date = first_day + timedelta(days=days_in_current_month + days_from_next_month)

    # Get the current date for comparison
    today = datetime.now().date()

    # Generate the array of dates and tags
    date_array = []
    for i in range((end_date - start_date).days):
        current_date = start_date + timedelta(days=i)
        date_str = current_date.strftime('%d')
        date_id = current_date.strftime('%Y-%m-%d')
        tag = "today" if current_date.date() == today else "otherMonth" if current_date.month != month else ""
        date_array.append({"date": date_str, "tag": tag, "id": date_id})

    return date_array
