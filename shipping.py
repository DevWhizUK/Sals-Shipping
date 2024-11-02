# ground shipping 

def ground_shipping(weight):
    if weight <= 2:
        ground_cost = (weight * 1.50) + 20
    elif weight <= 6:
        ground_cost = (weight * 3) + 20
    elif weight <= 10:
        ground_cost = (weight * 4) + 20
    else:
        ground_cost = (weight * 4.75) + 20
    
    print(f"Ground Shipping Costs: ${ground_cost:.2f}")
    return ground_cost

# premium ground shipping

premium_ground_shipping = 125


# drone shipping

def drone_shipping(weight):
    if weight <= 2:
        drone_cost = weight * 4.50
    elif weight <= 6:
        drone_cost = weight * 9
    elif weight <= 10:
        drone_cost = weight * 12
    else:
        drone_cost = weight * 14.25
    
    print(f"Drone Shipping Costs: ${drone_cost:.2f}")
    return drone_cost

weight = float(input("Enter the weight in lbs: "))

ground_shipping(weight)
print(f"Premium Ground Costs: ${premium_ground_shipping:.2f}")
drone_shipping(weight)