import Mainmenu
def read_file():
    global lines
    global f
    with open("productdata.csv", "r+") as f:
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
def search(row):
    print(records[row])
def program():
    print("========Menu======= \n 1.Product Data\n 2.Search Data \n 3.Back To Main Menu")
    a = int(input("Choose Menu:"))
    if a == 1:
        print("------Show Data------")
        show_data()
        return program()
    elif a == 2:
        print("-------Search--------")
        row = int(input("row : "))
        search(row)
        return program()
    elif a == 3:
        Mainmenu.menu()
    elif a==6:
        exec(open("permiss2.py").read());
    else:
        exec(open("permiss2.py").read());
    
