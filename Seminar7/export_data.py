def export_data():
    with open('phone.csv', 'r') as file:
        data = []
        t = []
        for line in file:
            if line != '\n':
                t.append(line.strip())
            else:
                data.append(t)
                t = []
    return data
