def main():
    f = open('1-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    total = 0
    for line in lines:
        total += (int(line) // 3) - 2

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 3262991
