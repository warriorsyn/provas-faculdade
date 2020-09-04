def dateToExtensive(date: str) -> str:
    months = {1: 'Janeiro', 2: 'Feveiro', 3: 'Marco', 4: 'Abril',
              5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    data_splited = birth_date.split('/')

    return f"{data_splited[0]} de {months[int(data_splited[1])]} de {data_splited[2]}"


birth_date = input("Insert your birthday: ")

print(dateToExtensive(birth_date))
