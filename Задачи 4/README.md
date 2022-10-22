# 4_1


___
```
###На вход поступает целое число, вернуть true, если число является целым палиндромом. Целое число является палиндромом, если оно читается так же, как в прямом, так и в обратном порядке.
```
# Листинг 4_1
___
```py
def main()
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
    
    
if __name__=='__main__':
    main()
```
### Мой результат выполнения программы
```
Input: 121
Output: True
Input: 123
Output: False
```
##Мое пояснение к программе
### Программа определяет ,является ли число палиндромом и выводит соответствующий результат('True' or 'False').
