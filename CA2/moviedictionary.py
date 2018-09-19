"""
Stephen O'Donovan
102554291
Assignment 2

**************************************************

Code for part 2:

import math
movie_list = ["Four Lions", "Wonder Woman", "Touch of Evil", "Delicatessen"]
file_list = [build_tree('small_movies_metadata.txt'), build_tree('small_repeated_movies_metadata.txt'),
             build_tree('movies_metadata.txt')]
for f in file_list:
    print('%s' % '*'*20)
    print('Answers for file ')
    print('Number of unique movies: ' + str(f.size()))
    print('Height of tree: ' + str(f.height()))
    log = math.floor(math.log((f.size() +1), 2)) - 1
    print('Minimum height for tree to be perfectly balanced: ' + str(log))
    print('%s' % '*'*20)
    for m in movie_list:
        movie_node = f.search(m)
        if movie_node:
            print('%s' % '*'*20)
            print('Found node for %s' % (m))
            print('Node Statistics: ')
            print(movie_node._stats())
            print('Node Structure:')
            print(movie_node._print_structure())
            print('%s' % '*'*20)

#**************************************************
********************
Answers for file 'small_movies_metadata.txt'
Number of unique movies: 12
Height of tree: 5
Minimum height for tree to be perfectly balanced: 3
********************
********************
Found node for Four Lions
Node Statistics: 
size = 2; height = 1
Node Structure:
Four Lions(1)[* Four Lovers] -- Four Last Songs
Four Lovers(0)[* *] -- Four Lions

********************
********************
Answers for file 'small_repeated_movies_metadata.txt'
Number of unique movies: 19
Height of tree: 7
Minimum height for tree to be perfectly balanced: 4
********************
********************
Found node for Wonder Woman
Node Statistics: 
size = 19; height = 7
Node Structure:
Wonder Woman(7)[Wonder Bar Wonderwall] -- *
Wonder Bar(6)[Won Ton Ton: the Dog Who Saved Hollywood Wonder Man] -- Wonder Woman
Won Ton Ton: the Dog Who Saved Hollywood(5)[Women's Prison Massacre *] -- Wonder Bar
Women's Prison Massacre(4)[Women's Prison *] -- Won Ton Ton: the Dog Who Saved Hollywood
Women's Prison(3)[Women Without Men *] -- Women's Prison Massacre
Women Without Men(2)[Women Vs Men Women's Day] -- Women's Prison
Women Vs Men(1)[* Women Who Flirt] -- Women Without Men
Women Who Flirt(0)[* *] -- Women Vs Men
Women's Day(1)[Women vs. Men *] -- Women Without Men
Women vs. Men(0)[* *] -- Women's Day
Wonder Man(1)[Wonder Boys *] -- Wonder Bar
Wonder Boys(0)[* *] -- Wonder Man
Wonderwall(5)[Wonder Women *] -- Wonder Woman
Wonder Women(4)[* Wonderland] -- Wonderwall
Wonderland(3)[Wonderful Days *] -- Wonder Women
Wonderful Days(2)[Wonder Women!: The Untold Story of American Superheroines Wonderful and Loved by All] -- Wonderland
Wonder Women!: The Untold Story of American Superheroines(0)[* *] -- Wonderful Days
Wonderful and Loved by All(1)[Wonderful World *] -- Wonderful Days
Wonderful World(0)[* *] -- Wonderful and Loved by All

********************
********************
Answers for file 'movies_metadata.txt'
Number of unique movies: 41750
Height of tree: 34
Minimum height for tree to be perfectly balanced: 15
********************
********************
Found node for Four Lions
Node Statistics: 
size = 2; height = 1
Node Structure:
Four Lions(1)[* Four Lovers] -- Four Last Songs
Four Lovers(0)[* *] -- Four Lions

********************
********************
Found node for Wonder Woman
Node Statistics: 
size = 1; height = 0
Node Structure:
Wonder Woman(0)[* *] -- Wonder Women

********************
********************
Found node for Touch of Evil
Node Statistics: 
size = 10; height = 5
Node Structure:
Touch of Evil(5)[Touch and Go Touch of Pink] -- Touchez Pas au Grisbi
Touch and Go(1)[Touch Touch of Death] -- Touch of Evil
Touch(0)[* *] -- Touch and Go
Touch of Death(0)[* *] -- Touch and Go
Touch of Pink(4)[* Touch the Sound] -- Touch of Evil
Touch the Sound(3)[Touch of the Light Touch the Top of the World] -- Touch of Pink
Touch of the Light(0)[* *] -- Touch the Sound
Touch the Top of the World(2)[* Touchback] -- Touch the Sound
Touchback(1)[* Touched with Fire] -- Touch the Top of the World
Touched with Fire(0)[* *] -- Touchback

********************
********************
Found node for Delicatessen
Node Statistics: 
size = 11; height = 7
Node Structure:
Delicatessen(7)[Delbaran Delirious] -- Deja Vu
Delbaran(6)[* Delgo] -- Delicatessen
Delgo(5)[* Delhi-6] -- Delbaran
Delhi-6(4)[Delhi Belly Delicacy] -- Delgo
Delhi Belly(3)[* Delhi in a Day] -- Delhi-6
Delhi in a Day(2)[Delhi Safari *] -- Delhi Belly
Delhi Safari(1)[Delhi Dance *] -- Delhi in a Day
Delhi Dance(0)[* *] -- Delhi Safari
Delicacy(1)[Deli Man *] -- Delhi-6
Deli Man(0)[* *] -- Delicacy
Delirious(0)[* *] -- Delicatessen

********************

"""

