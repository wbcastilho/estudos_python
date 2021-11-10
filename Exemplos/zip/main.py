"""
    zip
    >>> first_name = ['Joe','Earnst','Thomas','Martin']
    >>> last_name = ['Schmoe','Ehlmann','Fischer','Walter']
    >>> age = [23, 65, 11, 36]
    >>> print(list(zip(first_name,last_name, age)))
    [('Joe', 'Schmoe', 23), ('Earnst', 'Ehlmann', 65), ('Thomas', 'Fischer', 11), ('Martin', 'Walter', 36)]

    unzip
    >>> full_name_list = [('Joe', 'Schmoe', 23), ('Earnst', 'Ehlmann', 65), ('Thomas', 'Fischer', 11)]
    >>> first_name, last_name, age = list(zip(*full_name_list))
    >>> print(f"first name: {first_name} last name: {last_name} age: {age}")
    first name: ('Joe', 'Earnst', 'Thomas') last name: ('Schmoe', 'Ehlmann', 'Fischer') age: (23, 65, 11)
"""