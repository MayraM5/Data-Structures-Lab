"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    file = open(filename)
    for line in file:
        data_species = line.rstrip().split("|")[1]
        species.add(data_species)

    return species

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    
    #Create a list of sets (every line is a set),search string in set[1] and return its set[0]
    villager = []
    village_name = []
    species = []

    file = open(filename)
    for line in file:
        data_species = line.rstrip().split("|")[0]
        village_name.append(data_species)
        data_species = line.rstrip().split("|")[1]
        species.append(data_species)

    villagers = list(zip(village_name, species))

    for data in villagers:
        if data[1] == search_string:
            villager.append(data[0])    

    return sorted(villager)

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    file = open(filename)
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    names = []
    hobby = []
    for line in file:
        data = line.rstrip().split("|")[0]
        names.append(data)
        data = line.rstrip().split("|")[3]
        hobby.append(data)

    name_and_hobby = list(zip(names, hobby))

    for name in name_and_hobby:
        if name[1] == "Fitness":
            fitness.append(name[0])
        elif name[1] == "Nature":
            nature.append(name[0])    
        elif name[1] == "Education":
            education.append(name[0])    
        elif name[1] == "Music":
            music.append(name[0])    
        elif name[1] == "Fashion":
            fashion.append(name[0])
        elif name[1] == "Play":
            play.append(name[0])                    

    return [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
    ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
       
    all_data = []

    data = open(filename)

    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    
    names = []
    motto = []

    file = open(filename)

    for line in file:
        data = line.rstrip().split("|")[0]
        names.append(data)
        data = line.rstrip().split("|")[4]
        motto.append(data)

    villagers = list(zip(names, motto))

    for name in villagers:
        if name[0] == villager_name:
            return name[1]

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    names = []
    personality = []
    # file = open(filename)

    for line in open(filename):
        data = line.rstrip().split("|")[0]
        names.append(data)
        data = line.rstrip().split("|")[2]
        personality.append(data)

    villagers = list(zip(names, personality))

    for name in villagers:
        if name[0] == villager_name:
            search_personality = name[1]
    set_names = set()
    for name in villagers:
        if search_personality == name[1]:
             set_names.add(name[0])

    return set_names    