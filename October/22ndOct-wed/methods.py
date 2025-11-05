print(
    '''
    *****************
    * Class Methods *
    *****************
    '''
)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello {self.name}")
        print(f"Your age is {self.age}")
    def celebrating_birthday(self):
        self.age+=1
        print(f"Happy Birthday You are now {self.age}")
    
obj1=Person("Linus",30)
print(obj1.name)
obj1.greet()
print("\n")
print("Modifying Properties in Methods....")
obj1.celebrating_birthday()
obj1.celebrating_birthday()
print("\n")
print("Multiple Methods in a class...")
class Colors:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_songs(self,song):
        self.songs.append(song)
        print(f"Added : {song}")
    def rm_songs(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed : {song}")
    def display(self):
        print(f"PlayList : {self.name}")
        for song in self.songs:
            print(f"- {song}")

obj2=Colors("Fav")
obj2.add_songs("FDsds")
obj2.add_songs("FDdds")
obj2.rm_songs("FDsds")
obj2.display()
        
