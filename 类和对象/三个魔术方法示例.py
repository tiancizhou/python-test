"""演示 Python 中常见的三个魔术方法。"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}今年{self.age}岁"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"


if __name__ == "__main__":
    person = Person("Tom", 20)
    print("print(person) 的输出：")
    print(person)
    print()
    print("repr(person) 的输出：")
    print(repr(person))
