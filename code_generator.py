from tkinter import messagebox
from qrcode import *
from tkinter import *
import image 

#Creating the window
window= Tk()
window.title('GUI application')
window.geometry('1000x1000')
window.config(bg='black')

#Label for the window
headingFrame = Frame(window,bg="white",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headinglabel = Label(headingFrame, font= ('Times', 25, 'bold'), bg= 'turquoise', fg='white', text= 'QR Code Generator')
headinglabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code
label1 = Label(window, text= 'Enter the text/URL : ', fg= 'turquoise', bg='black', font=('times', 15))
label1.place(x=150, y=170)

entry1 = Entry(window, bg='whitesmoke', fg='red', font=('times', 15), width= 70, bd= 3)
entry1.place(x= 150,y=200)

#Getting input of the location to save QR Code
label2 = Label(window, text= 'Enter the location to save the QR code : ', fg= 'turquoise', bg='black', font=('times', 15))
label2.place(x=150, y=270)

entry2 = Entry(window, bg='whitesmoke', fg='red', font=('times', 15), width= 70, bd= 3)
entry2.place(x= 150,y=300)

#Getting input of the QR Code image name
label3 = Label(window, text= 'Enter the name of QR code : ', fg= 'turquoise', bg='black', font=('times', 15))
label3.place(x=150, y=370)

entry3 = Entry(window, bg='whitesmoke', fg='red', font=('times', 15), width= 70, bd= 3)
entry3.place(x= 150,y=400)

#Getting the input of the size of the QR Code
label4 = Label(window, text= 'Enter the size from 1 to 40 with 1 being 21x21 : ', fg= 'turquoise', bg='black', font=('times', 15))
label4.place(x=150, y=470)

entry4 = Entry(window, bg='whitesmoke', fg='red', font=('times', 15), width= 70, bd= 3)
entry4.place(x= 150,y=500)

location= entry1.get()
path_save= entry2.get()
name_qr= entry3.get()
size= entry4.get()

def gen_code():
    qr= qrcode.QRCode( version= size,
                       border= 5,
                       box_size= 10
                     )
    qr.add_data(location)
    qr.make(fit= True)
    img= qr.make_image( fill= 'black', back_colour= 'white')

    fileDirec = path_save+ '\\' + name_qr
    img.save(fileDirec.png)

    messagebox.showinfo('QR Code Generator', 'QR Code is saves successfully !')


#Button to generate and save the QR Code
button = Button(window, bg= 'turquoise', fg='blue', font=('times', 15, 'bold'), bd= 3, text='Generate Code', command= gen_code )
button.place(x= 425, y= 600)


#Runs the window till it is closed manually
window.mainloop()
