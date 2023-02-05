# I just learned what classes are today and I think this will be best to get the appropriate key/values for ffxiv
# crafting Will need to iterate through each "Name" key to find the values Bonuses.*.Value is the percentage
class Buffs:
    def __init__(self, cp_percent = 0, cp_value = 0, craft_percent = 0, craft_value = 0, control_percent = 0, control_value = 0, name = 0):
        self.cp_percent = cp_percent
        self.cp_value = cp_value
        self.crafsmanship_percent = craft_percent
        self.crafsmanship_value = craft_value
        self.control_percent = control_percent
        self.control_value = control_value
        # self.hq = hq
        # self.id = id
        self.name = name




