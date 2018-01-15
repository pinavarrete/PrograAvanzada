from pickle import dump, dumps, load, loads


if __name__ == '__main__':
    path = 'pickle_file.txt'
    dic = {1: 'a', 2: 'b', 3: 'c'}

    serializado = dumps(dic)
    print(type(serializado))
    deserializado = loads(serializado)

    with open(path, 'wb') as pickle_file:
        dump(dic, pickle_file)

    with open(path, 'rb') as pickle_file:
        objeto = load(pickle_file)

    print(objeto)
