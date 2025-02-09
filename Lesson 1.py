 def __init__(self, name, species, age, gender, height):
        self.name = name
        self.species = species 
        self.age = age
        self.gender = gender
        self.height = height
        self.hunger = 50  
        self.energy = 50  
        
    def yeda(self):
        if self.hunger > 10:
            self.hunger -= 10
        else:
            self.hunger = 10
        print(f"{self.name} нашел птицу. голодать(ахах): {self.hunger}/100")
        
    def igrushka(self):
        if self.energy > 10:
            self.energy -= 10
            self.hunger += 10
            print(f"{self.name} ташла игрушку!! сила:: {self.energy}/100, голодать: {self.hunger}/100")
        
    def vmestosnaigratkiom(self):
        if self.energy < 90:
            self.energy += 20
        print(f"{self.name} сидела24 часа за компом. сила: {self.energy}/100")
        
    def что за животное(self):
        print(f"\nИнформация о питомце:")
        print(f"Имя: {self.name}\nВид: {self.species}\nВозраст: {self.age}\nПол: {self.gender}\nРост: {self.height} см")
        print(f"Голод: {self.hunger}/100\nЭнергия: {self.energy}/100\n")
        
murka = Pet("Мурка", "cat", 2, "female", 24)
chapa = Pet("Чапа", "dog", 5, "male", 90)
murka.status()
murka.feed()
murka.play()
murka.sleep()
murka.status()

chapa.status()
chapa.play()
chapa.feed()
chapa.sleep()
chapa.status()
#начало скопировал с вашего аккаунта
