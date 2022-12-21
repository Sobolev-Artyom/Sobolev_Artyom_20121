# Листинг 5_1
С клавиатуры поступает строка. Необходимо вывести самую длинную подстроку без повторных символов.

```py
def main():
    my_str = 'qweasdfdqw'

    def find_not_repeat(my_str):
        result = ''
        for symbol in my_str:
            if symbol not in result:
                result += symbol
            else:
                break
        return result

    all_variants = []
    for i in range(len(my_str)-1):
        all_variants.append(find_not_repeat(my_str[i:]))

    longest_str = sorted(all_variants, key=lambda x: len(x))[-1]
    print(longest_str)

if __name__ == '__main__':
    main()
```
## Результат выполнения программы:
Input: “qweasdfdqw”
Output: “qweasd”
____

# Листинг 5_2
. С клавиатуры поступает строка. Необходимо вывести строку, где порядок слов в противоположном направлении. Первое слово с заглавной буквы, остальные с маленькой. МЕЖДУ словами только ОДИН пробел.  
 ```py
 def main():
    my_str_1 = "it     waS     cool  "
    lst = [el for el in my_str_1.split(' ') if el != '']
    reverse_lst = [lst[i].lower() for i in range(len(lst)-1, -1, -1)]
    result = " ".join(reverse_lst).capitalize()
    print(result) 
if __name__ == '__main__':
    main()
```
## Результат выполнения программы:
Input: “  it       was     cool     ”
Output: “Cool was it”
____
# Листинг 5_3
С клавиатуры поступает строка, которая имеет только символы: '(', ')', '{', '}', '[' и ‘]’. Необходимо проверить правильно ли сформированы скобки. Если ВСЕ скобки сформированы правильно, то вывести True, если нет, то вывести самую длинную правильно сформированную подстроку скобок, если такой подстроки нету, то вывести False. (Сначала лучше сделать True и False, а потом работать с подстроками).
```py




