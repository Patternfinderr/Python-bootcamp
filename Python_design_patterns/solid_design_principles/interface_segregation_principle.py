from abc import abstractmethod

class Machine:
    def print(self, document) -> None:
        raise NotImplementedError()

    def fax(self, document) -> None:
        raise NotImplementedError()

    def scan(self, document) -> None:
        raise NotImplementedError()

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        # okay - print stuff
        pass

    def fax(self, document):
        pass # do nothing because old printer dont fax

    def scan(self, document):
        """Not Supported"""
        raise NotImplementedError("Printer cannot scan")

class Printer:
    @abstractmethod
    def print(self, document): pass

class Scanner:
    @abstractmethod
    def scan(self, document): pass

class Fax:
    @abstractmethod
    def fax(self, document): pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class MyScanner(Scanner):
    def scan(self, document) -> None:
        print(document)

class MyFaxer(Fax):
    def fax(self, document) -> None:
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        scan(document)

class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner, fax) -> None:
        self.printer = printer
        self.scanner = scanner
        self.faxer = fax

    def print(self, document) -> None:
        self.printer.print(document)

    def scan(self, document) -> None:
        self.scanner.scan(document)

    def fax(self, document) ->None:
        self.faxer.fax(document)

# old_printer = OldFashionedPrinter()
# old_printer.print(123)

printer = MyPrinter()
scanner = MyScanner()
faxer = MyFaxer()

mfm = MultiFunctionMachine(printer, scanner, faxer)

mfm.print("write something on the board")
mfm.scan("Scanning something")
mfm.fax("Sending something through fax")








