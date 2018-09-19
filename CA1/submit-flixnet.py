"""
Stephen O'Donovan
102554291

Creates a library of movie objects implemented as
a doubly-linked list
"""

class Movie:
    """Class to create Movie Objects"""

    def __init__(self, name, director, dateadded, viewed):

        self._name = name
        self._director = director
        self._dateadded = dateadded
        self._viewed = viewed

    def __str__(self):

        return '("' + self._name + '", "' + self._director + '", ' \
                      + str(self._dateadded) + ', ' + str(self._viewed) + ')'

    def get_title(self):

        return self._name

    def play(self):

        self._viewed = True
        return self.__str__()

class DLLNode:
    """An internal node in a doubly-linked list"""

    def __init__(self, element, prevnode, nextnode):

        self._element = element
        self._next = nextnode
        self._prev = prevnode

class FlixNetLibrary:
    """Creates a list of Movie Objects, sorted by date descending
       and uses various methods to add, delete, play, search,
       report and move through list"""

    def __init__(self):

        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0
        self._cursor = None

    def __str__(self):
        """Returns a list of the movie names in the library.
           Also indicates which, if any, movie is currently selected"""

        outstr = "---\n"

        node = self._head._next
        while node != self._tail:
            outstr = outstr + '"'+ node._element.get_title()
            if self._cursor == node:
                outstr += ' *** Current Selection ***'
            outstr += '"\n'
            node = node._next
        return outstr + "---\n\n"

    def add_movie(self, movie):
        """Adds movies to library in order of date descending"""

        # Checks first if list is empty
        if self._size == 0: 
            prevnode = self._tail._prev
            nextnode = self._tail
        else:
            node = self._head._next
            
            while node:
                # Checks if at end of list
                if node == self._tail._prev: 
                    prevnode = node
                    nextnode = node._next
                    break
                # Checks if movie is newer than currently compared movie
                elif node._element._dateadded < movie._dateadded:  
                    prevnode = node._prev
                    nextnode = node
                    break
                node = node._next
                
        newnode = DLLNode( movie, prevnode, nextnode)
        prevnode._next = newnode
        nextnode._prev = newnode
        self._size += 1

    def get_current(self):
        """Prints the currently selected movie, if any"""
        
        if self._cursor:
            print ('Current Movie: ' + str(self._cursor._element))

    def next_movie(self):
        """Moves to the next movie in the library.
           Moves to start of library if currently at end or nothing
           currently selected"""
        
        if self._cursor is None or self._cursor._next == self._tail:
            self.reset()
        else:
            self._cursor = self._cursor._next

    def prev_movie(self):
        """Moves to the previous movie in the library.
           Moves to end of library if currently at start or nothing
           currently selected"""
        
        if self._cursor == self._head._next or self._cursor is None:
            self._cursor = self._tail._prev
        else:
            self._cursor = self._cursor._prev

    def reset(self):
        """Moves to first movie in the library"""

        self._cursor = self._head._next

    def play(self):
        """Reports the currently selected movie, if one is selected,
           and sets its boolean 'viewed' to True"""

        if self._cursor:
            print ("Currently playing: " + self._cursor._element.play() )

    def remove_current(self):
        """Deletes the currently selected movie, returns 'None' if
           nothing selected or list is empty"""

        # for empty list or unset cursor
        if self._cursor == None or self._size == 0:
            return None
        
        # moves cursor to first movie if removing last movie
        if self._cursor._next == self._tail:
            nextmovie = self._head._next
        else:
            nextmovie = self._cursor._next

        current = self._cursor
        prevnode = current._prev
        nextnode = current._next
        prevnode._next = nextnode
        nextnode._prev = prevnode
        self._size -= 1

        # clears cursor if list is empty
        if self._size == 0:
            self._cursor = None
        else:
            self._cursor = nextmovie

    def length(self):
        """Reports the number of movies in the library"""

        print( "Number of movies in library: " +  str(self._size) )

    def search_movie(self, name):
        """Searches by string or substring for movie by name.
           Begins at currently selected movie and wraps the list if necessary.
           If found, sets movie as current selection and returns True,
           otherwise returns False"""
        
        # Check cursor has been set
        if not self._cursor:
            return None

        current = self._cursor
        library_count = self._size
        count = 0

        while library_count > count:
            if name in current._element.get_title():
                self._cursor = current
                return True
            self.next_movie()
            current = self._cursor
            count += 1
        return False

    def search_director(self, name):
        """Searches by string or substring for movie by director.
           Begins at currently selected movie and wraps the list if necessary.
           If found, sets movie as current selection and returns True,
           otherwise returns False"""

        # Check cursor has been set
        if not self._cursor:
            return None

        current = self._cursor
        library_count = self._size
        count = 1

        while library_count > count:
            if name in current._element._director:
                self._cursor = current
                return True
            self.next_movie()
            current = self._cursor
            count += 1
        return False

