mobile_number = str(input("Enter mobile number: "))
if len(mobile_number) != 11:
    print("Invalid mobile number")
elif mobile_number[0:2] != "09":
    print("Invalid mobile number")
else:
    if mobile_number[0:4] == "0913" or mobile_number[0:4] == "0914" or mobile_number[0:4] == "0920" or mobile_number[0:4] == "0921" or mobile_number[0:4] =="0928" or mobile_number[0:4] == "0929" or mobile_number[0:4] == "0930":
         print("The network of the mobile number is Smart")
    elif mobile_number[0:4] == "0909" or mobile_number[0:4] == "0910" or mobile_number[0:4] == "0911" or mobile_number[0:4] == "0912" or mobile_number[0:4] == "0918" or mobile_number[0:4] == "0919":
         print("The network of the mobile number is TNT")
    elif mobile_number[0:4] == "0922" or mobile_number[0:4] == "0923" or mobile_number[0:4] =="0932" or mobile_number[0:4] == "0933":
         print("The network of the mobile number is Sun")
    elif mobile_number[0:4] == "0915" or mobile_number[0:4] == "0916" or mobile_number[0:4] == "0917" or mobile_number[0:4] == "0925" or mobile_number[0:4] == "0926" or mobile_number[0:4] == "0927":
         print("The network of the mobile number is Globe")
    elif mobile_number[0:4] == "0903" or mobile_number[0:4] == "0904" or mobile_number[0:4] == "0905" or mobile_number[0:4] == "0906" or mobile_number[0:4] == "0907":
         print("The network of the mobile number is TM")
    elif mobile_number[0:4] == "0901" or mobile_number[0:4] == "0902" or mobile_number[0:4] == "0924":
         print("The network of the mobile number is Red")
    elif mobile_number[0:4] == "0991" or mobile_number[0:4] == "0992" or mobile_number[0:4] == "0993" or mobile_number[0:4] == "0994" or mobile_number[0:4] == "0995" or mobile_number[0:4] == "0996" or mobile_number[0:4] == "0997" or mobile_number[0:4] == "0998":
         print("The network of the mobile number is DITO")
    else:
         print("Unknown network")