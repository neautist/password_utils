from password_generator.password_generator import password_generator
length=input("Введите число для генерации длины пароля")
password=password_generator(int(length))
print(f"Ваш пароль: {password}")