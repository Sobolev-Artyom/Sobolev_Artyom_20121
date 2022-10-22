
val = input()
num_list = list(map(int, val))
is_polindrom = True

size = int(len(num_list))
for i in range(0, int(size / 2)):
    if num_list[i] != num_list[size - i-1]:
        is_polindrom = False
        break

if is_polindrom:
    print("True")
else:
    print("False")
