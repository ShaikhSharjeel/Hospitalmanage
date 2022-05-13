from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox

class Hospital:
    def __init__(self,root) -> None:
        self.root = root
        self.root.title ("Hospital Management System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background='powder blue')
        
        tabletname = StringVar()
        ref = StringVar()
        dose = StringVar()
        nooftablets = StringVar()
        issuedate = StringVar()
        dailydose = StringVar()
        pid = StringVar()
        pname = StringVar()
        pdob = StringVar()
        page = StringVar()
        bloodpressure = StringVar()
        pnumber = StringVar()
        doctor = StringVar()
        paddress = StringVar()
        prescription = StringVar()
        
        # Function
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def iPrescription():
            self.prescription.insert(END,'Name of Tablet : \t\t' + tabletname.get() +"\n")
            self.prescription.insert(END,'Reference No : \t\t' + ref.get() +"\n")
            self.prescription.insert(END,'Dosage : \t\t' + dose.get() +"\n")
            self.prescription.insert(END,'Date of issue : \t\t' + issuedate.get() +"\n")
            self.prescription.insert(END,'Daily dosage : \t\t' + dailydose.get() +"\n")
            self.prescription.insert(END,'Patient ID : \t\t' + pid.get() +"\n")
            self.prescription.insert(END,'Patient Name : \t\t' + pname.get() +"\n")
            self.prescription.insert(END,'Patient age : \t\t' + page.get() +"\n")
            self.prescription.insert(END,'Consulting Doctor : \t\t' +'Dr'+doctor.get() +"\n")
            # self.prescription.insert(END,'Name of Tablet : \t\t' + tabletname.get() +"\n")
            
            return
        
        def iPrescriptionData():
            # self.lbllabel = Label(framedetail, font=('arial',8,'bold'), text="Name of tablet\tReference No.\tDosage\t No. of Tabletst\tIssue Date\tDaily Dose\t Blood Pressure\tDoctor\tPatient ID\tPatient Name\tPatient Age\tPatient DOB\tPhone No.\tAddress ", pady=8)
            # self.lbllabel.grid(row=0,column=0)
            
            self.detailframe.insert(END,tabletname.get() +'\t\t   '+ref.get()+'\t        '+dose.get()+'\t      '+nooftablets.get()+'\t\t'+issuedate.get()+'\t\t'+dailydose.get()+'\t\t'+bloodpressure.get()+'\t'+doctor.get()+'\t'+pid.get()+'\t   '+pname.get()+'\t\t'+page.get()+'\t'+pdob.get()+'\t        '+pnumber.get()+'\t\t'+paddress.get()+'\n')
        
            return
        
        def iDelete():
            tabletname.set("")
            # self.tabletname.current(0)
            ref.set("")
            dose.set("")
            nooftablets.set("")
            issuedate.set("")
            dailydose.set("")
            pid.set("")
            pname.set("")
            pdob.set("")
            page.set("")
            bloodpressure.set("")
            pnumber.set("")
            doctor.set("")
            paddress.set("")
            self.prescription.delete("1.0",END)
            self.detailframe.delete("1.0",END)
        
        def iReset():
            tabletname.set("")
            # self.tabletname.current(0)
            ref.set("")
            dose.set("")
            nooftablets.set("")
            issuedate.set("")
            dailydose.set("")
            pid.set("")
            pname.set("")
            pdob.set("")
            page.set("")
            bloodpressure.set("")
            pnumber.set("")
            doctor.set("")
            paddress.set("")
            self.prescription.delete("1.0",END)
            # self.detailframe.delete("1.0",END)
        
        
        
        mainframe = Frame(self.root)
        mainframe.grid()
        
        titleframe = Frame(mainframe, bd=20, width=1350, padx=20, relief=RIDGE)
        titleframe.pack(side=TOP)
        
        self.lbltitle = Label(titleframe, font=('arial',40,'bold'), text="Hospital Management System", padx=2)
        self.lbltitle.grid()
        
        framedetail = Frame(mainframe, bd=20, width=1350, height=150, padx=20, relief=RIDGE)
        framedetail.pack(side=BOTTOM)
        
        buttonframe = Frame(mainframe, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        buttonframe.pack(side=BOTTOM)
        
        Dataframe = Frame(mainframe, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        Dataframe.pack(side=BOTTOM)
        
        dataframeleft = LabelFrame(Dataframe, bd=10, width=900, height=300, padx=20, relief=RIDGE, font=('times new roman',12,'bold'), text="Patient's information : ")
        dataframeleft.pack(side=LEFT)
        
        dataframeright = LabelFrame(Dataframe, bd=10, width=450, height=300, padx=20, relief=RIDGE, font=('times new roman',12,'bold'), text="Prescription : ")
        dataframeright.pack(side=RIGHT)
        
        # dataframe left
        label_tablet = Label(dataframeleft,text="Name of Tablet",font=('times new roman',12,'bold'))
        label_tablet.grid(row=0,column=0,sticky=W)
        
        box_tablet = ttk.Combobox(dataframeleft,textvariable=tabletname, font=('times new roman',12,'bold'),width=33)
        box_tablet['values'] =("Nice","Paracetemol","Ativan","Amlodipine","Crocin","Sumo")
        # self.box_tablet.current(0)
        box_tablet.grid(row=0,column=1)
        
        
        label_ref = Label(dataframeleft,text="Reference No",font=('times new roman',12,'bold'),padx=2)
        label_ref.grid(row=1,column=0,sticky=W)
        txt_ref = Entry(dataframeleft,textvariable=ref,font=('times new roman',12,'bold'),width=35)
        txt_ref.grid(row=1,column=1)
        
        label_dose = Label(dataframeleft,text="Dose",font=('times new roman',12,'bold'),padx=2,pady=2)
        label_dose.grid(row=2,column=0,sticky=W)
        txt_dose = Entry(dataframeleft,textvariable=dose,font=('times new roman',12,'bold'),width=35)
        txt_dose.grid(row=2,column=1)
        
        label_no_oftablets = Label(dataframeleft,text="No of Tablets",font=('times new roman',12,'bold'))
        label_no_oftablets.grid(row=3,column=0,sticky=W)
        txt_notablets = Entry(dataframeleft,textvariable=nooftablets,font=('times new roman',12,'bold'),width=35)
        txt_notablets.grid(row=3,column=1)
        
        label_issuedate = Label(dataframeleft,text="Date of Issue",font=('times new roman',12,'bold'))
        label_issuedate.grid(row=4,column=0,sticky=W)
        txt_issuedate = Entry(dataframeleft,textvariable=issuedate,font=('times new roman',12,'bold'),width=35)
        txt_issuedate.grid(row=4,column=1)
        
        label_dailydose = Label(dataframeleft,text="Daily Dose",font=('times new roman',12,'bold'))
        label_dailydose.grid(row=5,column=0,sticky=W)
        txt_dailydose = Entry(dataframeleft,textvariable=dailydose,font=('times new roman',12,'bold'),width=35)
        txt_dailydose.grid(row=5,column=1)
        
        
        label_bloodpressure = Label(dataframeleft,text="Blood Pressure",font=('times new roman',12,'bold'))
        label_bloodpressure.grid(row=6,column=0,sticky=W)
        txt_bloodpressure = Entry(dataframeleft,textvariable=bloodpressure,font=('times new roman',12,'bold'),width=35)
        txt_bloodpressure.grid(row=6,column=1)      
    
        
        
        label_doctor = Label(dataframeleft,text="Doctor",font=('times new roman',12,'bold'))
        label_doctor.grid(row=0,column=4,sticky=W)
        txt_doctor = Entry(dataframeleft,textvariable=doctor,font=('times new roman',12,'bold'),width=35)
        txt_doctor.grid(row=0,column=5)
        
        label_patientid = Label(dataframeleft,text="Patient Id",font=('times new roman',12,'bold'))
        label_patientid.grid(row=1,column=4,sticky=W)
        txt_patientid = Entry(dataframeleft,textvariable=pid,font=('times new roman',12,'bold'),width=35)
        txt_patientid.grid(row=1,column=5)
        
        label_patientname = Label(dataframeleft,text="Patient Name",font=('times new roman',12,'bold'))
        label_patientname.grid(row=2,column=4,sticky=W)
        txt_patientname = Entry(dataframeleft,textvariable=pname,font=('times new roman',12,'bold'),width=35)
        txt_patientname.grid(row=2,column=5)
        
        label_patientage = Label(dataframeleft,text="PatientAge",font=('times new roman',12,'bold'))
        label_patientage.grid(row=3,column=4,sticky=W)
        txt_patientage = Entry(dataframeleft,textvariable=page,font=('times new roman',12,'bold'),width=35)
        txt_patientage.grid(row=3,column=5) 
        
        label_patientDOB = Label(dataframeleft,text="PatientDOB",font=('times new roman',12,'bold'))
        label_patientDOB.grid(row=4,column=4,sticky=W)
        txt_patientDOB = Entry(dataframeleft,textvariable=pdob,font=('times new roman',12,'bold'),width=35)
        txt_patientDOB.grid(row=4,column=5)       
        
        label_patientno = Label(dataframeleft,text="Phone No",font=('times new roman',12,'bold'))
        label_patientno.grid(row=5,column=4,sticky=W)
        txt_patientno = Entry(dataframeleft,textvariable=pnumber,font=('times new roman',12,'bold'),width=35)
        txt_patientno.grid(row=5,column=5)
        
        label_patientadd = Label(dataframeleft,text="Address",font=('times new roman',12,'bold'))
        label_patientadd.grid(row=6,column=4,sticky=W)
        txt_patientnoadd = Entry(dataframeleft,textvariable=paddress,font=('times new roman',12,'bold'),width=35)
        txt_patientnoadd.grid(row=6,column=5)
        
        # Dataframe right
        
        self.prescription = Text(dataframeright,font=('times new roman',12,'bold'),width=43,height=14,padx=2,pady=6)
        self.prescription.grid(row=0,column=0)
        
        # Button frame
        self.btnPrescription = Button(buttonframe, text="Prescription",font=('times new roman',12,'bold'),width=27,command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        
        self.btnPrescriptionData = Button(buttonframe, text="Prescription Data",font=('times new roman',12,'bold'),width=27,command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0,column=1)
        
        self.btnDelete = Button(buttonframe, text="Delete",font=('times new roman',12,'bold'),width=27,command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        
        self.btnReset = Button(buttonframe, text="Reset",font=('times new roman',12,'bold'),width=27,command=iReset)
        self.btnReset.grid(row=0,column=3)
        
        self.btnExit = Button(buttonframe, text="Exit",font=('times new roman',12,'bold'),width=27,command=iExit)
        self.btnExit.grid(row=0,column=4)
        
        # Detail frame
        
        self.lbllabel = Label(framedetail, font=('arial',9,'bold'), text="Name of tablet\tReference No.\tDosage\t No. of Tabletst\tIssue Date\tDaily Dose\t     BP      \tDoctor\tPatient ID\tPatient Name\tPatient Age\tPatient DOB\tPhone No.\tAddress ", pady=8)
        self.lbllabel.grid(row=0,column=0)
        
        self.detailframe = Text(framedetail,font=('times new roman',12,'bold'),width=160,height=4,padx=2,pady=4)
        self.detailframe.grid(row=1,column=0)
        
if __name__ == '__main__':
    root = Tk()
    application = Hospital(root)
    root.mainloop()
    
        