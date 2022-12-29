# Листинг 10

Построить отрезок графика полученной функции (график 1) и выполнить
следующие пункты:
1. Вывести первую и вторую производную и построить их графики
(график 2 и 3)
2. Найти наибольшее и наименьшее значение функции на отрезке и
отобразить точкой (на графике 1)
3. Составить уравнение касательной и нормали к точке, а затем построить
их (на графике 1)
4. Построить касательное расслоение (график 4) (то есть касательные к
множеству точек кривой)
5. Найти длину кривой через интеграл

```py
def main():
    import matplotlib.pyplot as plt
    import math
    import numpy as np

    def f(x):
        return (2*math.pow(x, 2) -3*x+7)*math.cos(7+math.pow(x, 2)/2)
    def df_1(x):
        return ((-2*math.pow(x, 3))+3*math.pow(x, 2)-7*x)*math.sin(math.pow(x, 2)/2+7)+4*x*math.cos(math.pow(x, 2)/2+7)-3*math.cos(math.pow(x, 2)/2+7)
    def df_2(x):
        return (9*x-10*math.pow(x, 2))*math.sin(math.pow(x, 2)/2+7)-7*math.sin(math.pow(x, 2)/2+7)+((-2*math.pow(x, 4))+3*math.pow(x, 3)-7*math.pow(x, 2))*math.cos(math.pow(x, 2)/2+7)+4*math.cos(math.pow(x, 2)/2+7)
    def kasatel(x, x0):
        return f(x0)+df_1(x0)*(x-x0)
    def normal(x, x0):
        return f(x0)-((x-x0)/(df_1(x0)))    
    
    x = np.linspace(0, 5, 100000)
    y = [f(x_i) for x_i in x]
    dy1 = [df_1(x_i) for x_i in x]
    dy2 = [df_2(x_i) for x_i in x]

    x_max = 4.19958
    y_kas = [kasatel(x_i, x_max) for x_i in x]
    x_norm = np.linspace(4.19, 4.2, 10)
    y_norm = [normal(x_i, x_max) for x_i in np.linspace(4.19, 4.2, 10)]

    all_kas = []
    x_kas = np.linspace(3, 5, 10)
    for x_i in x_kas:
        one_kas = []
        for x_j in x_kas:
            kasatel(x_j, x_i)
            one_kas.append(kasatel(x_j, x_i))
        all_kas.append(one_kas)

    plt.figure(figsize=(10, 5))
    plt.plot(x,y);
    plt.grid()

    x_min, y_min = 4.19958, f(4.19958)
    x_max, y_max = 4.88546, f(4.88546)
    plt.plot([x_min], [y_min], 'o', color = 'b');
    plt.plot([x_max], [y_max], 'o', color = 'b');
    plt.plot(x, y_kas);
    plt.plot(x_norm, y_norm);    
    
    plt.figure(figsize=(10, 5))
    plt.plot(x,dy1);
    plt.grid()
    
    plt.figure(figsize=(10, 5))
    plt.plot(x,dy2);
    plt.grid()
    
    plt.figure(figsize=(10, 5))
    plt.plot(x,y, linestyle=":");
    plt.grid()
    plt.xlim((3,5))
    for kas in all_kas:
        plt.plot(x_kas, kas);


if __name__ == "__main__":
    main()    
```
## Графики
![image](https://user-images.githubusercontent.com/115024655/209986769-9619dded-b99c-40e8-bffb-3230ffc69f99.png)
![image](https://user-images.githubusercontent.com/115024655/209986803-2b5dba7a-dbdd-41f3-938d-920b56c6e866.png)
![image](https://user-images.githubusercontent.com/115024655/209986827-3be18709-5c66-412f-9954-7198beb834fb.png)
![image](https://user-images.githubusercontent.com/115024655/209986891-2bf0a5ca-698c-4b0a-8494-52217ed78842.png)


