"""
Template for Programming Assignment FIT1045 - OCT 2021
Family Trees

In this assignment we create a Python module to implement some
basic family tree software, where users can look up various relationships
that exist in the database, as well as merging two family tree databases
that may contain overlapping information.

Functions  1-7 are due in Part 1 of the assignment. Functions
for 8 and 9 are due in Part 2.

We represent each entry in a family tree database as a list of three
strings [name, father, mother], where name is a person's name, father
is the name of their father, and mother is the name of their mother.
Where a particular relationship is unknown, the value None is used.
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


The file hobbit-family.txt is also provided for testing. The database
used in this file has been compiled using the info at
http://lotrproject.com/hobbits.php. Character names are by J.R.R. Tolkein.

For more information see the function documentations below and the
assignment sheet.

"""


# Part 1 (due Week 6) #

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
    This function determines p1 and p2 have a direct correlation in terms of ancestral base.
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
    # Finding if p1 is descendant of p2:
    checker = False
    generation = 0
    p1_ancestor = [p1]
    temp = []

    # This loop stops when p2 is found to be apart of p1's ancestor.
    while p2 not in p1_ancestor:
        # Temporarily creating the list of ancestor by finding the grandparents of all the people in the previous list.
        for i in range(len(p1_ancestor)):
            temp.append(father(p1_ancestor[i],family))
            temp.append(mother(p1_ancestor[i],family))
        p1_ancestor = temp
        temp = []
        # This condition ensures that if the while loop condition is not found then the loop can still exit.
        if all(people is None for people in p1_ancestor):
            checker = True
            break
        # Iterating each generation.
        generation += 1
    # Return condition.
    if checker == False:
        return p2 + " is a direct ancestor of " + p1 + ", " + str(generation) + " generations apart." 

    # Finding if p2 is descendant of p1:
    # Note: This is the same process as the loop above except p1 and p2 switch to find the other way.
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
    
    # Return a non-connection response:
    elif checker == True:
        return p1 + " is not a direct ancestor or descendant of " + p2 + "." 

def element_same_check(lst,lst2):
    """
    This function checks two list and check if any of the item in the list has the same item.
    """
    for i in lst:
        for j in lst2:
            if i == j and i != None:
                return True
    return False


def grandparent_degree(person1, person2, family):
    """
    This function compares the nth great grandparents of p1 and p2. It returns the degree + 1 to get
    the type of cousins if their is a match of a grandparent. Or it returns -1 if the a match is not
    found.
    """
    # Initialisation of parents and grandparents to empty list (to be found).
    parents1 = [father(person1,family),mother(person1,family)]
    grand_parents1 = []
    parents2 = [father(person2,family),mother(person2,family)]
    grand_parents2 = []
    degree_counter = 0
    # This while loop will exit if either one of the parents list have None; therefore, no comparison.
    while all(people is None for people in parents1 or parents2) != True:
        for i in parents1:
            grand_parents1.append(father(i,family))
            grand_parents1.append(mother(i,family))
        for j in parents2:
            grand_parents2.append(father(j,family))
            grand_parents2.append(mother(j,family))
        # The condition is to make sure it doesn't iterate till the second time.
        if degree_counter >= 1:
            if element_same_check(grand_parents1,grand_parents2) == True:
                return degree_counter + 1
        # Assign the new comparison variables and reset the old one. And also increase counter gen count.
        parents1 = grand_parents1
        parents2 = grand_parents2
        grand_parents1 = []
        grand_parents2 = []
        degree_counter += 1
    # Return -1 if there is no match.
    return -1



def cousin_degree(p1, p2, family):
    """
    This function determines if p1 or p2 have a direct corellation as one or nth type of cousin.
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
    # First condition: check to see if they are siblings.
    if [father(p1,family),mother(p1,family)] == [father(p2,family),mother(p2,family)]:
        return 0
    # Second condition: check to see if they are both first cousins.
    elif p1 in cousins(p2,family):
        return 1
    # Third condition: pre-written condition to the nth cousin problem. Also, pre-program -1 already.
    else:
        return grandparent_degree(p1,p2,family) 
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
