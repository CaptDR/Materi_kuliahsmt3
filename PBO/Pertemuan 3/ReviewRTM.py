#Class Hero
class Hero:
    #Membuat konstruktor untuk menampung atribut
    def __init__(self, name, role, health_point, attack_damage, skill):
        self.nm = name
        self.rl = role
        self.hp = health_point
        self.ad = attack_damage
        self.sk = skill
    #Method Attack
    def attack(self, target):
        target.hp -= self.ad
        print(f"{self.nm} menyerang {target.nm}")
        print(f"{target.nm} kehilangan {self.ad} HP")
    #Method Use Skill
    def useSkill(self, target):
        target.hp -= self.ad * 2.5
        print(f"{self.nm} Menggunakan Skill {self.sk} !\n{target.nm} kehilangan {int(self.ad * 2.5)} HP")
    #Method Show Stats
    def showStats(self):
        print(f"Status  : {self.nm}")
        print(f"Role    : {self.rl}")
        print(f"HP      : {int(self.hp)}")
        print(f"AD      : {self.ad}")
        print(f"Skill   : {self.sk}")
        print("==========================")
#Stats
layla = Hero("Layla", "Marksman", 450, 50, "Destruction Rush")
layla.showStats()
tigreal = Hero("Tigreal", "Tank", 500, 40, "Sacred Hammer")
tigreal.showStats()
#Battle
layla.attack(tigreal)
tigreal.useSkill(layla)
layla.showStats()
tigreal.showStats()