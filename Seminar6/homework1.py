# Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_text = 'Напишите программу, удаляющую из текста все слова, содержащие "абв".'
my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
my = " ".join(my_text)
print(my)
