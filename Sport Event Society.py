# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import random
import csv

names = ["Alvin Carpenter","Lorna Jenkins","Nisha Vang","Ashlee Owens",
        "Rojin Sparrow","Madeeha Bellamy","Ewen Stott","Franco Crouch",
        "Jensen Conroy","Clarissa Churchill","Batman","Aron Parsons",
        "Tyron Goodman","Shahzaib Petty","Julius Colley","Calista Cummings",
        "Eiliyah West","Adem Wardle","Keaton Ferry","Salman Whitley",
        "Simran Dudley","Halle Sampson","Zander Spencer","Gurveer Lutz",
        "Hasnain Mendoza","Scarlette Mohammed","Nadeem Craft","Ajay Bryan",
        "Kiera Ridley","Otto Valenzuela","Tarik Corona","Ella-Rose Choi",
        "Roland Burns","Sheena Walls","Robert Horne","Eleasha Firth",
        "Gracie Hood","Albert Cross","Domonic Keller","Kenya Hartman",
        "Luna Crosby","Isabella-Rose Hawkins","Kathryn Lindsey","Karen Diaz",
        "Gianluca Walker","Ephraim Booth","Zayan Yang","Conal Taylor",
        "Jimmie Gallegos","Ritik Moses","Lois Wong","Sylvie Yoder",
        "Romana Wagner","Kelly Hodge","Romy Cohen","Renee Park",
        "Siraj Blevins","Lexi Hendricks","Mario Easton","Aoife Wynn",
        "Devon Lowry","Mathias Russo","Fionn Cochran","Ella-Grace Hollis",
        "Karis Lane","Huseyin Sargent","Charlene Myers","Leighton Bloggs",
        "Marilyn Burks","Alessio Day","Maisha Frost","Keri Rocha","Lillie Paterson",
        "Andre Matthews","Blair Torres","Roscoe Dunne","Larissa Kinney","Camron Rees",
        "Jagdeep Sims","Sandra Wickens","Soraya Bevan","Libbi Driscoll","Shanaya Bouvet",
        "Zaynab Markham","Sinead Holland","Dougie Whelan","Rylee Hinton","Federico Ray",
        "Fatima Goodwin","Amandeep Mclean","Eleri Garza","Heath Robson","Areebah Calhoun",
        "Nour Fox","Lillie-Mae O'Neill","Margot Reyna","Ibrahim Witt","Rukhsar Roman",
        "Frida Rayner","Keir Soto","Cody Buckley"]

    
sports = ["Archery","Badminton","Cricket","Bowling","Boxing",
        "Curling","Tennis","Skateboarding","Surfing","Hockey",
        "Figure skating","Yoga","Fencing","Fitness","Gymnastics",
        "Karate","Volleyball","Weightlifting","Basketball",
        "Baseball","Rugby","Wrestling","High jumping",
        "Hang gliding","Car racing","Cycling","Running",
        "Table tennis","Fishing","Judo","Climbing","Pool",
        "Shooting","Horse racing","Horseback riding","Golf","Soccer"]

genders = ['Male', 'Female', 'Non-binary']

f1 = open('members.csv','w', newline='\n')
writer = csv.writer(f1)

for n in range(random.randint(500, 1000)):
    writer.writerow([n+1, random.choice(names), random.choice(sports),
                     random.choice(genders), random.randint(12, 86)])

f1.close()

"""
______________________________________________________________________________
START TO YOUR CODE FROM HERE
______________________________________________________________________________
"""
import sys
#import pandas as pd #use ir for graph if need
#import seaborn as sns #use ir for graph if need
#import matplotlib.pyplot as plt #use ir for graph if need


"""
Function to print index and members
"""
def list_of_members():         
   file = open("members.csv")  
   reader = csv.reader(file)   
   for row in reader:
       print(row[0], row[1])   

"""
Function to print list of sports
"""
def sport_list ():             
    file = open('members.csv') 
    reader = csv.reader(file)  
    for row in reader:
        print(row[2])    
        
"""
Function to filter the sport typed and print the amount of members 
"""
def members_by_sport (sport):  
    file = open('members.csv') 
    reader = csv.reader(file)  
    members = []               
    count = 0                   
    for row in reader:          
        if (row[2] == sport):
            count = count + 1     
            members.append(row)  
    print('\nTotal members on ' + sport + ' is: ' + str(count) + '\n') 
    return members                

