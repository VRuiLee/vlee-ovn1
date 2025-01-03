# Victoria Lee, grudat24 upg 1.2

class ListElement:
    """A list element that stores a value of type T."""

    def __init__(self, data=None, next=None):
        """The constructor that is called when we create a new element"""
        self.data = data
        self.next = next  

class LinkedList:
    """A singly linked list of elements of type T"""

    def __init__(self):
        """Create an empty list"""
        self._first = None
        self._last = None
        self._size = 0
        

    def addFirst(self, element): #Chatgpd void = ingen return och hur en lista i en class funkar
        """Insert the given element at the beginning of this list."""
        # Time O(1) constant regardless of n
        new_element = ListElement(element, self._first)
        self._first = new_element
        self._size += 1
        if self._size == 1:  #Om det bara finns ett element i listan, är det både det första och sista
            self._last = new_element
        

    def addLast(self, element):
        """Insert the given element at the end of this list."""
        # O(1) constant regardless of n
        new_element = ListElement(element)
        if self._size == 0:
            self._first = self._last = new_element
        else:
            self._last.next = new_element
            self._last = new_element
        self._size += 1
     
       
    
    def getFirst(self):
        """Return the first element of this list.
        Return null if the list is empty."""
        # O(1) constant regardless of n
        
        return self._first.data if self._first else None

    def getLast(self):   
        """Return the last element of this list.
        Return null if the list is empty."""
        # O(1) constant regardless of n
        return self._last.data if self._last else None

    
    def get(self, index):
        """Return the element at the specified position in this list.
        Return null if index is out of bounds."""
        # O(n) can go through the whole list, for loop

        if not isinstance(index,int) or index >= self._size or index < 0:
            return None
        
        element = self._first
        for i in range(index):
            element = element.next
        return element.data


    def removeFirst(self):
        """Remove and returns the first element from this list.
        Return null if the list is empty."""
        # O(1) constant regardless of n
        if self._size == 0:
            return None
        
        first = self._first.data
        self._first = self._first.next
        self._size -= 1
    
        if self._size == 0:
            self._last = self._first

        return first


    def clear(self):
        """Remove all elements from this list."""
        # O(1) constant regardless of n
    
        self._first = None
        self._last = None
        self._size = 0
        


    def size(self):
        """Return the number of elements in this list"""
        # O(1) constant regardless of n
        return self._size


    
    def string(self):
        """Return a string representation of this list.
        The elements are enclosed in square brackets ("[]").
        Adjacent elements are separated by ", "."""
        #O(n) goes through the whole list, for loop

        element = self._first
        text = []

        for i in range(self._size):
            text.append(str(element.data))
            element = element.next
        return '[' + ', '.join(text) + ']'


# Unit test

def main():
    """Unit test for LinkedList()"""
    l = LinkedList()

    # Test empty list
    assert l.getFirst() == None
    assert l.getLast() == None
    assert l.get(0) == None
    assert l.removeFirst() == None
    assert l.size() == 0
    assert l.string() == '[]'

    # Test addFirst and addLast 
    l.addFirst('a')
    assert l.getFirst() == 'a'
    assert l.getLast() == 'a'

    l.addLast(3)
    l.addFirst(2)
    l.addLast(True)

    # Test string and size
    assert l.string() == '[2, a, 3, True]'
    assert l.size() == 4

    # Test getFirst and getLast
    assert l.getFirst() == 2
    assert l.getLast() == True

    # Test removeFirst
    assert l.removeFirst() == 2
    assert l.size() == 3
    assert l.getFirst() == 'a'

    # Test get
    assert l.get(0) == 'a'
    assert l.get(2) == True
    assert l.get(3) == None
    assert l.get('a') == None
    
    
    # Test clear
    l.clear()
    assert l.size() == 0
    assert l.string() == '[]'

    # Test add and remove
    l.addFirst(3)
    l.removeFirst()
    assert l.getFirst() == None
    assert l.getLast() == None 
    assert l.size() == 0

    
    print ("The test is done")


if __name__ == "__main__":
    main()
        
