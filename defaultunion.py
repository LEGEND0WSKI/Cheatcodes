profile = {
    'name': 'N/A',
    'email': 'N/A',
    'phone': 'N/A',
    'address': 'N/A',
    'city': 'N/A',
    'state': 'N/A',
    'zip': 'N/A',
    'country': 'N/A'
}

user_1 = {
    **profile,  # merge profile with user_1 dictionary
    'name': 'John Doe',
    'phone': '555-555-5555'
}

profile |= user_1
print(profile)