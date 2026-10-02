def lvl_1(method,text):
    if method == "upper":
        return text.upper()
    elif method =="lower":
        return text.lower()
    elif method =="capitalize":
        return text.capitalize()
        
def lvl_2(method,text):
    if method == "find":
        print ('Напишите слово,индекс которого хотите найти')
        wrd = input()
        return text.find(word)
    elif  method == "replace":
        print ('Напишите слово, которое хотите заменить')
        wrd1 = input()
        print ('Напишите слово для замены')
        wrd2 = input()
        return text.replace(wrd1,wrd2)
    elif method == "count":
        print ('Напишите слово или строку,количество которых хотите посчитать')
        wrd = input()
        return text.count(wrd)
        
        
def lvl_3(method,text):
    if method == "split":
        print ("Напишите символ,по которому делится строка")
        sym1 = input()
        print ("Напишите символ, на который заменить предыдущий символ")
        sum2 = input()
        return sum2.join(text.split(sum1))
    elif method == "join":
        print ("Напишите символ,по которому делятся элементы списка")
        sum = input()
        return sum.join(text.split(','))
        
        
        
def lvl_4(method, text):
    if method == "isdigit":
        return text.isdigit()
    elif method == "isalpha":
        return text.isalpha()
    elif method == "strip":
        print ("Напишите символы, которые хотите удалить")
        sum = input()
        return text.strip(sum)
        
        
while True:
    print ("Выберите уровень (1,2,3,4,5)")
    lvl = int(input())
    if lvl == 1:
        test = "пРиВет МИР"
        print ("Метод upper: пРиВет МИР - ",test.upper())
        print ("Метод lower: пРиВет МИР - ",test.lower())
        print ("Метод capitalize: пРиВет МИР - ",test.capitalize())
        print("Выберите медот: upper, lower, capitalize")
        method = input()
        print (lvl_1(method,text))
    if lvl == 2:
        test = "Ботать это круто. Очень круто"
        print (f"Тестовая строка - {test}")
        print ("метод find ( ищем индекс первого вхождения слова 'круто') - ", test.find("круто"))
        print ("метод replace (замена слова 'круто' на слово 'некруто') - ", test.replace("круто", "не круто"))
        print ("метод count ( считаем количество букв 'о') - ", test.count("о"))
        print ("выберите метод(find,replace,count)")
        method = input()
        print ("Напишите свой текст")
        text = input()
        print(lvl_2(method,text))
    if lvl == 3:
        test = "1,2,3,4"
        print (f"Текстовая строка - {test}")
        print ("Метод split (делим строку по запятым)", test.split(","))
        print ("Метод split+join(разделяем строку пробелами)"," ".join(test.split(",")))
        print ("Метод join(разделяем список символами'!'):", '!'.join(test.split(",")))
        print (" Выберите метод (split,split+join,join)")
        method = input()
        print ("Напишите свой текст")
        text = input()
        print (lvl_3(method,text))
    if lvl == 4:
        test1 = "1,2,3,4*&%$"
        test2 ="   abc1234   "
        print (f"Текстовые строки - '{test1}' '{test2}'")
        print ("Метод isdigit (проверяет все ли символы в строке являются цифрами):", test1.isdigit(), test2.isdigit())
        print ("Метод isalpha (проверяет все ли символы в строке являются буквами):", test1.isalpha(), test2.isalpha())
        print ("Метод strip( убирает символы в начаок и в конце строки):", test1.strip(), test2.strip())
        print (" Выберите метод (isdigit,isalpha,strip)")
        method = input()
        print ("Напишите свой текст")
        text = input()
        print (lvl_4(method,text))  
    if lvl == 5:
        test = '       pYtHon;is;AWESome;       '
        test = test.strip()
        test = " ".join(test.split(";"))
        test = test.lower()
        print (test.capitalize())
