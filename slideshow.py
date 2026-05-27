from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("image Slideshow Viewer=")
# list of image path..
image_paths=[
    r" #path of the picture....",
    r" path of another pictures..."
]
# resize iimages to 1080*1080
image_size=(100,100)
images =[Image.open(path).resize(image_size)for path in image_paths]
photo_images=[ImageTk.PhotoImage(image)for image in images]

label=tk.Label(root)
label.pack()
def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)
slideshow=cycle(photo_images)

def start_Slideshow():
    for _ in range(len(image_paths)):
        update_image()

# to stop slideshow
def stop_slideshow(event=None):
    root.destroy()
    
root.bind("<space>",stop_slideshow)

play_button=tk.Button(root,text="---PLAY SlideShow!!----",command=start_Slideshow)
play_button.pack()
root.mainloop()