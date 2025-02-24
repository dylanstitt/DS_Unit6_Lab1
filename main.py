# Dylan Stitt
# Unit 6 Lab 1
# Recursion Review

from random import randint
import os

def createIntList():
    return [randint(5, 20) for i in range(randint(5, 20))]

def recursiveSum(n):
    if len(n) == 1:
        return n[0]

    return n[0] + recursiveSum(n[1:])

def main():
    l1 = createIntList()
    l2 = createIntList()
    l3 = createIntList()

    sum1 = recursiveSum(l1)
    sum2 = recursiveSum(l2)
    sum3 = recursiveSum(l3)

    print(f'Int List: {l1} = {sum1}')
    print(f'Int List: {l2} = {sum2}')
    print(f'Int List: {l3} = {sum3}')

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
