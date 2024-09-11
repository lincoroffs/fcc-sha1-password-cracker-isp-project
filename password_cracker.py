import hashlib

def crack_sha1_hash(hash, use_salts = False):
    # Read the list of top 10,000 passwords
    with open('top-10000-passwords.txt', 'r') as file:
        passwords = file.read().splitlines()
        
    if use_salts:
        # Read the list of salts if use_salts is true
        with open('known-salts.txt', 'r') as file:
            salts = file.read().splitlines()
        
        # Try all combinations of passwords with salts prepended and appended
        for password in passwords:
            for salt in salts:
                # Hash with salt prepended
                salted_hash = hashlib.sha1((salt + password).encode()).hexdigest()
                if salted_hash == hash:
                    return password
                
                # Hash with salt appended
                salted_hash = hashlib.sha1((password + salt).encode()).hexdigest()
                if salted_hash == hash:
                    return password
    else:
        # Just hash and compare each password
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password
            
    return "PASSWORD NOT IN DATABASE"