#SECTION A
#No 1
def circle_area():
    radius=int(input("Enter the radius of the circle"))
    pie=float(3.14)
    area=pie*radius**2
    print(f"The circle area of radius {radius} and pie {pie} is {area}")
circle_area()    

# #No ii    
number=(4,7,2,9,12,15)
sum_odd=0
for num in number:
    if num !=0:
       sum_odd+=num
       print(sum_odd)
       
       
    #No iii
num1=int(input('Enter the first number'))
num2=int(input('Enter the second number'))
run=0
if run==0:
    sum=num1 +num2
    sum+=sum
    print(f"The sum of the numbers is{sum}")


    
    
    #No iv
student_info={'name':'Alice','age':20,'grade':'A'
                  
        
    }
student_info['age']=26
print(student_info)
    
    ##QUESTION number 2
student_name='Gloria Arinda'
student_number='SEP/BCS/088U/F'
programming=90
data_science=87
computer_application=77
    
total_marks=programming+data_science+computer_application
print(total_marks)
    
total_no_subjects=3
print(total_no_subjects)
    
Average=total_marks/total_no_subjects
print(f"The average mark is{Average :3f}")
    
    #ii
    #MGP=miles_driven/galons_used
mile_driven=int(input('Enter the miles driven'))
galons_used=int(input('Enter the galons used'))
cars_miles_galons_used= mile_driven/galons_used
print(cars_miles_galons_used)

    #iii
for number in range(1,111):
          number=0
if number%2!=0:
        print(number)
        
#QUESTION 4
#a
#object oriented programing is a language used to design software
# around objects other than functions and logic
#it implements real world things or entities like mobile app settings
#
#b
# A class is a blue print in oop
#4ii
sentence=['python exam']
for word in sentence.split():
    word_counts[word]= counts.get(word,0)+1
print(word_counts)
#4iii
def sum_two_no():
    a=3
    b=4
    
#4iv
class Car:
    def __init__(self, brand, name,color):
        self.brand = brand 
        self.name=name 
        self.color = color
          
        
my_car = Car("Toyota","pickup" "Red")

print("Brand:", my_car.brand)
print("name",my_car.name)
print("Color:", my_car.color)

#4v

class Car:
    def __init__(self, brand, color):
        self.brand = brand  
        self.color = color  

    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started.")  

my_car = Car("Toyota", "Red")

my_car.start_engine()






