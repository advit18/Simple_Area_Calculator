import math
from tkinter import *
from tkinter import messagebox
root = Tk()

mainframe = LabelFrame(root,
                       bg = 'black',
                       fg='medium spring green',
                       text = "Area Calculator!",
                       padx = 10,
                       pady = 10,
                       font = 25)
mainframe.pack()               

def main_menu():
    global frame1 
    frame1 = LabelFrame(mainframe,text = "Main Menu",
                        padx = 110,
                        pady = 40,
                        bg = 'black',
                        fg = 'plum2',
                        font = 25)
    frame1.pack(padx = 96,pady = 80)
    frame1.tkraise()

    button_area = Button(frame1,text = 'Area',
                         command = lambda : area_press(),
                         width = 10,
                         height = 2,
                         bg = 'plum2')
    button_area.grid(pady = 2,row = 0,column = 0,padx = 2)
    
    button_history = Button(frame1,
                            text = "History",
                            command = lambda : history_press(),
                            width = 10,
                            height = 2,
                            bg = 'plum2')
    button_history.grid(pady = 2,row = 0,column = 1,padx = 2)                     
    
    button_formulae = Button(frame1,text = 'Formulae',
                             command = lambda : formulae_press(),
                             width = 10,
                             height = 2,
                             bg = 'plum2')
    button_formulae.grid(pady = 2,row = 1,column = 0,padx = 2)
    
    button_quit = Button(frame1,text = 'Quit',
                         command = lambda : root.destroy(),
                         width = 10,
                         height = 2,
                         bg = 'plum2')
    button_quit.grid(pady = 2,row = 1,column = 1,padx = 2)


def main_menu_duplicate(var):
    global frame1
    frame1 = LabelFrame(mainframe,text = "Main Menu",
                        padx = 110,
                        pady = 40,
                        bg = 'black',
                        fg = 'plum2',
                        font = 25)
    frame1.pack(padx = 96,pady = 80)
    frame1.tkraise()
    var.after(3,var.destroy())

    button_area = Button(frame1,text = 'Area',
                         command = lambda : area_press(),
                         width = 10,
                         height = 2,
                         bg = 'plum2')
    button_area.grid(pady = 2,row = 0,column = 0,padx = 2)
    
    button_history = Button(frame1,
                            text = "History",
                            command = lambda : history_press(),
                            width = 10,
                            height = 2,
                            bg = 'plum2')
    button_history.grid(pady = 2,row = 0,column = 1,padx = 2)                     
    
    button_formulae = Button(frame1,text = 'Formulae',
                             command = lambda : formulae_press(),
                             width = 10,
                             height = 2,
                             bg = 'plum2')
    button_formulae.grid(pady = 2,row = 1,column = 0,padx = 2)
    
    button_quit = Button(frame1,text = 'Quit',
                         command = lambda : root.destroy(),
                         width = 10,
                         height = 2,
                         bg = 'plum2')
    button_quit.grid(pady = 2,row = 1,column = 1,padx = 2)


def check(inp):
    if inp.isalpha():
        messagebox.showerror("Invalid Input" , "Please Enter a Valid Input")
        return False
    elif(float(inp)<=0):
       messagebox.showerror("Invalid Input" , "Please Enter a Valid Input")
       return False
    else:
        return True
    
       
def area_press():
    frame1.pack_forget()
    global frame_area
    frame_area = LabelFrame(mainframe,
                            text = "Type Of Shape",
                            padx = 115,
                            pady = 50,
                            bg = 'black',
                            fg = 'plum2',
                            font = 25)
    frame_area.pack(padx = 135,pady = 70)
    button_2D = Button(frame_area,
                       text = "2D Shapes",
                       command = lambda : twoDimension_press(),
                       width = 10,
                       height = 2,
                       bg = 'plum2')
    button_2D.pack(pady = 3)
    
    button_3D = Button(frame_area,
                       text = "3D Shapes",
                       command = lambda : threeDimension_press(),
                       width = 10,
                       height = 2,
                       bg = 'plum2')
    button_3D.pack()    


def history_store(area,shape):
    f1 = open("data.txt","a")
    f1.write("Area of "+ shape + " = " + str(area) + "\n")
    f1.close()
    
    
def history_view():
    global frame_history
    frame_history.pack_forget()
    global frame_view
    frame_view = LabelFrame(mainframe,
                          text = "View History",
                          padx = 40,
                          pady = 40,
                          bg = 'black',
                          fg = 'DarkOrange1',
                          font = 25,
                          )
    frame_view.pack(padx = 86,pady = 46)
    
    f2 = open("data.txt","r")
    list_area = f2.read().splitlines()
    list1 = Listbox(frame_view, 
                    height = 6,
                    width = 40,
                    bg = "black",
                    fg = "DarkOrange1")
    for i in list_area:
        list1.insert(0,i)
    list1.pack(side = LEFT,fill = X)
    scroll = Scrollbar(frame_view)
    scroll.pack(side = RIGHT,fill = Y)
    scroll.config(command = list1.yview)
    f2.close()
    button_return = Button(frame_view,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_view))
    button_return.place(anchor = SW,
                        relx = 0.53,
                        rely = 1.31)
                   

