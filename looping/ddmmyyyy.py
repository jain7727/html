current_year=int(input("enter the current year"))
current_month=int(input("enter the current month"))
current_date=int(input("enter the current date"))
my_year=int(input("enter my year"))
my_month=int(input("enter my month"))
my_date=int(input("enter my date"))

if(current_year >= my_year) & (current_month >= my_month) & (current_date >= my_date):
    print(current_year-my_year, current_month-my_month, current_date-my_date)

elif(current_year >= my_year) & (current_month >= my_month) & (current_date <= my_date):
    current_month -= 1
    print(current_year-my_year, current_month-my_month, 30-my_date+current_date)

elif(current_year >= my_year) & (current_month <= my_month) & (current_date >= my_date):
    current_year -= 1
    print(current_year - my_year, 12-my_month+current_month, current_date-my_date)

elif(current_year >= my_year) & (current_month < my_month) & (current_date <= my_date):
    current_year -= 1
    current_month -= 1
    print(current_year - my_year, 12-my_month+current_month, 30-my_date+current_date )

else:
    print("error")
