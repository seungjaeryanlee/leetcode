class Solution1:
    """
    Naive DFS. Time limit exceeds.
    """
    def update_mins(self, mins: list[int], new: int):
        if new < mins[0]:
            if mins[0] < mins[1]:
                return [new, mins[0]]
            else:
                return [new, mins[1]]
        elif new < mins[1]:
            if mins[1] < mins[0]:
                return [new, mins[1]]
            else:
                return [new, mins[0]]
        
        return mins

    def recursion(self, coins: list[list[int]], current_money: int, i: int, j: int, mins: lint[int]) -> int:
        coin = coins[i][j]
        # print((i, j), current_money, mins, current_money + coin - mins[0] - mins[1])
        if i == len(coins) - 1 and j == len(coins[0]) - 1:
            new_mins = self.update_mins(mins, coin)
            return current_money + coin - new_mins[0] - new_mins[1]

        new_mins = self.update_mins(mins, coin)
        if i == len(coins) - 1:
            return self.recursion(coins, current_money + coin, i, j+1, new_mins)
        if j == len(coins[0]) - 1:
            return self.recursion(coins, current_money + coin, i+1, j, new_mins)

        return max(
            self.recursion(coins, current_money + coin, i+1, j, new_mins),
            self.recursion(coins, current_money + coin, i, j+1, new_mins),
        )

    def maximumAmount(self, coins: list[list[int]]) -> int:
        if len(coins) == 1 and len(coins[0]) == 1:
            return coins[0][0] if coins[0][0] > 0 else 0

        return self.recursion(coins, 0, 0, 0, [0, 0])

# -----

from dataclasses import dataclass

def update_mins(mins: list[int], new: int) -> list[int]:
    if new < mins[0]:
        if mins[0] < mins[1]:
            return [new, mins[0]]
        else:
            return [new, mins[1]]
    elif new < mins[1]:
        if mins[1] < mins[0]:
            return [new, mins[1]]
        else:
            return [new, mins[0]]
    
    return mins

@dataclass
class State:
    current_money: int
    mins: list[int]

    def update_state(self, coin: int) -> State:
        return State(
            self.current_money + coin,
            update_mins(self.mins, coin),
        )
    
    def profit(self) -> int:
        return self.current_money - self.mins[0] - self.mins[1]

class Solution2:
    """
    Wrong greedy approach.
    """
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])

        if m == 1 and n == 1:
            return coins[0][0] if coins[0][0] > 0 else 0

        states = [[None] * n for _ in range(m)]
        states[0][0] = State(0, [0, 0])
        for k in range(m+n):
            for i in range(k+1):
                j = k - i
                if not (0 <= i < m) or not (0 <= j < n):
                    continue
                # print(i, j)

                # Check up
                if i > 0:
                    state_from_up = states[i-1][j].update_state(coins[i-1][j])
                    if states[i][j] is None or states[i][j].profit() < state_from_up.profit():
                        states[i][j] = state_from_up

                # Check left
                if j > 0:
                    state_from_left = states[i][j-1].update_state(coins[i][j-1])
                    if states[i][j] is None or states[i][j].profit() < state_from_left.profit():
                        states[i][j] = state_from_left
                
                print(i, j, states[i][j])

        return states[-1][-1].update_state(coins[-1][-1]).profit()

# -----

from dataclasses import dataclass

@dataclass
class State:
    profit_with_0_neut: int
    profit_with_1_neut: int
    profit_with_2_neut: int

    def update_state(self, coin: int) -> State:
        return State(
            self.profit_with_0_neut + coin,
            max(self.profit_with_1_neut + coin, self.profit_with_0_neut),
            max(self.profit_with_2_neut + coin, self.profit_with_1_neut),
        )
    
    def merge_state(self, other):
        self.profit_with_0_neut = max(self.profit_with_0_neut, other.profit_with_0_neut)
        self.profit_with_1_neut = max(self.profit_with_1_neut, other.profit_with_1_neut)
        self.profit_with_2_neut = max(self.profit_with_2_neut, other.profit_with_2_neut)

    def profit(self):
        return max(
            self.profit_with_0_neut,
            self.profit_with_1_neut,
            self.profit_with_2_neut,
        )

class Solution3:
    """
    Correct solution.
    """
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])

        if m == 1 and n == 1:
            return coins[0][0] if coins[0][0] > 0 else 0

        states = [[None] * n for _ in range(m)]
        states[0][0] = State(0, 0, 0)
        for k in range(m+n):
            for i in range(k+1):
                j = k - i
                if not (0 <= i < m) or not (0 <= j < n):
                    continue

                # Check up
                if i > 0:
                    state_from_up = states[i-1][j].update_state(coins[i-1][j])
                    if states[i][j] is None:
                        states[i][j] = state_from_up
                    else:
                        states[i][j].merge_state(state_from_up)

                # Check left
                if j > 0:
                    state_from_left = states[i][j-1].update_state(coins[i][j-1])
                    if states[i][j] is None:
                        states[i][j] = state_from_left
                    else:
                        states[i][j].merge_state(state_from_left)
                
                # print(i, j, states[i][j])

        return states[-1][-1].update_state(coins[-1][-1]).profit()
