
class Threat:
    
    def __init__(self,description, location, damage, time):
        self.description = description
        self.location = location
        self.damage = float(damage)
        self.time = float(time)
    def __str__(self):
        return 'Threat:\nDescription:{}\nLocation:{}\nDamage:{}\nTime:{}'.format(self.description,self.location,self.damage,self.time)
    
    
    
'''
treat1 = Threat('Aliens',(5,-2),200,50)
print(treat1.__str__())
'''
