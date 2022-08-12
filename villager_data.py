"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    species_file = open(filename)
    for line in species_file:
        villagers_lst = line.split("|")
        species.add(villagers_lst[1])

    return species
# file_in_question = 'villagers.csv'
# print(all_species(file_in_question))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    villagers_by_species_file = open(filename)

    for line in villagers_by_species_file:
        villagers_lst = line.split("|")
        if search_string == villagers_lst[1]:
            villagers.append(villagers_lst[0])
        else:
            villagers.append(villagers_lst[0])

    return sorted(villagers)

# file_in_question = 'villagers.csv'log
# print(get_villagers_by_species(file_in_question))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    # [[villager1, villager2],[villager3, villager4]]
    # TODO: replace this with your code
    villagers_hobby_lst = []

    villagers_by_hobby = open(filename)
    fitness = []
    nature = []
    education = []
    music = []
    fashion =[]
    play = []

    for line in villagers_by_hobby:
        villagers_hobby_lst = line.split("|")
        if villagers_hobby_lst[3] == "Fitness":
            fitness.append(villagers_hobby_lst[0])
        elif villagers_hobby_lst[3] == "Nature":
            nature.append(villagers_hobby_lst[0])
        elif villagers_hobby_lst[3] == "Education":
            education.append(villagers_hobby_lst[0])
        elif villagers_hobby_lst[3] == "Music":
            music.append(villagers_hobby_lst[0])
        elif villagers_hobby_lst[3] == "Fashion":
            fashion.append(villagers_hobby_lst[0])
        elif villagers_hobby_lst[3] == "Play":
            play.append(villagers_hobby_lst[0])
    
    villagers_hobby_lst = [fitness, nature, education, music, fashion, play]
        
    return villagers_hobby_lst

# file_in_question = 'villagers.csv'
# print(all_names_by_hobby(file_in_question))

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

    all_data_in_file = open(filename)

    for line in all_data_in_file:
        data_line = line.split("|")
        data_line = tuple(data_line)
        all_data.append(data_line)

    return all_data

file_in_question = 'villagers.csv'
print(all_data(file_in_question))


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

    # TODO: replace this with your code


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

    # TODO: replace this with your code
