import tkinter as tk # Importing the tkinter module
from PIL import ImageTk, Image # Importing the ImageTk and Image module from pillow library
import random # Importing the random module

window = tk.Tk() # Creating the window
window.title("Roll The Dice") # Adding a title to the window
window.geometry("300x320") # Setting the size of the window

dice_arr = ["one.png", "two.png", "three.png", "four.png", "five.png", "six.png"] # Creating a list of dice images
dice_img = ImageTk.PhotoImage(Image.open(random.choice(dice_arr)).resize((200, 200))) # Creating a random dice image (ImageTk.PhotoImage is used to convert the image into a tkinter readable format, PhotoImage is used to display the image, Image.open is used to open the image, random.choice is used to choose a random image from the list, dice_arr is the list of dice images, resize is used to resize the image)
dice_label = tk.Label(window, image=dice_img) # Creating a label to display the dice image (label is used to display text or images, window is the window in which the label is displayed, image is used to display the image, dice_img is the image to be displayed)
# what is label?
# label is used to display text or images in a window or frame (label is a widget)
dice_label.image = dice_img # Storing the image in the label
#dice_label.pack(expand=True) # Placing the label in the window (pack is used to place the widget in the window, expand is used to expand the widget to fill the window)
dice_label.place(x=50, y=40) # Placing the label in the window (place is used to place the widget in the window, x is the x coordinate of the widget, y is the y coordinate of the widget)
def roll():
    dice_img = ImageTk.PhotoImage(Image.open(random.choice(dice_arr)).resize((200, 200))) # Creating a random dice image 
    dice_label.configure(image=dice_img) # Configuring the label to display the dice image (label is used to display text or images, image is used to display the image, dice_img is the image to be displayed)
    dice_label.image = dice_img # Storing the image in the label

button = tk.Button(window, text="Roll The Dice", command=roll, bg="crimson", fg="white", font="Helvetica 16 bold", padx=5, pady=2.5, borderwidth=2, relief="raised") # Creating a button to roll the dice (button is used to create a button, window is the window in which the button is displayed, text is the text displayed on the button, command is the function called when the button is clicked, roll is the function called when the button is clicked)
button.place(x=75, y=260) # Placing the button in the window (place is used to place the widget in the window, x is the x coordinate of the widget, y is the y coordinate of the widget)




window.mainloop()
