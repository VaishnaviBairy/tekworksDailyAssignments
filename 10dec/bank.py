class Bank:
    totalamount = 100000
    def Deposit(self):
        damount =int(input("Enter the amount to deposit: "))
        if  (damount%100)==0 and 100<damount<50000:
            print("Deposit accept")
        else:
            print("Deposit reject")

    def Withdraw(self, totalamount=100000):
        noOtrans=3
        limitamount=20000
        for i in range(noOtrans):
            withdrawamount = int(input("Withdraw amount: "))
            if  totalamount>500 and withdrawamount>=100 and withdrawamount%100==0 and withdrawamount<totalamount and withdrawamount<=limitamount:
                balance=totalamount-withdrawamount
                print(balance)
                print("Withdraw accept")
                break
            else:
                remtrans=noOtrans-(i+1)
                if(remtrans>0):
                    print("Withdraw reject")
                    print("remaining chances:",remtrans)
                else:
                    print("no more attemps")
    def balEnquiry(self):
        return

    def viewOptions(self):
        print('1.Deposit \n 2.Withdraw \n 3.balEnquiry\n 4.exit')
        options=int(input("choose the options"))
        if options==1:
            obj.Deposit()
        elif options==2:
           obj.Withdraw()
        elif options==3:
            obj.balEnquiry()
        elif options==4:
            exit()

    def validate(self):
        noOfchances = 3
        for i in range(noOfchances):
            pinnum = int(input("Enter Pin Number: "))
            if pinnum == 1234:
                self.viewOptions()
                return
            else:
                remainingattempts=noOfchances-(i+1)
                if(remainingattempts>0):
                    print("Invalid Pin Number")
                    print("remaining attempts:",remainingattempts)
                else:
                    print("no more attempts")
obj=Bank()
obj.validate()

