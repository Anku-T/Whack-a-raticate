import customtkinter
from tkinter import *
from PIL import Image
import random
from time import *
import threading

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 


app = customtkinter.CTk()

width = 1440
height = 900

app.geometry(f"{width}x{height}")
app.attributes('-fullscreen', True)
app.title("Whack A Raticate")

score = 0
hole = 0
highscore= 0 


 #all the musics
 



#background image!!!
homepic =  customtkinter.CTkImage(Image.open("home screen.png"), size=(width, height))

Home_screen =  customtkinter.CTkLabel(app, image = homepic, text = '')
Home_screen.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#scoreboard label!!
score_label = customtkinter.CTkLabel(master=Home_screen,
                                     text = f"Score:{score}",
                                     bg_color="#1d5731",#21c65a
                                     width = 220,
                                     height = 50,
                                     font = ("PokemonGB",25,),
                                     text_color="white"
                                     )
score_label.place(x = 110, y =130)


#High score board!
highscore_dekhau = customtkinter.CTkLabel(master=Home_screen,
                                          text = f"High Score: {highscore}",
                                          bg_color = "#21c65a",
                                          width=10,
                                          height=50,
                                          font=("PokemonGB",25),
                                          text_color="Black"
                                          )
highscore_dekhau.place(x = 960, y = 130)

#rat image when it is clicked aka. hit
bonked = customtkinter.CTkImage(Image.open("rat.png"), size=(170,160))
shiny_bonk = customtkinter.CTkImage(Image.open("shiny_bonk.png"), size=(170,160))

#the "ready!" "set!" "go!" ko placeholder
kailesurugarne = customtkinter.CTkLabel(text = '',
                                        master=Home_screen,
                                        bg_color = "Black",
                                        corner_radius=0,
                                        fg_color= "white",
                                        width=250,
                                        height=50,
                                        font =("PokemonGB",30),
                                        text_color="black"
                                        )

#when start button pressed, this will happen
def start(): 
    
    global score
    score = 0
    score_label.configure(text = f"Score:{score}")
    replaybtn.place_forget()
    kailesurugarne.place(x = width/2-150, y = 130)
    t = threading.Thread(target=whac_a_mole)
    t.start()
 
#when a rat is hit aka whacked, this def will run  
def onwhack():
    global hole
    global score
    if hole == 1:
        trigger_rat1.configure(state='disabled', image=bonked)
    elif hole == 2:
        trigger_rat2.configure(state='disabled', image=bonked)
    elif hole == 3:
        trigger_rat3.configure(state='disabled', image=bonked)
    elif hole == 4:
        trigger_rat4.configure(state='disabled', image=bonked)
    elif hole == 5:
        trigger_rat5.configure(state='disabled', image=bonked)
    elif hole == 6:
        trigger_rat6.configure(state='disabled', image=bonked)
    elif hole == 7:
        trigger_rat7.configure(state='disabled', image=bonked)
    elif hole == 8:
        trigger_rat8.configure(state='disabled', image=bonked) 

    score += 10
    score_label.configure(text=f"Score:{score}")
    
def goldwhack():
    global hole
    global score
    trigger_ratG.configure(state='disabled', image=shiny_bonk)

    score += 250
    score_label.configure(text=f"Score:{score}")
  
#all the rat images for the 8 holes  

rat1 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (160, 160))
rat2 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (170, 160))
rat3 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (170, 160))
rat4 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (170, 160))
rat5 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (170, 160))
rat6 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (170, 160))
rat7 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (170, 160))
rat8 = customtkinter.CTkImage(Image.open("rat on mud.png"), size = (170, 160))
ratG = customtkinter.CTkImage(Image.open("shiny_rat.png"), size = (170, 160))

#rat1
trigger_rat1 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat1, 
                                      command= onwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      )  

#rat2
trigger_rat2 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat2, 
                                      command=onwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 

#rat3
trigger_rat3 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat3, 
                                      command=onwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 

#rat4
trigger_rat4 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat4, 
                                      command=onwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 
  
#rat5
trigger_rat5 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat5, 
                                      command=onwhack, 
                                      text='',
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 

#rat6
trigger_rat6 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat6, 
                                      command=onwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 

#rat7
trigger_rat7 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat7, 
                                      command=onwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 

