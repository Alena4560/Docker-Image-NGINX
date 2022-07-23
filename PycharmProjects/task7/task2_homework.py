def cookbook_dictionary():
    cook_book = dict()
    my_file = open('recipes.txt', 'r', encoding='cp1251')
    dish_name = '***'
    while dish_name != '':
        dish_name = my_file.readline().strip('\n')
        print('Блюдо:', dish_name)
        if dish_name == '':
            break
        ingredient_count = int(my_file.readline())
        print('Ингредиенты:', ingredient_count)
        ingredients = list()
        for i in range(ingredient_count):
            ingredient_line = my_file.readline().strip('\n').split(' | ')
            print(i + 1, '---', ingredient_line[0])
        ingredient_dict = dict()
        ingredient_dict['ingredient_name'] = ingredient_line[0]
        ingredient_dict['quantity'] = int(ingredient_line[1])
        ingredient_dict['measure'] = ingredient_line[2]
        ingredients.append(ingredient_dict)
        cook_book[dish_name] = ingredients
        my_file.readline()
    my_file.close()
    return(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    print('Введите список блюд:')
    dishes = list()
    flag = True
    while flag:
        dishes.append(input('Название блюда:'))
        print('Продолжить? [Y/N]')
        c = input()
        if c == 'n' or c == 'N':
            flag = False
            break
    person_count = int(input('Введите количество персон:'))
    result = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if name in result:
                result[name]['quantity'] += ingredient['quantity'] * person_count
            else:
                record = dict()
                record['measure'] = ingredient['measure']
                record['quantity'] = ingredient['quantity'] * person_count
                result[name] = record
    return (result)

def merging_files():
    def read_file(filename):
        result = dict()
        result['name'] = filename
        f = open(filename, 'r')
        result['data'] = f.readlines()
        f.close()
        result['lines'] = len(result['data'])
        return result
    def get_lines(file_record):
        return file_record['lines']
    files = list()
    for i in range(1,4):
        filename = str(i) + '.txt'
        files.append(read_file(filename))
    files.sort(key=get_lines)
    f = open('result.txt', 'w')
    for file_record in files:
        f.write(str(file_record['name']) + '\n')
        f.write(str(file_record['lines']) + '\n')
        for line in file_record['data']:
            f.write(line)
        f.write('\n')
    f.close()

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'cookbook_dictionary':
            return(cookbook_dictionary())
        elif command == 'get_shop_list_by_dishes':
            return(get_shop_list_by_dishes(dishes, person_count))
        elif command == 'merging_files':
            return(merging_files())
        else:
            return('Введена несуществующая команда')
main()
