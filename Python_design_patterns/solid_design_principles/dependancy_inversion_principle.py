
from abc import abstractmethod
from enum import Enum

class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.next = None

class Linkedlist:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def traverse(self) -> None:
        if self.count > 0:
            current = self.head
            while current:
                print(current.value, '-> ', end='')
                current = current.next
            print()
       
    def append(self, value:object) -> bool:
        node = Person(value)
        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
        return True
    
    def pop(self) -> None:
        if self.count > 0:
            temp = self.head
            if self.count == 1:
                self.head = None
                self.tail = None
            else:
                pre = None
                while temp:
                    pre = temp
                    temp = temp.next
                self.tail = pre
                self.tail.next = None
            self.count -= 1
            return temp

"""
    This is a principle that states high-level modules should  
    depend on abstractions rather then concrete implementations

    Now the idea behind concrete is that all methods in the class
    has implementations and this is something we have to stay away 
    from and so its best to use the idea of dependency inversion 
    behavior so that we make sure not all methods have but should be 
    used for its own purposes 
"""

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class RelationshipBrowser: # High level
    @abstractmethod
    def find_all_children_of(self, name): pass

class Relationships(RelationshipBrowser): # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append( (parent, Relationship.PARENT, child) )
        self.relations.append( (child, Relationship.PARENT, parent) )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:
    # dependency of a low level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, Relationships):
    #     # high level: find all of johns children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'john' and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}")

    def __init__(self, parent, browser):
        for p in browser.find_all_children_of(parent):
            print(f"John has a child called {p}")

# parent = Person("John")
# child1 = Person("Chris")
# child2 = Person("Matt")
#
# # low level module
# relationships = Relationships()
# relationships.add_parent_and_child(parent, child1)
# relationships.add_parent_and_child(parent, child2)
#
# Research(relationships)




