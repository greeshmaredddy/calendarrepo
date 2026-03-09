import calendar
from datetime import datetime

def display_calendar():
    """Display calendar for a given year and month"""
    print("=" * 50)
    print("    CALENDAR APPLICATION")
    print("=" * 50)
    
    while True:
        try:
            # Get year and month from user
            year = int(input("\nEnter year (e.g., 2026): "))
            month = int(input("Enter month (1-12): "))
            
            # Validate input
            if month < 1 or month > 12:
                print("❌ Invalid month! Please enter a number between 1 and 12.")
                continue
            
            if year < 1:
                print("❌ Invalid year! Please enter a positive number.")
                continue
            
            # Get calendar details
            month_name = calendar.month_name[month]
            
            print("\n" + "=" * 50)
            print(f"    {month_name.upper()} {year}")
            print("=" * 50)
            
            # Display calendar
            print(calendar.month(year, month))
            
            # Display additional details
            print("-" * 50)
            print("📋 CALENDAR DETAILS:")
            print("-" * 50)
            
            # Get first and last day
            first_day = calendar.monthrange(year, month)[0]
            num_days = calendar.monthrange(year, month)[1]
            last_day = calendar.weekday(year, month, num_days)
            
            day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
            print(f"Month: {month_name}")
            print(f"Year: {year}")
            print(f"Total Days: {num_days}")
            print(f"First Day: {day_names[first_day]}")
            print(f"Last Day: {day_names[last_day]}")
            print(f"Number of Weeks: {len(calendar.monthcalendar(year, month))}")
            
            # Count weekdays
            print("\n📊 WEEKDAY BREAKDOWN:")
            print("-" * 50)
            weekday_count = {day: 0 for day in day_names}
            for date in calendar.monthcalendar(year, month):
                for day_idx, day_num in enumerate(date):
                    if day_num != 0:
                        weekday_count[day_names[day_idx]] += 1
            
            for day, count in weekday_count.items():
                if count > 0:
                    print(f"{day}: {count} days")
            
            # Ask if user wants another calendar
            print("\n" + "=" * 50)
            choice = input("Do you want to view another month? (yes/no): ").lower()
            if choice not in ['yes', 'y']:
                print("Thank you for using Calendar Application! Goodbye!")
                break
        
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    display_calendar()
