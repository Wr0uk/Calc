x = input("Введите выражение: ")
allowed = set(' 1234567890()+-/*\\')
if allowed.issuperset(x):
    print("Ответ: ", eval(x))
else:
    print("Выражение неккоректно.")