from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]


def function():
    print("Выберите действие:\n\
    1 - Импорт;\n\
    2 - Экспорт;\n\
    3 - Поиск контакта.")
    func = input("Введите цифру: ")
    if func == '1':
        import_data(input_data())
    elif func == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(20), "Примечание".center(20))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20))
        else:
            print("Данные не обнаружены")
