import random
import string

def password_fi(size):
    password = "".join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits)for i in range(size))
    return password

size = int(input("Enter the size of the password: "))
password = password_fi(size)
print("The Strong password you got is: %s" % password)


# # Intern Random Password



from tkinter import *
import random 
import string 
def password_generator(size):
    return "".join(random.choice(string.punctuation + string.ascii_letters + string.digits)for i in range(size))
def logic(): 
    try:
        size=int(e1.get())
        password=password_generator(size)
        result_la.config(text=f"Generated password: {password}")
    except:
        result_la.config(text="Please enter a valid number")
root =Tk()        
w = Label(root, text='PASSWORD GENERATOR')
w.grid(row=0,column=0,columnspan=2,pady=10)

e1_label=Label(root,text="Enter the required size password")
e1_label.grid(row=1,column=0,padx=10,pady=10,sticky=E)

e1=Entry(root,width=45,borderwidth=5)
e1.grid(row=1,column=1,padx=10,pady=10)

button_success=Button(root,text="password",padx=20,pady=20,command=logic)
button_success.grid(row=2,column=1,columnspan=2,pady=10)

result_la=Label(root,text="")
result_la.grid(row=3,column=0,columnspan=2,pady=10)

root.mainloop()







