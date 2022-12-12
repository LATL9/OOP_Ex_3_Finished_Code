class Product:
    def __init__(self,description,price,inventory):
        self.__description = description
        self.__price = price
        self.__inventory = inventory

Product1 = Product("parsnip",0.5,12)
Product2 = Product("cucumber",0.75,16)
