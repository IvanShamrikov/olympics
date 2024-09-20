# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
# You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

# Example 2:

# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

def canCompleteCircuit(gas, cost):
    sum_cost = sum(cost)
    sum_gas = sum(gas)
    print(f"Сумарна к-сть бензину на заправках = {sum_gas}, сумарка к-сть бензину шоб проїхати всі відрізки = {sum_cost}")
    if sum_cost > sum_gas:
        print("Задача не є рішабельною, бо потреба в бензині більша за сумарний бензин, який ми можемо купити на всіх заправках")
        return -1

    current_gas = 0
    starting_index = 0

    print("Переберемо всі станції і спробуємо зробити вояж, починаючи з кожної")
    for i in range(len(gas)):
        print(f"Ми на заправці під індексом {i}. В нас в баку {current_gas}л, заправляємось на {gas[i]}л, витрачаємо до наступної заправки {cost[i]}л.")
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            print(f"Бензину не вистачило, тож стпробуємо стартанути заново з заправки під індексом {i + 1}")
            current_gas = 0
            starting_index = i + 1
    print("Заправка, з якої треба починати вояж = індекс {starting_index}")
    return starting_index

print(canCompleteCircuit(gas, cost))