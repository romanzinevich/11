class Product():
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Store():
    def __init__(self, product, count):
        self.all_products={}
    @staticmethod
    def add_products(self, product1, count1):
        self.product1=product1
        self.count=count1
        all_products[product1]=count1

    def _product_details(self, product):
        message_template = "Количество товара %s: %s штук, стоимость: %s. Суммарная стоимость: %s "

        count1 = self.all_products[product1]
        title1 = product1.title
        price1 = product1.price
        total_price = price1 * count1

        rendered_message = message_template % (product_title, product_count, product_price, product_total_price)

        return rendered_message

    def showcase(self, product=None):
        print(f"Отчет по магазину {self.title}:")
        if product:
            print(self._product_details(product1))
        else:
            for product in self.all_products.keys():
                print(self._product_details(product1))


class Manager():
    @staticmethod
    def create_product(self):
        answer1 = 'да'
        while answer1 == 'да':
            print('Хотите создать новый продукт?')
            answer1 = input()
            if answer1 == 'да':
                print('Введите название продукта')
                product1title = input()
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
                product1 = Product(product1title, product1price)
                print('Продукт успешно создан')
                print('Введите количество продута')
                product1count=input()
                product1.add_products(product1, int(product1count))
                print('Продукт '+product1title+' в колиечтве '+product1count+'  добавлен в магазин' )

    @staticmethod
    def changin_of_count():
        print('Хотите добавить уже существующие продукты?')
        answer2 = input()
        if answer2 == 'да':
            print('Введите название продукта')
            title99 = input()
            print('Введите количество продукта')
            count99 = input()

            for i in all_products:

                if title99 == i.title:
                    product1.count = int(product1.count) + int(count99)
                else:
                    print('Такого продукта не существует')

