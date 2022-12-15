# This program will take user inputs about USA road trip and display the
# total costs and each participants share of the trip in USD.
# Developer: Angela Tackett          CMIS102                     03JUL2022

#welcome function
def Welcome():
    print('\n\t\tRoadtrip Cost Calculator\n\n')

#input function
def Inputs():
    #prompt for number of people
    tot_people = int(input('Enter number of people on trip: '))
    while True:
        if tot_people <=0:
            tot_people = int(input('Enter number of people on trip: '))
        else:
            break
        
    #prompt for trip length    
    tot_days = int(input('Enter length of trip [days]: '))
    while True:
        if tot_days <= 0:
            tot_days = int(input('Enter length of trip [days]: '))
        else:
            break

    #prompt daily food cost (loop validation included)
    x = int(tot_days)
    food = []
    f_cost = 1
    while f_cost <= x:
        costs = eval(input(f'Enter food cost for day {f_cost}: $ '))
        if costs <= 0:
            costs = eval(input(f'Enter food cost for day {f_cost}: $ '))
        else:
            food.append(costs)
            f_cost = f_cost + 1
 
    #prompt daily gas cost
    gas = []
    g_cost = 1
    while g_cost <= x:
        costs = eval(input(f'Enter gas cost for day {g_cost}: $ '))
        if costs <= 0:
            costs = eval(input(f'Enter gas cost for day {g_cost}: $ '))
        else:
            gas.append(costs)
            g_cost = g_cost + 1
    return (tot_people, tot_days, food, gas)

#calculation function
def CalcInputs(tot_people,tot_days,food,gas):
    #food_gas totals
    tot_food = sum(food)
    tot_gas = sum(gas)

    #total trip cost
    tot_trip = (tot_food + tot_gas)

    #share per person
    per_person = (tot_trip / tot_people)

    return (tot_food, tot_gas, tot_trip, per_person)

#display calculations
def DisplayCalcs(tot_food, tot_gas, tot_trip, per_person):

    print('\n\nTrip Summary:\n')
    print(f'Food total: ${tot_food:.2f} USD')
    print(f'Gas total: ${tot_gas:.2f} USD')
    print(f'Trip total: ${tot_trip:.2f} USD\n')
    print(f'Cost per person: ${per_person:.2f} USD') 
        

def main():

    Welcome()
    tot_people, tot_days, food, gas = Inputs()
    tot_food, tot_gas, tot_trip, per_person = CalcInputs(tot_people,tot_days,food,gas)
    DisplayCalcs(tot_food, tot_gas, tot_trip, per_person)

main()
    
        
            
        
    
    
