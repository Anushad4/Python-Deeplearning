
import operator
from collections import defaultdict


def listtupledictionary(list1):
    dict1 = defaultdict(list)


    # Iterating through the list elements and appending to the dictionary
    for key, value in list1:

        dict1[key].append(value)

    # Sorting the dictionary based on the key alphabets
    sorteddict = sorted(dict1.items(), key=operator.itemgetter(0))
    return sorteddict


def main():
    # Initializing the list with tuple elements

    list1 = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)),
             ('Mark', ('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]

    Resultdict = listtupledictionary(list1)

    # Printing the resultant dictionary
    print(Resultdict)



if __name__ == '__main__':
    main()


