#Question 2
#Variables
year = 0
month = 0
days = 30
#Input the Year, month and date
year = int(input("Enter the year. "))
month = int(input("Enter the month. "))
date_1 = int(input("Enter the date. "))
#Checking whether the date is valid or not based on the input data
#February (Additional Calculation for the leap year)
if year % 4 == 0 and month == 2 and date_1 == 29:
    month += 1
    date_1 = days - date_1
    print("Date is valid")
    print(f"The next date is {date_1}-{month}-{year}")
elif year % 4 == 0 and month == 2 and date_1 < 29:
    print("Date is valid")
    print(f"The next date is {date_1 + 1}-0{month}-{year}")
elif year % 4 == 0 and month == 2 and date_1 >29:
    print("Date is invalid.")
elif year % 4== 1 and month == 2 and date_1 >28:
    print("Date is invalid")
elif year % 4 == 1 and month == 2 and date_1 == 28:
    print("Date is valid")
    month+=1
    date_1 = (days - 1) - date_1
    print(f"The next date is {date_1}-0{month}-{year}")
elif year % 4 == 1 and month == 2 and date_1<28:
    date_1 += 1
    print("Date is valid.")
    print(f"The next date is {date_1}-0{month}-{year}")
#January
elif month == 1 and date_1 <31:
    date_1+= 1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 1 and date_1 == 31:
    month += 1
    date_1 = date_1 - days
    print("Data is valid.")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 1 and date_1 >31:
    print("Date is invalid")
#March
elif month == 3 and date_1 <31:
    date_1 +=1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 3 and date_1 == 31:
    month += 1
    date_1 = date_1 - days
    print("Date is valid.")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 3 and date_1 > 31:
    print("The date is invalid.")
#April
elif month == 4 and date_1 <30:
    date_1 += 1
    print("Date is valid.")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 4 and date_1 == 30 :
    date_1 = (days+1) - date_1
    month += 1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 4 and date_1 >30:
    print("Date is invalid")
#May
elif month == 5 and date_1 <31:
    date_1 += 1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 5 and date_1 == 31:
    month +=1
    date_1 = date_1 - days
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 5 and date_1 >31:
    print("Date is invalid")
#June
elif month == 6 and date_1 < 30:
    date_1 += 1
    print("Date is valid.")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 6 and date_1 == 30:
    month += 1
    date_1 = (days+1)- date_1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 6 and date_1 >30:
    print("Date is invalid.")
#July
elif month == 7 and date_1 <31:
    date_1 += 1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 7 and date_1 == 31:
    month += 1
    date_1 = date_1 - days
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 7 and date_1 >31:
    print("Date is invalid")
#August
elif month == 8 and date_1 <31:
    date_1+=1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 8 and date_1 == 31:
    month +=1
    date_1 = date_1 - days
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 8 and date_1 > 31:
    print("The date is invalid")
#September
elif month == 9 and date_1 <30:
    date_1+=1
    print("Date is valid.")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 9 and date_1 == 30:
    month += 1
    date_1 = (days+1) - date_1
    print("Date is valid")
    print(f"The next date is {date_1}-0{month}-{year}")
elif month == 9 and date_1 > 30:
    print("The date is invalid")
#October
elif month == 10 and date_1 < 31:
    date_1 += 1
    print("Date is valid")
    print(f"The next date is {date_1}-{month}-{year}")
elif month == 10 and date_1 == 31:
    month += 1
    date_1 = date_1 - days
    print("Date is valid")
    print(f"The next date is {date_1}-{month}-{year}")
elif month == 10 and date_1 >31:
    print("The date is invalid")
#Novermber
elif month == 11 and date_1 <30:
    date_1 += 1
    print("Date is valid")
    print(f"The next date is {date_1}-{month}-{year}")
elif month == 11 and date_1 == 30:
    month += 1
    date_1 = (days + 1) - date_1
    print("Date is valid")
    print(f"The next date is {date_1}-{month}-{year}")
elif month == 11 and date_1 >30:
    print("The date is invalid")
#December
elif month == 12 and date_1 <31:
    date_1 += 1
    print("Date is valid")
    print(f"The next date is {date_1}-{month}-{year}")
elif month == 12 and date_1 == 31:
    year += 1
    month = month - 11
    date_1 = date_1 - days
    print("Date is valid")
    print(f"The next date is {date_1}-{month}-{year}")
elif month == 12 and date_1 >31:
    print("This date is invalid")
elif month >12:
    print("Date is invalid")
#End of code