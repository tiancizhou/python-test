"""演示 Python 继承 + super() + 重写 __str__/__repr__。"""


class Person:
    def __init__(self, name, age):
        # 父类负责“通用的基础属性”
        self.name = name
        self.age = age

    def __str__(self):
        # 面向用户/展示的字符串（使用 ASCII，避免 Windows 终端编码问题）
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        # 面向开发/调试的字符串（尽量包含关键信息）
        return f"Person(name={self.name!r}, age={self.age})"


class Student(Person):
    def __init__(self, name, age, grade):
        # 子类先复用父类初始化逻辑，再补充自己的字段
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        # 子类重写展示文本，把 grade 也体现出来（使用 ASCII）
        return f"Student {self.name} is {self.age}, grade {self.grade}"

    def __repr__(self):
        # 子类重写调试文本，把 grade 也体现出来
        return f"Student(name={self.name!r}, age={self.age}, grade={self.grade})"


if __name__ == "__main__":
    person = Person("Tom", 20)
    student = Student("Alice", 19, 3)

    print("str(person) ->", str(person))
    print("repr(person) ->", repr(person))
    print()
    print("str(student) ->", str(student))
    print("repr(student) ->", repr(student))
    print()
    print("isinstance(student, Person) ->", isinstance(student, Person))