from functools import total_ordering

@total_ordering
class Movie:
    """ Represents a single Movie. """

    def __init__(self, movietuple):
        """ Initialise a Movie Object with a tuple of the 7 data elements. """
        if len(movietuple) != 7:
            print("ERROR - not a valid tuple: " + str(movietuple))
        else:
            self._title = movietuple[0]
            self._date = movietuple[1]
            self._time = movietuple[2]
            self._status = movietuple[3]
            self._pop = movietuple[4]
            self._vote = movietuple[5]
            self._count = movietuple[6]

    def __str__(self):
        """ Return a short string representation of this movie. """
        outstr = self._title
        return outstr

    def full_str(self):
        """ Return a full string representation of this movie. """
        outstr = self._title + ": "
        outstr = outstr + str(self._date) + "; "
        outstr = outstr + str(self._time) + "; "
        outstr = outstr + str(self._status) + "; "
        outstr = outstr + str(self._pop) + "; "
        outstr = outstr + str(self._vote) + "; "
        outstr = outstr + str(self._count)
        return outstr

    def get_title(self):
        """ Return the title of this movie. """
        return self._title

    def __eq__(self, other):
        """ Return True if this movie has exactly same title as other. """
        if (other._title == self._title): 
            return True
        return False

    def __ne__(self, other):
        """ Return False if this movie has exactly same title as other. """
        return not (self == other)

    def __lt__(self, other):
        """ Return True if this movie is ordered before other. 

            A movie is ordered before another if it's title is alphabetically
            before. 
        """
        if other._title > self._title:
            return True
        return False

