class Person:# Создаём общий класс(базовый/главный)
    def __init__(self, name, age):# Вписываем общие параметры для будущих классов (имя и возраст)
        self.name = name
        self.age = age



class Teacher(Person): # Создаём класс "Учитель" который наследует свойства базового класса
    def __init__(self, name, age, knowledge, list_students):# добавляем к базовым свойствам новые свойства для этого класса
        super().__init__(name, age)# наследование из базового класса
        self.knowledge = knowledge
        self.list_students = list_students

    def to_teach(self, knowledge, student_index): # функция "Обучить" принимает 2 значения "Знания" и индекс студента
        for i in self.knowledge: # создаём цикл, в котором каждому ученику даём знания
            if i.get(knowledge): # При условии что есть чему учить
                self.list_students[student_index].to_get_knowledge(i)# из списка студентов берём одного по индексу и даём ему знания
                print(self.list_students[student_index].knowledge)# принтуем всё это




class Student(Person): #Создаём класс "Ученик"
    def __init__(self, name, age):# Даём ему свойства
        super().__init__(name, age)# наследуем их от родительского класса
        self.knowledge = [] # создаём пустой лист знаний, так как изначально ученик знает - ничего

    def to_get_knowledge(self, knowledge): # функция получить знания, будем использовать её внутри другой функции "Учить"
        self.knowledge.append(knowledge) #Добавляем наши знания в лист знаний ученика


c1 = Student('Pepper', 16)#уч №1
c2 = Student('Pepp', 15)# уч №2
c3 = Student('Per', 17)# уч №3
b = Teacher('Anna', 29, [{'Geometry' : 'Triangle'}], [c1,c2,c3])# Учитель(Имя, возраст, предмет и тема(это дикт в листе), и лист учеников

b.to_teach('Geometry', 0)# Вызываем функцию "Учить", для учителя(учит кто? - учитель), передаём 2 параметра - ключ по котому мы искали знания и индекс ученика из списка