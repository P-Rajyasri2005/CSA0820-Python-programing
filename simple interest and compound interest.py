
P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
SI = (P * N * R)/100
print("Simple interest : {}".format(SI))



p = float(input("Enter the principal amount : "))
t = float(input("Enter the number of years : "))
r = float(input("Enter the rate of interest : "))
ci =  p * (pow((1 + r / 100), t)) 
print("Compound interest : {}".format(ci))
