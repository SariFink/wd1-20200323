import datetime
import time

DATETIME_FORMAT = "%d.%m.%Y (%a)"
DATETIME_FORMAT_2 = "%d.%m.%Y %H:%M:%S"

# we now want to incorporate the time of the high score
# into the high score list
# for this we need the datetime library

current_time = datetime.datetime.now()
print(current_time)

# while True:
#     time.sleep(1)
#     print(datetime.datetime.now())

birthdatetime = datetime.datetime(1990, 5, 4, 9, 50, 0)
print(birthdatetime)
print(birthdatetime.isoformat())
print(birthdatetime.strftime(DATETIME_FORMAT))

user_birthdate = "20.12.1993 15:40:10"
new_birthdate = datetime.datetime.strptime(user_birthdate, DATETIME_FORMAT_2)
print(new_birthdate)

age_difference = birthdatetime - new_birthdate
print(age_difference)

person_10000_days_datetime = birthdatetime + datetime.timedelta(days=10000)
print(person_10000_days_datetime)



