class Movie:

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

    def __init__(self, element, prevnode, nextnode):

        self._element = element
        self._next = nextnode
        self._prev = prevnode

class FlixNetLibrary:

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

    def add_movie(self, movie):
        
        if self._size == 0:
            prevnode = self._tail._prev
            nextnode = self._tail
        else:
            node = self._head._next
            
            while node:
                if node == self._tail._prev:
                    prevnode = node
                    nextnode = node._next
                    break
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
        
        if self._cursor:
            print ('Current Movie: ' + str(self._cursor._element))
        return None

    def next_movie(self):
        
        if self._cursor is None or self._cursor._next == self._tail:
            self.reset()
        else:
            self._cursor = self._cursor._next

    def prev_movie(self):
        if self._cursor == self._head._next or self._cursor is None:
            self._cursor = self._tail._prev
        else:
            self._cursor = self._cursor._prev

    def reset(self):

        self._cursor = self._head._next

    def play(self):

        if self._cursor:
            print ("Currently playing: " + self._cursor._element.play() )
        else:
            return None

    def remove_current(self):

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
        self._cursor = nextmovie

    def length(self):

        print( "Number of movies in library: " +  str(self._size) )

    def search_movie(self, name):
        
        # Check cursor has been set
        if not self._cursor:
            return None

        current = self._cursor
        library_count = self._size
        count = 1

        while library_count > count:
            if name in current._element.get_title():
                self._cursor = current
                return True
            self.next_movie()
            current = self._cursor
            count += 1
        return False

    def search_director(self, name):

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

