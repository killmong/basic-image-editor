import ttkbootstrap as ttk 
from tkinter import filedialog,colorchooser,Scale,messagebox,Scrollbar,Text
from tkinter.messagebox import showerror,askyesno
from PIL import ImageTk ,Image,ImageOps,ImageFilter,ImageGrab
import numpy as np
import tkinter as tk


# defining global variables
WIDTH = 1000
HEIGHT = 700
file_path = ""
pen_size = 4
pen_color = "RED"

#Windows creation
root= ttk.Window(themename="cosmo")
root.title('Canvas')
root.geometry("1000x800+330+100")
root.resizable(False,False)
icon =ttk.PhotoImage(file='Images/Canvas.png')
root.iconphoto(False,icon)




#Left fraame to contain buttons

left_frame =tk.Frame(root,width=100,height=600,border=4,borderwidth=10,bg="Light pink")
left_frame.pack(side='left',fill='y')

#right canvas2 for displaying image
canvas2 = tk.Canvas(root,width=WIDTH,height=HEIGHT,border=4,borderwidth=5,bg='Sky blue',relief='groove')
canvas2.pack()

#adding widgets to left frame
filter_label= tk.Label(left_frame,text='Select Filter:',foreground="red",background='white')
filter_label.pack(pady=3)
#image filters
image_filters = ["NONE","Contour", "Black and White", "Blur", "Detail", "Emboss", "Edge Enhance", "Sharpen", "Smooth"]


filter_combobox= ttk.Combobox(left_frame,text='(None)',values=image_filters,width= 10)
filter_combobox.pack(padx=10,pady=5)
filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))



# function to open the image file
def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    if file_path:
        global image, photo_image
        image = Image.open(file_path)
        new_width = int((WIDTH/ 2))
        image = image.resize((new_width,HEIGHT), Image.LANCZOS)
            
        image = ImageTk.PhotoImage(image)
        canvas2.create_image(0, 0, anchor="nw", image=image)
        canvas2.config(scrollregion=canvas2.bbox(tk.ALL))
        
# a global variable for checking the flip state of the image
is_flipped = False

def flip_image():
    try:
        global image, photo_image, is_flipped
        if not is_flipped:
            # open the image and flip it left and right
            image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)
            is_flipped = True
        else:
            # reset the image to its original state
            image = Image.open(file_path)
            is_flipped = False
        # resize the image to fit the canvas2
        new_width = int((WIDTH / 2))
        image = image.resize((new_width, HEIGHT), Image.LANCZOS)
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas2
        photo_image = ImageTk.PhotoImage(image)
        canvas2.create_image(0, 0, anchor="nw", image=photo_image)

    except:
        showerror(title='Flip Image Error', message='Please select an image to flip!')
        
# global variable for tracking rotation angle
rotation_angle = 0

# function for rotating the image
def rotate_image_right():
    try:
        global image, photo_image, rotation_angle
        # open the image and rotate it
        
        image = Image.open(file_path)
        new_width = int((WIDTH / 2))
        image = image.resize((new_width,HEIGHT), Image.LANCZOS)
        rotated_image = image.rotate(rotation_angle - 90)
        rotation_angle += 90
        # reset image if angle is a multiple of 360 degrees
        if rotation_angle % 360 == 0:
            rotation_angle = 0
            image = Image.open(file_path)
            image = image.resize((new_width, HEIGHT), Image.LANCZOS)
            rotated_image = image
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas2
        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas2.create_image(0, 0, anchor="nw", image=photo_image)
    # catches errors
    except:
        showerror(title='Rotate Image Error', message='Please select an image to rotate!')
        
# function for rotating the image
def rotate_image_left():
    try:
        global image, photo_image, rotation_angle
        # open the image and rotate it
        
        image = Image.open(file_path)
        new_width = int((WIDTH / 2))
        image = image.resize((new_width, HEIGHT), Image.LANCZOS)
        rotated_image = image.rotate(rotation_angle + 90)
        rotation_angle += 90
        # reset image if angle is a multiple of 360 degrees
        if rotation_angle % 360 == 0:
            rotation_angle = 0
            image = Image.open(file_path)
            image = image.resize((new_width, HEIGHT), Image.LANCZOS)
            rotated_image = image
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas2
        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas2.create_image(0, 0, anchor="nw", image=photo_image)
    # catches errors
    except:
        showerror(title='Rotate Image Error', message='Please select an image to rotate!')
        
# function for applying filters to the opened image file
def apply_filter(filter):
    global image, photo_image
    try:
        # check if the image has been flipped or rotated
        if is_flipped:
            # flip the original image left and right
            flipped_image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)
            # rotate the flipped image
            rotated_image = flipped_image.rotate(rotation_angle)
            # apply the filter to the rotated image
            if filter == "Black and White":
                rotated_image = ImageOps.grayscale(rotated_image)
            elif filter == "Blur":
                rotated_image = rotated_image.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                rotated_image = rotated_image.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                rotated_image = rotated_image.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                rotated_image = rotated_image.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                rotated_image = rotated_image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                rotated_image = rotated_image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                rotated_image = rotated_image.filter(ImageFilter.SMOOTH) 
            elif filter == "NONE":
                image = rotated_image.filter(ImageFilter.NONE)       
            else:
                rotated_image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT).rotate(rotation_angle)
        elif rotation_angle != 0:
            # rotate the original image
            rotated_image = Image.open(file_path).rotate(rotation_angle)
            # apply the filter to the rotated image
            if filter == "Black and White":
                rotated_image = ImageOps.grayscale(rotated_image)
            elif filter == "Blur":
                rotated_image = rotated_image.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                rotated_image = rotated_image.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                rotated_image = rotated_image.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                rotated_image = rotated_image.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                rotated_image = rotated_image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                rotated_image = rotated_image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                rotated_image = rotated_image.filter(ImageFilter.SMOOTH)
            elif filter == "NONE":
                image = rotated_image.filter(ImageFilter.NONE)
            else:
                rotated_image = Image.open(file_path).rotate(rotation_angle)
        else:
            # apply the filter to the original image
            image = Image.open(file_path)
            if filter == "Black and White":
                image = ImageOps.grayscale(image)
            elif filter == "Blur":
                image = image.filter(ImageFilter.BLUR)
            elif filter == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
            elif filter == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
            elif filter == "Detail":
                image = image.filter(ImageFilter.DETAIL)
            elif filter == "Edge Enhance":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Contour":
                image = image.filter(ImageFilter.CONTOUR)
            rotated_image = image
        # resize the rotated/flipped image to fit the canvas2
        new_width = int((WIDTH / 2))
        rotated_image = rotated_image.resize((new_width, HEIGHT), Image.LANCZOS)
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas2
        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas2.create_image(0, 0, anchor="nw", image=photo_image)
    except:
        showerror(title='Error', message='Please select an image first!')

    
