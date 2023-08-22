rooms = {
    "harcówka_na_dole": False,
    "harcówka_na_górze": False,
    "gabinet": False,
    "sekret_room": False,
}

def lock_room(room_name):
    if room_name in rooms:
        if not rooms[room_name]:
            rooms[room_name] = True
            print(f"{room_name} is now locked.")
        else:
            print(f"{room_name} is already locked.")
    else:
        print(f"{room_name} is not a valid room.")

def unlock_room(room_name):
    if room_name in rooms:
        if rooms[room_name]:
            rooms[room_name] = False
            print(f"{room_name} is now unlocked.")
        else:
            print(f"{room_name} is already unlocked.")
    else:
        print(f"{room_name} is not a valid room.")

while True:
    print("\nDostępne Pokoje:")
    for room in rooms:
        status = "Locked" if rooms[room] else "Unlocked"
        print(f"{room}: {status}")

    action = input("\nWpisz nazwę pokoju i komendę lock żeby zająć pokój lub unlock żeby zwolnić pokój:").strip().lower()

    if action == 'quit':
        break
    elif action.startswith("lock"):
        room_name = action.split(" ")[-1]
        lock_room(room_name)
    elif action.startswith("unlock"):
        room_name = action.split(" ")[-1]
        unlock_room(room_name)
    else:
        print("Invalid command. Please use 'lock <room_name>' or 'unlock <room_name>'.")