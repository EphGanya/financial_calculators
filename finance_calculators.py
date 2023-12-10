import math

#this program will allow user to choose between investment and bond calculation
#user can choose between simple and compound interest
#the program then calculates the chosen item for the user and prints it out in the terminal


print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

while True:

    fin_calculation=input("Enter either 'investment' or 'bond' from the menu above to proceed or 'exit' to quit: ").lower()


    if fin_calculation == "investment":
        p= int(input("please enter the amount you wish deposit:"))
        print(p)

        interest_rate=float(input("Please enter the interest amount: "))

        r= interest_rate/100
        print(r)

        m=int(input("Please enter the number of compounding periods, enter 1 for simple interest: "))

        n=int(input("Please enter number of years:"))

        t=m*n
        print(t)

        interest = input("do you want to calculate simple or compound interest: ").lower()
        print(interest)

        if interest == "simple":
            Si= p*(1 + r*t)-p
            print(Si)

        else:
            A = p* math.pow((1+r),t)
            print(A)
 
    elif fin_calculation == "bond":
        P= int(input("Please enter current value of the house: "))
        print(P)

        interest_value= int(input("Please enter interest value: "))
        print(interest_value)

        interest_rate=interest_value/100

        i = interest_rate/12
        print(i) 

        n= int(input("Please enter number of years: "))
        print(n)

        repayment =(i * P)/(1 - (1 + i)**(-n)) 
        print("You will pay R"+str(repayment)+ " for your bond.")

    elif fin_calculation == "exit":
        print("Exiting financial calculator!")
        exit()

    else :
        print("Invalid input. Please try again")