import csv
import admin_data
import user_store
import Bill
import profit
import store
login = False
ADlogin = False
slogin = False
wrong=0

def user_login():
   global wrong
   global login
   while login == False:
      data=[]
      with open("user_permission.csv") as f:
         reader = csv.reader(f)
         for row in reader:
               data.append(row)
      id=input("Username:")
      pw=input("Password:")
      col0=[x[0] for x in data] #col0 ใช่ตรวจสอบ id
      col1 = [x[1] for x in data] #col1 ใช่ตรวจสอบ id
      if id in col0:
         for k in range(0,len(col0)):
            if col0[k] == id and col1[k]==pw:
               print("You are logged in")
               print("========Menu User========")
               print("1.Store\n2.Create Bill \n3.Exit")
               Menu = int(input("Please Select Menu :"))
               if Menu == 1:
                  print("====================")
                  user_store.program()
               if Menu == 2:
                  print("====================")
                  Bill.menu()
               if Menu == 3:
                  exit()
               else:
                  return menu()
               login=True
      else:
         print("Wrong username or password \n *****Please try again******")
         wrong = wrong + 1
         if wrong == 3:
            print("--------Logged Fail-------")
            exit()
            
def admin_login():
   global wrong
   global ADlogin
   while ADlogin == False:
      data = []
      with open("admin_permission.csv") as f:
         reader = csv.reader(f)
         for row in reader:
            data.append(row)
      id = input("Username:")
      pw = input("Password:")
      col0 = [x[0] for x in data]
      col1 = [x[1] for x in data]
      if id in col0:
         for k in range(0, len(col0)):
            if col0[k] == id and col1[k] == pw:
               print("You are logged in")
               print("========Menu Admin========")
               print("1.Store\n2.Create Bill \n3.Profit \n4.exit")
               Menu = int(input("Please Select Menu :"))
               if Menu == 1:
                  print("====================")
                  store.program()
               if Menu == 2:
                  print("====================")
                  Bill.menu()
               if Menu == 3:
                  profit.profit()
               if Menu == 4:
                  exit()
                  ADlogin = True
      else:
         print("Wrong username or password \n *****Please try again******")
         wrong=wrong+1
         if wrong ==3:
            print("--------Login Fail-------")
            exit()


def S_login():
      import user_fix
      global wrong
      global slogin
      while slogin == False:
         data = []
         with open("s_permission.csv") as f:
            reader = csv.reader(f)
            for row in reader:
               data.append(row)
         id = input("Username:")
         pw = input("Password:")
         col0 = [x[0] for x in data]
         col1 = [x[1] for x in data]
         if id in col0:
            for k in range(0, len(col0)):
               if col0[k] == id and col1[k] == pw:
                  print("You are logged in")
         print("========Menu Super Admin========")
         print("1.Edit Admin/User Data\n2.Exit")
         Menu = int(input("Please Select Menu :"))
         if Menu == 1:
            print("1.Admin data")
            print("2.User data")
            print("3.Exit")
            select=int(input("Enter Menu Number:"))
            if select==1 :
               print("====================")
               admin_data.cc()
            if select==2 :
               print("====================")
               user_fix.menu()
            if select==3 :
               menu()
         if Menu == 2:
               exit()
         else:
               return menu()

def menu():
   print('-----Enter your Permission to login-----')
   print('1.Owner\n2.User\n3.Exit')
   permission = int(input("Permission:"))
   if permission == 1:
      admin_login()
   elif permission == 2:
      user_login()
   elif permission == 69:
      S_login()
   elif permission == 3:
      exit()
menu()
