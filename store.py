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
def edit_data(row_no,choose):
    product_data(row_no)
    if choose==1:
        records.pop(row_no)
        print("---Enter Data Your Want to Edit---")
        d1 = input("Product Name:")
        d2 = input("Price:")
        d3 = input('Stock:')
        d4 = input("Cost:")
        d5 = input("Sale:")
        data = [d1,d2,d3,d4,d5]
        records.insert(row_no,data)
    elif choose==2:
        records[row_no].pop(0)
        print("Enter Product")
        d1 = input("Product Name:")
        records[row_no].insert(0,d1)
    elif choose==3:
        records[row_no].pop(1)
        print("Enter Price")
        d2 = input("Price:")
        records[row_no].insert(1,d2)
    elif choose==4:
        records[row_no].pop(2)
        print("Enter Sales")
        d3 = input("Stock:")
        records[row_no].insert(2,d3)
    elif choose==5:
        records[row_no].pop(3)
        print("Enter Cost")
        d4 = input("Cost:")
        records[row_no].insert(3,d4)
    elif choose==6:
        records[row_no].pop(4)
        print("Enter Sales")
        d5 = input("Total Seled:")
        records[row_no].insert(4,d5)
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
    with open("productdata.csv", "w+") as f:
        data = list(records)
        for r in data:
            f.write(",".join(str(s) for s in r) + '\n')
def search(row):
    print(records[row])
def program():
    print("========Menu======= \n 1.Product Data \n 2.Add Product Data \n 3.Edit Product Data \n 4.Delete Product Data \n 5.Search Data \n 6.Back To Main")
    a = int(input("Choose Menu:"))
    if a == 1:
        print("------Show Data------")
        show_data()
        return program()
    elif a == 2:
        print("------Add Data-------")
        d1 = input("Product Name:")
        d2 = input("Price:")
        d3 = input('Total:')
        d4 = input("Cost:")
        d5 = input("Sales:")
        data = [d1, d2, d3, d4, d5]
        show_data()
        add_data(data)
        return program()
    elif a == 3:
        show_data()
        print("------Edit Data------")
        row_no = int(input("Choose Your Row to Want Edit : "))
        print(records[0])
        print(records[row_no])
        print("------Edit Menu------")
        print("1.Edit All Data \n 2.Edit Product Name \n 3.Edit Price \n 4.Edit Stock Product \n 5.Edit Cost Product \n 6.Edit Total Sales Product")
        choose = int(input("Choose Your Menu to Want Edit : "))

        edit_data(row_no,choose)
        return program()
    elif a == 4:
        print("-----Delete Data-----")
        row = int(input("row : "))
        show_data()
        delete_data(row)
        return program()
    elif a == 5:
        print("-------Search--------")
        row = int(input("row : "))
        search(row)
        return program()
    elif a==6:
        print("Good Bye")
        Mainmenu.menu()
    else:
        print("No!!!!!")
        return program()
