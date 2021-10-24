from tkinter import *
import tkinter.messagebox as tmsg

def check():
    statusvar.set("Calculating..")
    sbar.update()
    import time
    from speedtest import Speedtest
    st = Speedtest()
    time.sleep(2)
    statusvar.set("Result is Ready... ")
    tmsg.showinfo("Test-Result",f"Your {var.get()} Download Speed  {round(st.download()) /  1048576}Mb/s & upload speed is {round(st.upload())/   1048576}Mb/s")

    print("Done")




root=Tk()
root.geometry("544x233")
root.title("@Avk NetSpeed")
root.maxsize(544,233)

Label(root,text="NetSpeed Test",font="lucida 19  bold",bg="black",fg="white").pack()




var=StringVar()
var.set("ISP")

statusvar=StringVar()
statusvar.set("Run")

sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)

Label(root,text="Which type of Connection you use ?",font="lucida 19  bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Mobie Data",font="lucida 12 ",padx=14,variable=var,value="Mobile Data").pack(anchor="w")
radio=Radiobutton(root,text="Wifi",font="lucida 12 ",padx=14,variable=var,value="Wifi").pack(anchor="w")

Button(root,text="Start Test",command=check).pack()

# Add StatusBar



root.mainloop()


