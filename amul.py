from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random

root = Tk()
root.title("Connecting Jobs")
root.geometry("600x600")

lbl_selected_dr = Label(root)
lbl_selected_dr.place(relx = 0.5, rely = 0.2, anchor = CENTER)


lbl_selected_it = Label(root)
lbl_selected_it.place(relx = 0.5, rely = 0.5, anchor = CENTER)


lbl_selected_chemical = Label(root)
lbl_selected_chemical.place(relx = 0.5, rely = 0.8, anchor = CENTER)

class Parent():
    
    def __init__(self):
        print("This is Parent Class.")
        
    def Dr(dr_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0, 3)
        lbl_selected_dr["text"] = dr_name + " has been alloted to " + hospital_list[random_hospital]
            
    def Software_Engineer(it_name):
        it_company_list = ["I Code", "Web Access", "Dotcom Services", "ATOS"]
        random_it_company = random.randint(0, 3)
        lbl_selected_it["text"] = it_name + " has been alloted to " + it_company_list[random_it_company]
        
    def Chemical_Engineer(chemical_name):
        company_list = ["Amul Doodh Peetha Hai India", "Cadbury", "Flipkart"]
        random_company = random.randint(0, 2)
        lbl_selected_chemical["text"] = chemical_name + " has been alloted to " + company_list[random_company]
            
class Child1(Parent):
    
    def __init__(self):
        print("This is Child Class.")
        
    def get_dr(self):
        name = "Micheal"
        Parent.Dr(name)
        
class Child2(Parent):
    
    def __init__(self):
        print("This is Child Class.")
        
    def get_it(self):
        name = "Jessica"
        Parent.Software_Engineer(name)
        
class Child3(Parent):
    
    def __init__(self):
        print("This is Child Class.")
        
    def get_chemical(self):
        name = "Prateek"
        Parent.Chemical_Engineer(name)
        
child1_obj = Child1()
child2_obj = Child2()
child3_obj = Child3()

btn_dr = Button(root, text = "Show the Hospital Alloted", command = child1_obj.get_dr)
btn_dr.place(relx = 0.5, rely = 0.1, anchor = CENTER)

btn_it = Button(root, text = "Show the IT Company Alloted", command = child2_obj.get_it)
btn_it.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn_chemical = Button(root, text = "Show the Chemical Company Alloted", command = child3_obj.get_chemical)
btn_chemical.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()