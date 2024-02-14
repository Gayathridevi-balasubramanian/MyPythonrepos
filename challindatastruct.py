user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

print(user_preferences)
# remove the none values and display only the not null value : key pairs

def update_userpreferences(usr_pref):
    return {key : value for key , value in usr_pref.items() if value is not None}
    # update_user_preferences = {}
    # for key , value in usr_pref.items():
    #     if value is not None:
    #         update_user_preferences[key] = value
    # return update_user_preferences
        

update_userpreferences = update_userpreferences(user_preferences)
print(update_userpreferences)