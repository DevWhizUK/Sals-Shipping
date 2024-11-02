# Sal's Shipping

Sal's Shippers is the largest shipping company in the tri-county area, dedicated to providing affordable and reliable shipping options to customers. In this project, you’ll develop a Python program that calculates the cheapest shipping option for a given package weight.

## Project Overview

This program helps customers find the most affordable shipping method offered by Sal’s Shippers based on the weight of their package. Sal’s Shippers offers three shipping options:

1. **Ground Shipping** - Includes a flat charge plus a weight-based rate.
2. **Ground Shipping Premium** - A single flat charge with no weight-based rate.
3. **Drone Shipping** - No flat charge, but the weight-based rate is triple that of ground shipping.

The program will prompt the user to enter the package weight and will return the cheapest shipping option and its cost.

## Shipping Options and Pricing

### Ground Shipping

| Weight of Package                         | Price per Pound | Flat Charge |
|-------------------------------------------|-----------------|-------------|
| 2 lb or less                              | $1.50          | $20.00      |
| Over 2 lb but less than or equal to 6 lb  | $3.00          | $20.00      |
| Over 6 lb but less than or equal to 10 lb | $4.00          | $20.00      |
| Over 10 lb                                | $4.75          | $20.00      |

### Ground Shipping Premium

- **Flat charge**: $125.00 (no weight-based rate)

### Drone Shipping

| Weight of Package                         | Price per Pound | Flat Charge |
|-------------------------------------------|-----------------|-------------|
| 2 lb or less                              | $4.50          | $0.00       |
| Over 2 lb but less than or equal to 6 lb  | $9.00          | $0.00       |
| Over 6 lb but less than or equal to 10 lb | $12.00         | $0.00       |
| Over 10 lb                                | $14.25         | $0.00       |

## Features

- Prompts the user to input the package weight.
- Calculates the cost of shipping using each method.
- Determines and displays the cheapest shipping option and its total cost.

## Usage

Upon running, the program will ask for the weight of your package. After entering the weight, it will display the cheapest shipping option and the corresponding cost.

Example:
```plaintext
Enter the weight of the package: 8
The cheapest shipping method is Ground Shipping, costing $52.00.
