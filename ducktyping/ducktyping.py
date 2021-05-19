class Vscode:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("executing using vscode")
    def debug(self):
        print("debugging using vscode")

class Atom:
    def compile(self):
        print("compiling using atom")
    def execute(self):
        print("executing using atom")
    def debug(self):
        print("debugging using atom")


class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()

devop=Programmer()
pyc=Vscode()
devop.coding(pyc)




