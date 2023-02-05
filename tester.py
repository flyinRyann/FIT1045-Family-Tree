def read_family(filename):
    file = open(filename,"r")
    res = []
    for line in file:
        line = line.strip().replace(", ", ",").split(",")
        res.append(line)
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] == '\n' or res[i][j] == '':
                res[i][j] = None
    return res
def person_index(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The index value of the person's entry in the family tree,
            or None if they have no entry.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> person_index('Dewey Duck', duck_tree)
    8
    >>> person_index('Daffy Duck', duck_tree)
    
    """
    for i in range(len(family)):
        if family[i][0] == person:
            return i
    return None
    pass

def father(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's father, or None if the information is
            not in the database.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> father('Della Duck', duck_tree)
    'Quackmore Duck'
    >>> father('Huey Duck', duck_tree)

    >>> father('Daffy Duck', duck_tree)
    
    """
    for i in range(len(family)):
        if family[i][0] == person:
            return family[i][1]
    return None
    pass

def mother(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's mother, or None if the information is
            not in the database.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> mother('Hortense McDuck', duck_tree)
    'Downy ODrake'
    >>> mother('Fergus McDuck', duck_tree)

    >>> mother('Daffy Duck', duck_tree)
    
    """
    for i in range(len(family)):
        if family[i][0] == person:
            return family[i][2]
    return None
    pass

def children(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all of person's children.
    
    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(children('Della Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> children('Donald Duck', duck_tree)
    []
    >>> sorted(children('Fergus McDuck', duck_tree))
    ['Hortense McDuck', 'Scrooge McDuck']
    >>> children('Donald Mallard', duck_tree)
    []
    
    """
    res = []
    for i in range(len(family)):
        if family[i][1] == person or family[i][2] == person:
            res.append(family[i][0])
    return res
    pass

def grandchildren(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing only the names of the grandchildren of person
        that are stored in the database.
    
    For example:
    >>> duck_tree = [['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard'],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(grandchildren('Quackmore Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> sorted(grandchildren('Downy ODrake', duck_tree))
    ['Della Duck', 'Donald Duck']
    >>> grandchildren('Della Duck', duck_tree)
    []

    """
    children = []
    for i in range(len(family)):
        if family[i][1] == person or family[i][2] == person:
            children.append(family[i][0])
    res = []
    for j in children:
        for k in range(len(family)):
            if family[k][1] == j or family[k][2] == j:
                res.append(family[k][0])
    return res
    pass


def cousins(person, family):
    parents = [mother(person,family),father(person,family)]
    gra_par_mum = [mother(parents[0],family),father(parents[0],family)]
    gra_par_dad = [mother(parents[1],family),father(parents[1],family)]
    parent_fam = []

    for i in range(len(family)):
        if family[i][2] == gra_par_mum[0] and family[i][1] == gra_par_mum[1]:
            if family[i][0] != parents[0]:
                parent_fam.append(family[i][0])

    for i2 in range(len(family)):
        if family[i2][2] == gra_par_dad[0] and family[i2][1] == gra_par_dad[1]:
            if family[i2][0] != parents[1]:
                parent_fam.append(family[i2][0])

    res = []
    temp = []
    for j in range(len(parent_fam)):
        temp = children(parent_fam[j],family)
        for k in range(len(temp)):
            res.append(temp[k])
    return res
    
hobbits = read_family('hobbit-family.txt')
print(sorted(cousins('Frodo Baggins', hobbits)))

