# sometimes you'll want to accept an arbitrary number of arguments,
# but you won't know ahead of time what kind of information will be
# passed to the function

# the double asterisks (**) before the parameter **user_info cause
# Python to create an empty dictionary called user_info and pack
# whatever name-value pairs it recieves into this dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(user_profile)