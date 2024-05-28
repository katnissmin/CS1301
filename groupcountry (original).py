def groupCountries(countries):
    a_dict = {}
    
    a_file = open("cookBook.txt", "r")
    title = a_file.readline()
    space = a_file.readline()
    myFile = a_file.read()
    myBook = myFile.split("\n\n")
    a_file.close()
    print(myBook)

    for i in myBook:
        recipe = i.split("\n")
        name = recipe[0]
        time = recipe[1]
        country = recipe[2]
        if country not in a_dict:
            a_dict[country] = [name]
        else:
            a_dict[country].append(name)
            a_dict[country].sort()

    print(a_dict)

    the_dict = {}
    for (friends, country) in countries:
        if country not in a_dict:
            return "Throw the book or get new friends!"
        else:
            the_dict[friends] = a_dict[country]
    return the_dict


print(groupCountries([("Marco", "Italy"),("Isabelle", "Lebanon")]))
