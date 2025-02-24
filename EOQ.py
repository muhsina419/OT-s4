import math

def calculate_eoq(annual_demand, ordering_cost, holding_cost):
    """
    Calculates the Economic Order Quantity (EOQ).
    :param annual_demand: Annual demand for the product (D)
    :param ordering_cost: Ordering cost per order (S)
    :param holding_cost: Holding cost per unit per year (H)
    :return: EOQ (optimal order quantity)
    """
    eoq = math.sqrt((2 * annual_demand * ordering_cost) / holding_cost)
    return eoq

# Given company data
annual_demand = 10000  # D
ordering_cost = 200     # S
holding_cost = 5        # H

# Calculate EOQ
eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)

# Print the result
print(f"The Economic Order Quantity (EOQ) is: {eoq:.2f}")
