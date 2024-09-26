class Hero:
    def __init__(self, name, role, hp, ad, skill):
        self.name = name          # Nama Hero
        self.role = role          # Role Hero (marksman, tank, mage, dll)
        self.hp = hp              # Health Points
        self.ad = ad              # Attack Damage
        self.skill = skill        # Skill khusus

    # Method untuk melakukan serangan
    def attack(self, enemy):
        print(f"{self.name} menyerang {enemy.name}!")
        enemy.hp -= self.ad       # Mengurangi HP musuh berdasarkan AD
        print(f"{enemy.name} sekarang memiliki {enemy.hp} HP")

    # Method untuk menggunakan skill khusus
    def use_skill(self, enemy):
        print(f"{self.name} menggunakan {self.skill} pada {enemy.name}!")
        # Bisa tambahkan efek skill spesifik, ini hanya contoh umum
        enemy.hp -= (self.ad * 1.5)
        print(f"{enemy.name} sekarang memiliki {enemy.hp} HP")

    # Method untuk menampilkan statistik Hero
    def show_stats(self):
        print(f"Nama: {self.name}")
        print(f"Role: {self.role}")
        print(f"HP: {self.hp}")
        print(f"AD: {self.ad}")
        print(f"Skill: {self.skill}")
        print("-----------------------")


# Membuat 3 object Hero
Moskov = Hero("Moskov", "Marksman", 2500, 150, "Spear of Destruction")
Franco = Hero("Franco", "Tank", 5000, 100, "Bloody Hunt")
Nana = Hero("Nana", "Mage", 2000, 170, "Molina Blitz")

# Simulasi pertarungan
print("=== Simulasi Pertarungan ===")
Moskov.attack(Nana)
Franco.use_skill(Moskov)
Nana.attack(Franco)
print("============================")

# Menampilkan statistik dari masing-masing Hero
print("---Status Moskov---")
Moskov.show_stats()
print("---Status Franco---")
Franco.show_stats()
print("---Status Nana---")
Nana.show_stats()