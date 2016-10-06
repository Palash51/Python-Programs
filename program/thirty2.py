# Enter your code here. Read input from STDIN. Print output to STDOUT
meal = float(input())
tip = input()
tax = input()

total_Cost = meal + (tip*meal)/100 + (tax*meal)/100

print "The total meal cost is"+ " " + str(int(round(total_Cost))) + " dollars"  
