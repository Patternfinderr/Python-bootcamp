
from abc import abstractmethod
from enum import Enum

# from solid_design_principles import dependancy_inversion_principle
from solid_design_principles.dependancy_inversion_principle import (
            Person,
            Linkedlist,
            Relationships,
            Research
        )

amir = Person("Amir")
child1 = Person("Tyson")
child2 = Person("Taker")

brenda = Person("Brenda")
child3 = Person("cherry")
child4 = Person("Apple")

"""
    we know that at this point we have a parent and children relationship

    Now we need to build a Relationship between the parent and other parents 
    which has relationship to the parent and not the children 

"""

relationsiphs = Relationships()
relationsiphs.add_parent_and_child(amir, child1)
relationsiphs.add_parent_and_child(amir, child2)

Research(amir, relationsiphs)

# print(relationsiphs.relations)

