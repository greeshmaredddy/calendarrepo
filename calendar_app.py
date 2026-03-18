import calendar
from datetime import datetime, timedelta
import os

class CalendarApp:
    """Enhanced Calendar Application with additional features"""
    
    # US Federal Holidays (add more for other countries)
    HOLIDAYS = {
        (1, 1): "New Year's Day",
        (7, 4): "Independence Day",
        (12, 25): "Christmas Day",
        (12, 31): "New Year's Eve",
    } 


    def __init__(self):
        self.today = datetime.now()
        self.current_year = self.today.year
        self.current_month = self.today.month
    
    def get_holidays_for_month(self, year, month):
        """Get holidays for a specific month"""
        holidays = {}
        for (h_month, h_day), h_name in self.HOLIDAYS.items():
            if h_month == month:
                holidays[h_day] = h_name
        return holidays
    
    def display_calendar(self):
        """Display calendar for a given year and month"""
        print("=" * 60)
        print("         📅 CALENDAR APPLICATION 📅")
        print("=" * 60)
        
        while True:
            try:
                print("\n" + "─" * 60)
                print("Options:")
                print("  1. View specific month     2. View current month")
                print("  3. View next month         4. View previous month")
                print("  5. Export calendar         6. Exit")
                print("─" * 60)
                
                choice = input("Select option (1-6): ").strip()
                
                if choice == "6":
                    print("\n✨ Thank you for using Calendar Application! Goodbye!")
                    break
                
                if choice == "2":
                    year = self.current_year
                    month = self.current_month
                elif choice == "3":
                    year = self.current_year
                    month = self.current_month + 1
                    if month > 12:
                        month = 1
                        year += 1
                elif choice == "4":
                    year = self.current_year
                    month = self.current_month - 1
                    if month < 1:
                        month = 12
                        year -= 1
                elif choice == "5":
                    self.export_calendar_to_file()
                    continue
                elif choice == "1":
                    year = int(input("Enter year (e.g., 2026): "))
                    month = int(input("Enter month (1-12): "))
                else:
                    print("❌ Invalid option! Please select 1-6.")
                    continue
                
                # Validate input
                if month < 1 or month > 12:
                    print("❌ Invalid month! Please enter a number between 1 and 12.")
                    continue
                
                if year < 1:
                    print("❌ Invalid year! Please enter a positive number.")
                    continue
                
                self.display_month_details(year, month)

            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")
            except Exception as e:
                print(f"❌ An error occurred: {e}")
    
    def display_month_details(self, year, month):
        """Display detailed information for a month"""
        month_name = calendar.month_name[month]
        
        print("\n" + "=" * 60)
        print(f"              {month_name.upper()} {year}")
        print("=" * 60)
        
        # Display calendar
        print(calendar.month(year, month))
        
        # Get first and last day
        first_day = calendar.monthrange(year, month)[0]
        num_days = calendar.monthrange(year, month)[1]
        last_day = calendar.weekday(year, month, num_days)
        
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Display detailed information
        print("─" * 60)
        print("📋 CALENDAR DETAILS:")
        print("─" * 60)
        print(f"Month: {month_name}")
        print(f"Year: {year}")
        print(f"Total Days: {num_days}")
        print(f"First Day: {day_names[first_day]}")
        print(f"Last Day: {day_names[last_day]}")
        print(f"Number of Weeks: {len(calendar.monthcalendar(year, month))}")
        
        # Check for leap year
        is_leap = calendar.isleap(year)
        print(f"Leap Year: {'✅ Yes' if is_leap else '❌ No'}")
        
        # Count weekdays
        print("\n📊 WEEKDAY BREAKDOWN:")
        print("─" * 60)
        weekday_count = {day: 0 for day in day_names}
        for date in calendar.monthcalendar(year, month):
            for day_idx, day_num in enumerate(date):
                if day_num != 0:
                    weekday_count[day_names[day_idx]] += 1
        
        for day, count in weekday_count.items():
            if count > 0:
                print(f"  {day:12}: {count} days")
        
        # Show holidays
        holidays = self.get_holidays_for_month(year, month)
        if holidays:
            print("\n🎉 HOLIDAYS:")
            print("─" * 60)
            for day, holiday_name in sorted(holidays.items()):
                print(f"  {holiday_name} - {month_name} {day}, {year}")
        
        # Highlight today's date if in this month
        if year == self.today.year and month == self.today.month:
            print(f"\n📍 Today: {month_name} {self.today.day}, {year}")
    
    def export_calendar_to_file(self):
        """Export calendar to a text file"""
        try:
            year = int(input("Enter year to export (e.g., 2026): "))
            month = int(input("Enter month to export (1-12): "))
            
            if month < 1 or month > 12:
                print("❌ Invalid month!")
                return
            
            month_name = calendar.month_name[month]
            filename = f"calendar_{month_name}_{year}.txt"
            
            with open(filename, 'w') as f:
                f.write(f"Calendar: {month_name} {year}\n")
                f.write("=" * 60 + "\n\n")
                f.write(calendar.month(year, month))
                f.write("\n" + "=" * 60 + "\n")
                
                first_day = calendar.monthrange(year, month)[0]
                num_days = calendar.monthrange(year, month)[1]
                last_day = calendar.weekday(year, month, num_days)
                day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                
                f.write("\nCalendar Details:\n")
                f.write(f"Month: {month_name}\n")
                f.write(f"Year: {year}\n")
                f.write(f"Total Days: {num_days}\n")
                f.write(f"First Day: {day_names[first_day]}\n")
                f.write(f"Last Day: {day_names[last_day]}\n")
                f.write(f"Leap Year: {calendar.isleap(year)}\n")
            
            print(f"✅ Calendar exported to '{filename}'")
        
        except ValueError:
            print("❌ Invalid input!")
        except Exception as e:
            print(f"❌ Error exporting calendar: {e}")

if __name__ == "__main__":
    app = CalendarApp()
    app.display_calendar()
