import Mainmenu
import user_data
def menu():
   print('-----Edit Data-----')
   print('1.User\n2.Exit')
   gg = int(input("Enter Menu Number:"))
   if gg == 1:
       user_data.program()
   elif gg == 2:
       Mainmenu.menu()