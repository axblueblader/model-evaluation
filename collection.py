import os


def read_all_files():
    print("Reading files and making collection")
    doc_map = dict()
    class_map = dict()
    path = 'collection/'
    dirList = os.listdir(path)
    for i in dirList:
        file_path = os.path.join(path, i)
        file_list = os.listdir(file_path)
        class_map[i] = set(file_list)
        for x in file_list:
            file = open(os.path.join(file_path, x), 'r', encoding="ISO-8859-1")
            doc_map[x] = file.read()
    return doc_map, class_map


if __name__ == "__main__":
    doc_map, class_map = read_all_files()
    for key, value in doc_map.items():
        print(key)
    for key, value in class_map.items():
        print(key, value)
