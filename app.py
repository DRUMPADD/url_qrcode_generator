import qrcode
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning
app = Tk()
app.title("QR code generator")
app.geometry("300x100")
url_choices = {
    "com": "com",
    "mx": "mx",
    "gov": "gov",
    "gob": "gob",
    "org": "org",
    "net": "net",
    "biz": "biz",
    "info": "info",
    "edu": "edu",
}

principal = ttk.LabelFrame(app, padding=20, text="Principal", borderwidth=10).pack()
url = StringVar()

def convert_to_qrcode(box_size=0):
    url_correct = str(url.get())
    if len(url_correct.split(".")) > 1 and url_correct.split(".")[0] != "":
        if url_correct.split(".")[1] in url_choices:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size= box_size if box_size > 0 else 20, border=1)
            qr.add_data(url.get())
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save("{0}_qrcode.png".format(url_correct.split(".")[0]))
            if img:
                showinfo("Success", "QR code created")
        else:
            showwarning("Warning", "Url incorrect")
    else:
        showerror("Error", "Must provide an url")

ttk.Label(principal, text="URL: ").pack()
ttk.Entry(principal, textvariable=url, width=25).pack()
ttk.Button(principal, text="Convert", command=convert_to_qrcode, width=20).pack()


app.mainloop()