"""
    SRP: single responsibility principle
    SOC: sepearate of concern

    Takeaway from this is to not over load your primary object 
    with too many responsibilities
"""

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text) -> None:
        self.count += 1
        self.entries.append(f"{self.count}:{text}")

    def remove_entry(self, pos) -> None:
        del self.entries[pos]

    def __str__(self) -> list:
        return '\n'.join(self.entries)
    
    # extra and adding more responsibility
    # when adding below more responsibility it breaks the single responsibility principle
    # def save(self, filename) -> None:
    #     file = open(filename)
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename) -> None:
    #     pass
    #
    # def low_from_web(self, uri) -> None:
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename) -> None:
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry("Testing 1")
j.add_entry("Testing 2")
print(f"Journal entries:\n{j}")

# serialize data to file and reading from file is a better solution
file = "journal.txt"
PersistenceManager.save_to_file(j, file)

# with open(file) as file:
#     print(file.read())
