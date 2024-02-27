class Bruh():
    def __init__(self) -> None:
        pass

    def something(self):
        self.lul()
    
    def lul(self):
        print('idk how it works')
    
    print('oi')

# Works
bro = Bruh()
bro.something()

# doesn't work
Bruh.something()