# the function for saving an image
def save_image():
    global file_path, is_flipped, rotation_angle
    if file_path:
        # create a new PIL Image object from the canvas2
        image = ImageGrab.grab(bbox=(canvas2.winfo_rootx(), canvas2.winfo_rooty(), canvas2.winfo_rootx() + canvas2.winfo_width(), canvas2.winfo_rooty() + canvas2.winfo_height()))
        # check if the image has been flipped or rotated
        if is_flipped or rotation_angle % 360 != 0:
            # Resize and rotate the image
            new_width = int((WIDTH / 2))
            image = image.resize((new_width, HEIGHT), Image.LANCZOS)
            if is_flipped:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            if rotation_angle % 360 != 0:
                image = image.rotate(rotation_angle)
            # update the file path to include the modifications in the file name
            file_path = file_path.split(".")[0] + "_mod.jpg"
        # apply any filters to the image before saving
        filter = filter_combobox.get()
        if filter:
            if filter == "Black and White":
                image = ImageOps.grayscale(image)
            elif filter == "Blur":
                image = image.filter(ImageFilter.BLUR)
            elif filter == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
            elif filter == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
            elif filter == "Detail":
                image = image.filter(ImageFilter.DETAIL)
            elif filter == "Edge Enhance":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Contour":
                image = image.filter(ImageFilter.CONTOUR)
            elif filter == "None":
                image = image.filter(ImageFilter.NONE)
            # update the file path to include the filter in the file name
            file_path = file_path.split(".")[0] + "_" + filter.lower().replace(" ", "_") + ".jpg"
        # open file dialog to select save location and file type
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
     
            if askyesno(title='Save Image', message='Do you want to save this image?'):
                # save the image to a file
                image.save(file_path)
                
        else:
                messagebox.showinfo("Info", "Image not saved.")
                # Optionally, you can destroy the dialog box
                root.update_idletasks()
                root.update()
                root.focus_set()
                root.destroy()
                

# function for drawing lines on the opened image
def draw(event):
    global file_path
    if file_path:
        x1, y1 = (event.x - pen_size), (event.y - pen_size)
        x2, y2 = (event.x + pen_size), (event.y + pen_size)
        canvas2.create_oval(x1, y1, x2, y2, fill=pen_color, outline="", width=pen_size, tags="oval")



# binding the Canvas to the B1-Motion event
canvas2.bind("<B1-Motion>", draw)


#images of buttons 
imageadd=ttk.PhotoImage(file='Images/Add.png').subsample(12,12)
flip_icon =ttk.PhotoImage(file='Images/flip.png').subsample(12,12)
color_icon =ttk.PhotoImage(file='Images/color.png').subsample(12,12)
erase_icon =ttk.PhotoImage(file='Images/erase.png').subsample(12,12)
rotate_left=ttk.PhotoImage(file='Images/rotate left.png').subsample(12,12)
rotate_right= ttk.PhotoImage(file='Images/rotate right.png').subsample(12,12)
save_icon=ttk.PhotoImage(file='Images/save.png').subsample(12,12)

# function for changing the pen color
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]
colorbtn=ttk.Button(left_frame,image=color_icon,bootstyle='light',command=change_color)






# function for erasing lines on the opened image
def erase_lines():
    global file_path
    if file_path:
        canvas2.delete("oval")

erasebtn=ttk.Button(left_frame,image=erase_icon,bootstyle='light',command=erase_lines)




file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
save_button = ttk.Button(left_frame, image=save_icon, bootstyle="light", command=save_image)




# buttons on left frame
imageadd_btn=ttk.Button(left_frame,text='ADD',image=imageadd,bootstyle = 'light',command=open_image)
flipbtn=ttk.Button(left_frame,image=flip_icon,text='flip',bootstyle='light',command=flip_image)
rotateleft_btn=ttk.Button(left_frame,image=rotate_left,text='rotate right',bootstyle='light',command=rotate_image_left)
rotateright_btn=ttk.Button(left_frame,image=rotate_right,text='rotate left',bootstyle='light',command=rotate_image_right)
savebtn=ttk.Button(left_frame,image=save_icon,text='Save',bootstyle='light',command=save_image)


#packing buttons
imageadd_btn.pack(pady=5)
flipbtn.pack(pady=5)
rotateleft_btn.pack(pady=5)
rotateright_btn.pack(pady=5)
colorbtn.pack(pady=5)
erasebtn.pack(pady=5)
savebtn.pack(pady=5)
        






root.mainloop()