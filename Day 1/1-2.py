def main():
    f = open('1-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    total = 0
    for line in lines:
        num = int(line)
        while num > 0:
            total += num
            num = (num // 3) - 2
        total -= int(line)

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 4891620
