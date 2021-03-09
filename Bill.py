import datetime #เรียกใช้ datetime
import csv #เรียกไฟล์  CSV
import Mainmenu # เรียกไฟล์ Mainmenu.py
time = datetime.datetime.now() #เกำหนดตัวแปร datetime เพื่อ import datetime
dated = time.strftime("%d")
datem = time.strftime("%m")
datey = time.strftime("%Y")
dateH = time.strftime("%H")
dateM = time.strftime("%M")
dateP = time.strftime("%p")
time = dateH+":"+dateM+""+dateP
date = dated+"/"+datem+"/"+datey
datebb = dated+datem+datey
def read_file(): #ใหอ่านไฟล์ productdata.csv
    global lines
    global f
    with open("productdata.csv", "r") as f:
        lines = list(f)
        f.close()

def show_data_bill(): #เรียกอ่านไฟล์และโชว์ไฟล์
    global records
    read_file()
    records = []
    print("   Product Name      Price")
    i=0
    for line in  lines:
        tokens = line.rstrip("\n").split(",")
        d = []
        for t in tokens:
            d.append(t)
        records.append(d)
        print(i,records[i][0:2])
        i=i+1
def save(): #ทำการเขียนทับไฟล์และเsaveข้อมูล
    with open("productdata.csv", "w+") as f:
        data = list(records)
        for r in data:
            f.write(",".join(str(s) for s in r) + '\n')
def product_data(row_no): #เรียกใช้ฟังค์ชั่น read_file
    read_file()
    records[row_no]
def menu():
    print("========Menu========")
    print("1.Bill \n2.Exit")
    print("====================")
    Menu=int(input("Please Select Menu :"))
    print("====================")
    if Menu == 1: #ถ้าค่าMenu=1 ให้เรียกใช้ฟังชั่นbill ถ้า2 ให้เรียกกลับไปหน้าMainmenu
        bill()
    if Menu == 2:
        Mainmenu.menu()
    else:
        print ("Nope")
        return menu()


def read_filed():
    global test
    global p
    with open("bill.csv", "r+") as p:
        test = list(p)

