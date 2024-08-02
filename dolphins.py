import random
import numpy as np

class Dolphin:
    def __init__(self, name, sex, **kwargs):
        # Attributes relating to gender, parents, and name
        self.name = name
        self.sex = sex
        self.mother = kwargs["mother"] if "mother" in kwargs else None
        self.father = kwargs["father"] if "father" in kwargs else None

        # Attributes relating to procreation
        self.procreation_cooldown = 0
        # self.procreate = False

        # Attributes relating to age and death
        self.age = 0
        self.death_age = int(np.random.randn()*5 + 35)
        self.dead = False
        
        # Attributes relating to printing the progress of the population
        """
        TO SEE EACH DOLPHIN PROGRESS THROUGH THE TRIAL, ENABLE print_progress
        Do so at your own risk, for your computer may blow up!
        """
        self.print_progress = False


    def age_record(self):
        # Keeps track of the dolphin's age and years since procreation
        # and determines whether the dolphin dies.
        
        # Increment age
        self.age += 1
        
        # Check procreation rate
        self.procreation_cooldown -= 1
        if self.procreation_cooldown < 0:
            self.procreation_cooldown = 0
        
        # Did the dolphin reach the death age?
        if self.age >= self.death_age:
            self.dead = True
            return self.dead

    def request_procreation(self, dolphin_other):            
        """
        Procreation System of Checks and Balances
        """
        try:
            # Check: Is dolphin_other a parent of dolphin? If so, return False
            if self.mother == dolphin_other or self.father == dolphin_other:
                if self.print_progress:
                    print(f"GENEALOGY ERROR: {self.name}'s parent is {dolphin_other.name}.")
                return False
            
            # Check: Is dolphin a parnet of dolphin_other
            if dolphin_other.mother == self or dolphin_other.father == self:
                if self.print_progress:
                    print(f"GENEALOGY ERROR: {dolphin_other.name}'s parent is {self.name}.")
                return False
            # Check: Are the dolphins full siblings of each other
            if (dolphin_other.mother != None) and (self.mother != None) and (dolphin_other.father != None) and (self.father != None):
                if (dolphin_other.mother == self.mother) and (dolphin_other.father == self.father):
                    if self.print_progress:
                        print(f"FULL SIBLING ERROR: {dolphin_other.name} and {self.name} are full siblings")
                    return False
            
            # Check: Are both of the dolphins within ten years of each other in age?
            if abs(dolphin_other.age - self.age) > 10:
                if self.print_progress:
                    print(f"AGE DIFFERENCE ERROR: {dolphin_other.name} and {self.name} have too wide an age gap ({abs(dolphin_other.age - self.age)})")
                return False
            
            # Check: Can both of the dolphins procreate based on the conditions at the beginning of this method?
            if (self.age < 6) and (dolphin_other.age < 6):
                if self.print_progress:
                    print(f"MATURITY ERROR: {self.name}'s age: {self.age}, {dolphin_other.name}'s age: {dolphin_other.age}.")
                return False

            # Check: Dolphins produce no more than 1 calf per every 5 years. If a dolphin's birthing cooldown is not 0, return False
            if (self.procreation_cooldown != 0) and (dolphin_other.procreation_cooldown != 0):
                if self.print_progress:
                    print(f"COOLDOWN ERROR: {self.name}'s cooldown: {self.procreation_cooldown}, {dolphin_other.name}'s cooldown: {dolphin_other.procreation_cooldown}.")
                return False

            # If all checks pass, then create a new dolphin is a go. Return True
            if self.print_progress:
                print(f"{dolphin_other.name} and {self.name} can procreate.")
            dolphin_other.procreation_cooldown = 5
            self.procreation_cooldown = 5
            return True 

        except AttributeError:
            if self.print_progress:
                print(f"INIT DOLPHINS: {self.name} and {dolphin_other.name} are the initial dolphins of the population")
            if self.procreation_cooldown == 0 and dolphin_other.procreation_cooldown == 0:
                if self.print_progress:
                    print(f"{dolphin_other.name} and {self.name} can procreate.")
                dolphin_other.procreation_cooldown = 5
                self.procreation_cooldown = 5
                return True 
            
            

# Half sibling procreation:
# if (Mom A == Mom B) and (Dad A == Dad B) -> do not procreate
# otherwise, do procreate