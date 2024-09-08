class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name, self.weight, self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        _open = open(self.__file_name, 'r')
        _product = _open.read()
        _open.close()
        return _product

    def __add__(self, *products):
        product = self.get_products()
        _open = open(self.__file_name, 'a')
        for i in products:
            if str(i) in product:
                print(f'Продукт {i} уже есть в магазине')
            else:
                _open.write(f'{str(i)}\n')
                product += str(i), '\n'
        _open.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.__add__(p1, p2, p3)

print(s1.get_products())