def history_clear():
    f3 = open('data.txt','w').close()
    messagebox.showinfo("Information" , "History Has Been Cleared")
    global frame_history
    frame_history.pack_forget()
    main_menu()
    
    
def history_press():
    global frame1
    frame1.pack_forget()
    global frame_history
    frame_history = LabelFrame(mainframe,
                          text = "History",
                          padx = 115,
                          pady = 50,
                          bg = 'black',
                          fg = 'PaleTurquoise1',
                          font = 25,
                          )
    frame_history.pack(padx = 135,pady = 70)
    button_view = Button(frame_history,
                         text  = "View History",
                         bg = "PaleTurquoise1",
                         width = 10,
                         height = 2,
                         command = lambda : history_view())
    button_view.pack(pady = 2)
    button_clear = Button(frame_history,
                         text  = "Clear History",
                         bg = "PaleTurquoise1",
                         width = 10,
                         height = 2,
                         command = lambda : history_clear())
    button_clear.pack(pady = 2)


def formulae_press():
    global frame1
    frame1.pack_forget()
    global frame_formulae
    frame_formulae = LabelFrame(mainframe,
                            text = "Type Of Shape",
                            padx = 115,
                            pady = 50,
                            bg = 'black',
                            fg = 'plum2',
                            font = 25)
    frame_formulae.pack(padx = 135,pady = 71)
    button_2D = Button(frame_formulae,
                       text = "2D Shapes",
                       command = lambda : twoDimension_press_formulae(),
                       width = 10,
                       height = 2,
                       bg = 'plum2')
    button_2D.pack(pady = 3)
    
    button_3D = Button(frame_formulae,
                       text = "3D Shapes",
                       command = lambda : threeDimension_press_formulae(),
                       width = 10,
                       height = 2,
                       bg = 'plum2')
    button_3D.pack()    

                         
