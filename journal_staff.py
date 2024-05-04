__main__ 2024-05-04 13:49:03,279 ERROR Ошибка:Недопустимое имя
Traceback (most recent call last):
  File "C:\Users\Sajne\Documents\DZ_SEMINAR_15\staff.py", line 104, in <module>
    person = Person("", "John", "Doe", 30)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Sajne\Documents\DZ_SEMINAR_15\staff.py", line 64, in __init__
    raise InvalidNameError(last_name)
InvalidNameError: Invalid name: . Name should be a non-empty string.