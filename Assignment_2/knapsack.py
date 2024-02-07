def knapsack_fractions(units, capacity):
    value_per_weight_list = []
    units_used = []
    tot_value = 0
    for weight, value in units:
        value_per_weight = value / weight
        value_per_weight_list.append((value_per_weight,weight, value))
    value_per_weight_list.sort(reverse=True)
    for value_per_weight, weight, value in value_per_weight_list:
        if capacity > 0:
            if weight <= capacity:
                capacity -= weight
                tot_value += value_per_weight * weight
                units_used.append((value, weight))
            else:
                tot_value += value_per_weight * capacity
                units_used.append((value, capacity))
                capacity = 0
    return tot_value, units_used


def knapsack_0_1(units, capacity):
    n = len(units)
    
    table = []

    # Create a table with items rows and capacity columns
    for _ in range(n + 1):
        inner_list = [0] * (capacity + 1)
        table.append(inner_list)

    # Fills the table, adds base case where there are no items
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            weight, value = units[i - 1]
            if weight > w:
                #If weight is greater than capacity, set the value to the value of the previous item
                table[i][w] = table[i - 1][w]   
            else:
                #Set the value to the maximum of the previous item or the current item plus the value of the previous item
                table[i][w] = max(table[i - 1][w], value + table[i - 1][w - weight]) #https://www.youtube.com/watch?v=nLmhmB6NzcM
    return table[n][capacity]

if __name__ == "__main__":
    #(kg, price)
    units = [(10, 60), (20, 100), (30,120)]
    capacity = 50
    print(knapsack_fractions(units, capacity))
    print(knapsack_0_1(units, capacity))