class Payment: #базовый класс для всех платежей
    def __init__(self, amount, payer): #конструктор — вызывается при создании объекта
        self.amount = amount #сумма платежа
        self.payer = payer #плательщик
        self._status = "ожидает" #статус платежа (инкапсуляция)
    
    @property
    def status(self): #property — доступ к защищённому атрибуту
        return self._status
    
    @status.setter   #установка значения с проверкой
    def status(self, value):
        allowed = ["ожидает", "выполнен", "отклонён"] #допустимые статусы
        if value not in allowed: #значение не из списка
            raise ValueError("Недопустимый статус платежа!")
        self._status = value #новое значение
    
    def process(self): #общий метод обработки платежа (будет переопределён)
        return 0  #комисия 0
    
    def get_info(self): #получение инфы (полиморфизм)
        return f"Платёж на {self.amount} руб. от {self.payer}" #возврат строку с информацией
    
    def __str__(self): #спец метод — строковое представление объекта
        return f"{self.get_info()} | Статус: {self.status}" #возв описание платежа


class CardPayment(Payment): #производный класс — платёж картой (наследование)
    def __init__(self, amount, payer, card_number): #конструктор 
        super().__init__(amount, payer) #вызов конструктора родителя (super)
        self.card_number = card_number #номер карты
    
    def process(self): #переопределение метода process (полиморфизм)
        commission = self.amount * 0.02 #комиссия 2% от суммы
        self.status = "выполнен" #замена статуса
        return commission
    
    def get_info(self): #переопределение метода get_info
        return f"Карточный платёж на {self.amount} руб. (карта {self.card_number})"


class CashPayment(Payment): #производный класс — наличный платёж
    def __init__(self, amount, payer):
        super().__init__(amount, payer)
    
    def process(self):
        commission = 0 #комиссия отсутствует
        self.status = "выполнен"
        return commission
    
    def get_info(self):
        return f"Наличный платёж на {self.amount} руб."


class PaymentSystem: #класс-композиция — содержит список платежей (HAS-A)
    def __init__(self):
        self.payments = [] #пустой список платежей (композиция)
    
    def add_payment(self, payment): #метод добавления платежа
        self.payments.append(payment)  #добавляем объект в список
        print("Платёж добавлен!")
    
    def show_all(self): #вывод всех платежей
        if not self.payments:
            print("Платежей нет!")
            return
        for index, payment in enumerate(self.payments, start=1): #перебираем с номером
            print(f"{index}. {payment}")  #выводим объект (через __str__)
    
    def process_all(self): #обработка всех платежей (полиморфизм)
        if not self.payments:
            print("Платежей нет!")
            return
        total_commission = 0  #сумма всех комиссий
        for payment in self.payments:
            commission = payment.process() #вывов общего метода
            total_commission += commission
            print(f"{payment.get_info()} — комиссия: {commission:.2f} руб.")
        print(f"Общая комиссия: {total_commission:.2f} руб.")
    
    def show_stats(self): #статистика
        if not self.payments:
            print("Платежей нет!")
            return
        total = sum(p.amount for p in self.payments) #общая сумма через генератор
        average = total / len(self.payments) #средняя сумма
        maximum = max(self.payments, key=lambda p: p.amount) 
        minimum = min(self.payments, key=lambda p: p.amount)
        print(f"Всего платежей: {len(self.payments)}")
        print(f"Общая сумма: {total:.2f} руб.")
        print(f"Средний платёж: {average:.2f} руб.")
        print(f"Максимальный: {maximum.amount:.2f} руб. ({maximum.payer})")
        print(f"Минимальный: {minimum.amount:.2f} руб. ({minimum.payer})")
    
def menu(): #ф-я
    print("\n===== МЕНЮ =====")
    print("1. Добавить карточный платёж")
    print("2. Добавить наличный платёж")
    print("3. Показать все платежи")
    print("4. Обработать все платежи")
    print("5. Статистика")
    print("0. Выход")


def main():
    system = PaymentSystem() #создаём платёжную систему
    
    while True:
        menu()
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            amount = float(input("Введите сумму: "))
            payer = input("Введите плательщика: ")
            card = input("Введите номер карты: ")
            system.add_payment(CardPayment(amount, payer, card)) #создаём и добавляем
        elif choice == "2":
            amount = float(input("Введите сумму: "))
            payer = input("Введите плательщика: ")
            system.add_payment(CashPayment(amount, payer))
        elif choice == "3":
            system.show_all()
        elif choice == "4":
            system.process_all()
        elif choice == "5":
            system.show_stats()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()