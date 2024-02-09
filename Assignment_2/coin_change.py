import copy


def greedy_coin_change(c, N):
    selected_coins = []
    for coin in reversed(c):
        while coin <= N:
            selected_coins.append(coin)
            N -= coin
        if N == 0:
            break
    return selected_coins


def dynamic_coin_change(c, N):
    # make solution for all subproblems <=N
    subproblems = []
    for n in range(1, N + 1):
        # amount of coins in best solution
        best_amount = float("inf")
        # actual coins to get best solution
        best_coins = []

        for coin in c:
            # check if coin is a possible solution
            if coin <= n:
                remainder = n - coin
                if remainder > 0:
                    # add coin to a solution for a subproblem that is already solve
                    this_solution = copy.deepcopy(subproblems[remainder - 1])
                    this_solution.append(coin)
                else:
                    this_solution = [coin]
                # check if this solution is best
                if len(this_solution) < best_amount:
                    best_coins = this_solution
                    best_amount = len(this_solution)
        subproblems.append(best_coins)

    return subproblems[N - 1]


# print(greedy_coin_change([1, 3, 4], 6))
print(dynamic_coin_change([1, 5, 11], 15))
print()
print(dynamic_coin_change([1, 2, 8], 13))
print(greedy_coin_change([1, 2, 8], 13))
print()

# norwegian coins
print(dynamic_coin_change([1, 5, 10, 20], 101))
print(greedy_coin_change([1, 5, 10, 20], 101))