"""
Function to use the sport typed, filter and print by age  split in 4 groups
"""
def total_by_age (sport):              
    members = members_by_sport(sport)  
    count_age_1 = 0                    # will count how many member for each group
    count_age_2 = 0                    
    count_age_3 = 0                    
    count_age_4 = 0                    
    for n in members:
        if (int(n[4]) >= 12 and int(n[4]) <= 20):   # will filter by the ages
            count_age_1 = count_age_1 + 1           # will add to the count in the range of age
        elif (int(n[4]) >= 21 and int(n[4]) <= 40): 
            count_age_2 = count_age_2 + 1            
        elif (int(n[4]) >= 41 and int(n[4]) <= 60): 
            count_age_3 = count_age_3 + 1           
        elif (int(n[4]) >= 61 and int(n[4]) <= 86): 
            count_age_4 = count_age_4 + 1           
    print('Between 12 to 20 Years Old there are '+ str(count_age_1) +' Members') # will print how many member in the following range
    print('Between 21 to 40 Years Old there are '+ str(count_age_2) +' Members') 
    print('Between 41 to 60 Years Old there are '+ str(count_age_3) +' Members') 
    print('Between 61 to 86 Years Old there are '+ str(count_age_4) +' Members\n') 
    return total_by_age

"""
Function to use the sport typed, filter and print by gender
"""
def total_by_gender (sport):                     
    members = members_by_sport(sport)            
    count_male = 0                               # will count how many members for each gender
    count_female = 0                             
    count_nonbinary = 0                          
    for m in members:
        if (m[3] == 'Male'):                     # will filter by gender
            count_male = count_male + 1          # will add to the count of gender
        elif (m[3] == 'Female'):                 
            count_female = count_female + 1      
        else:                                    
            count_nonbinary = count_nonbinary +1 
            
    print('There Are ' + str(count_male) + ' Males')            # will print how many member are in the following gender
    print('There Are ' + str(count_female) + ' Females')        
    print('There Are ' + str(count_nonbinary) + ' Non-binary\n')  
    
"""
Function for main menu with 3 options
""" 
def menu ():  
    while True:                                                 
        choice = input("Please, choose one of the following options: \n 1.View all members. \n 2.View relevant data about a particular sport. \n 3.Close the program. \n")
        if (choice == '1'):                                    # will check if the user typed the option '1', if so, print list of members list_of_bembers()
            print('List of Members: \n')                       
            list_of_members()                                  
        elif (choice == '2'):                                  # will check if the user typed the option '2', if so, print the submenu()
            submenu()                                                        
        elif (choice == '3'):                                  # will check if the user typed the option '3', if so, close the program
            print('The program has been closed')               
            sys.exit(0)                                            
        else:                                                  
            print(choice + ' Is not a Valid Option')           # will check if the user typed the something different, if so, repeat the main menu  
    
"""
Function for submenu with one input then 3 options
""" 
def submenu ():                                                
    print('List of sports avaiable: \n')                        
    for s in sports:                                            
        print(s)                                               # will print list of sports avaiable     
    while True:                                                
        choice_2 = str.capitalize(input('Please, type one sport from the list or type menu to return to main menu\n')) 
        if choice_2 in sports:                                 # will check if the user typed one sport from the list, if so, will print the following 3 options
            option = input('Please, choose one of the following options: \n 1. View  breakdown by age. \n 2. View breakdown by gender.\n 3. To return to main menu and choose a different sport. \n ')
            if option == '1':                                  # will check if the user typed the option '1', if so, print the breakdown by age - total_by_age()
                total_by_age(choice_2)                         
            elif option == '2':                                # will check if the user typed the option '2', if so, print the breakdown by gender -total_by-gender()
                total_by_gender(choice_2)                      
            elif option == '3':                                # will check if the user typed the option '3', if so, will return to main menu - menu()
                menu()                                         
            else:                                              # will check if the user typed something different, if so, will repeat submenu 
                print(option + ' Is not a Valid Option')       
        elif choice_2 == 'Menu':                               # will check if the user typed the option 'Menu', if so, will return to main menu - menu()                 
            menu()                                              
        elif choice_2 not in sports:                           # will check if the user typed something different from the list, if so, will repeat the question               
            print(choice_2 + ' Is not a option')    
            
"""
Welcome screen then menu
"""     
print("Welcome to Sport Event Society \n")                     # first line of the program "Wellcome"    
menu()                                                         # will open de function menu and start the loops      


