#Compound interest
print("Please input the value of your Principal(P)")
p = float(input())

print("Please input the value of your Range(R)")
r = float(input())

print("Please state the amount of years elapsed(T)")
t = float(input())

print("please state the number of times your interest applied(n)")
n = float(input())

n_t = n*t

compound_interest = p*(1.0 + r/n)**n_t

print("Your compound interest is: ", compound_interest)