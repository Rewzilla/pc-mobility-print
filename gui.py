from tkinter import messagebox
from pcmobilityprint import *
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import *

# Color customization! -> Tkinter still messes up with themes sometimes
FG_PRINTER_LIST_SEL = "#bdc3c7"
BG_PRINTER_LIST_SEL = "#2c3e50"
FG_PRINTER_LIST     = "#2c3e50"
BG_PRINTER_LIST     = "#bdc3c7"
FG_HOVER_BUTTON     = "#2c3e50"
BG_HOVER_BUTTON     = "#bdc3c7"
FG_CHECKBOX         = "#ecf0f1"
BG_CHECKBOX         = "#2c3e50"
FG_BUTTON           = "#2c3e50"
BG_BUTTON           = "#bdc3c7"
FG_ENTRY            = "#2c3e50"
BG_ENTRY            = "#bdc3c7"
FG_LABEL            = "#ecf0f1"
BG_LABEL            = "#2c3e50"
BG_ROOT             = "#2c3e50"

class App:
    def __init__(self, root):
        # Need this dood for adding / listing
        self.pcmp = None
        self.verify_ssl = BooleanVar()
        self.network_printer_list = StringVar()

        root.title("PC Mobility Print")

        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ft = tkFont.Font(family='Times',size=14)

        ## This Section is organized...
        # LABEL
        # ENTRY
        ##

        ## PRINTER LIST BOX
        self.printer_list=Listbox(root, listvariable=self.network_printer_list, selectmode=MULTIPLE)
        self.printer_list["borderwidth"] = "1px"
        self.printer_list["font"] = ft
        self.printer_list["fg"] = FG_ENTRY
        self.printer_list["bg"] = BG_ENTRY
        self.printer_list["selectforeground"] = FG_PRINTER_LIST_SEL
        self.printer_list["selectbackground"] = BG_PRINTER_LIST_SEL
        self.printer_list.place(x=25,y=20,width=305,height=400)

        ## USERNAME
        username_id=Label(root)
        username_id["font"] = ft
        username_id["fg"] = FG_LABEL
        username_id["bg"] = BG_LABEL
        username_id["justify"] = "center"
        username_id["text"] = "Username"
        username_id.place(x=360,y=20,width=205,height=30)

        self.username=Entry(root)
        self.username["borderwidth"] = "1px"
        self.username["font"] = ft
        self.username["fg"] = FG_ENTRY
        self.username["bg"] = BG_ENTRY
        self.username["justify"] = "center"
        self.username.place(x=360,y=50,width=205,height=30)


        # PASSWORD
        password_id=Label(root)
        password_id["font"] = ft
        password_id["fg"] = FG_LABEL
        password_id["bg"] = BG_LABEL
        password_id["justify"] = "center"
        password_id["text"] = "Password"
        password_id.place(x=360,y=100,width=205,height=30)

        self.password=Entry(root)
        self.password["borderwidth"] = "1px"
        self.password["font"] = ft
        self.password["show"] = "*"
        self.password["fg"] = FG_ENTRY
        self.password["bg"] = BG_ENTRY
        self.password["justify"] = "center"
        self.password.place(x=360,y=130,width=205,height=30)

        # SERVER
        server_id=Label(root)
        server_id["font"] = ft
        server_id["fg"] = FG_LABEL
        server_id["bg"] = BG_LABEL
        server_id["justify"] = "center"
        server_id["text"] = "Server"
        server_id.place(x=360,y=180,width=205,height=30)

        self.server=Entry(root)
        self.server["borderwidth"] = "1px"
        self.server["font"] = ft
        self.server["fg"] = FG_ENTRY
        self.server["bg"] = BG_ENTRY
        self.server["justify"] = "center"
        self.server.place(x=360,y=210,width=205,height=30)

        # DOMAIN
        domain_id=Label(root)
        domain_id["font"] = ft
        domain_id["fg"] = FG_LABEL
        domain_id["bg"] = BG_LABEL
        domain_id["justify"] = "center"
        domain_id["text"] = "Domain"
        domain_id.place(x=360,y=260,width=205,height=30)

        self.domain=Entry(root)
        self.domain["borderwidth"] = "1px"
        self.domain["font"] = ft
        self.domain["fg"] = FG_ENTRY
        self.domain["bg"] = BG_ENTRY
        self.domain["justify"] = "center"
        self.domain.place(x=360,y=290,width=205,height=30)


        # BUTTONS
        scan_button=Button(root)
        scan_button["font"] = ft
        scan_button["fg"] = FG_BUTTON
        scan_button["bg"] = BG_BUTTON
        scan_button["activeforeground"] = FG_HOVER_BUTTON
        scan_button["activebackground"] = BG_HOVER_BUTTON
        scan_button["justify"] = "center"
        scan_button["text"] = "Scan"
        scan_button.place(x=25,y=430,width=305,height=50)
        scan_button["command"] = self.scan_button_command

        add_button=Button(root)
        add_button["font"] = ft
        add_button["fg"] = FG_BUTTON
        add_button["bg"] = BG_BUTTON
        add_button["activeforeground"] = FG_HOVER_BUTTON
        add_button["activebackground"] = BG_HOVER_BUTTON
        add_button["justify"] = "center"
        add_button["text"] = "Add Printers"
        add_button.place(x=360,y=370,width=205,height=65)
        add_button["command"] = self.add_button_command

        # Checkbox
        verify_ssl=Checkbutton(root)
        verify_ssl["fg"] = FG_CHECKBOX
        verify_ssl["bg"] = BG_CHECKBOX
        verify_ssl["activeforeground"] = FG_CHECKBOX
        verify_ssl["activebackground"] = BG_CHECKBOX
        verify_ssl["selectcolor"] = BG_CHECKBOX
        verify_ssl["justify"] = "center"
        verify_ssl["text"] = "Verify SSL"
        verify_ssl["variable"] = self.verify_ssl
        verify_ssl.place(x=360,y=450,width=70,height=30)
        verify_ssl["command"] = lambda: self.update_pcmp()
        verify_ssl["onvalue"] = True
        verify_ssl["offvalue"] = False


    def scan_button_command(self):
        self.update_pcmp()
        self.printer_list.delete(0, END)
        printers = self.pcmp.get_printers()
        self.network_printer_list.set(' '.join([f"{printer['name']:24}" for printer in printers]))

# ??? this adds duplicate lines, looks broken, commenting out unless there's a reason I don't understand?
#        for printer in self.network_printer_list.get().split(" "):
#            self.printer_list.insert(END, printer)

    def add_button_command(self):
        self.update_pcmp()

        username = self.username.get()
        password = self.password.get()

        if not self.pcmp.authenticate(username, password):
            print("Authentication error")
            return

        selected_printers = self.printer_list.curselection()
        for i in selected_printers:
            entry = self.printer_list.get(i)
            self.pcmp.add_printer(entry)

        messagebox.showinfo('Success!','Printers added!')

    def update_pcmp(self):
        server_entry = self.server.get()
        domain_entry = self.domain.get()

        server = None if server_entry == "" else server_entry
        domain = None if domain_entry == "" else domain_entry

        self.pcmp = PCMobilityPrint(server=server, domain=domain)
        self.pcmp.verify_ssl = self.verify_ssl.get()

if __name__ == "__main__":
    root = Tk()
    root['bg'] = BG_ROOT
    app = App(root)
    root.mainloop()