def twoDimension_press():
    global frame_area
    frame_area.pack_forget()
    global frame_2D
    frame_2D = LabelFrame(mainframe,
                          text = "2D",
                          padx = 40,
                          pady = 40,
                          bg = 'black',
                          fg = 'DarkOrange1',
                          font = 25)
    frame_2D.pack(padx = 83,pady = 43)
    label_select = Label(frame_2D,
                         text = "Select Any Shape of Your Choice!",
                         bg = 'black',
                         fg = 'DarkOrange1')
    label_select.grid(row = 0,
                      column = 0,
                      columnspan = 3)
    button_rectangle = Button(frame_2D,
                      text = 'Rectangle',
                      padx = 10,
                      pady = 10,
                      command = lambda : area_rectangle(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_rectangle.grid(row = 1,
                          column = 0,
                          padx = 1,
                          pady = 1)
     
    button_square = Button(frame_2D,
                      text = 'Square',
                      padx = 10,
                      pady = 10,
                      command = lambda : area_square(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_square.grid(row = 1,
                       column = 1,
                       padx = 1,
                       pady = 1)
     
    button_circle = Button(frame_2D,
                      text = 'Circle',
                      padx = 10,
                      pady = 10,
                      command = lambda : area_circle(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_circle.grid(row = 1,
                       column = 2,
                          padx = 1,
                          pady = 1)
     
    button_ellipse = Button(frame_2D,
                      text = 'Ellipse',
                      padx = 10,
                      pady = 10,
                      command = lambda : area_ellipse(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_ellipse.grid(row = 2,
                          column = 0,
                          padx = 1,
                          pady = 1)
     
    button_parallelogram = Button(frame_2D,
                      text = 'Parallelogram',
                      padx = 10,
                      pady = 10,
                      command = lambda :area_parallelogram(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_parallelogram.grid(row = 2,
                          column = 1,
                          padx = 1,
                          pady = 1)
     
    button_triangle = Button(frame_2D,
                      text = 'Triangle',
                      padx = 10,
                      pady = 10,
                      command = lambda : area_triangle(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_triangle.grid(row = 2,
                         column = 2,
                          padx = 1,
                          pady = 1)
     
    button_rhombus = Button(frame_2D,
                      text = 'Rhombus',
                      padx = 10,
                      pady = 10,
                      command = lambda : area_rhombus(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_rhombus.grid(row = 3,
                          column = 0,
                          padx = 1,
                          pady = 1)
    button_trapezoid = Button(frame_2D,
                      text = 'Trapezoid',
                      padx = 10,
                      pady = 10,
                      command = lambda : area_trapezoid(),
                      width = 12,
                      bg = 'DarkOrange1',
                      fg = 'white')
    button_trapezoid.grid(row = 3,
                          column = 1,
                          padx = 1,
                          pady = 1)


def threeDimension_press():
    global frame_area
    frame_area.pack_forget()
    global frame_3D
    frame_3D = LabelFrame(mainframe,
                          text = "3D",
                          padx = 40,
                          pady = 20,
                          bg = 'black',
                          fg = 'SkyBlue2',
                          font = 25)
    frame_3D.pack(padx = 83,pady = 43)
    label_select = Label(frame_3D,
                         text = "Select Any Shape of Your Choice!",
                         bg = 'black',
                         fg = 'SkyBlue2')
    label_select.grid(row = 0,
                      column = 0,
                      columnspan = 3)
    button_cube = Button(frame_3D,
                      text = 'Cube',
                      padx = 10,
                      pady = 10,
                      width = 12,
                      bg = 'SkyBlue2',
                      fg = 'white',
                      command = lambda : area_cube())
    button_cube.grid(row = 1,
                     column =0,
                     padx = 1,
                     pady = 1)
     
    button_cuboid= Button(frame_3D,
                      text = 'Cuboid',
                      padx = 10,
                      pady = 10,
                      width = 12,
                      bg = 'SkyBlue2',
                      fg = 'white',
                      command = lambda : area_cuboid(),)
    button_cuboid.grid(row = 1,
                       column = 1,
                       padx = 1,
                       pady = 1)
     
    button_sphere = Button(frame_3D,
                      text = 'Sphere',
                      padx = 10,
                      pady = 10,
                      width = 12,
                      bg = 'SkyBlue2',
                      fg = 'white',
                      command = lambda : area_sphere())
    button_sphere.grid(row = 1,
                       column =2,
                       padx = 1,
                       pady = 1)
     
    button_cone = Button(frame_3D,
                      text = 'Cone',
                      padx = 10,
                      pady = 10,
                      width = 12,
                      bg = 'SkyBlue2',
                      fg = 'white',
                      command = lambda : area_cone())
    button_cone.grid(row = 2,
                     column =0,
                     padx = 1,
                     pady = 1)
     
    button_cylinder = Button(frame_3D,
                      text = 'Cylinder',
                      padx = 10,
                      pady = 10,
                      width = 12,
                      bg = 'SkyBlue2',
                      fg = 'white',
                      command = lambda : area_cylinder())
    button_cylinder.grid(row = 2,
                         column = 1,
                         padx = 1,
                         pady = 1)
     
    button_hemisphere = Button(frame_3D,
                      text = 'Hemisphere',
                      padx = 10,
                      pady = 10,
                      width = 12,
                      bg = 'SkyBlue2',
                      fg = 'white',
                      command = lambda : area_hemisphere())
    button_hemisphere.grid(row = 2,
                           column = 2,
                           padx = 1,
                           pady = 1)
    
    button_squarepyramid = Button(frame_3D,
                      text = 'Square Pyramid',
                      padx = 10,
                      pady = 10,
                      width = 12,
                      bg = 'SkyBlue2',
                      fg = 'white',
                      command = lambda : area_squarepyramid())
    button_squarepyramid.grid(row = 3,
                              column = 0,
                              padx = 1,
                              pady = 1)


def twoDimension_press_formulae():
    global frame_formulae
    frame_formulae.pack_forget()
    frame_formulae_2D = LabelFrame(mainframe,
                          text = "2D Shape Formulae",
                          padx = 40,
                          pady = 40,
                          bg = 'black',
                          fg = 'DarkOrange1',
                          font = 25)
    frame_formulae_2D.pack(padx = 120,pady = 75)
    
    f2 = open("data_formulae2D.txt","r")
    list_area = f2.read().splitlines()
    list_area.reverse()
    list1 = Listbox(frame_formulae_2D, 
                    height = 6,
                    width = 40,
                    bg = "black",
                    fg = "DarkOrange1")
    for i in list_area:
        list1.insert(0,i)
    list1.pack(side = LEFT,fill = X)
    scroll = Scrollbar(frame_formulae_2D)
    scroll.pack(side = RIGHT,fill = Y)
    scroll.config(command = list1.yview)
    f2.close()
    button_return = Button(frame_formulae_2D,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_formulae_2D))
    button_return.place(anchor = SW,
                        relx = 0.53,
                        rely = 1.31)


def threeDimension_press_formulae():
    global frame_formulae
    frame_formulae.pack_forget()
    frame_formulae_3D = LabelFrame(mainframe,
                          text = "3D Shape Formulae",
                          padx = 40,
                          pady = 40,
                          bg = 'black',
                          fg = 'DarkOrange1',
                          font = 25)
    frame_formulae_3D.pack(padx = 120,pady = 75)
    
    f2 = open("data_formulae3D.txt","r")
    list_area = f2.read().splitlines()
    list_area.reverse()
    list1 = Listbox(frame_formulae_3D, 
                    height = 6,
                    width = 40,
                    bg = "black",
                    fg = "DarkOrange1")
    for i in list_area:
        list1.insert(0,i)
    list1.pack(side = LEFT,fill = X)
    scroll = Scrollbar(frame_formulae_3D)
    scroll.pack(side = RIGHT,fill = Y)
    scroll.config(command = list1.yview)
    f2.close()
    button_return = Button(frame_formulae_3D,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_formulae_3D))
    button_return.place(anchor = SW,
                        relx = 0.53,
                        rely = 1.31)


#2D Shapes
def area_rectangle():
    global frame_2D
    frame_2D.pack_forget()
    global frame_rectangle
    frame_rectangle = LabelFrame(mainframe,
                                 text = "Area of Rectangle",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_rectangle.pack(padx = 80,pady = 84)
    label1 = Label(frame_rectangle,
                   text = "Enter side 1 : ")
    label1.grid(row = 0,
                column = 0)
    
    label2 = Label(frame_rectangle,
                   text = "Enter side 2 : ")
    label2.grid(row = 1,
                column = 0)
    
                       
    side1 = StringVar()
    side2 = StringVar()
    num1 = Entry(frame_rectangle,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    num2 = Entry(frame_rectangle,
                 textvariable = side2,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num2.grid(row = 1,
              column = 1)
    
    def generate():
        
        if check(side1.get()) != False and check(side2.get()) != False:
            num3 = float(side1.get())* float(side2.get())
            history_store(num3,"Rectangle")
            label_result = Label(frame_rectangle,
                                 text ="Area = " + str(num3))
            label_result.grid(row = 3, 
                              column =2,
                              padx = 1,
                              pady = 3)
        button_return = Button(frame_rectangle,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_rectangle))
        button_return.grid(row = 4,
                               column = 2,
                               padx = 1,
                               pady = 1)
        
        
        
    
    generate=Button(frame_rectangle,
                    text="Result",
                    width=28,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate,
                    borderwidth = 1)
    generate.grid(row=2,
                  column=0,
                  columnspan = 2,
                  padx = 1,
                  pady = 3)
    

def area_square():
    global frame_2D
    frame_2D.pack_forget()
    frame_square = LabelFrame(mainframe,
                              text = "Area Of Square",
                              padx = 45,
                              pady = 24,
                              bg = 'black',
                              fg = 'medium spring green',
                              font = 25)
    frame_square.pack(padx = 87,pady = 90)
    label1 = Label(frame_square,
                   text = "Enter side : ")
    label1.grid(row = 0,
                column = 0)
    side = StringVar()
    num = Entry(frame_square,
                textvariable = side,
                bg = "light goldenrod",
                borderwidth = 2)
    num.grid(row = 0,column = 1)
    
    def generate():
        
        if check(side.get()) != False:
            num_area = float(side.get()) * float(side.get())
            num_area = round(num_area,2)
            history_store(num_area,"Square")
            label_result = Label(frame_square,text = "Area = " + str(num_area))
            label_result.grid(row = 3,
                              column = 2,
                              padx = 1,
                              pady = 3)
        button_return = Button(frame_square,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_square))
        button_return.grid(row = 4,
                               column = 2,
                               padx = 1,
                               pady = 3)
    
    generate = Button(frame_square,
                    text="Result",
                    width=27,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate,
                    borderwidth = 1)
    generate.grid(row= 2,
                  column= 0,
                  columnspan = 2,
                  padx = 1,
                  pady = 3)
         
        
def area_circle():
    global frame_2D
    frame_2D.pack_forget()
    frame_circle = LabelFrame(mainframe,
                              text = "Area Of Circle",
                              padx = 42,
                              pady = 23,
                              bg = 'black',
                              fg = 'medium spring green',
                              font = 25)
    frame_circle.pack(padx = 82,pady = 85)
    label1 = Label(frame_circle,
                   text = "Enter Radius : ")
    label1.grid(row = 0,
                column = 0)
    side = StringVar()
    num = Entry(frame_circle,
                textvariable = side,
                bg = "light goldenrod",
                borderwidth = 2)
    num.grid(row = 0,column = 1)
    
    def generate():
        
        if check(side.get()) != False:
            num_area = float(side.get()) * 3.14 * float(side.get())
            num_area = round(num_area,2)
            history_store(num_area,"Circle")
            label_result = Label(frame_circle,text = "Area = " + str(num_area))
            label_result.grid(row = 3,
                          column = 2,
                          padx = 1,
                          pady = 3)
        button_return = Button(frame_circle,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_circle))
        button_return.grid(row = 4,
                           column = 2,
                           padx = 1,
                           pady = 3)
    
    generate = Button(frame_circle,
                    text="Result",
                    borderwidth = 1,
                    width= 29,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan = 2,
                  padx = 1,
                  pady = 3)


def area_ellipse():
    global frame_2D
    frame_2D.pack_forget()
    global frame_ellipse
    frame_ellipse = LabelFrame(mainframe,
                                 text = "Area of Ellipse",
                                 padx = 25,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_ellipse.pack(padx = 67,pady = 84)
    label1 = Label(frame_ellipse,
                   text = "Enter length of major axis : ")
    label1.grid(row = 0,
                column = 0)
    
    label2 = Label(frame_ellipse,
                   text = "Enter length of minor axis : ")
    label2.grid(row = 1,
                column = 0)
    
                       
    side1 = StringVar()
    side2 = StringVar()
    num1 = Entry(frame_ellipse,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    num2 = Entry(frame_ellipse,
                 textvariable = side2,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num2.grid(row = 1,
              column = 1)
    
    def generate():
        
        if check(side1.get()) != False and check(side2.get()) != False:
            num3 = float(side1.get())*float(side2.get()) * 3.14
            num3 = round(num3,2)
            history_store(num3,"Ellipse")
            label_result = Label(frame_ellipse,text ="Area = " + str(num3))
            label_result.grid(row = 3, 
                              column =2,
                              padx = 1,
                              pady = 3)
        button_return = Button(frame_ellipse,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_ellipse))
        button_return.grid(row = 4,
                               column = 2,
                               padx = 1,
                               pady = 3)
        
        
        
    
    generate=Button(frame_ellipse,
                    text="Result",
                    width= 39,
                    borderwidth = 1,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan = 2,
                  padx = 1,
                  pady = 3)


def area_parallelogram():
    global frame_2D
    frame_2D.pack_forget()
    global frame_parallelogram
    frame_parallelogram = LabelFrame(mainframe,
                                 text = "Area of Parallelogram",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_parallelogram.pack(padx = 82,pady = 82)
    label1 = Label(frame_parallelogram,
                   text = "Enter Height : ",
                   width = 11)
    label1.grid(row = 0,
                column = 0)
    
    label2 = Label(frame_parallelogram,
                   text = "Enter Base : ",
                   width = 11)
    label2.grid(row = 1,
                column = 0)
    
                       
    side1 = StringVar()
    side2 = StringVar()
    num1 = Entry(frame_parallelogram,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    num2 = Entry(frame_parallelogram,
                 textvariable = side2,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num2.grid(row = 1,
              column = 1)
    
    def generate():
        
        if check(side1.get()) != False and check(side2.get()) != False:
            num3 = float(side1.get())*float(side2.get())
            num3 = round(num3,2)
            history_store(num3,"Parallelogram")
            label_result = Label(frame_parallelogram,text ="Area = " + str(num3))
            label_result.grid(row = 3, 
                              column =2,
                              padx = 1,
                              pady = 3)
        button_return = Button(frame_parallelogram,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_parallelogram))
        button_return.grid(row = 4,
                               column = 2,
                               padx = 1,
                               pady = 3)
        
        
        
    
    generate=Button(frame_parallelogram,
                    text="Result",
                    width=29,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate,
                    borderwidth = 1)
    generate.grid(row=2,
                  column=0,
                  columnspan = 2,
                  padx = 1,
                  pady = 3)


def area_triangle():
    global frame_2D
    frame_2D.pack_forget()
    global frame_triangle
    frame_triangle = LabelFrame(mainframe,
                                 text = "Area of Triangle",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_triangle.pack(padx = 82,pady = 83)
    label1 = Label(frame_triangle,
                   text = "Enter Height : ",
                   width = 11)
    label1.grid(row = 0,
                column = 0)
    
    label2 = Label(frame_triangle,
                   text = "Enter Base : ",
                   width = 11)
    label2.grid(row = 1,
                column = 0)
    
                       
    side1 = StringVar()
    side2 = StringVar()
    num1 = Entry(frame_triangle,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    num2 = Entry(frame_triangle,
                 textvariable = side2,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num2.grid(row = 1,
              column = 1)
    
    def generate():
        
        if check(side1.get()) != False and check(side2.get()) != False:
            num3 = (float(side1.get())*float(side2.get()))/2
            history_store(num3,"Triangle")
            label_result = Label(frame_triangle,text ="Area = " + str(num3))
            label_result.grid(row = 3, 
                              column =2,
                              padx = 1,
                              pady = 3)
        button_return = Button(frame_triangle,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_triangle))
        button_return.grid(row = 4,
                               column = 2,
                               padx = 1,
                               pady = 3)
        
        
        
    
    generate=Button(frame_triangle,
                    text="Result",
                    width=29,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate,
                    borderwidth=1)
    generate.grid(row=2,
                  column=0,
                  columnspan = 2,
                  padx = 1,
                  pady = 3)


def area_rhombus():
    global frame_2D
    frame_2D.pack_forget()
    global frame_rhombus
    frame_rhombus = LabelFrame(mainframe,
                                 text = "Area of Rhombus",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_rhombus.pack(padx = 76,pady = 86)
    label1 = Label(frame_rhombus,
                   text = "Enter Diagonal 1 : ")
    label1.grid(row = 0,
                column = 0)
    
    label2 = Label(frame_rhombus,
                   text = "Enter Diagonal 2 : ")
    label2.grid(row = 1,
                column = 0)
    
                       
    side1 = StringVar()
    side2 = StringVar()
    num1 = Entry(frame_rhombus,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    num2 = Entry(frame_rhombus,
                 textvariable = side2,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num2.grid(row = 1,
              column = 1)
    
    def generate():
        
        if check(side1.get()) != False and check(side2.get()) != False:
            num3 = (float(side1.get())*float(side2.get()))/2
            history_store(num3,"Rhombus")
            label_result = Label(frame_rhombus,text ="Area = " + str(num3))
            label_result.grid(row = 3, 
                              column =2,
                              padx = 1,
                              pady = 3)
        button_return = Button(frame_rhombus,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_rhombus))
        button_return.grid(row = 4,
                               column = 2,
                               padx = 1,
                               pady = 3)
        
        
        
    
    generate=Button(frame_rhombus,
                    text="Result",
                    borderwidth=1,
                    width=32,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan=2,
                  padx = 1,
                  pady = 3)


def area_trapezoid():
    global frame_2D
    frame_2D.pack_forget()
    global frame_trapezoid
    frame_trapezoid = LabelFrame(mainframe,
                                 text = "Area of Trapezoid",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_trapezoid.pack(padx=83,pady=83)
    label1 = Label(frame_trapezoid,
                   text = "Enter Side 1 : ",
                   width = 11)
    label1.grid(row = 0,
                column = 0)
    
    label2 = Label(frame_trapezoid,
                   text = "Enter Side 2 : ",
                   width = 11)
    label2.grid(row = 1,
                column = 0)
    
    label3 = Label(frame_trapezoid,
                   text = "Enter Height : ",
                   width = 11)
    label3.grid(row = 2,
                column = 0)
                       
    side1 = StringVar()
    side2 = StringVar()
    height = StringVar()
    num1 = Entry(frame_trapezoid,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    num2 = Entry(frame_trapezoid,
                 textvariable = side2,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num2.grid(row = 1,
              column = 1)
    num3 = Entry(frame_trapezoid,
                 textvariable = height,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num3.grid(row = 2,
              column = 1)         
    
    def generate():
        
        if check(side1.get()) != False and check(side2.get()) != False and check(height.get()) != False:
            num4 = 0.5 * (float(num1.get()) + float(num2.get())) * float(num3.get())
            num4 = round(num4,2)
            history_store(num4,"Trapezoid")
            label_result = Label(frame_trapezoid,text ="Area = " + str(num4))
            label_result.grid(row = 4, 
                              column =2,
                              padx = 1,
                              pady = 3)
        button_return = Button(frame_trapezoid,
                                   text = "Return to Main Menu",
                                   command = lambda : main_menu_duplicate(frame_trapezoid))
        button_return.grid(row = 5,
                               column = 2,
                               padx = 1,
                               pady = 3)
        
        
        
    
    generate=Button(frame_trapezoid,
                    text="Result",
                    borderwidth=1,
                    width=29,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=3,
                  column=0,
                  columnspan=2,
                  padx = 1,
                  pady = 3)


#3D Shapes
def area_cube():
    global frame_3D
    frame_3D.pack_forget()
    global frame_cube
    frame_cube = LabelFrame(mainframe,
                                 text = "Area of Cube",
                                 padx = 45,
                                 pady = 24,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_cube.pack(padx = 68,pady = 93)
    label1 = Label(frame_cube,
                   text = "Enter Side Length: ")
    label1.grid(row = 0,
                column = 0)
                       
    side1 = StringVar()
    num1 = Entry(frame_cube,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
 
    def generate():
        
        if check(side1.get()) != False:
            num2 = float(side1.get())*float(side1.get())*6
            num2 = round(num2,2)
            label_result = Label(frame_cube,text ="Area = " + str(num2))
            label_result.grid(row = 3, 
                              column =2,
                              padx = 1,
                              pady = 3)
            history_store(num2,"Cube")
        button_return = Button(frame_cube,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_cube))
        button_return.grid(row = 4,
                           column = 2,
                           padx = 1,
                           pady = 2)
        
        
        
    
    generate=Button(frame_cube,
                    text="Result",
                    borderwidth=1,
                    width=32,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan=2,
                  padx = 1,
                  pady = 3)


def area_cuboid():
    global frame_3D
    frame_3D.pack_forget()
    global frame_cuboid
    frame_cuboid = LabelFrame(mainframe,
                                 text = "Area of Cuboid",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_cuboid.pack(padx=64,pady=78)
    label1 = Label(frame_cuboid,
                   text = "Enter  Length of Cuboid : ",
                   width=19)
    label1.grid(row = 0,
                column = 0)
    label2 = Label(frame_cuboid,
                   text = "Enter Breadth of Cuboid : ",
                   width=19)
    label2.grid(row = 1,
                column = 0)
    label3 = Label(frame_cuboid,
                   text = "Enter Height of Cuboid : ",
                   width=19)
    label3.grid(row = 2,
                column = 0)
                       
    l = StringVar()
    b = StringVar()
    h = StringVar()
    num1 = Entry(frame_cuboid,
                 textvariable = l,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    num2= Entry(frame_cuboid,
                textvariable = b,
                bg = "light goldenrod",
                borderwidth = 2)
    num2.grid(row = 1,
              column = 1)
    num3 = Entry(frame_cuboid,textvariable = h,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num3.grid(row = 2,
              column = 1)
 
    def generate():
        
        if check(l.get()) != False and check(b.get()) != False and check(h.get()) != False:
            num4 = (2*float(l.get())*float(b.get()))+(2*float(b.get())*float(h.get()))+(2*float(h.get())*float(l.get()))
            num4 = round(num4,2)
            label_result = Label(frame_cuboid,text ="Area = " + str(num4))
            label_result.grid(row = 4, 
                              column =2,
                              padx = 1,
                              pady = 3)
            history_store(num4,"Cuboid")
        button_return = Button(frame_cuboid,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_cuboid))
        button_return.grid(row = 5,
                           column = 2,
                           padx = 1,
                           pady = 3)
        
        
        
    
    generate=Button(frame_cuboid,
                    text="Result",
                    borderwidth=1,
                    width=37,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=3,
                  column=0,
                  columnspan=2,
                  padx = 1,
                  pady = 3)


def area_sphere():
    global frame_3D
    frame_3D.pack_forget()
    global frame_sphere
    frame_sphere = LabelFrame(mainframe,
                                 text = "Area of Sphere",
                                 padx = 45,
                                 pady = 24,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_sphere.pack(padx = 56,pady = 92)
    label1 = Label(frame_sphere,
                   text = "Enter Radius of Sphere : ")
    label1.grid(row = 0,
                column = 0)
                       
    side1 = StringVar()
    num1 = Entry(frame_sphere,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
 
    def generate():
        
        if check(side1.get()) != False: 
            num2 = (float(side1.get())**3)* 1.34 * 3.14
            num2=round(num2,2)
            label_result = Label(frame_sphere,text ="Area = " + str(num2))
            label_result.grid(row = 3, 
                          column =2,
                          padx = 1,
                          pady = 3)
            history_store(num2,"Sphere")
        button_return = Button(frame_sphere,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_sphere))
        button_return.grid(row = 4,
                           column = 2,
                           padx = 1,
                           pady = 3)
        
        
        
    
    generate=Button(frame_sphere,
                    text="Result",
                    borderwidth=1,
                    width='36',
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan=2,
                  padx = 1,
                  pady = 3)
  
  
def area_cone(): 
    global frame_3D
    frame_3D.pack_forget()
    global frame_cone
    frame_cone = LabelFrame(mainframe,
                                 text = "Area of Cone",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_cone.pack(padx = 74,pady = 81)
    label1 = Label(frame_cone,
                   text = "Enter  Radius of Cone : ",
                   width=18)
    label1.grid(row = 0,
                column = 0)
    label2 = Label(frame_cone,
                   text = "Enter Height of Cone : ",
                   width=18)
    label2.grid(row = 1,
                column = 0)
  
                       
    r = StringVar()

    h = StringVar()
    num1 = Entry(frame_cone,
                 textvariable = r,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    
    num3 = Entry(frame_cone,
                 textvariable = h,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num3.grid(row = 1,
              column = 1)
 
    def generate():
        
        if check(r.get()) != False and check(h.get()) != False:
            num4 = 3.14*float(r.get())*(float(r.get())+math.sqrt((float(h.get())**2)+(float(r.get())**2)))
            num4=round(num4,2)
            label_result = Label(frame_cone,text ="Area = " + str(num4))
            label_result.grid(row = 3, 
                          column =2,
                          padx = 1,
                          pady = 3)
            history_store(num4,"Cone")
        button_return = Button(frame_cone,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_cone))
        button_return.grid(row = 4,
                           column = 2,
                           padx = 1,
                           pady = 3)
        
        
        
    
    generate=Button(frame_cone,
                    text="Result",
                    borderwidth=1,
                    width=36,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan=2,
                  padx = 1,
                  pady = 3)


def area_cylinder():
    global frame_3D
    frame_3D.pack_forget()
    global frame_cylinder
    frame_cylinder = LabelFrame(mainframe,
                                 text = "Area of Cylinder",
                                 padx = 40,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_cylinder.pack(padx = 74,pady = 81)
    label1 = Label(frame_cylinder,
                   text = "Enter  Radius of Cylinder : ",
                   width=20)
    label1.grid(row = 0,
                column = 0)
    label2 = Label(frame_cylinder,
                   text = "Enter Height of Cylinder : ",
                   width=20)
    label2.grid(row = 1,
                column = 0)
  
                       
    r = StringVar()

    h = StringVar()
    num1 = Entry(frame_cylinder,
                 textvariable = r,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    
    num3 = Entry(frame_cylinder,
                 textvariable = h,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num3.grid(row = 1,
              column = 1)
 
    def generate():
        
        if check(r.get()) != False and check(h.get()) != False:
            num4 = 2*3.14*float(r.get())*float(h.get()) + (2*3.14+(float(r.get())**2))
            num4 = round(num4,2)
            label_result = Label(frame_cylinder,text ="Area = " + str(num4))
            label_result.grid(row = 3, 
                          column =2,
                          padx = 1,
                          pady = 3)
            history_store(num4,"Cylinder")
        button_return = Button(frame_cylinder,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_cylinder))
        button_return.grid(row = 4,
                           column = 2,
                           padx = 1,
                           pady = 3)
        
        
        
    
    generate=Button(frame_cylinder,
                    text="Result",
                    borderwidth='2',
                    width=38,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan=2,
                  padx = 1,
                  pady = 3)


def area_hemisphere():
    global frame_3D
    frame_3D.pack_forget()
    global frame_hemisphere
    frame_hemisphere = LabelFrame(mainframe,
                                 text = "Area of HemiSphere",
                                 padx = 40,
                                 pady = 26,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_hemisphere.pack(padx = 48,pady = 92)
    label1 = Label(frame_hemisphere,
                   text = "Enter Radius of HemiSphere : ")
    label1.grid(row = 0,
                column = 0)
                       
    side1 = StringVar()
    num1 = Entry(frame_hemisphere,
                 textvariable = side1,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
 
    def generate():
        
        if check(side1.get()) != False:
            num2 = 3*3.14*(float(side1.get())**2)
            num2 = round(num2,2)
            label_result = Label(frame_hemisphere,text ="Area = " + str(num2))
            label_result.grid(row = 3, 
                          column =2,
                          padx = 1,
                          pady = 3)
            history_store(num2,"Hemisphere")
        button_return = Button(frame_hemisphere,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_hemisphere))
        button_return.grid(row = 4,
                           column = 2,
                           padx = 1,
                           pady = 3)
        
        
        
    
    generate=Button(frame_hemisphere,
                    text="Result",
                    borderwidth = 1,
                    width= 40,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  columnspan = 2,
                  padx = 1,
                  pady = 3)


def area_squarepyramid():
    global frame_3D
    frame_3D.pack_forget()
    global frame_squarepyramid
    frame_squarepyramid = LabelFrame(mainframe,
                                 text = "Area of Square Pyramid",
                                 padx = 37,
                                 pady = 20,
                                 bg = 'black',
                                 fg = 'medium spring green',
                                 font = 25)
    frame_squarepyramid.pack(padx = 75,pady = 77)
    label1 = Label(frame_squarepyramid,
                   text = "Enter Base: ",
                   width = 11)
    label1.grid(row = 0,
                column = 0)
    label2 = Label(frame_squarepyramid,
                   text = "Enter Height: ",
                   width = 11)
    label2.grid(row = 1,
                column = 0)
  
                       
    r = StringVar()

    h = StringVar()
    num1 = Entry(frame_squarepyramid,
                 textvariable = r,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num1.grid(row = 0,
              column = 1)
    
    num3 = Entry(frame_squarepyramid,
                 textvariable = h,
                 bg = "light goldenrod",
                 borderwidth = 2)
    num3.grid(row = 1,
              column = 1)
 
    def generate():
        
        if check(r.get()) != False and check(h.get()) != False:
            num4 = (float(r.get())**2)+(2*float(r.get())*math.sqrt(((float(r.get())**2)/4)+(float(h.get())**2)))
            num4 = round(num4,2)
            label_result = Label(frame_squarepyramid,text ="Area = " + str(num4))
            label_result.grid(row = 3, 
                          column =2,
                          padx = 1,
                          pady = 3)
            history_store(num4,"Square Pyramid")
        button_return = Button(frame_squarepyramid,
                               text = "Return to Main Menu",
                               command = lambda : main_menu_duplicate(frame_squarepyramid))
        button_return.grid(row = 4,
                           column = 2,
                           padx = 1,
                           pady = 3)

    generate=Button(frame_squarepyramid,
                    text="Result",
                    width=29,
                    fg="Black",
                    bg="DarkOliveGreen2",
                    command=generate)
    generate.grid(row=2,
                  column=0,
                  padx = 1,
                  pady = 3,
                  columnspan = 2)

main_menu() 

root.mainloop()
