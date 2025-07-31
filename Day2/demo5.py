#!/usr/bin/env python3

# Define the Filter Function
# From a list of email Ids filter out all the invalid emails
import re
list_of_emails = ['vishwas@cloudthat.com','123@123,','vihs','vishwas@gmail', 'vishwas@gmail.com']

def is_valid_email(email):
    pattern = r'^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]'
    valid = re.match(pattern,email)
    return valid

filtered_emails = filter(is_valid_email, list_of_emails)
print(f"Valid Emails are: ")
for item in filtered_emails:
    print(item)