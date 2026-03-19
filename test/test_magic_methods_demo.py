import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "类和对象" / "三个魔术方法示例.py"


def load_demo_module():
    spec = importlib.util.spec_from_file_location("magic_methods_demo", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法加载模块: {MODULE_PATH}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestPersonMagicMethods(unittest.TestCase):
    def test_init_sets_attributes(self):
        module = load_demo_module()
        person = module.Person("Tom", 20)

        self.assertEqual(person.name, "Tom")
        self.assertEqual(person.age, 20)

    def test_str_returns_readable_text(self):
        module = load_demo_module()

        self.assertEqual(str(module.Person("Tom", 20)), "Tom今年20岁")

    def test_repr_returns_debug_text(self):
        module = load_demo_module()

        self.assertEqual(repr(module.Person("Tom", 20)), "Person(name='Tom', age=20)")


if __name__ == "__main__":
    unittest.main()
