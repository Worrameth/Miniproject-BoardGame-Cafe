import csv
import Mainmenu

with open('Bill_Detail.csv', 'r+') as P:  ##  เปิดไฟล์ชื่อ ฺBill_Detail.csv
    def read_file(P):  # อ่านไฟล์ แล้วเก็บในตัวแปร show
        global reader
        t = 0
        reader1 = csv.reader(P)
        reader = []
        for i in reader1:
            reader.append(i)
        return reader


    show = read_file(P)  # อ่านไฟล์ แล้วเก็บในตัวแปร show


    def show_file(show=show):  # แสดงไฟล์ โดยดึงตัวแปร show มาแสดง เพื่อทำให้การรันผลลัพธ์ เป็นทรรทัด
        yo = 0
        print("|Date | Time | Bill No	| Item1	| Item1_EA	| Item2	| Item2_EA	| Item3	| Item3_EA | Item4 | Item4_EA |	T_Price| Cost |	Profit |")
        for i in show:
            print(yo, ','.join([str(e) for e in i]))
            yo = yo + 1


    with open('Bill_Detail.csv', 'r+') as P:  ##  เปิดไฟล์ชื่อ ฺBill_Total.csv
        def read_file(P):
            t = 0
            reader1 = csv.reader(P)
            reader = []
            for i in reader1:
                reader.append(i)

            return reader


        show2 = read_file(P)  # อ่านไฟล์ แล้วเก็บในตัวแปร show2


        def show_file2(show2=show2):  # แสดงไฟล์ โดยดึงตัวแปร show2 มาแสดง เพื่อทำให้การรันผลลัพธ์ เป็นทรรทัด
            for i in show2:
                print(','.join([str(e) for e in i]))


    def search_date():  # โปรแกรมค้นหาข้อมูลบิลรายวัน
        a = 0
        search = input("Enter date/month/year : ")
        print(','.join([str(e) for e in show[0]]))  # แสดงหัวข้อมูล
        for i in show:
            if search in show[a]:  # ตรวจสอบ ่า search มีค่าในตรงกับใน show รึป่าว
                print(','.join([str(e) for e in i]))
            else:
                print("No Data has Not Found")
            a += 1


    def search_month_year():  # โปรแกรมค้นหาข้อมูลบิลรายเดือน
        a = 0
        search = input("Enter month/year : ")
        print(','.join([str(e) for e in show[0]]))
        for i in show:
            if search in show[a][0]:  # ตรวจสอบ ่า search มีค่าในตรงกับใน show array หลัก จ รึป่าว
                print(','.join([str(e) for e in i]))
            else:
                print("No Data has Not Found")
            a += 1


    def show_profit_date():  # โปรแกรมแสดงผลกำไลรายวัน
        a = 0
        search = input("Enter date/month/year : ")
        t = 0  # ตัวแปรงเก็บค่าผลรวม
        for i in show2:
            x = int(show2[a][13])  # แปลงค่า ในหลักที่ 3 ทั้งหมดเป็นตัวเลขเพื่อจะนำมาคำนวน
            if search in show2[a]:  # ตรวจสอบ ่า search มีค่าในตรงกับใน show รึป่าว
                t = t + x  # นำค่า x ที่ผ่าน if ทั้งหมดมาเข้าในตัวแปรง t
            a += 1
        print("Total Income on", search, "=", t, "")
        print("Daily Cost on", search, "=", 500, "")
        print("Total Profit on", search, "=", t - 500, "")


    def show_profit_month():  # โปรแกรมแสดงผลกำไลรายเดือน
        a = 0
        day = 0  # ตัวแปรจำนวนวันในแต่ละเดือน
        search = input("Enter month/year : ")
        t = 0  # ตัวแปรงเก็บค่าผลรวม
        dc = 500 * 26  # ตัวแปรงเก็บค่าจำนวนวันภายในเดือนนั้น ๆ
        for i in show2:
            x = int(show2[a][13])
            if search in show2[a][0]:
                t = t + x
                day = day + 1  # นับจำนวนวันในแต่ละรอบ
            a += 1
        print("Total Income on", search, day, "Day", "=", t, "")
        print("Daily Cost on", search, "=", dc, "")
        print("Total Profit on", search, "=", t - dc, "")


    def show_profit_year():  # โปรแกรมแสดงผลกำไลรายเดือน
        a = 0
        day = 0  # ตัวแปรจำนวนวันในแต่ละเดือน
        search = input("Enter year : ")
        t = 0  # ตัวแปรงเก็บค่าผลรวม
        dc = 500 * 312  # ตัวแปรงเก็บค่าจำนวนวันภายในเดือนนั้น ๆ
        for i in show2:
            x = int(show2[a][13])
            if search in show2[a][0]:
                t = t + x
                day = day + 1  # นับจำนวนวันในแต่ละรอบ
            a += 1
        print("Total Income on", search, day, "Day", "=", t, "")
        print("Daily Cost on", search, "=", dc, "")
        print("Total Profit on", search, "=", t - dc, "")


def save_detail():
    with open("Bill_Detail.csv", "w+") as f:
        data = list(reader)
        for r in data:
            f.write(",".join(str(s) for s in r) + '\n')


def delete_data(row_no, show=show):
    print("****" * 10)
    print(show[row_no])
    print("****" * 10)
    del show[row_no]
    for i in show:
        print(i)


def profit():  # ตัวโปรแกรม Profit
    print("======================================")
    print("[1] Show Bill Detail")
    print("[2] Exit")
    print("======================================")
    n = int(input("Enter number : "))
    if n == 1:
        print("======================================")
        print("[1] Show Bill All")
        print("[2] Search date")
        print("[3] Search month/year")
        print("[4] Search profit date")
        print("[5] Search profit month")
        print("[6] Search profit year")
        print("[7] Delete Bill")
        print("[8] Exit")
        print("======================================")
        r = int(input("Select : "))
        if r == 1:
            show_file()
            return profit()
        elif r == 2:
            search_date()
            return profit()
        elif r == 3:
            search_month_year()
            return profit()
        elif r == 4:
            show_profit_date()
            return profit()
        elif r == 5:
            show_profit_month()
            return profit()
        elif r == 6:
            show_profit_year()
            return profit()
        elif r == 7:
            show_file()
            row = int(input("Delete Row:"))
            print(delete_data((row)))
            save_detail()
            show_file()
            return profit()
        elif r == 8:
            Mainmenu.menu()
    else:
        Mainmenu.menu()
