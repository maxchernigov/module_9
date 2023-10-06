records = {}

def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Use help"
    return inner

@user_error
def hello(*args):
    return "How can I help you?"


@user_error
def add_contact(*args):
    contact_name = args[0]
    contact_number = args[1]
    records[contact_name] = contact_number
    return(f"Added contact: {contact_name = } , {contact_number = }")

@user_error
def change_contact(*args):
    change_name = args[0]
    change_number = args[1]
    records[change_name] = change_number
    return(f"Change contact: {change_name = } , {change_number = }")
    
@user_error
def phone(*args):
    contact_name = args[0]
    if contact_name in records:
        return f"Phone number for {contact_name}, {records[contact_name]}"

@user_error
def show_all(*args):
    return records


COMMANDS = {hello: "hello",
            add_contact: "add",
            change_contact: "change",
            phone: "phone",
            show_all: "show all",
}

def parser(text:str):
    for func , kw in COMMANDS.items():
        if text.lower().startswith(kw):
            return func, text[len(kw):].strip().split()
    return None, None  



def main():
    while True:
        user_input = input(">>>").strip().lower()
        func, data = parser(user_input)
        if func is not None:
            result = func(*data)
            print(result)
        if user_input.lower() == "good bye" or user_input.lower() == "exit" or user_input.lower() == "close":
            print("Good Bye")
            break
        

if __name__ == "__main__":
    main()

