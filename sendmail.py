from tkinter import*

def SlcBack():
    SendMail.destroy()
    import option


SendMail = Tk()
SendMail.title("Gửi Mail")
SendMail.geometry("300x300")

### button để quay lại tab option
btnBack = Button(SendMail,text="Back",command = SlcBack)
btnBack.place(x=250,y=260)
