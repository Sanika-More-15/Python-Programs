class BookStore:
    NoOfBooks=0

    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        
        BookStore.NoOfBooks += 1

    def Display(self):
        print("Book Name is :",self.Name)
        print("Author Name is :",self.Author)


b1=BookStore("Clean Code","Robert C.Martin")
b2=BookStore("The Alchemist","Paulo Coelho")

b1.Display()
print()

b2.Display()
print()

print("Total no of Books :",BookStore.NoOfBooks)

    

    