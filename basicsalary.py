bsalary = int(input("enter the basic salary "))
if bsalary <= 10000:
    hra = (67 / 100) * bsalary
    da = (73 / 100) * bsalary
elif bsalary <= 20000:
    hra = (69 / 100) * bsalary
    da = (76 / 100) * bsalary
else :
    hra = (73 / 100) * bsalary
    da = (89 / 100) * bsalary
gs = hra + da + bsalary
print(f"gross salary", gs)