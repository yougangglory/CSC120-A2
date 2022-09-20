# Computer is the name of the class
class Computer: 

    # What attributes will it need?
# It will need a description, processor type,hard drive type,memory,operating system,year made and price

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str,hard_drive_capacity: int,
     memory: int,operating_system: str,year_made: int,price: int)-> None:
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price =price
                
                
       