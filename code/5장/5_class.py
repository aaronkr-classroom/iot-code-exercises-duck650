#5_class.py

class Animal:
    def __init__(self, name): # _init_이 아니라 __init__ 입니다.
        self.name = name
        
    def speak(self):
        pass # 자식 클래스에서 내용을 채울 부분
    
    def setName(self, name: str):
        """
        set the Animal class's name.
        Animal 클래스의 이름을 재정의하는 함수.
        :param name: 새로운 Animal의 이름
        """
        
        self.name=name
        
    def getName(self)->str:
        """
        Return the Animal class's name.
        Animal 클래스의 이름을 반환하는 함수.
        :return: Animal의 이름
        """
        return self.name
    
class Dog(Animal): # Animal을 상속받음 (is-a 관계)
    def __init__(self, name, age=3):
        super().__init__(name) # 부모 클래스의 생성자 호출
        self.age = age # Dog만의 속성 (has-a)
        
    def speak(self):
        print(f"{self.name}가 멍멍! 하고 짖습니다. (나이: {self.age})")
        
class Cat(Animal):
    def speak(self):
        # 별도의 __init__이 없으면 부모의 것을 그대로 사용합니다.
        print(f"{self.name}가 야옹~ 하고 웁니다.")
        
# 객체 생성 및 호출
my_dog = Dog("초코")
my_cat = Cat("나비")

my_dog.speak()
my_cat.speak()