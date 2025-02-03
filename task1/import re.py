import re

def process_file(filename):
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(',')
            name = parts[0].strip()
            email = parts[1].strip() if len(parts) > 1 else ''
            user_id = parts[2].strip() if len(parts) > 2 else ''
            
            if not user_id.isdigit():
                print(f"Warning: Invalid or missing ID for {name}")
                continue
            
            if not re.match(r'^[\w\.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                print(f"Warning: Invalid email for {name}")
                continue
            
            parity = 'even' if int(user_id) % 2 == 0 else 'odd'
            print(f"The ID {user_id} of {email} is {parity} number.")

process_file("/Users/abdelaatyh2/Documents/technical/users.txt")


