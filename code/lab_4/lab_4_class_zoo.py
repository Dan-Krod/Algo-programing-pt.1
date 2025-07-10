class Zoo:
    # Конструктор 
   def __init__(self, visitors_per_year = 0, name = "", animal_count = 0, species_amount = 0, animal_species = ''):
      self.__visitors_per_year = visitors_per_year
      self.__name = name
      self.__animal_count = animal_count
      self.public_species_amount = species_amount
      self.public_animal_species = animal_species

    # Геттери
   def get_visitors_per_year(self):
      return self.__visitors_per_year
    
   def get_name(self):
      return self.__name
    
   def get_animal_count(self):
      return self.__animal_count
    
    # Сеттери
   def set_visitors_per_year(self,new_visitors):
      self.__visitors_per_year = new_visitors
    
   def set_name(self,new_name):
      self.__name = new_name
    
   def set_animal_count(self,new_animal_count):
      self.__animal_count = new_animal_count

   # Метод __repr__
   def __repr__(self):
      return f"Зоопарк: Назва зооопарку: {self.__name}, Кількість відвідувачів в рік: {self.__visitors_per_year}, Кількість тварин: {self.__animal_count}"
   
   # Метод __str__
   def __str__(self):
      return f"Зоопарк: Назва зооопарку: {self.__name}, Кількість відвідувачів в рік: {self.__visitors_per_year}, Кількість тварин: {self.__animal_count}"
   
   # Деструктор
   def __del__(self):
      print(f"Зоопарк під назвою {self.__name},з кількістю відвідувачів в рік: {self.__visitors_per_year} та кількістю тварин: {self.__animal_count} закривається!")

def main():
   zoo_1= Zoo(10000,"Мир і природа", 500, 40,"Слони, папуги та інші...") 
   zoo_2= Zoo(20000,"Тропічне диво", 300, 20,"Мавпи,тигри та інші...") 
   zoo_3= Zoo(10000,"Сафарі пригода", 600, 45,"Леви,ягуари та інші...") 
   
   print(zoo_1)
   print(zoo_2)
   print(zoo_3)
   print("")

   print("Зоопарк №1 :")
   print(f"Ім*я: {zoo_1.get_name()}")
   print(f"Кількість відвідувачів в рік: {zoo_1.get_visitors_per_year()}")
   print(f"Кількість тварин: {zoo_1.get_animal_count()}")
   print("")

   print("Зоопарк №2 :")
   print(f"Ім*я: {zoo_2.get_name()}")
   print(f"Кількість відвідувачів в рік: {zoo_2.get_visitors_per_year()}")
   print(f"Кількість тварин: {zoo_2.get_animal_count()}")
   print("")

   print("Зоопарк №3 :")
   print(f"Ім*я: {zoo_3.get_name()}")
   print(f"Кількість відвідувачів в рік: {zoo_3.get_visitors_per_year()}")
   print(f"Кількість тварин: {zoo_3.get_animal_count()}")
   print("\n Метод repr:")

   print(repr(zoo_1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
   print(repr(zoo_2))
   print(repr(zoo_3))
   print("")

main()
