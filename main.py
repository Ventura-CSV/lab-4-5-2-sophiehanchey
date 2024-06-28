import random


def main():
    total = 0
    numbers = []
    lastnum = 0
    
    while total < 100:
        
        newnum = random.randint(0,100)
        
        numbers.append(newnum)
        total += newnum
        lastnum = newnum

    total -= lastnum

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
