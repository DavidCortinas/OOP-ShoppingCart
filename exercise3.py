def addressbook():
    addressbook = []
    done = False
    while not done:
        name = input('What is your name?')
        address =  input('What is your address?')
        addressbook = {
            'name': name,
            'address': address,
        }

    
addressbook()