import traceback


class PositiveValueError(ValueError):
    def __init__(self, value, *args):
        self.value = value
        for item in args:
            print(item)

    def __str__(self):
        return f'Ваше число {self.value} отрицательно. А возраст не может быть меньше 0'


class Bear:
    def __init__(self, name, age):
        self.name = name

        if age < 0:
            # Исключение 1 - генерация
            # raise Exception('Возраст не может быть отрицательным')
            raise PositiveValueError(age)
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


print('Start exception.py')
bear = Bear('Faust', 5)
print(bear)
name = 'Фауст'
age = int(input('Введите возраст: '))

# 2. Обработка исключений
try:
    bear = Bear(name, age)
except PositiveValueError as e:
    print('Была ошибка', e)
    # print('Была ошибка', traceback.format_exc())
except ValueError:
    print('Ошибка в числе')
except Exception:
    print('Что то пошло не так?')
else:
    print('Медведь создан')
    print(bear)
finally:
    # Выпонить в любом случае была или не была
    print('end')
