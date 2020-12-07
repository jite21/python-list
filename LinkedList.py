# -*- coding: utf-8 -*-
"""
Spyder Editor

This py file has LinkedList, queue, stack and graph Implementation
1. Iterable
2. Magic/Dunder functions in python
3. Tree implementation.
4. BFS, DFS implementation
"""

class IndexNotFoundException(Exception):
    '''If Inded is not present in the List'''
    
    def __str__(self):
        return 'Custom Exception Raised when Index is not found'


class Node:
    '''Node class which will hold value and next_node'''
    
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    '''Linked List implementation in python'''
    
    def __init__(self):
        '''
        Set length, start and end of the linkedlist
        '''
        
        self._len = 0
        self._start = None
        self._end   = None
    
    def additem(self,value):
        '''
        Adds a node to end of the list
        '''
        
        temp = Node(value)
        if self._start == None:
           self. _start,self._end = temp,temp
        else:
            self._end.next_node,self._end = temp,temp
        
        self._len += 1
    
    def _getitem(self,index):
        '''
        To get element from the linkedlist
        '''
        
        i = 0
        temp = self._start
        while temp and i != index:
            i += 1
            temp = temp.next_node
            
        return temp
    
    def __len__(self):
        '''
        Dunder function to get the length of the list.
        
        l = LinkedList()
        l.additem(1)
        len(l)
        '''
        
        return self._len
    
    def __getitem__(self,index):
        '''
        Dunder function to get an item in LinkedList
        
        l = LinkedList()
        l.additem(1)
        l[0]
        '''
        
        index = index if index >= 0 else self._len + index
        if index < 0:
            raise IndexNotFoundException
        
        temp = self._getitem(index)
        if temp:
            return temp.value
        else:
            raise IndexNotFoundException
        
    def __setitem__(self,index,value):
        '''
        To update in LinkedList
        
        l = LinkedList()
        l.additem(1)
        l[0] = 'Test'
        '''
        
        index = index if index >= 0 else self._len + index
        if index > self._len-1:
            raise IndexNotFoundException

        temp = self._getitem(index)
        temp.value = value
        
    # Iter and next function will make Linked list Iterable
    def __iter__(self):
        self._next = self._start
        return self
    
    def __next__(self):
        if not self._next:
            raise StopIteration
        else:
            temp = self._next
            self._next = self._next.next_node
            return temp
        
    def __str__(self):
        '''
        To convert to String and to make it usable with python print statement
        
        l = LinkedList()
        l.additem(1)
        print(l)
        '''
        
        s = ''
        temp = self._start
        while temp:
            s += str(temp.value) + ' '
            temp = temp.next_node
            
        return s
    
    def deletefirstnode(self):
        if self._start == self._end:
            #if we have only one node left in list
            self._start = None
            self._end = None
        else:
            #if we have only two or more node left in list
            prev_start = self._start
            new_start = prev_start.next_node
            prev_start = None
            self._start = new_start
            
    def deletelastnode(self):
        if self._start == self._end:
            #if we have only one node left in list
            self._start = None
            self._end = None
        else:
            #if we have only two or more node left in list
            temp = self._getitem(self._len-2)
            temp.next_node = None
            self._end = None
            self._end = temp
            
    def deletemidnode(self,index):
        temp = self._getitem(index)
        nextnode = temp.next_node
        temp.value = nextnode.value
        temp.next_node = nextnode.next_node
        nextnode = None
        
    def __delitem__(self, index):
        '''
        To delete an item from LinkedList.
        
        l = LinkedList()
        l.additem(1)
        del(l[0])
        '''
        
        index = index if index >= 0 else self._len + index
        if index > self._len-1 or index < 0:
            raise IndexNotFoundException
            return None
        
        if index == 0:
            self.deletefirstnode()
        elif index == self._len-1:
            self.deletelastnode()
        else:
            self.deletemidnode(index)

        self._len -= 1
                   
            
class MyQueue:
    '''This is queue Implementation : FIFO'''

    def __init__(self):
        self._l = LinkedList()
        pass
    
    def add(self,value):
        self._l.additem(value)
        
    def top(self):
        return self._l[0]
        
    def remove(self):
        try:
            del self._l[0]
        except IndexNotFoundException:
            print('Queue Empty')
        except Exception as e:
            print(str(e))
        
    def __str__(self):
        return str(self._l)
    
    def length(self):
        return len(self._l)
    
    def __len__(self):
        return self.length()
    
    def __iter__(self):
        return self._l.__iter__()
    
    def __next__(self):
        return self._l.__next__()
    
        
class MyStack:
    '''This is a Stack Implementation : LIFO'''

    def __init__(self):
        self._l = LinkedList()
        pass
    
    def add(self,value):
        self._l.additem(value)
        
    def top(self):
        return self._l[-1]
        
    def remove(self):
        try:
            del self._l[-1]
        except IndexNotFoundException:
            print('Queue Empty')
        except Exception as e:
            print(str(e))
        
    def __str__(self):
        return str(self._l)
    
    def length(self):
        return len(self._l)
    
    def __len__(self):
        return self.length()
    
    def __iter__(self):
        return self._l.__iter__()
    
    def __next__(self):
        return self._l.__next__()
    
class MyBasicGraph():
    '''Tree Implementation this is 0 based index so '0' will be the root'''
    
    def __init__(self, verts=None):
        self._tree = LinkedList()
        if verts:
            self.addverts(verts)
                
    def addverts(self, verts):
        for i in range(verts):
            self._tree.additem(LinkedList())

    def addedge(self, from_vert, *to_verts):
        for vert in to_verts:
            self._tree[from_vert].additem(vert)
            
    def getedge(self,vert):
        return self._tree[vert]
    
    def getverts(self):
        return range(len(self._tree))
            
    def __str__(self):
        s = 'FROM ---> TO\n'
        for (i,vert) in enumerate(self._tree):
            s += str(i)+' ---> '
            for j in self.getedge(i):
               s += str(j.value)+ ', '
            s += '\n'
               
        return s

class GraphTraversal:
    '''BFS and DFS tree traversal'''
    
    @staticmethod
    def traverse(graph, q):
        '''
        static method to traverse graphs, BFS and DFS, based on object passed in q
        if q is stack then DFS
        if q in queus then BFS
        
        Using duck-typing here.
        '''
        
        visited = set()
        s = ''
        
        visit = 0
        q.add(visit)
        visited.add(visit)
        while len(q):
            visit = q.top()
            s += str(visit) + ' '
            q.remove()
            
            for i in graph.getedge(visit):
                if i.value not in visited:
                    visited.add(i.value)
                    q.add(i.value)
                
        return s

if __name__ == '__main__':
    l = LinkedList()
    l.additem('test1')
    l.additem('test2')
    l.additem('test3')
    l.additem('test4')
    l.additem('test5')
    
    print('values in Linked List : ',l)
    
    q = MyQueue()
    q.add(1)
    q.add('test')
    q.add(3.0)
    q.add(4)
    q.add(5)
    
    print('value in queue : ',q)
    
    g = MyBasicGraph(6)
    g.addedge(0,1,2,5)
    g.addedge(1,3,5)
    g.addedge(2,4)
    g.addedge(3,4)
    bfs = GraphTraversal.traverse(g, MyQueue())
    dfs = GraphTraversal.traverse(g, MyStack())
    
    print('Graph :: \n',g)
    print('BFS :: ', bfs)
    print('DFS :: ',dfs)