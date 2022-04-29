def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

angelProfile = build_profile('angel', 'marquez', enneagram_type=4, nationality='mexican', work_field='software engineer')
print(angelProfile)