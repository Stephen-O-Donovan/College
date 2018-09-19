class Movie:

    def __init__(self, name, director, dateadded, viewed):

        self._name = name
        self._director = director
        self._dateadded = dateadded
        self._viewed = viewed

    def __str__(self):

        return ' ("' + self._name + '", "' + self._director + '", ' \
                      + str(self._dateadded) + ', ' + str(self._viewed) + ')'

    def get_title(self):

        return self._name

    def play(self):

        self._viewed = True
        return self.__str__()

class DLLNode:

    def __init__(self, element, prevnode, nextnode):

        self._element = element
        self._next = nextnode
        self._prev = prevnode

class DLinkedList:

    def __init__(self):

        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0
        self._cursor = None

    def __str__(self):

        outstr = "---\n"

        node = self._head._next
        while node:
            if node == self._tail:
                break
            outstr = outstr + '"'+ node._element.get_title()
            if self._cursor == node:
                outstr += ' *** Current Selection***'
            outstr += '"\n'
            node = node._next
        return outstr + "---\n\n"

    def add(self, movie, prevnode, nextnode):

        newnode = DLLNode( movie, prevnode, nextnode)
        prevnode._next = newnode
        nextnode._prev = newnode
        self._size += 1

    def current(self):
        if self._cursor:
            return self._cursor._element
        return None

    def get_next(self):

        self._cursor = self._cursor._next
        if  self.current()== None:
            self.reset()

    def get_prev(self):

        self._cursor = self._cursor._prev
        if  self.current()== None:
            self.get_last()

    def reset(self):

        self._cursor = self._head._next

    def get_last(self):

        self._cursor = self._tail._prev

    def play(self):
        if self._cursor:
            print ("Currently playing: " + self._cursor._element.play() )
        else:
            return None

    def remove(self, node):

        prevnode = node._prev
        nextnode = node._next
        prevnode._next = nextnode
        nextnode._prev = prevnode
        self._size -= 1
        prevnode = None
        nextnode = None
            
    def length(self):

        return self._size

    def search_by_movie(self, name):

        # Check cursor has been set
        if not self._cursor:
            return False
        current = self._cursor
        library_count = self.length()
        count = 1

        while library_count >= count:
            if name in current._element.get_title():
                self._cursor = current
                return True
            self.get_next()
            current = self._cursor
            count += 1
        return False

    def search_by_director(self, name):

        # Check cursor has been set
        if not self._cursor:
            return False
        current = self._cursor
        library_count = self.length()
        count = 1

        while library_count >= count:
            if current._element._director == name:
                self._cursor = current
                return True
            self.get_next()
            current = self._cursor
            count += 1
        return False
        

class FlixNetLibrary:

    def __init__(self):

        self._library = DLinkedList()

    def __str__(self):

        return self._library.__str__()

    def add_movie(self, movie):
        
        if self._library.length() == 0:
            self._library.add(movie, self._library._tail._prev, self._library._tail)
        else:
            node = self._library._head._next
            
            while node:
                if node == self._library._tail._prev:
                    self._library.add(movie, node, node._next)
                    break
                elif node._element._dateadded < movie._dateadded:
                    self._library.add(movie, node._prev, node)
                    break
                node = node._next

    def get_current(self):

        print( "Current Movie: " + str(self._library.current()) )

    def next_movie(self):

        if self._library._cursor:
            self._library.get_next()
        else:
            self._library.reset()

    def prev_movie(self):

        if self._library._cursor:
            self._library.get_prev()
        else:
            self._library.get_last()

    def reset(self):

        self._library.reset()

    def play(self):

        self._library.play()

    def remove_current(self):

        # For empty list
        if self._library._cursor == None or self._library._size == 0:
            self._library._cursor = None
            return None
        
        # moves cursor to first item if removing last item 
        if self._library._cursor._next._element: 
            nextnode = self._library._cursor._next
        else:
            nextnode = self._library._head._next

        current = self._library._cursor
        self._library.remove(current)
        self._library._cursor = nextnode

    def length(self):

        print( "Number of movies in library: " +  str(self._library.length() ) )

    def search_movie(self, name):

        return self._library.search_by_movie(name)

    def search_director(self, name):

        return self._library.search_by_director(name)

