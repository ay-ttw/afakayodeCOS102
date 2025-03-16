#Annuity Plan
print("Please input the value of your Payment(PMT)")
p = float(input())

print("Please input the value of your Range(R)")
r = float(input())

print("please state the number of times your interest applied(n)")
n = float(input())

print("Please state the amount of years elapsed(T)")
t = float(input())

n_t = n*t

annuity_plan = (p*((1.0 + r/n)**n_t - 1.0))/(r/n)

print("Your Annuity Plan is: ",annuity_plan)
