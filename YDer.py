from tkinter import *
from tkinter import  filedialog
from pytube  import YouTube
from PIL import Image, ImageTk
import threading

# -------------------- Main Functions --------------------



def browse():

    directory = filedialog.askdirectory(title="Save Video")
    FloderLink.delete(0,"end")
    FloderLink.insert (0,directory)


def down_yt():
    Status.config(text="Status: Downloading ...")
    Link =  YouTube(YtLink.get(), on_complete_callback=finsh)
    Folder = FloderLink.get() 
    video_stream = Link.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().first()
    video_stream.download(output_path=Folder)



def finsh(stream= None,chunk= None,file_handle= None,remining= None,):
    Status.config(text="Status: Complete ...")

# -------------------- GUI --------------------


root = Tk()
root.title("YDer")
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position - 60}")
root.resizable(False, False)

#img Logo
ImgLogo = Image.open("C:/Users/Admin.DESKTOP-QKNRRPJ/Desktop/YDer/ImgLogo.png")
resize_image = ImgLogo.resize((125, 125))
img = ImageTk.PhotoImage(resize_image)
image = Label(root, image=img)
image.place(x=5, y=15 )

#Youtube Link 
YtLable = Label(root , text="Youtube Link")
YtLable.place(  x=110,y=150)

YtLink = Entry(root ,width=60)
YtLink.place(x=220,y=150)


# Download Folder
FloderLable = Label(root , text="Download Folder")
FloderLable.place( x=110,y=180 )

FloderLink = Entry(root ,width=50)
FloderLink.place(x=220,y=180)


#Browse Button 
browse = Button(root, text="Browse",command = browse)
browse.place(x=530,y=180)

#Download Button

download =  Button(root, text="Download",command=threading.Thread(target=down_yt).start)
download.place(x=350 , y=220)

# Status bar 
Status = Label(root, text="Status: Ready" , font="Calibre 10 italic", fg="black" , bg="white" , anchor="w")
Status.place(rely= 1 , anchor="sw" , relwidth=1 )

root.mainloop()