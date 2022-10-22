def print_zigzag(string, k):
    if k == 0:
        return

    if k == 1:
        print(string)

    # Первая строка
    for i in range(0, len(string), (k - 1) * 2):
        print(string[i], end='')

    # Средние строки
    for i in range(1, k-1):
        is_down = True
        j = i
        while j < len(string):
            print(string[j], end="")
            space = 0
            if is_down:
                space = (k - i - 1) * 2
            else:
                space = (k - 1) * 2 - (k - i - 1) * 2
            j += space
            is_down = not is_down

    # Последняя строка
    for i in range(k-1, len(string), (k-1) * 2):
        print(string[i], end='')


string = input()
k = int(input())

print_zigzag(string, k)
