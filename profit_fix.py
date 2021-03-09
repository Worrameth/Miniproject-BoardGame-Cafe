import csv
import Mainmenu
def delete_data(row):
    reader.pop(row)
with open('Bill_Detail.csv', 'r+') as P:
    def read_file(P):
        global reader
        t=0
        reader1 = csv.reader(P)
        reader = []
        for i in reader1:
            reader.append(i)
        return reader

    show = read_file(P)

    def show_file(show=show):
        yo=0
        for i in show:
            print(yo,i)
            yo=yo+1

    with open('Bill_Total.csv', 'r+') as P:
        def read_file(P):
            t = 0
            reader1 = csv.reader(P)
            reader = []
            for i in reader1:
                reader.append(i)

            return reader

        show2 = read_file(P)

        def show_file2(show2=show2):
            for i in show2:
                print(','.join([str(e) for e in i]))

    def search_date():
        a = 0
        search = input("Enter date/month/year : ")
        print(','.join([str(e) for e in show[0]]))
        for i in show:
            if search in show[a]:
                print(','.join([str(e) for e in i]))
            else:
                print("No Data has Not Found")
            a += 1
            
    def search_month_year():
        a = 0
        search = input("Enter month/year : ")
        print(','.join([str(e) for e in show[0]]))
        for i in show:
            if search in show[a][0]:
                print(','.join([str(e) for e in i]))
            else:
                print("No Data has Not Found")
            a += 1

    def show_profit_date():
        a=0
        search = input("Enter date/month/year : ")
        t=0
        for i in show2:
            x = int(show2[a][3])
            if search in show2[a]:
                t=t+x
            a+=1
        print("Total Income on",search,"=",t,"")
        print("Daily Cost on",search,"=",500,"")
        print("Total Profit on",search,"=",t-500,"")

    def show_profit_month():
        a=0
        day=0
        search = input("Enter month/year : ")
        t=0
        dc=0
        for i in show2:
            x = int(show2[a][3])
            if search in show2[a][0]:
                t=t+x
                dc=dc+500
                day=day+1
            a+=1
        print("Total Income on",search,day,"Day","=",t,"")
        print("Daily Cost on",search,"=",dc,"")
        print("Total Profit on",search,"=",t-dc,"")

    def delete_data(row_no,show=show):
        print("****"*10)
        print(show[row_no])
        print("****"*10)
        del show[row_no]
        for i in show:
            print(i)


    def save_total():
        with open("Bill_Total.csv", "w+") as f:
            data = list(reader)
            for r in data:
                f.write(",".join(str(s) for s in r) + '\n')
    def save_detail():
        with open("Bill_Detail.csv", "w+") as f:
            data = list(reader)
            for r in data:
                f.write(",".join(str(s) for s in r) + '\n')

def profit():
    print("======================================")
    print("[1] Show Bill Detail")
    print("[2] Exit")
    print("======================================")
    n =int(input("Enter number : "))
    if n == 1:
        print("======================================")
        print("[1] Show Bill All")
        print("[2] Search date")
        print("[3] Search month/year")
        print("[4] Search profit date")
        print("[5] Search profit month/year")
        print("[6] Delete Bill")
        print("[7] Exit")
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
        elif r== 6:
            show_file()
            row = int(input("Delete Row:"))
            print(delete_data((row)))
            save_detail()
            save_total()
            show_file()
            return profit()

        else :
            Mainmenu.menu()
    else:
        Mainmenu.menu()
