def name_file(file_name):
    with open(file_name, 'r') as open_file:
        list_of_names = open_file.read()
    list_of_names = list_of_names.split()
    names = {}

    for name in list_of_names:
        if (name in names) == False:
            names[name] = 1
        else:
            names[name] += 1
    print(names)
def photos(file_name):
    with open(file_name, 'r') as open_file:
        list_of_photos = open_file.read()
    list_of_photos = list_of_photos.split(sep='/')