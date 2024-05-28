"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""

#########################################
class People:
    def __init__(self, name, age, isAsleep, canCook=False):
        # canCook can have an assigned value (default to False)
        # but not Friends (initialized to an empty list)
        self.name = name
        self.age = age
        self.isAsleep = isAsleep
        self.canCook = canCook
        self.friends = []

    def wakeUp(self):
        if self.isAsleep:
            self.isAsleep = False
        else:
            return "{} is already awake.".format(self.name)

    def invite(self, people):
        self.friends.append(people)

    def __str__(self):
        if self.canCook:
            return "My name is {} and I can cook.".format(self.name)
        else:
            return "My name is {} and I can't cook.".format(self.name)

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):  # provided
        return f"People({self.name}, {self.age}, {self.isAsleep}, {self.canCook}, {len(self.friends)})"

    def __eq__(self, other):  # provided
        return self.name == other.name and self.age == other.age and self.isAsleep == other.isAsleep and self.canCook == other.canCook and self.friends == other.friends


#########################################
class Food:

    def __init__(self, name, ingredients, prepTime):
        self.name = name
        self.ingredients = ingredients
        self.prepTime = prepTime

    def __str__(self):
        return "{} takes {} to make.".format(self.name, self.prepTime)

    def __repr__(self):  # provided
        return f"Food({self.name}, {len(self.ingredients)}, {self.prepTime})"


#########################################

class Activities:

    def __init__(self, ingredientsDict={}):
        self.ingredientsDict = ingredientsDict

    def cook(self, food):
        # no indexing in dictionaries
        # need to loop through ingredients
        for ingredient, serving in food.ingredients:
            if serving > self.ingredientsDict[ingredient]:
                return "We did not have enough ingredients to make {}.".format(food.name)

        for ingredient, serving in food.ingredients:
            self.ingredientsDict[ingredient] -= serving

        return "We made {}!".format(food.name)

    def kidsTable(self, guests):
        aList = []
        for i in guests:
            aList += [(i.age, i.name)]

        aList.sort()  # sort by first element in alphabetical order

        youngest = []
        for age, name in aList[:4]:
            youngest.append(name)
        return youngest

    def buyIngredients(self, ingredientName, ingredientAmount):
        if ingredientName not in self.ingredientsDict:
            self.ingredientsDict[ingredientName] = ingredientAmount
        else:
            self.ingredientsDict[ingredientName] += ingredientAmount

    def __repr__(self):  # provided
        return f"Activities({len(self.ingredientsDict)})"
