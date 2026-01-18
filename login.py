def login():
    users = {}

    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or "," not in line:
                    continue

                u, p = line.split(",", 1)
                users[u.strip()] = p.strip()
    except FileNotFoundError:
        print("users.txt not found")
        return False

    attempts = 3

    while attempts > 0:
        print("\n===== LOGIN =====")
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if username in users and users[username] == password:
            print("Login Successful")
            return True
        else:
            attempts -= 1
            print("Invalid credentials")

    return False