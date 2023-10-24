def print_mas(mas,a,b): # вывод двумерного массива на экран 
    for i in range(0,a):
        for j in range(0,b):
            print(mas[i][j],end=" ")
        print("\n")

def symb_compare(str1,str2): #просто посимвольное сравнение двух строк
    num=abs(len(str1)-len(str2))
    if len(str1)>len(str2):
        for i in range(0,len(str2)):
            if str1[i]!=str2[i]:
                num+=1
        return num
    else:
        for i in range(0,len(str1)):
            if str1[i]!=str2[i]:
                num+=1
        return num    
    
def levenshtein_distance(s, t): # расстояние Левенштейна по алгоритму
    m = len(s)
    n = len(t)
    d = [[0] * (n + 1) for i in range(m + 1)] 
    for i in range(1, m + 1):
        d[i][0] = i
    for j in range(1, n + 1):
        d[0][j] = j
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,      # удаление
                          d[i][j - 1] + 1,      # вставка
                          d[i - 1][j - 1] + cost) # замена  
    return d[m][n]

str1 = input()
str2 = input()
print(symb_compare(str1,str2))
print(levenshtein_distance(str1,str2))