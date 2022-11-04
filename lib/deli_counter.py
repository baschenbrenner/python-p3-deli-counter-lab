

def line(list):
    if len(list) == 0:
        print("The line is currently empty.")
    else:
        str = ""
        for index, name in enumerate(list):
            str += f'{index+1}. {name} '
            
        string = str[0:len(str)-1]
        print(f"The line is currently: {string}")
    pass

def take_a_number(list, name):
    list.append(name)
    print(f"Welcome, {name}. You are number {len(list)} in line.")
    pass

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        name = list.pop(0)
        print(f"Currently serving {name}.")
    pass