class BSTNode:
    """ An internal node for a BST representing a MovieLibrary.

        Each node will store items with a movie title as a unique key.
    """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

            The string will be created by an in-order traversal.
        """
        outstr = ''
        if self._leftchild:
            outstr = outstr + str(self._leftchild)
        outstr = outstr + ' ' + str(self._element)
        if self._rightchild:
            outstr = outstr + str(self._rightchild)
        return outstr

    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))
    
  
    def search(self, title):
        """ Return the first subtree rooted with that movie title, or None. """

        if self._element.get_title() == title:
            return self
        if self._leftchild:
            node = self._leftchild.search(title)
            if node != None:
                return node
        if self._rightchild:
            node = self._rightchild.search(title)
            if node != None:
                return node
        return None

    def add(self, movie):
        """ Add item to the tree, maintaining BST properties.
            Note: if a movie with same title is already in the tree,
            this does nothing.
        """

        if self._element.__eq__(movie):
            return None

        if not self._element.__lt__(movie):
            if self._leftchild is None:
                self._leftchild = BSTNode(movie)
                self._leftchild._parent = self
            else:
                self._leftchild.add(movie)

        else:
            if self._rightchild is None:
                self._rightchild = BSTNode(movie)
                self._rightchild._parent = self
            else:
                self._rightchild.add(movie)
        
    def findmin(self):
        """ Return the minimal element below this node. 
		    Updated 12/11/2017: should be interpreted as 
			   return the minimal element in the subtree rooted at this node.
		"""
        return self._findminnode()
    
    def _findminnode(self):
        """ Return the BSTNode with the minimal element below this node. 
		    Updated 12/11/2017: should be interpreted as 
			   return the BSTNode with the minimal element in the subtree rooted at this node.
		"""

        if self._leftchild:
            return self._leftchild._findminnode()
        if self._rightchild:
            return self._rightchild._findminnode()
        return self._element

    def findmax(self):
        """ Return the maximal element below this node. 
		    Updated 12/11/2017: should be interpreted as 
			   return the maximal element in the subtree rooted at this node.
		"""
        return self._findmaxnode()

    def _findmaxnode(self):
        """ Return the BSTNode with the maximal element below this node. 
		    Updated 12/11/2017: should be interpreted as 
			   return the BSTNode with the maximal element in the subtree rooted at this node.
		"""

        if self._rightchild:
            return self._rightchild._findmaxnode()
        if self._leftchild:
            return self._leftchild._findmaxnode()
        return self._element
    
    def height(self):
        """ Return the height of this node.

            Note that with the recursive definition of the tree the height
            of the node is the same as the depth of the tree rooted at this
            node.
        """

        leftheight = -1
        if self._leftchild:
            leftheight = self._leftchild.height()
        rightheight = -1
        if self._rightchild:
            rightheight = self._rightchild.height()
        return 1 + max(leftheight, rightheight)

    def size(self):
        """ Return the size of this subtree.

            The size is the number of nodes (or elements) in the tree.
        """

        if self._leftchild:
            leftsize = self._leftchild.size()
        else:
            leftsize = 0
        if self._rightchild:
            rightsize = self._rightchild.size()
        else:
            rightsize = 0

        return 1 + leftsize + rightsize

    def leaf(self):
        """ Return True if this node has no children. """

        if self._leftchild or self._rightchild:
            return False
        return True

    def semileaf(self):
        """ Return True if this node has exactly one child. """

        if self._leftchild and self._rightchild or self.leaf():
            return False
        return True

    def full(self):
        """ Return true if this node has two children. """

        if self._leftchild and self._rightchild:
            return True
        return False

    def internal(self):
        """ Return True if this node has at least one child. """

        if self._leftchild or self._rightchild:
            return True
        return False

    def remove(self, title):
        """ Remove and return a movie.

            Remove the movie with the given title from the tree rooted
            at this node.

            Maintains the BST properties.
        """

        movie = self.search(title)
        if movie:
            return movie._remove_node()
            
    def _remove_node(self):
        """ (Private) Remove this BSTBode from its tree.

            Maintains the BST properties.
        """
        #if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild up into its place, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild up into its place, and clean up
            #return the original element

        if self._parent:

            if self.full():
                temp = self
                left_max = self._leftchild.findmax()
                node = self.search(str(left_max))
                node._parent._leftchild = None
                node = None
                self._element = left_max
                return temp

            elif self.leaf():
                temp = self
                parent = self._parent
                if parent._leftchild:
                    parent._leftchild = None
                else:
                    parent._rightchild = None
                self._parent = None
                self = None
                return temp

            elif self._leftchild:
                temp = self
                if self._leftchild._element > self._parent._element:
                    self._leftchild._parent = self._parent
                    self._parent._rightchild = self._leftchild
                    self._leftchild = None
                else:
                    self._leftchild._parent = self._parent
                    self._parent._leftchild = self._leftchild
                    self._rightchild = None
                self.remove(self)
                return temp

            else:
                temp = self
                if self._rightchild._element > self._parent._element:
                    self._rightchild._parent = self._parent
                    self._parent._rightchild = self._rightchild
                    self._rightchild = None
                else:
                    self._rightchild._parent = self._parent
                    self._parent._leftchild = self._rightchild
                    self._leftchild = None
                self.remove(self)

            return temp

        else:
            if self._leftchild:

                left_max = self._leftchild.findmax()
                node = self.search(str(left_max))
                node._parent._leftchild = None
                node = None
                self._element = left_max
            else:
                right_min = self._rightchild.findmin()
                node = self.search(str(right_min))
                node._parent._rightchild = None
                node = None
                self._element = right_min


    def _pullup(self, node):
        """ Pull up the data from a child (subtree) node into this BSTNode.

            Note: rather than updates the links so that the child node takss
            the place of the removed semileaf, instead, we will copy the
            child's element into the semileaf, and then readjust the links, and
            then remove the now empty child node. This measn that when we remove
            a root semileaf, the code that called the remove method still
            maintains a reference to the root of the tree, and so can continue
            processing the tree (otherwise, if we remvoed the actual BSTNode
            that was the root, the calling code would lose all reference to
            the tree). 
        """
        #method body here
        
    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        outstr = str(self._element) + '(' + str(self.height()) + ')['
        if self._leftchild:
            outstr = outstr + str(self._leftchild._element) + ' '
        else:
            outstr = outstr + '* '
        if self._rightchild:
            outstr = outstr + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '*]'
        if self._parent:
            outstr = outstr + ' -- ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- *'
        print(outstr)
        if self._leftchild:
            self._leftchild._print_structure()
        if self._rightchild:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False          
        if self._parent:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok

    def _testadd():
        node = BSTNode(Movie(("Memento", "11/10/2000", 113, "Released", 15.45, 8.1, 4168)))
        node._print_structure()
        print('> adding Melvin and Howard')
        node.add(Movie(("Melvin and Howard", "19/09/1980", 95, "Released", 6.737, 6.8, 18)))
        node._print_structure()
        print('> adding a second version of Melvin and Howard')
        node.add(Movie(("Melvin and Howard", "21/03/2007", 112, "Released", 4.321, 3.5, 7)))
        node._print_structure()
        print('> adding Mellow Mud')
        node.add(Movie(("Mellow Mud", "21/09/2016", 92, "Released", 9.321, 9.5, 7001)))
        node._print_structure()
        print('> adding Melody')
        node.add(Movie(("Melody", "21/03/2007", 113, "Released", 5.321, 3.5, 7)))
        node._print_structure()
        return node
            
    def _test():
        node = BSTNode(Movie(("B", "b", 1, "b", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "A")
        node.add(Movie(("A", "a", 1, "a", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "A")
        node.remove("A")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie(("C", "c", 1, "c", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "F")
        node.add(Movie(("F", "f", 1, "f", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie(("C", "c", 1, "c", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "D")
        node.add(Movie(("D", "d", 1, "d", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie(("C", "c", 1, "c", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "E")
        node.add(Movie(("E", "e", 1, "e", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "D")
        node.remove("D")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "E")
        node.remove("E")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "L")
        node.add(Movie(("L", "l", 1, "l", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "H")
        node.add(Movie(("H", "h", 1, "h", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "I")
        node.add(Movie(("I", "i", 1, "i", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "G")
        node.add(Movie(("G", "g", 1, "g", 1, 1, 1)))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "L")
        node.remove("L")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "H")
        node.remove("H")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "I")
        node.remove("I")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "G")
        node.remove("G")
        print('Ordered:', node)
        node._print_structure()
        print(node)

            
def read_movies(filename):
    """ Read and return a list of movies. """
    movies = []
    file = open(filename, 'r')
    count = 0
    for line in file:
        line = line.replace('\n','')
        new_tuple = tuple(line.split('\t'))
        movies.append(Movie(new_tuple))
        #print(new_tuple[0])
        count += 1
    file.close()
    #for movie in movies:
        #print(movie)
    print("Read in " + str(count) + " movies ...")
    return movies

def build_tree(filename):
    movielist = read_movies(filename)
    bst = BSTNode(movielist[-1])
    movielist.pop()
    for movie in movielist:
        #print("Adding movie ", movie)
        bst.add(movie)
    print("Built a tree of height " + str(bst.height()))
    return bst


