"""
Georgia Institute of Technology - CS1301
HW07 -  File I/O
"""
#########################################
"""
Function Name: lazyMeal()
Parameters: maxPrepTime (int)
Returns: recipe (list)
"""
def lazyMeal(maxPrepTime):
    file = open('cookBook.txt', 'r')
    file.readline()
    file.readline()
    data = file.readlines()
    #need to get rid of the \n
    file.close()

    filelist = []
    namelist = []

    for i in range(0, len(data)):
        num = data[i].strip('\n')
        filelist.append(num)

    for j in range(1, len(filelist), 4):
        print(filelist[j])
        if int(filelist[j]) <= maxPrepTime:
            name = filelist[j-1]
            namelist.append(name)
            namelist.sort()

    if len(namelist) == 0:
        namelist = "Waffle House it is!"

    return namelist
            
#########################################
"""
Function Name: groupCountries()
Parameters: countries(list)
Returns: recipeDict (dict)

#loop through file
#create a dictionary that maps each country to the recipe
#loop throuh the tuple countries
#check if country is in the dictionary I created
#add to the dictionary, the name of the person mapped of the recipe from the old dictionary
"""
def groupCountries(countries):
    file = open('cookBook.txt', 'r')
    title = file.readline()
    space = file.readline()
    data = file.read()
    filelist = data.split("\n\n")
    file.close()
    print(filelist)

    countrydict = {}

    for i in filelist:
        items = i.split("\n")
        name = items[0]
        time = items[1]
        country = items[2]
        if country not in countrydict:
            countrydict[country] = [name]
        else:
            countrydict[country].append(name)
            countrydict[country].sort()
    
    finaldict = {}
    for (friends, country) in countries:
        if country not in countrydict:
            return "Throw the book or get new friends!"
        else:
            finaldict[friends] = countrydict[country]
    return finaldict


#########################################
"""
Function Name: favRecipes()
Parameters: recipeList (list)
Returns: None
"""
def favRecipes(recipeList):
    a_file = open("cookBook.txt", "r")
    title = a_file.readline()
    space = a_file.readline()
    final = a_file.readlines()
    a_file.close()
    
    filelist = []
    for i in range(0, len(final)):
        num = final[i].strip()
        filelist.append(num)
    print(filelist)

    count = 0
    b_file = open("favRecipes.txt", "w")
    b_file.write(title)
    b_file.write(space)

    for i in range(0, len(filelist), 4):
        if filelist[i] in recipeList:
            count += 1
            if filelist[i] == recipeList[-1]:
                b_file.write(filelist[i])
                b_file.write("\n")
                b_file.write(filelist[i+1])
                b_file.write("\n")
                b_file.write(filelist[i+2])
            else:
                b_file.write(filelist[i])
                b_file.write("\n")
                b_file.write(filelist[i+1])
                b_file.write("\n")
                b_file.write(filelist[i+2])
                b_file.write("\n")
                b_file.write("\n")
    if count == 0:
        b_file = open("favRecipes.txt", "w")
        b_file.write("No information found.")
    b_file.close()
    
#########################################
"""
Function Name: orderCandy()
Parameters: prices (dict), maxCost (float)
Returns: None
"""
def orderCandy(prices, maxCost):
    
    dic_key = list(prices.keys())
    dic_val = list(prices.values())
    print(dic_key)
    print(dic_val)
    buycandy = []
    for i in range(0, len(dic_val)):
        if dic_val[i] <= maxCost:
            buycandy.append(dic_key[i])
    print(buycandy)

    myfile = open("candyOrder.txt", "w")

    a = open("friends.txt", "r")
    final = a.readlines()
    a.close()
    print(final)

    filelist = []

    for i in range(0, len(final)):
        num = final[i].strip()
        filelist.append(num)
    print(filelist)

    d = {}
    for i in range(0, len(buycandy)):
        friendchoice = 0
        for j in range(2, len(filelist), 5):
            if filelist[j] == buycandy[i] or filelist[j+1] == buycandy[i]:
                if buycandy[i] in d:
                    d[buycandy[i]] += 1
                else:
                    d[buycandy[i]] = 1
    i = 0
    for candy,count in d.items():
        if count >= 3:
            myfile.write("{name}: {vote}\n".format(name=candy, vote=count))
            i+=1
    if i == 0:
        myfile = open("candyOrder.txt", "w")
        myfile.write("Ask again.")
    myfile.close()
    
 
    myfile = open("candyOrder.txt")
    content = myfile.read()
    content = content.strip()
    myfile.close()
    myfile = open("candyOrder.txt",'w')
    myfile.write(content)
    myfile.close()

#########################################
"""
Function Name: moviePicker()
Parameters: potentialMovie (str)
Returns: isOption(bool)
"""
def moviePicker(potentialMovie):
    a = open("friends.txt", "r")
    final1 = a.readlines()
    a.close()
    
    friendlist = []
    for i in range(0, len(final1)):
        num = final1[i].strip()
        friendlist.append(num)

    b = open("movies.txt", "r")
    final2 = b.readlines()
    b.close()
    
    movielist = []
    for i in range(0, len(final2)):
        num = final2[i].strip()
        movielist.append(num)

    picker_rating = ""
    for i in range(0, len(movielist)):
        if movielist[i] == potentialMovie:
            picker_rating = movielist[i+1]
##    if picker_rating == '':
##        return False

    for j in range(1, len(friendlist), 5):
        if len(picker_rating) == 0:
            return False
        if int(friendlist[j]) <= int(picker_rating):
            return False
        else:
            return True
