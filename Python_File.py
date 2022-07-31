"""
Created on Sun Jul 31 16:46:21 2022
Created By Alistair Thorogood
July 2022
for MEC4406 Week 1
"""

#Initialise variables
i = 0
favNum = 3

# Write in python that prints your name
print ("Alistair Thorogood")

#count to favourite number squared and print
for i in range (0, favNum**2):
    i += 1
    print (i)
    
class Engineers:
    def getSkill(self):
        print("Skill = Problem Solver")
    def __init__(self, name, engType, experience):
        self.name = name
        self.engType = engType
        self.experience = experience
    def getName(self):
            print("Name = " + self.name)
    def getType(self):
            print("Discpline = " + self.engType)
    def getExperience(self):
            print("Years Experience = " + self.experience + " Years")
    def getAttribute(self):
        self.getSkill()
        self.getName()
        self.getType()
        self.getExperience()


engineer1 = Engineers("Bob", "Mechanical", "5")
engineer2 = Engineers("Mary", "Chemical", "25")

print("\nEngineer 1 has following attributes:")
engineer1.getAttribute()

print("\nEngineer 2 has following attributes:")
engineer2.getAttribute()


