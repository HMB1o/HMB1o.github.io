Food= input("What type of sandwich do you want?\n chicken for $5.25,\n beef for $6.25,\n tofu for $5.75 \n")
if Food.lower:
    print("Confirming a" + " " + Food + " " + "sandwich")

    if Food.lower() =="chicken":
        SCost = "5.25"
    else:
        if Food.lower() == "beef":
            SCost = "6.25"
        else: SCost = "5.75"
    SYN = "1"


Drink= input("Do you want a drink?\n")
if Drink.lower() == "yes":
    Type = input("What drink?\n -Coke \n -Pepsi\n")
    Size = input("What size\n -Small drink for $1.00, \n -Medium drink for $1.75,\n -Large drink for $2.25 \n")
    if Size.lower() =="small":
        SiCost = "1.00"
    else:
        if Size.lower() == "medium":
            SiCost = "1.75"
        else: SiCost = "2.25"
    total = float(SCost) + float(SiCost)
    print("Confirming a"+ " " + Size + " " + Type +" with a" + " " + Food + " ")
    DYN = "1"
else:
    print ("Your order consists of a" + " " + Food + " " + "sandwich" + " ")
    SiCost = "0"

    Size = "no drink"
    Type= ""
    DYN = "0"
 
Fries = input ("Would you like Fries?\n")
if Fries.lower() == "yes":
    FSize = input("What size\n -Small fries for $1.00, \n -Medium fries for $1.50,\n -Large fries for $2.00 \n")
    if FSize.lower() =="small":
        Ssize = input("Would you like to mega size your fries, for a $2.00?\n")
        if Ssize.lower() == "yes":
            FCost = "2.00" 
        else: FCost = "1.00"
    else:
        if Size.lower() == "medium":
            FCost = "1.50"
        else: FCost = "2.00"
    print("Confirming a"+" "+ FSize + " " + "fries" + " " + "with a"+ " "+ Food + " "+"sandwich"+ " " + Size + " " + Type)
    FYN = "1"

else: 
  FCost = "0"
  total = float(SCost) + float(SiCost) 
  FYN = "0"
  FSize = "no"
  print ("Your order consists of a" + " " + Food + " " + "sandwich" + " " + FSize + " " + "fries"+ " "+ Size + " " + Type)


Ketchup = input("How many ketchup packets for $0.25 each do you want?\n")
if Ketchup.isdigit():
    KCost = (float(Ketchup)*0.25)
    total = float(SCost) + float(SiCost) + float(FCost) + float(KCost)
    MDeal = float(SYN) + float(DYN) + float(FYN)
    if MDeal == 3:
        total= total-1
    print("Confirming a"+" "+ FSize + " " + "fries" + " " + "with a"+ " "+ Food + " "+ "sandwich"
          + " " + Size + " " + Type + " "+ Ketchup + " " + "packets of ketchup" + " "+ "for a total of " + " $" + str(total))
else:
    Ketchup =input("Please input the amount of Ketchup packets you want if you want none input 0 \n")




    

