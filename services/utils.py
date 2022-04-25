def readfile(path: str):
    f = open(path, encoding='UTF-8')
    data = f.read()
    f.close()
    return data