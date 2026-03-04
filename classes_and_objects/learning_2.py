class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce_self(self):
        return f'My name is {self.name}'

r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 40)
print(r1.introduce_self())
print(r2.introduce_self())

class Person:
    def __init__(self, name, personality, is_Sitting):
       self.name = name
       self.personality = personality
       self.is_Sitting = is_Sitting
       
       
    def sit_Down(self):
        self.is_Sitting = 'True'
            
    def stand_Up(self):
       self.is_Sitting = 'False'
    
p1 = Person('Ana', 'aggressive', False)
p2 = Person('Becky', 'talkative', True)
    
       
p1.robot_owned = r2
p2.robot_owned = r1

print(p1.robot_owned.introduce_self())