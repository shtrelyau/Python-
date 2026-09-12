def add_visitor(visitors): #функция добавления посетителя
    name = input("Введите имя: ")
    
    age = int(input("Введите возраст: "))
    if age < 0 or age > 117:
        print("ОШИБКА! Возраст должен быть от 0 до 117!")
        return
    
    city = input("Введите город: ")
    
    ticket = input("Введите категорию билета: ")
    
    visitor = {       #(множество)словарь с (элементами)данными посетителя
        "name": name,
        "age": age,
        "city": city,
        "ticket": ticket
    }
    visitors.append(visitor)
    print(f"Посетитель {name} добавлен!")


def show_visitors(visitors): #вывод всех посетителей
    if not visitors:
        print("Список пуст!")
        return
    
   
    for index, visitor in enumerate(visitors, start=1): #enumerate даёт номер и элемент, начиная с 1

        print(f"{index}. {visitor['name']} | Возраст: {visitor['age']} | "
              f"Город: {visitor['city']} | Билет: {visitor['ticket']}")


def find_city(visitors): #поиск по городу
    city = input("Введите город для поиска: ").strip() #strip убирает пробелы
    
    result = [] #список подходящих посетителей
    for v in visitors: 
        if v["city"].lower() == city.lower(): #совпадает ли город посетителя с введнным
            result.append(v)         #lower-нижний регистр
    
    if not result:
        print(f"\n--- Посетители из города {city} не найдены. ---")
        return
    
    print(f"\n--- Найдены посетители из города {city}: ---")
    for visitor in result:
        print(f"{visitor['name']} | Возраст: {visitor['age']} | Билет: {visitor['ticket']}")


def filter_age(visitors):  #фильтр по возрасту
    limit = int(input("Введите минимальный возраст: "))
    
    result = [v for v in visitors if v["age"] >= limit] #новый список с посетителями >=мин.возрасту
    
    if not result:
        print(f"Нет посетителей с возрастом >= {limit}")
        return
    
    print(f"\n--- Посетители с возрастом >= {limit} ---")
    for visitor in result:
        print(f"{visitor['name']} | Возраст: {visitor['age']} | Город: {visitor['city']}")


def sort_age(visitors): #сортировка по возрасту
    if not visitors:
        print("Список пуст!")
        return
    
    result = sorted(visitors, key=lambda v: v["age"]) #сортировка по возрасту от меньшего к большему
    #sorted возвращает новый отсортированный список не меняя исходный, l-возьми верни
    print("\n--- Посетители, отсортированные по возрасту ---")

    for index, visitor in enumerate(result, start=1):
        print(f"{index}. {visitor['name']} | Возраст: {visitor['age']} | Город: {visitor['city']}")


def show_stats(visitors): #статистика
    if not visitors:
        print("Список пуст!")
        return
    
    ages = [v["age"] for v in visitors] #список всех возрастов
    
    average = sum(ages) / len(ages)
    
    youngest = min(visitors, key=lambda v: v["age"]) #самый маленький посетитель
    
    oldest = max(visitors, key=lambda v: v["age"]) #самый взрослый
    
    cities_count = len({v["city"] for v in visitors}) #{множество} кол-во(len) уникальных городов
    
    print("\n~~~ Статистика ~~~")
    print(f"Всего посетителей: {len(visitors)}") 
    print(f"Средний возраст: {average:.2f}") #до 2 знаков, после запятой
    print(f"Самый молодой: {youngest['name']} ({youngest['age']})")
    print(f"Самый взрослый: {oldest['name']} ({oldest['age']})")
    print(f"Уникальных городов: {cities_count}")


def show_unique(visitors): #функция уникальных значений
    if not visitors:
        print("Список пуст!")
        return
    
    cities = {v["city"] for v in visitors} #множество городов
    
    tickets = {v["ticket"] for v in visitors} #множество билетов
    
    print("\n~~~ Уникальные значения ~~~")
    print(f"Города ({len(cities)}): {', '.join(sorted(cities))}") #города через , с указанием кол-ва
    print(f"Категории билетов ({len(tickets)}): {', '.join(sorted(tickets))}")


def count_by_city(visitors): #группировка по городам
    if not visitors:
        print("Список пуст!")
        return
    
    groups = {} #словарь для группировки
    for visitor in visitors:
        city = visitor["city"]
        if city not in groups:
            groups[city] = [] #добавляем в словарь новый город и пустой список в качестве значения
        groups[city].append(visitor["name"])
        #добавка имени посетителя в список, соответст городу 
    
    print("\n~~~ Группировка по городам ~~~")
    for city, names in groups.items(): #перебор пары ключ-значение
        print(f"{city} ({len(names)}): {', '.join(names)}") #город, количество имён и список имён чз ,


def menu():
    print("\n===== МЕНЮ =====")
    print("1. Добавить посетителя")
    print("2. Показать всех")
    print("3. Найти по городу")
    print("4. Фильтр по возрасту")
    print("5. Сортировка по возрасту")
    print("6. Статистика")
    print("7. Уникальные значения")
    print("8. Группировка по городам")
    print("0. Выход")


def main():
    visitors = [] #список посетителей
    
    while True:
        menu()
        choice = input("Выберите действие: ").strip() #strip убирает лишние пробелы
        
        if choice == "1":
            add_visitor(visitors)
        elif choice == "2":
            show_visitors(visitors)
        elif choice == "3":
            find_city(visitors)
        elif choice == "4":
            filter_age(visitors)
        elif choice == "5":
            sort_age(visitors)
        elif choice == "6":
            show_stats(visitors)
        elif choice == "7":
            show_unique(visitors)
        elif choice == "8":
            count_by_city(visitors)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()