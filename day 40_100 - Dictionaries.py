Name= input("Enter your name: ")
Birth = input("Enter your Birth: ")
Number = input("Enter your Number: ")
Email = input("Enter your Email: ")
Adress = input("Enter your Adress: ")

myUser = {"Name": Name, "Birth":Birth ,"Number":Number ,"Email":Email ,"Adress": Adress}

print(f"Hi {myUser['Name']} . Our dictionary says that you were born on {myUser['Birth']}, we can call you on {myUser['Number']}, email {myUser['Email']}, or write to your address which is {myUser['Adress']} .")