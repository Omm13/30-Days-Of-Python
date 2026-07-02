# DAY 15 

# Python Error types

# 1. Syntax Error
# print 'hello world'  # ❌ SyntaxError: Missing parentheses

# 2. Name Error
# print(hello)  # ❌ NameError: name 'hello' is not defined

# 3. Index Error
# my_list = [1, 2, 3]
# print(my_list[3])  # ❌ IndexError: list index out of range

# 4. Module not found Error
# import non_existent_module  # ❌ ModuleNotFoundError: No module named 'non_existent_module'

# 5. Import Error
# From math import power # ❌ ImportError: cannot import name 'power' from 'math'

# 6. Attribute Error
# math.PI # ❌ AttributeError: module 'math' has no attribute 'PI'

# 7. Key Error
# my_dict = {'a': 1, 'b': 2}
# print(my_dict['c'])  # ❌ KeyError: 'c'

# 8. Value Error
# int('abc')  # ❌ ValueError: invalid literal for int() with base 10: 'abc'

# 9. Type Error
# '2' + 2  # ❌ TypeError: can only concatenate str (not "int") to str

# 10. Zero Division Error
# 1 / 0  # ❌ ZeroDivisionError: division by zero