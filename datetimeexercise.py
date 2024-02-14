from datetime import datetime, timedelta, timezone


now = datetime.now()
print(now.date())
print(" time :",now.time())
print(" year : ", now.year)
print(" month:", now.month)
print(" day  :", now.day)
print(" hour :", now.hour)
print(" minutes :", now.minute)
print(" seconds :", now.second)
print(" fold    :", now.fold)

# Create a timezone with daylight saving time
tz_with_dst = timezone(timedelta(hours=-5), name='Eastern Standard Time')

# Create two datetime objects with a DST transition (fallback)
dt1 = datetime(2022, 11, 6, 1, 30, tzinfo=tz_with_dst)
dt2 = datetime(2022, 11, 6, 1, 30, tzinfo=tz_with_dst)

# Set the fold attribute to distinguish between the two occurrences
dt1 = dt1.replace(fold=0)
dt2 = dt2.replace(fold=1)

# Print the datetime objects and their fold attributes
print("Datetime 1:", dt1, "Fold:", dt1.fold)
print("Datetime 2:", dt2, "Fold:", dt2.fold)