class Person:
    def __init__(self, intitialAge):

        if intitialAge < 0:
            print("age is not valid, set age to zero")
            self.age = 0
        else:
            self.age = intitialAge

    def Yearpasses(self):
        self.age += 1

    def AmIold(self):
        if self.age <= 13:
            print("you're young")
        elif self.age >= 13 and self.age <= 18:
            print("you're teenager")
        else:
         print("you're Old")


t = int(input())
for i in range(0, t):
     p= Person(intitialAge=int(input()))
     p.AmIold()
     p.Yearpasses()
