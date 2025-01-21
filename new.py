class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Температура не может быть ниже абсолютного нуля!")
        else:
            self.__celsius = value

temp = Temperature(25)
print(temp.celsius)  # Выведет: 25
temp.celsius = -300  # Выведет: Температура не может быть ниже абсолютного нуля!
temp.celsius = 20
print(temp.celsius)  # Выведет: 20
