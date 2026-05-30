def display(state: list) -> None:
    for row in state:

        for box in row:
            print(box, end=' ')

        print() # New Line

if __name__ == '__main__':
    display([['#', '#', '#'],
            ['#', '#', '#'],
            ['#', '#', '#']])

