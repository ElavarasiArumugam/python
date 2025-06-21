
print("Welcome to coffee machine maker")
menu = {
          "espresso": {
              "ingredients":{
                  "water":50,
                  "coffee":20,
                  "milk": 10
              },
               "cost":2.5
          },
          "latte":{
              "ingredients":{
                  "water":50,
                  "coffee":35,
                  "milk":100
              },
              "cost":3.5
          },
          "cappuccino":{
              "ingredients":
              {
                  "water":45,
                  "coffee":45,
                  "milk":100
                  
              },
              "cost":4.5
          }
}
resources = {
    "water":300,
    "milk":200,
    "coffee":100
}
coins = {
          "penny":0.01,
          "nickel":0.05,
          "dime":0.10,
          "quarter":0.25,
     
        }
def get_coins():
     penny_number = int(input("How many number of penny coins?"))
     nickel_number= int(input("How many number of nickel coins?"))
     dime_number = int(input("How many number of dime coins?"))
     quarter_number = int(input("How many number of quarter coins? "))
     return (penny_number*coins["penny"] + nickel_number*0.05 + dime_number*0.10 + quarter_number*0.25)
    
def is_resource_sufficient(coffee_type):
    ingredients = menu[coffee_type]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, not enough {item}. We don't have sufficient resources to make your coffee.\n")
            return False
    return True

def print_report():
    print("\nCurrent Resource Report:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\n")
   

while True:
    coffee = input("what would you like to drink?(cappuccino/latte/espresso) or type 'report' ").lower()
    if coffee == "report":
        print_report()
        continue
    elif coffee not in menu:
        print("you entered an unavailable coffee.Thank you!")
        break
    elif coffee == "off":
       print("Machine is shutting down. GoodBye!")
       break
    if not is_resource_sufficient(coffee): 
        continue
    total_amount = get_coins()
    cost = menu[coffee]["cost"]
    
    if total_amount >= cost:
        print(f"Your coffee cost is ${cost:.2f}. You paid ${total_amount:.2f}.")
        change = total_amount - cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        
        # Deduct used resources
        for item in resources:
            resources[item] -= menu[coffee]["ingredients"].get(item, 0)
        
        print("Enjoy your coffee! ☕")
        print_report()
        
    else:
        print("Insufficient balance. Money refunded.\n")  