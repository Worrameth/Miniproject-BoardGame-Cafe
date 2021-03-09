import Mainmenu
def read_file():
    global lines
    global f
    with open("admin_permission.csv", "r+") as f:
        lines = list(f)
def show_data():
    global records
    read_file()
    records = []
    i=0
    for line in lines:
        tokens = line.rstrip("\n").split(",")
        d = []
        for t in tokens:
            d.append(t)
        records.append(d)
        print(i,records[i])
        i=i+1
def product_data(row_no):
    read_file()
    records[row_no]
def edit_data(row_no,choose):
    product_data(row_no)
    if choose==1:
        records.pop(row_no)
        print("---Enter Data Your Want to Edit---")
        d1 = input("ID:")
        d2 = input("Password:")
        d3 = input('UserName:')
        data = [d1,d2,d3]
        records.insert(row_no,data)
    elif choose==2:
        records[row_no].pop(0)
        print("Enter New ID")
        d1 = input("ID:")
        records[row_no].insert(0,d1)
    elif choose==3:
        records[row_no].pop(1)
        print("Enter New Password")
        d2 = input("ID:")
        records[row_no].insert(1,d2)
    elif choose==4:
        records[row_no].pop(2)
        print("Enter New Username")
        d3 = input("Username:")
        records[row_no].insert(2,d3)
    else:
        return program()
    save()
def add_data(data):
    records.append(data)
    save()
def delete_data(row):
    records.pop(row)
    save()
def save():
    with open("admin_permission.csv", "w+") as f:
        data = list(records)
        for r in data:
            f.write(",".join(str(s) for s in r) + '\n')
def search(row):
    print(records[row])
def cc():
    print("========Menu======= \n 1.Admin Data \n 2.Add Admin Data \n 3.Edit Admin Data \n 4.Delete Admin Data \n 5.Back To Main")
    a = int(input("Choose Menu:"))
    if a == 1:
        print("------Show Data------")
        show_data()
        return cc()
    elif a == 2:
        print("------Add Data-------")
        d1 = input("ID:")
        d2 = input('Password:')
        d3 = input("User Name:")
        data = [d1, d2, d3]
        show_data()
        add_data(data)
        return cc()
    elif a == 3:
        print("------Edit Data------")
        row_no = int(input("Choose Your Row to Want Edit : "))
        print(records[0])
        print(records[row_no])
        print("------Edit Menu------")
        print("1.Edit  Data \n 2.Edit Password\n 3.Edit Password \n 4.Edit Username")
        choose = int(input("Choose Your Menu to Want Edit : "))
        edit_data(row_no,choose)
        return cc()
    elif a == 4:
        print("-----Delete Data-----")
        row = int(input("row : "))
        delete_data(row)
        return cc()
    elif a==5:
        print("Good Bye")
        Mainmenu.menu()
    else:
        print("Noooooooo")
        return cc()

