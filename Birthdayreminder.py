
dict={}
while True:
      print("***********Birthday reminder*********")
      print("1.Display the birthday")
      print("2.Add Birthday")
      print("3.Exit")
      choice=int(input("Enter the Options--"))
      if choice == 1:
         if len(dict.keys())==0:
            print("No data")
         else:
            name=input("Enter name for Birthday")
            birthday=dict.get(name,"no data")
            print(birthday)
      elif choice == 2:
        name = input("Enter the Birthday Boy/girl name")
        date=input("enter birthdate")
        dict[name]=date
        print("Birthday Added")
      elif choice ==3:
          break
      else:
         print("Invalid Request")
        

