'''
~ Creating a database file

Python file that contains the logic that interacts with the data store.
For now the data store is a list, but later on it'll be a database.
'''
entries = []

# Decoupling data from display

# Add an entry to the data store
def add_entry(entry_content, entry_date):
    '''Add/Append new entry into `entries` list of dictionaries.'''
    entries.append({"content": entry_content, "date": entry_date})


# Get entries from the data store
def get_entries():
    '''Get all content from the `entries` list of dictionaries'''
    return entries
