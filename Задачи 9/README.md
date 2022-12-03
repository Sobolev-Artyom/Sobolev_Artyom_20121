# Листинг 9_1
Вы санта. Вы попросили эльфа вернуть вам список пользователей, где каждый пользователь представляет собой еще один список, который содержит один или два элемента: строка (имя пользователя) и его почтовый индекс. Напишите функцию santa_users(), которая принимает двумерный список, и возвращает словарь с элементом для каждого пользователя, где ключ - это имя пользователя, а значение - почтовый индекс пользователя. Если нет индекса, тогда значение должно быть None.
 
```py
def main():
    spisok = [['oleg pushkin',89765],['kirill mendeleev',54378],['john kun'],['ivan popov',98745]]



    def santa_users(massive):
        bumagka = {}
        for place in massive:
            if len(place)==2:
                bumagka[place[0]] = place[1]
            else:
                bumagka[place[0]] = None
            return bumagka

    print(santa_users(spisok))

if __name__ == '__main__':
    main()
    
```
## Результат выполнения программы

____

# Листинг 9_2
## Римские цифры и их вывод.
```py
def main():
    roma_arab_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

    def from_roma_to_arab(string_number, roma_arab_dict):
        if len(string_number) > 15 and len(string_number) < 1:
            print("Некорректное количество символов")
            return False
        for symbol in string_number:
            if symbol not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                print("Некорректный символ")
                return False

        res_arab = 0
        for index, symbol in enumerate(string_number):
            if index == len(string_number)-1 or roma_arab_dict[symbol] >= roma_arab_dict[string_number[index+1]]:
                res_arab += roma_arab_dict[symbol]
            else:
                res_arab -= roma_arab_dict[symbol]
        return res_arab

    print(from_roma_to_arab('MCMXCIV', roma_arab_dict))


if __name__ =='__main__':
    main()
```    

## Результат выполнения программы
____

# Листинг 9_3
Напишите функцию get_pins(), которая принимает строку(предполагаемый PIN код) , и возвращает список строк с возможными вариантами. 
Ввод PIN кода производится с клавиатуры. 

```py

