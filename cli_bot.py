def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
    except  ValueError:
        return "Values should be name and phone."
    #should be checked for phone number, out of scope
    contacts[name] = phone
    return "Contact added."


def add_username_phone(args, contacts):
    try:
        name = args
    except  ValueError:
        return "Value should be name."
    name = ''.join(name)
    if is_contact_exists(name, contacts):
        return contacts[name]
    else:
        return "No such contact in the list."


def change_username_phone(args, contacts):
    try:
        name, phone = args
    except  ValueError:
        return "Values should be name and phone."
    name = ''.join(name)
    #should be checked for phone number, out of scope
    phone = ''.join(phone)
    if is_contact_exists(name, contacts):
        contacts[name] = phone
        return "Phone was changed."
    else:
        return "No such contact in the list."


def is_contact_exists(name, contacts):
     if contacts.get(name) != None:
         return True
     return False


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command.strip() in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(add_username_phone(args, contacts))
        elif command == "all":
            text = ""
            for k, v in contacts.items():
                text += f"{k} {v}\n"
            print(text)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()