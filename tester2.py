def read_family(filename):
    """
    Input: A filename (filename) containing a family tree database where
    each line is in the form name, father, mother
    Output: A family tree database containing the contents of the file
    in the format specified above, or None if the file is in the incorrect
    format.
    
    For example:

    >>> hobbits = read_family('hobbit-family.txt')
    >>> len(hobbits)
    119
    >>> hobbits[118]
    ['Sancho Proudfoot', 'Olo Proudfoot', None]

     """
    file = open(filename,"r")
    res = []
    for line in file:
        line = line.strip().replace(", ", ",").split(",")
        res.append(line)
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] == '\n' or res[i][j] == '':
                res[i][j] = None
    file.close()
    return res
    pass


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
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all cousins of person that
            are stored in the database.
    
    For example:
    
    >>> hobbits = read_family('hobbit-family.txt')
    >>> sorted(cousins('Frodo Baggins', hobbits))
    ['Daisy Baggins', 'Merimac Brandybuck', 'Milo Burrows', 'Saradoc Brandybuck', 'Seredic Brandybuck']
    
    """
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
    pass


# Part 2: (due Week 11) #

def direct_ancestor(p1, p2, family):
    """
    Input: Two names (p1, p2) and a family tree database (family).
    Output: One of the following three string outputs (where p1 and
            p2 are the given input strings, and n is a non-negative integer):
            "p1 is a direct ancestor of p2, n generations apart."
            "p2 is a direct ancestor of p1, n generations apart."
            "p1 is not a direct ancestor or descendant of p2."

    For example:

    >>> hobbits = read_family('hobbit-family.txt')
    >>> direct_ancestor('Frodo Baggins', 'Frodo Baggins', hobbits)
    'Frodo Baggins is a direct ancestor of Frodo Baggins, 0 generations apart.'
    >>> direct_ancestor('Frodo Baggins', 'Gormadoc Brandybuck', hobbits)
    'Gormadoc Brandybuck is a direct ancestor of Frodo Baggins, 5 generations apart.'
    
    """
    checker = False
    generation = 0
    p1_ancestor = [p1]
    temp = []
    # Finding if p1 is descendant of p2:
    while p2 not in p1_ancestor:
        for i in range(len(p1_ancestor)):
            temp.append(father(p1_ancestor[i],family))
            temp.append(mother(p1_ancestor[i],family))
        p1_ancestor = temp
        temp = []
        if all(people is None for people in p1_ancestor):
            checker = True
            break
        generation += 1
    if checker == False:
        return p2 + " is a direct ancestor of " + p1 + ", " + str(generation) + " generations apart." 

    # Finding if p2 is descendant of p1:
    checker = False
    generation = 0
    p2_ancestor = [p2]
    temp = []
    while p1 not in p2_ancestor:
        for i in range(len(p2_ancestor)):
            temp.append(father(p2_ancestor[i],family))
            temp.append(mother(p2_ancestor[i],family))
        p2_ancestor = temp
        temp = []
        if all(people is None for people in p2_ancestor):
            checker = True
            break
        generation += 1
    if checker == False:
        return p1 + " is a direct ancestor of " + p2 + ", " + str(generation) + " generations apart." 
    elif checker == True:
        return p1 + " is not a direct ancestor or descendant of " + p2 + "." 

def list_check_none(lst):
    res = True
    for i in lst:
        if i is not None:
            return False
    return True

def element_same_check(lst,lst2):
    for i in lst:
        for j in lst2:
            if i == j and i != None:
                return True
    return False


def grandparent_degree(person1, person2, family):
    """
    # Degree indicates the amount of "great" that comes before the grandparent.
    """
    parents1 = [father(person1,family),mother(person1,family)]
    grand_parents1 = ["temp"]
    parents2 = [father(person2,family),mother(person2,family)]
    grand_parents2 = ["temp"]
    degree_counter = 0
    while all(people is None for people in parents1 or parents2) != True:
        if "temp" in grand_parents1 and "temp" in grand_parents2:
            grand_parents1 = []
            grand_parents2 = []
    #list_check_none(grand_parents1) == False and list_check_none(grand_parents2) == False:
        for i in parents1:
            grand_parents1.append(father(i,family))
            grand_parents1.append(mother(i,family))
        for j in parents2:
            grand_parents2.append(father(j,family))
            grand_parents2.append(mother(j,family))
        if degree_counter >= 1:
            if element_same_check(grand_parents1,grand_parents2) == True:
                return degree_counter + 1
        parents1 = grand_parents1
        parents2 = grand_parents2
        print(parents1)
        print(parents2)
        print(grand_parents1)
        print(grand_parents2)
        grand_parents1 = []
        grand_parents2 = []
        degree_counter += 1
    return -1



def cousin_degree(p1, p2, family):
    """
    Input: Two names (p1, p2) and a family tree database (family).
    Output: A number representing the minimum distance cousin relationship between p1 and p2, as follows:
            -   0 if p1 and p2 are siblings
            -   1 if p1 and p2 are cousins
            -   n if p1 and p2 are nth cousins, as defined at https://www.familysearch.org/blog/en/cousin-chart/
            -   -1 if p1 and p2 have no cousin or sibling relationship
    
    For example:
    >>> hobbits = read_family("hobbit-family.txt")
    >>> cousin_degree('Minto Burrows', 'Myrtle Burrows', hobbits)
    0
    >>> cousin_degree('Estella Bolger', 'Meriadoc Brandybuck', hobbits)
    3
    >>> cousin_degree('Frodo Baggins', 'Bilbo Baggins', hobbits)
    -1
    
    """
    if [father(p1,family),mother(p1,family)] == [father(p2,family),mother(p2,family)]:
        return 0
    elif p1 in cousins(p2,family):
        return 1
    else:
        return grandparent_degree(p1,p2,family) 


    
hobbits = read_family("hobbit-family.txt")
print(cousin_degree('Estella Bolger', 'Meriadoc Brandybuck', hobbits))
print(cousin_degree('Frodo Baggins', 'Bilbo Baggins', hobbits))
