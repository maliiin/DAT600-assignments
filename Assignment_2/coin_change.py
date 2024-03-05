import copy


def greedy_coin_change(c, N):
    c.sort(reverse=True)
    selected_coins = []
    for coin in c:
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


def compare_greedy_dynamic(c, n):
    similarity_count = 0
    for i in range(1, n + 1):
        greedy = greedy_coin_change(c, i)
        dynamic = dynamic_coin_change(c, i)
        greedy.sort()
        dynamic.sort()
        if dynamic == greedy:
            similarity_count += 1
    return similarity_count


print(greedy_coin_change([5, 1, 11], 15))
print(dynamic_coin_change([1, 5, 11], 15))
print()
print(dynamic_coin_change([1, 2, 8, 9], 73))
print(greedy_coin_change([1, 2, 8, 9], 73))
print()

# norwegian coins
print(dynamic_coin_change([1, 5, 10, 20], 101))
print(greedy_coin_change([1, 5, 10, 20], 101))


similarity1 = compare_greedy_dynamic([1, 5, 11], 1000)
similarity2 = compare_greedy_dynamic([1, 5, 10, 20], 1000)
print(similarity1)
print(similarity2)
