#I just learned what classes are today and I think this will be best to get the appropriate key/values for ffxiv crafting
#Will need to iterate through each "Name" key to find the values
#Bonuses.*.Value is the percentage
class Meals:

    def __init__(self, cp_percent, cp_value, craft_percent, craft_value, hq, id, name):
        self.cp_percent = cp_percent
        self.cp_value = cp_value
        self.crafsmanship_percent = craft_percent
        self.crafsmanship_value = craft_value
        self.hq = hq
        self.id = id
        self.name = {name}
