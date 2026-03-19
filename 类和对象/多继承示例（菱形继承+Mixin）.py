"""演示 Python 多继承：菱形继承（diamond）+ Mixin 风格组合。"""


# ----------------------------
# 1）菱形继承（diamond）演示
# ----------------------------
class A:
    def say(self):
        return "A"


class B(A):
    def say(self):
        # super() 会沿着 MRO（方法解析顺序）向后找：
        # D -> B -> C -> A -> object
        return f"B({super().say()})"


class C(A):
    def say(self):
        return f"C({super().say()})"


class D(B, C):
    # 这里不实现 say：D 会先继承 B.say，
    # 再通过协作式 super() 继续走到 C.say，最后走到 A.say。
    pass


# ----------------------------
# 2）Mixin 风格演示（组合多个能力）
# ----------------------------
class CanSpeak:
    def speak(self, msg="hello"):
        return f"Speak: {msg}"


class CanFly:
    def fly(self):
        return "Fly: up!"


class Player(CanSpeak, CanFly):
    # Player 同时继承 CanSpeak 和 CanFly，实现“能力拼装”。
    pass


def _class_names(mro_list):
    return [cls.__name__ for cls in mro_list]


if __name__ == "__main__":
    # 这里使用 ASCII 文本，避免 Windows 终端编码显示乱码
    print("=== Diamond inheritance: MRO + super() ===")
    print("D.mro() ->", _class_names(D.mro()))
    print("D().say() ->", D().say())

    print()
    print("=== Mixin style: combine abilities ===")
    p = Player()
    print("p.speak('hi') ->", p.speak("hi"))
    print("p.fly() ->", p.fly())
    print("isinstance(p, CanSpeak) ->", isinstance(p, CanSpeak))
    print("isinstance(p, CanFly) ->", isinstance(p, CanFly))

