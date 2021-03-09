import Mainmenu

def read_file():
    global lines
    global f
    with open("user_permission.csv", "r+") as f:
        lines = list(f)
def show_data():
    global recordss
    read_file()
    recordss = []
    i=0
    for line in lines:
        tokens = line.rstrip("\n").split(",")
        d = []
        for t in tokens:
            d.append(t)
        recordss.append(d)
        print(i,recordss[i])
        i=i+1
def product_data(row_no):
    read_file()
    records[row_no]
def edit_data(row_no,choose):
    product_data(row_no)
    if choose==1:
        recordss.pop(row_no)
        print("---Enter Data Your Want to Edit---")
        d1 = input("ID:")
        d2 = input("Password:")
        d3 = input('UserName:')
        data = [d1,d2,d3]
        recordss.insert(row_no,data)
    elif choose==2:
        recordss[row_no].pop(0)
        print("Enter New ID")
        d1 = input("ID:")
        recordss[row_no].insert(0,d1)
    elif choose==3:
        recordss[row_no].pop(1)
        print("Enter New Password")
        d2 = input("ID:")
        recordss[row_no].insert(1,d2)
    elif choose==4:
        recordss[row_no].pop(2)
        print("Enter New Username")
        d3 = input("Username:")
        recordss[row_no].insert(2,d3)
    else:
        return program()
    save()
def add_data(data):
    recordss.append(data)
    save()
def delete_data(row):
    recordss.pop(row)
    save()
def save():
    with open("user_permission.csv", "w+") as f:
        data = list(recordss)
        for r in data:
            f.write(",".join(str(s) for s in r) + '\n')
def search(row):
    print(recordss[row])
def program():
    print("========Menu======= \n 1.User Data \n 2.Add User Data \n 3.Edit User Data \n 4.Delete User Data \n 5.Back To Main")
    a = int(input("Choose Menu:"))
    if a == 1:
        print("------Show Data------")
        show_data()
        return program()
    elif a == 2:
        print("------Add Data-------")
        d1 = input("ID:")
        d2 = input('Password:')
        d3 = input("User Name:")
        data = [d1, d2, d3]
        show_data()
        add_data(data)
        return program()
    elif a == 3:
        print("------Edit Data------")
        row_no = int(input("Choose Your Row to Want Edit : "))
        print(recordss[0])
        print(recordss[row_no])
        print("------Edit Menu------")
        print("1.Edit User Data \n 2.Edit Password \n 3.Edit Username")
        choose = int(input("Choose Your Menu to Want Edit : "))
        edit_data(row_no,choose)
        return program()
    elif a == 4:
        print("-----Delete Data-----")
        row = int(input("row : "))
        delete_data(row)
        return program()
    elif a==5:
        print("Good Bye")
        Mainmenu.menu()
    else:
        print("Noooooooo")
        return program()