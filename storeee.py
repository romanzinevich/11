class Product():
    def __init__(self, title, count, price):  #создал класс продукты
        self.title = title
        self.price = price
        self.count = count

class Store():
    all_products=[]
    def add_products(self):
        print('Хотите добавить уже существующие продукты?')  #создал класс магазин, в котором есть список,
        answer2 = input()                                    # который хранит продукты и метод, который их
        if answer2 == 'да':                                  #добавляет
            print('Введите название продукта')
            title99 = input()
            print('Введите количество продукта')
            count99 = input()

            for i in allproducts:

                if title99 == i.title:
                    product1.count = int(product1.count) + int(count99)
                else:
                    print('Такого продукта не существует')



class Manager():                                      #класс менеджер только создает новые продукты
    def create_product(self):
        answer1 = 'да'
        while answer1 == 'да':
            print('Хотите создать новый продукт?')
            answer1 = input()
            if answer1 == 'да':
                print('Введите название продукта')
                product1title = input()
                print('Введите количество продукта')
                product1count = input()
                print('Введите цену продукта')
                product1price = input()
                product1price = int(product1price)
                while product1price > 1000:
                    print('Это дорого, желаете поменять цену?')
                    newanswer = input()
                    if newanswer == 'нет':
                        print('Ваша цена сохранена')
                        break
                    else:
                        print('Введите цену продукта')
                        product1price = input()
                        product1price = int(product1price)
                product1 = Product(product1title, product1count, product1price)
                allproducts.append(product1)
                print('Продукт успешно создан')

        else allproducts.add_products():                 #здесь у меня затуп, я не могу вызвать метод, который добавляет продукты