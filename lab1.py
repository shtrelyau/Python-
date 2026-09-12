def statistics(att, students): # статистика посещаемости 
    if not att:
        return 0, 0, 0, 0, 0, 0
    
    summa = 0 # вся посещаемость
    for i in att:
        summa += i

    count = len(att) # кол-во занятий всего (длина списка)
    ave_att = summa / count # ср посещаемость 
    maximum = max(att)   
    minimum = min(att)
 
    
    low_60 = 0  # счетчики для >60, <90 + переменная для %
    high_90 = 0
    percents = 0 
    
    for i in att:
        percent = (i / students) * 100 #присутствующие / всего
        percents += percent
        if percent < 60:
            low_60 += 1
        if percent > 90:
            high_90 += 1
    
    average = percents / count #средний процент 
    
    return ave_att, maximum, minimum, average, low_60, high_90 


def get_data(): #функция ввода данных
    students = int(input("Введите общее количество студентов: "))
    if students <= 0:
        print("Ошибочка! Количество студентов должно быть положительным!")
        return None, None, None #сигнал ошибки
    
    count = int(input("Введите количество занятий: "))
    if count <= 0:
        print("Ошибочка! Количество занятий должно быть положительным!")
        return None, None, None

    att = []
    for index in range(count): #цикл по занятиям
        i = int(input("Введите количество студентов на занятии " + str(index + 1) + ": "))
        if i < 0:
            print("Ошибочка! Количество не может быть отрицательным!")
            return None, None, None
        if i > students:
            print("На занятии не может быть больше " + str(students) + " студентов!")
            return None, None, None
        att.append(i) #вносим в список
    
    return att, students, count


def main():
    att, students, count = get_data() #вводим данные, если ошибка, выход
    if att is None:
        return
    
    ave_att, maximum, minimum, average, low, high = statistics(att, students) #расчитываем значения
    
    print("Всего занятий: " + str(count))
    print("Средняя посещаемость: " + str(ave_att))
    print("Максимальная посещаемость: " + str(maximum))
    print("Минимальная посещаемость: " + str(minimum))
    print("Средний процент: " + str(average))
    print("Занятий < 60%: " + str(low))
    print("Занятий > 90%: " + str(high))
    
    if average >= 80:
        print("Посещаемость высокая.")
    elif average >= 60:
        print("Посещаемость удовлетворительная.")
    else:
        print("Посещаемость низкая.")


if __name__ == "__main__": 
    main()
    