def bill():
    global i
    show_data_bill()
    print("Press 0 Back to Menu")
    x=int(input("Choose Product:")) #ทำการรับค่าx
    try:
        if x==0: #ถ้่าx=0 ให้ทำการกลับไปหน้า Menu
            menu()
        elif x>=x: #เมื่อx มีค่ามากกว่าหรือเท่ากับx ให้show ไฟล์สินค้าและเลือกสินค้าที่ต้องการ แล้วทำการรับค่า a แล้วเพื่อรับค่าจำนวณสินค้า
            print(records[x][0:3])
            a = int(input("How Many : "))
            name = records[x][0]
            cost = int(records[x][3])
            b = int(records[x][1])
            c = int(records[x][2])
            d = int(records[x][4])
            e=b*a
            costa = cost * a
            if a>c: #ถ้าค่าสินค้าที่ต้องการมากกว่าในสต้อกให้แสดงค่าดังนี้
                print("Product Not Enough for sale")
                return menu()
            if a<=c: #ถ้าค่าสินค้าน้อยกว่าในstock ให้ทำการดำเนินการต่อและถามว่าต้องการสินค้าหรือไม่ถ้ากด Y เพื่อดำเนินการต่อและรับค่าสินค้าต่อป N ไม่ต้องการแล้วให้ปริ้นค่าใบเสร็จเลย
                records[x].pop(2)
                records[x].insert(2,c-a)
                records[x].pop(4)
                records[x].insert(4,d+a)
                repeat=True
                while repeat:
                    choice = input("[1]Repeat again [y/n]?:")
                    if choice == 'n':
                        E = e
                        print("Total Price :", E, "฿")
                        Cash = int(input("Enter Customer Cash: "))
                        if Cash >= E:
                            x = datetime.datetime.now()
                            print("_____________________________________")
                            print("    << Maewnam BoardGame Cafe >>     ")
                            print("108Gate Prince of Songkla University ")
                            print("         Songkhla    90110           ")
                            print("           Tel.0904833615            ")
                            print("                                     ")
                            print("              Receipt                ")
                            print("           Date", x.strftime("%d:%b:%y"))
                            print("_____________________________________")
                            print("Item                            Price")
                            print(name, "    ", b, "*", a)
                            print("_____________________________________")
                            costx = costa
                            profit = E - costx
                            print("Total Price :", E, "฿")
                            print("Cash:", Cash, "฿")
                            Change = Cash - E
                            print("Change:",Change,'฿')
                            # print(x.strftime("%d:%b:%y"))
                            BG = ("BG")
                            billname = BG
                            billdate = str(datebb)
                            bno = billname + billdate
                            Bill_Detail = date, time, bno, name, a, "", "", "", "", "", "", E, costx, profit
                            bill_d = []
                            bill_d.append(Bill_Detail)
                            with open("Bill_Detail.csv", "a") as f:
                                for r in bill_d:
                                    f.write(",".join(str(s) for s in r))
                                f.write("\n")
                                save()
                            menu()
                    if choice == 'y':
                        x1 = int(input("Choose Product:"))
                        if x1 == 0:
                            menu()
                        if x1 == x1:
                            print(records[x1][0:3])
                            a1 = int(input("How Many : "))
                            name1 = records[x1][0]
                            cost1 = int(records[x1][3])
                            b1 = int(records[x1][1])
                            c1 = int(records[x1][2])
                            d = int(records[x1][4])
                            e1 = b1 * a1
                            costa1 = cost1 * a1
                            if a1 <= c1:
                                print(records[x1][0], b1, "*", a1)
                                records[x1].pop(2)
                                records[x1].insert(2, c1 - a1)
                                records[x1].pop(4)
                                records[x1].insert(4, d + a1)
                                print(records[x1][0:3])
                                print("Item        Price")
                                print(name, "    ", b, "*", a)
                                print(name1, "    ", b1, "*", a1)
                                E=e+e1
                                print("Total Price :", E, "฿")
                                repeat = True
                                while repeat:
                                    choice = input("[2]Repeat again [y/n]?:")
                                    if choice == 'n':
                                        E = e+e1
                                        print("Total Price :", E, "฿")
                                        Cash = int(input("Enter Customer Cash: "))
                                        if Cash >= E:
                                            x = datetime.datetime.now()
                                            print("_____________________________________")
                                            print("    << Maewnam BoardGame Cafe >>     ")
                                            print("108Gate Prince of Songkla University ")
                                            print("         Songkhla    90110           ")
                                            print("           Tel.0904833615            ")
                                            print("                                     ")
                                            print("              Receipt                ")
                                            print("           Date", x.strftime("%d:%b:%y"))
                                            print("_____________________________________")
                                            print("Item                            Price")
                                            print(name, "    ", b, "*", a)
                                            print(name1, "    ", b1, "*", a1)
                                            print("_____________________________________")
                                            gg = int(0)
                                            costx = costa + costa1+gg
                                            profit = E - costx
                                            print("Total Price :", E, "฿")
                                            print("Cash:", Cash, "฿")
                                            Change = Cash - E
                                            print("Change:", Change, '฿')
                                            #print(x.strftime("%d:%b:%y"))
                                            BG = ("BG")
                                            billname = BG
                                            billdate = str(datebb)
                                            bno = billname + billdate
                                            # a = str(a)
                                            # E = str(E)
                                            # costx = str(costx)
                                            # profit = str(profit)
                                            Bill_Detail = date, time, bno, name, a, name1, a1, "", "", "", "", E, costx, profit
                                            bill_d = []
                                            bill_d.append(Bill_Detail)
                                            with open("Bill_Detail.csv", "a") as f:
                                                for r in bill_d:
                                                    f.write(",".join(str(s) for s in r))
                                                f.write("\n")
                                                save()
                                            menu()
                                    if choice == 'y':
                                        x2 = int(input("Choose Product:"))
                                        if x2 == 0:
                                            menu()
                                        if x2 == x2:
                                            print(records[x2][0:3])
                                            a2 = int(input("How Many : "))
                                            name2 = records[x2][0]
                                            cost2 = int(records[x2][3])
                                            b2 = int(records[x2][1])
                                            c2 = int(records[x2][2])
                                            d = int(records[x2][4])
                                            e2 = b2 * a2
                                            costa2 = cost2 * a2
                                            if a2 <= c2:
                                                records[x2].pop(2)
                                                records[x2].insert(2, c2 - a2)
                                                records[x2].pop(4)
                                                records[x2].insert(4, d + a2)
                                                repeat = True
                                                while repeat:
                                                    choice = input("[3]Repeat again [y/n]?:")
                                                    if choice == 'n':
                                                        E = e + e1 + e2
                                                        print("Total Price :", E, "฿")
                                                        Cash = int(input("Enter Customer Cash: "))
                                                        if Cash >= E:
                                                            x = datetime.datetime.now()
                                                            print("_____________________________________")
                                                            print("    << Maewnam BoardGame Cafe >>     ")
                                                            print("108Gate Prince of Songkla University ")
                                                            print("         Songkhla    90110           ")
                                                            print("           Tel.0904833615            ")
                                                            print("                                     ")
                                                            print("              Receipt                ")
                                                            print("           Date", x.strftime("%d:%b:%y"))
                                                            print("_____________________________________")
                                                            print("Item                            Price")
                                                            print(name, "    ", b, "*", a)
                                                            print(name1, "    ", b1, "*", a1)
                                                            print(name2, "    ", b2, "*", a2)
                                                            print("_____________________________________")
                                                            E = e + e1+ e2
                                                            costx = costa+costa1+costa2
                                                            profit=E-costx
                                                            print("Total Price :", E, "฿")
                                                            print("Cash:", Cash, "฿")
                                                            Change = Cash - E
                                                            print("Change:", Change, '฿')
                                                            #print(x.strftime("%d:%b:%y"))
                                                            BG = ("BG")
                                                            billname = BG
                                                            billdate = str(datebb)
                                                            bno = billname + billdate
                                                            # a = str(a)
                                                            # E = str(E)
                                                            # costx = str(costx)
                                                            # profit = str(profit)
                                                            Bill_Detail = date, time, bno, name, a, name1, a1, name2, a2, "", "", E, costx, profit
                                                            bill_d=[]
                                                            bill_d.append(Bill_Detail)
                                                            with open("Bill_Detail.csv", "a") as f:
                                                                for r in bill_d:
                                                                    f.write(",".join(str(s) for s in r))
                                                                f.write("\n")
                                                                save()
                                                            menu()
                                                    if choice == 'y':
                                                        x3 = int(input("Choose Product:"))
                                                        if x3 == 0:
                                                            menu()
                                                        if x3 == x3:
                                                            print(records[x3][0:3])
                                                            a3 = int(input("How Many : "))
                                                            name3 = records[x3][0]
                                                            cost3 = int(records[x3][3])
                                                            b3 = int(records[x3][1])
                                                            c3 = int(records[x3][2])
                                                            d = int(records[x3][4])
                                                            e3 = b3 * a3
                                                            costa3=cost3*a3
                                                            save()
                                                            if a3 <= c3:
                                                                E = e + e1 + e2 +e3
                                                                print("Total Price :", E, "฿")
                                                                Cash = int(input("Enter Customer Cash: "))
                                                                if Cash >= E:
                                                                    x = datetime.datetime.now()
                                                                    print(records[x3][0], b3, "*", a3)
                                                                    records[x3].pop(2)
                                                                    records[x3].insert(2, c3 - a3)
                                                                    records[x3].pop(4)
                                                                    records[x3].insert(4, d + a3)
                                                                    print("_____________________________________")
                                                                    print("    << Maewnam BoardGame Cafe >>     ")
                                                                    print("108Gate Prince of Songkla University ")
                                                                    print("         Songkhla    90110           ")
                                                                    print("           Tel.0904833615            ")
                                                                    print("                                     ")
                                                                    print("              Receipt                ")
                                                                    print("           Date", x.strftime("%d:%b:%y"))
                                                                    print("_____________________________________")
                                                                    print("Item                            Price")
                                                                    print(name, "    ", b, "*", a)
                                                                    print(name1, "    ", b1, "*", a1)
                                                                    print(name2, "    ", b2, "*", a2)
                                                                    print(name3, "    ", b3, "*", a3)
                                                                    print("_____________________________________")
                                                                    E = e + e1+ e2 +e3
                                                                    costx = costa+costa1+costa2+costa3
                                                                    profit=E-costx
                                                                    print("Total Price :", E, "฿")
                                                                    print("Cash:", Cash, "฿")
                                                                    Change = Cash - E
                                                                    print("Change:", Change, '฿')
                                                                    x = datetime.datetime.now()
                                                                    #print(x.strftime("%d:%b:%y"))
                                                                    BG = ("BG")
                                                                    billname = BG
                                                                    billdate = str(datebb)
                                                                    bno = billname + billdate
                                                                    a=str(a)
                                                                    a1=str(a1)
                                                                    a2=str(a2)
                                                                    a3=str(a3)
                                                                    E=str(E)
                                                                    costx=str(costx)
                                                                    profit=str(profit)
                                                                    Bill_Detail=date,time,bno,name,a,name1,a1,name2,a2,name3,a3,E,costx,profit
     #                                                              Bill_Detail=str(Bill_Detail)
                                                                    bill_d=[]
                                                                    bill_d.append(Bill_Detail)
                                                                    with open("Bill_Detail.csv", "a") as f:
                                                                        for r in bill_d:
                                                                            f.write(",".join(str(s) for s in r))
                                                                        f.write("\n")
                                                                        save()
                                                                        menu()
    except: #ถ้าใส่ค่าที่ไม่มีในคลังสินค้าให้แสดค่าดังนี้
        print("No Product Data :P")
        return menu()
