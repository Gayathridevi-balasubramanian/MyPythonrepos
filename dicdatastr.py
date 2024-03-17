# dictionary : Key- Value pairs
states_capital = {
    "TN" : "Chennai" ,
    "AP" : "Talegana"
}

# accessing the dictionary

print(states_capital["TN"])

for keys in states_capital.keys():
    print(keys)

for keys in states_capital.values():
    print(keys)

for key, value in states_capital.items():
    print(keys,":",value)

print(states_capital)

user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}
print(user_preferences)
user_preferences["language"] = "Spanish"
user_preferences["enable_location"] = "True"

# adding the values
user_preferences["high-lightcolor"] = "yellow"

#deleting the values 
del user_preferences["currency"]

#deleting the values along with retrieving the value
dt = user_preferences.pop("date_format", "N/A")
print ("popeed date format", dt)
print(user_preferences)