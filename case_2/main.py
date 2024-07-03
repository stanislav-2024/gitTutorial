class Animal:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "<class 'Animal'>"
    
    def show(self):
        print('Я млекопитающее')
    

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "<class 'Cat'>"
    
    def show(self):
        super().show()
        print('Я из семейства кошачьих')
    
class Tiger(Cat):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "<class 'Tiger'>"
    
    def show(self):
        super().show()
        print('Я опасный хищник в полоску')
    




t = Tiger()
t.show()
print(t)