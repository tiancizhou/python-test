# Magic Methods Example Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a runnable example in `类和对象` that demonstrates `__init__`, `__str__`, and `__repr__` with a small automated test.

**Architecture:** The change adds a single educational example module with a `Person` class and a `__main__` demo block. A `unittest` test file loads the module from its file path and verifies initialization plus the two string representations.

**Tech Stack:** Python 3, standard-library `unittest`, `importlib.util`, `pathlib`

---

### Task 1: Add failing tests for the example

**Files:**
- Create: `test/test_magic_methods_demo.py`
- Create: `类和对象/三个魔术方法示例.py`

**Step 1: Write the failing test**

```python
def test_init_sets_attributes(self):
    person = Person("Tom", 20)
    self.assertEqual(person.name, "Tom")
    self.assertEqual(person.age, 20)
```

**Step 2: Run test to verify it fails**

Run: `.\.venv\Scripts\python.exe -m unittest test.test_magic_methods_demo -v`
Expected: FAIL because the demo module does not exist yet

**Step 3: Write minimal implementation**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**Step 4: Run test to verify it passes**

Run: `.\.venv\Scripts\python.exe -m unittest test.test_magic_methods_demo -v`
Expected: PASS for the initialization behavior

**Step 5: Commit**

```bash
git add test/test_magic_methods_demo.py 类和对象/三个魔术方法示例.py
git commit -m "feat: add magic methods example"
```

### Task 2: Add readable and debug string behavior

**Files:**
- Modify: `类和对象/三个魔术方法示例.py`
- Modify: `test/test_magic_methods_demo.py`

**Step 1: Write the failing tests**

```python
def test_str_returns_readable_text(self):
    self.assertEqual(str(Person("Tom", 20)), "Tom今年20岁")

def test_repr_returns_debug_text(self):
    self.assertEqual(repr(Person("Tom", 20)), "Person(name='Tom', age=20)")
```

**Step 2: Run test to verify they fail**

Run: `.\.venv\Scripts\python.exe -m unittest test.test_magic_methods_demo -v`
Expected: FAIL because `__str__` and `__repr__` are not implemented yet

**Step 3: Write minimal implementation**

```python
def __str__(self):
    return f"{self.name}今年{self.age}岁"

def __repr__(self):
    return f"Person(name={self.name!r}, age={self.age})"
```

**Step 4: Run test to verify they pass**

Run: `.\.venv\Scripts\python.exe -m unittest test.test_magic_methods_demo -v`
Expected: PASS

**Step 5: Commit**

```bash
git add test/test_magic_methods_demo.py 类和对象/三个魔术方法示例.py
git commit -m "feat: complete magic methods example"
```