#rat8
trigger_rat8 = customtkinter.CTkButton(master=Home_screen, 
                                      #image = rat8, 
                                      command=onwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 

#GOLDEN RAT!

trigger_ratG = customtkinter.CTkButton(master=Home_screen, 
                                      image = ratG, 
                                      command=goldwhack, 
                                      text='', 
                                      state='disabled',
                                      fg_color='#21c65a', 
                                      height=10, 
                                      width = 10,
                                      corner_radius=0,
                                      hover = False,
                                      ) 

trigger_rat1.place(x = 220, y = 255)
trigger_rat2.place(x = 600, y = 255)
trigger_rat3.place(x = 1000, y = 255)
trigger_rat4.place(x = 400, y = 400)
trigger_rat5.place(x = 790, y = 400)
trigger_rat6.place(x = 210, y = 530)
trigger_rat7.place(x = 600, y = 530)
trigger_rat8.place(x = 1000, y = 520)

    
def whac_a_mole():
    ready_set_whack()
    global hole
    global score
    global highscore
    for i in range(0, 76):
        hole = random.randint(1, 8)
        if i == 43 :
            if hole == 1:
                
                trigger_ratG.configure(
                   state='normal',)
                trigger_ratG.place(x = 220, y = 255)
                sleep(0.5)
                trigger_ratG.configure(state='disabled',)
                trigger_ratG.place_forget()
            elif hole == 2:
                
                trigger_ratG.configure(
                     state='normal',
                     image = ratG,)
                trigger_ratG.place(x = 600, y = 255)
                sleep(0.5)
                trigger_ratG.configure(state='disabled', text='',)
                trigger_ratG.place_forget()
            elif hole == 3:
                
                trigger_ratG.configure(
                    state='normal',
                    image = ratG,)
                trigger_ratG.place(x = 1000, y = 255)
                sleep(0.5)
                trigger_ratG.configure(state='disabled', text='',)
                trigger_ratG.place_forget()
            elif hole == 4:
                
                trigger_ratG.configure(
                    state='normal',
                    image = ratG,)
                trigger_ratG.place(x = 400, y = 400)
                sleep(0.5)
                trigger_ratG.configure(state='disabled', text='',)
                trigger_ratG.place_forget()
            elif hole == 5:
                
                trigger_ratG.configure(
                    state='normal',
                    image = ratG,)
                trigger_ratG.place(x = 790, y = 400)
                sleep(0.5)
                trigger_ratG.configure(state='disabled', text='',)
                trigger_ratG.place_forget()
            elif hole == 6:   
                
                trigger_ratG.configure(
                    state='normal',
                    image = ratG,)
                trigger_ratG.place(x = 210, y = 530)
                sleep(0.5)
                trigger_ratG.configure(state='disabled', text='',)
                trigger_ratG.place_forget()
            elif hole == 7:
                
                trigger_ratG.configure(
                    state='normal',
                    image = ratG,)
                trigger_ratG.place(x = 600, y = 530)
                sleep(0.5)
                trigger_ratG.configure(state='disabled', text='',)
                trigger_ratG.place_forget()
            elif hole == 8:
                
                trigger_ratG.configure(
                    state='normal',
                    image = ratG,)
                trigger_ratG.place(x = 1000, y = 520)
                sleep(0.5)
                trigger_ratG.configure(state='disabled', text='',)
                trigger_ratG.place_forget()
        else:
            if hole == 1:
                
                trigger_rat1.configure(
                   state='normal',
                  image = rat1,)
                trigger_rat1.place(x = 220, y = 255)
                sleep(0.75)
                trigger_rat1.configure(state='disabled',)
                trigger_rat1.place_forget()
            elif hole == 2:
                
                trigger_rat2.configure(
                     state='normal',
                     image = rat2,)
                trigger_rat2.place(x = 600, y = 255)
                sleep(0.75)
                trigger_rat2.configure(state='disabled', text='',)
                trigger_rat2.place_forget()
            elif hole == 3:
                
                trigger_rat3.configure(
                    state='normal',
                    image = rat3,)
                trigger_rat3.place(x = 1000, y = 255)
                sleep(0.75)
                trigger_rat3.configure(state='disabled', text='',)
                trigger_rat3.place_forget()
            elif hole == 4:
                
                trigger_rat4.configure(
                    state='normal',
                    image = rat4,)
                trigger_rat4.place(x = 400, y = 400)
                sleep(0.75)
                trigger_rat4.configure(state='disabled', text='',)
                trigger_rat4.place_forget()
            elif hole == 5:
                
                trigger_rat5.configure(
                    state='normal',
                    image = rat5,)
                trigger_rat5.place(x = 790, y = 400)
                sleep(0.75)
                trigger_rat5.configure(state='disabled', text='',)
                trigger_rat5.place_forget()
            elif hole == 6:   
                
                trigger_rat6.configure(
                    state='normal',
                    image = rat6,)
                trigger_rat6.place(x = 210, y = 530)
                sleep(0.75)
                trigger_rat6.configure(state='disabled', text='',)
                trigger_rat6.place_forget()
            elif hole == 7:
                
                trigger_rat7.configure(
                    state='normal',
                    image = rat7,)
                trigger_rat7.place(x = 600, y = 530)
                sleep(0.75)
                trigger_rat7.configure(state='disabled', text='',)
                trigger_rat7.place_forget()
            elif hole == 8:
                
                trigger_rat8.configure(
                    state='normal',
                    image = rat8,)
                trigger_rat8.place(x = 1000, y = 520)
                sleep(0.75)
                trigger_rat8.configure(state='disabled', text='',)
                trigger_rat8.place_forget()
    replaybtn.place(relx = 0.5, rely=0.5, anchor=CENTER)
    if score > highscore: 
        highscore = score
        highscore_dekhau.configure(text=f"High Score: {score}")

def ready_set_whack():
    kailesurugarne.configure(text="Ready",)
    sleep(1)
    kailesurugarne.configure(text="Set")
    sleep(1)
    kailesurugarne.configure(text="WHACK!!")
    sleep(1)
    kailesurugarne.place_forget()
    
replaybtn =customtkinter.CTkButton(master=Home_screen,
                                   text="Start",
                                   font=("PokemonGB", 30), 
                                   command=start,
                                   width = 80,
                                   height = 60,
                                   border_width=5,
                                   corner_radius= 5,
                                   border_spacing=5,
                                   bg_color='#21c65a', 
                                   border_color="#062b44", 
                                   hover=False                           
                                   )
replaybtn.place(relx = 0.5, rely=0.5, anchor=CENTER)
#replaybtn.place(x = 10, y = 10,)
app.mainloop()
