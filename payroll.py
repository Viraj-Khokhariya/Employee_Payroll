from tkinter import *
from tkinter import messagebox,ttk
import pymysql
import time
import os
import tempfile

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title(
            "Employee Payroll Management System | Developed By TBJ")
        self.root.geometry("1300x750+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="Employee Management Software | Developed By TBJ", font=(
            "times new roman", 30, "bold"), bg="#262626", fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        btn_emp = Button(self.root, text="All Employee", command=self.emp_frame, font=(
            "times new roman", 13, "bold"), fg="white", bg="grey").place(x=1100, y=10, width=120)
        # ==================Frame1==================#
        # ================variable====================
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_doj = StringVar()
        self.var_dob = StringVar()
        self.var_exp = StringVar()
        self.var_proof = StringVar()
        self.var_contact = StringVar()

        Frame1 = Frame(self.root, bd=3, relief=RIDGE)
        Frame1.place(x=10, y=70, width=675, height=440)
        title1 = Label(Frame1, text="Employee Details", font=("times new roman", 20),
                       bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        # =======================LEFT COLUMN=========================#
        lbl_code = Label(Frame1, text="Employee Code", font=(
            "times new roman", 15), fg="black").place(x=10, y=70)
        self.txt_code = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_emp_code,
                         bg="lightyellow", fg="black")
        self.txt_code.place(x=150, y=70, width=180)
        btn_code = Button(Frame1, text="Search", command=self.search, font=(
            "times new roman", 13, "bold"), fg="black", bg="lightgrey").place(x=340, y=65, width=110)

        lbl_designation = Label(Frame1, text="Designation", font=(
            "times new roman", 15), fg="black").place(x=10, y=110)
        txt_designation = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_designation,
                                bg="lightyellow", fg="black").place(x=120, y=110, width=210)
        lbl_name = Label(Frame1, text="Name", font=(
            "times new roman", 15), fg="black").place(x=10, y=150)
        txt_name = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_name,
                         bg="lightyellow", fg="black").place(x=120, y=150, width=210)
        lbl_age = Label(Frame1, text="Age", font=(
            "times new roman", 15), fg="black").place(x=10, y=190)
        txt_age = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_age,
                        bg="lightyellow", fg="black").place(x=120, y=190, width=210)
        lbl_gender = Label(Frame1, text="Gender", font=(
            "times new roman", 15), fg="black").place(x=10, y=230)
        txt_gender = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_gender,
                           bg="lightyellow", fg="black").place(x=120, y=230, width=210)
        lbl_email = Label(Frame1, text="Email", font=(
            "times new roman", 15), fg="black").place(x=10, y=270)
        txt_email = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_email,
                          bg="lightyellow", fg="black").place(x=120, y=270, width=210)
        lbl_address = Label(Frame1, text="Address", font=(
            "times new roman", 15), fg="black").place(x=10, y=310)
        self.txt_address = Text(Frame1, font=(
            "times new roman", 14), bg="lightyellow", fg="black")
        self.txt_address.place(x=120, y=310, width=540, height=110)

        # =======================RIGHT COLUMN=========================#
        lbl_doj = Label(Frame1, text="D.O.J.", font=(
            "times new roman", 15), fg="black").place(x=340, y=110)
        txt_doj = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_doj,
                        bg="lightyellow", fg="black").place(x=450, y=110, width=210)
        lbl_dob = Label(Frame1, text="D.O.B.", font=(
            "times new roman", 15), fg="black").place(x=340, y=150)
        txt_dob = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_dob,
                        bg="lightyellow", fg="black").place(x=450, y=150, width=210)
        lbl_exp = Label(Frame1, text="Experience", font=(
            "times new roman", 15), fg="black").place(x=340, y=190)
        txt_exp = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_exp,
                        bg="lightyellow", fg="black").place(x=450, y=190, width=210)
        lbl_proof = Label(Frame1, text="ID Proof", font=(
            "times new roman", 15), fg="black").place(x=340, y=230)
        txt_proof = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_proof,
                          bg="lightyellow", fg="black").place(x=450, y=230, width=210)
        lbl_contact = Label(Frame1, text="Contact No.", font=(
            "times new roman", 15), fg="black").place(x=340, y=270)
        txt_contact = Entry(Frame1, font=("times new roman", 14), textvariable=self.var_contact,
                            bg="lightyellow", fg="black").place(x=450, y=270, width=210)

        # ==================Frame2==================#
        # ================variable====================
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_tday = StringVar()
        self.var_abs = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_tds = StringVar()
        self.var_oth = StringVar()
        self.var_ded = StringVar()
        self.var_net_salary = StringVar()

        Frame2 = Frame(self.root, bd=3, relief=RIDGE)
        Frame2.place(x=690, y=70, width=575, height=300)
        title2 = Label(Frame2, text="Employee Salary Details", font=("times new roman", 20),
                       bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        # =====ROW1
        lbl_month = Label(Frame2, text="Month", font=(
            "times new roman", 15), fg="black").place(x=10, y=70)
        txt_month = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_month,
                          bg="lightyellow", fg="black").place(x=80, y=70, width=100)
        lbl_year = Label(Frame2, text="Year", font=(
            "times new roman", 15), fg="black").place(x=190, y=70)
        txt_year = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_year,
                         bg="lightyellow", fg="black").place(x=270, y=70, width=100)
        lbl_salary = Label(Frame2, text="Salary", font=(
            "times new roman", 15), fg="black").place(x=380, y=70)
        txt_salary = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_salary,
                           bg="lightyellow", fg="black").place(x=460, y=70, width=100)

        # =====ROW2
        lbl_day = Label(Frame2, text="T. Days", font=(
            "times new roman", 15), fg="black").place(x=10, y=120)
        txt_day = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_tday,
                        bg="lightyellow", fg="black").place(x=80, y=120, width=100)
        lbl_abs = Label(Frame2, text="Absents", font=(
            "times new roman", 15), fg="black").place(x=190, y=120)
        txt_abs = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_abs,
                        bg="lightyellow", fg="black").place(x=270, y=120, width=100)
        lbl_medical = Label(Frame2, text="Medical", font=(
            "times new roman", 15), fg="black").place(x=380, y=120)
        txt_medical = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_medical,
                            bg="lightyellow", fg="black").place(x=460, y=120, width=100)

        # =====ROW3
        lbl_pf = Label(Frame2, text="PF", font=(
            "times new roman", 15), fg="black").place(x=10, y=150)
        txt_pf = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_pf,
                       bg="lightyellow", fg="black").place(x=80, y=150, width=100)
        lbl_tds = Label(Frame2, text="TDS", font=(
            "times new roman", 15), fg="black").place(x=190, y=150)
        txt_tds = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_tds,
                        bg="lightyellow", fg="black").place(x=270, y=150, width=100)
        lbl_oth = Label(Frame2, text="Other", font=(
            "times new roman", 15), fg="black").place(x=380, y=150)
        txt_oth = Entry(Frame2, font=("times new roman", 14), textvariable=self.var_oth,
                        bg="lightyellow", fg="black").place(x=460, y=150, width=100)

        # =====ROW4
        lbl_ded = Label(Frame2, text="Total Deduction", font=(
            "times new roman", 15), fg="black").place(x=10, y=200)
        txt_ded = Entry(Frame2, font=("times new roman", 14), state='readonly', textvariable=self.var_ded,
                        bg="lightyellow", fg="black").place(x=160, y=200, width=140)
        lbl_nsalary = Label(Frame2, text="Net Salary", font=(
            "times new roman", 15), fg="black").place(x=320, y=200)
        self.txt_nsalary = Entry(Frame2, font=("times new roman", 14), state='readonly',textvariable=self.var_net_salary,
                            bg="lightyellow", fg="black")
        self.txt_nsalary.place(x=420, y=200, width=140)

        # =====ROW5
        btn_cal = Button(Frame2, text="Calculate", command=self.calculate, font=(
            "times new roman", 14, "bold"), fg="black", bg="orange").place(x=250, y=240, width=100)
        self.btn_save = Button(Frame2, text="Save", command = self.add, font=(
            "times new roman", 14, "bold"), fg="white", bg="green")
        self.btn_save.place(x=355, y=240, width=100)
        btn_clear = Button(Frame2, text="Clear", command=self.clear, font=(
            "times new roman", 14, "bold"), fg="black", bg="grey").place(x=460, y=240, width=100)

        self.btn_update = Button(Frame2, text="Update", command=self.update, state=DISABLED, font=(
            "times new roman", 14, "bold"), fg="white", bg="blue")
        self.btn_update.place(x=10, y=240, width=100)
        self.btn_delete = Button(Frame2, text="Delete", command=self.delete, state=DISABLED, font=(
            "times new roman", 14, "bold"), fg="white", bg="red")
        self.btn_delete.place(x=115, y=240, width=100)

        # ==================Frame3==================#
        Frame3 = Frame(self.root, bd=3, relief=RIDGE)
        Frame3.place(x=690, y=380, width=340, height=365)
        title3 = Label(Frame3, text="Salary Reciept", font=("times new roman", 20),
                       bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        sal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_Frame.place(x=0, y=35, relwidth=1, height=280)
        self.sample = f'''\tTBJ's Company\n\tAddress: Varachha, Surat
---------------------------------------------------
 Employee ID\t\t:  
 Salary Of\t\t:  Mon-YYYY
 Generated On\t\t:  DD-MM-YYYY
---------------------------------------------------
 Total Days\t\t:  DD
 Total Present\t\t:  DD
 Total Absent\t\t:  DD
 Medical\t\t:  ₹ ----
 PF\t\t:  ₹ ----
 TDS\t\t:  ₹ ----
 Other\t\t:  ₹ ----
 Total Deduction\t\t:  ₹ ----
 Gross Payment\t\t:  ₹ ----
 Net Salary\t\t:  ₹ ----
---------------------------------------------------
This is computer generated slip, not 
required any signature
'''

        scroll_y = Scrollbar(sal_Frame, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_receipt = Text(sal_Frame, font=(
            "times new roman", 14), bg="lightyellow", yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)

        self.btn_print = Button(Frame3, text="Print", state=DISABLED, command=self.print, font=(
            "times new roman", 13, "bold"), fg="black", bg="powder blue")
        self.btn_print.place(x=210, y=320, width=110)

        # ==================Frame4==================#
        Frame4 = Frame(self.root, bd=3, relief=RIDGE)
        Frame4.place(x=10, y=520, width=675, height=225)
        title3 = Label(Frame4, text="Employee Records", font=("times new roman", 20),
                       bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

    # ==============================Function========================
    def search(self):
        try:
            con = pymysql.connect(host='localhost',user='root',password='',db='empc')
            cur = con.cursor()

            cur.execute("select * from emp_detail where e_id=%s",(self.var_emp_code.get()))
            row = cur.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
            else:
                # print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_doj.set(row[6])
                self.var_dob.set(row[7])
                self.var_exp.set(row[8])
                self.var_proof.set(row[9])
                self.var_contact.set(row[10])
                self.var_month.set(row[11])
                self.var_year.set(row[12])
                self.var_salary.set(row[13])
                self.var_tday.set(row[14])
                self.var_abs.set(row[15])
                self.var_medical.set(row[16])
                self.var_pf.set(row[17])
                self.var_tds.set(row[18])
                self.var_oth.set(row[19])
                self.var_ded.set(row[20])
                self.var_net_salary.set(row[21])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END, row[22])
                file_=open('salary_reciept/'+str(row[23]),'r',encoding="utf-8")
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_receipt.insert(END,i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')
                self.btn_print.config(state=NORMAL)
                

        except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')
    

    def calculate(self):  
        sal = float(self.var_salary.get())
        med = float(self.var_medical.get())
        pf = float(self.var_pf.get())
        tds = float(self.var_tds.get())
        oth = float(self.var_oth.get())
        
        self.nt_sal = (sal - (med + pf + tds + oth))
        t_ded = (med + pf + tds + oth)
        self.net_salary = "₹", str('%.2f' %(self.nt_sal))
        
        self.var_ded.set(t_ded)
        self.var_net_salary.set(self.net_salary)
        self.txt_nsalary.config(state='readonly')
        new_sample = f'''\tTBJ's Company\n\tAddress: Varachha, Surat
---------------------------------------------------
 Employee ID\t\t:  {self.var_emp_code.get()}
 Salary Of\t\t:  {self.var_month.get()}-{self.var_year.get()}
 Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
---------------------------------------------------
 Total Days\t\t:  {self.var_tday.get()}
 Total Present\t\t:  {str(int(self.var_tday.get())-int(self.var_abs.get()))}
 Total Absent\t\t:  {self.var_abs.get()}
 Medical\t\t:  ₹ {self.var_medical.get()}
 PF\t\t:  ₹ {self.var_pf.get()}
 TDS\t\t:  ₹ {self.var_tds.get()}
 Other\t\t:  ₹ {self.var_oth.get()}
 Total Deduction\t\t:  ₹ {self.var_ded.get()}
 Gross Payment\t\t:  ₹ {self.var_salary.get()}
 Net Salary\t\t:  ₹ {self.nt_sal}
---------------------------------------------------
This is computer generated slip, not 
required any signature
'''
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,new_sample)

    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error",'Employee ID Must be Required')
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='empc')
                cur = con.cursor()

                cur.execute("select * from emp_detail where e_id=%s",(self.var_emp_code.get()))
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Are you sure you want to delete?")
                    if op==True:
                        cur.execute('delete from emp_detail where e_id=%s',(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Error","Employee Record Deleted Successfully",parent=self.root)
                        os.remove('salary_reciept/'+self.var_emp_code.get()+".txt")
                        self.clear()
                        
                        

            except Exception as ex:
                    messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def update(self):
        if self.var_emp_code.get()=='' and self.var_name.get()=='' and self.var_email.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error","All Fields are required")
        else:  
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='empc')
                cur = con.cursor()

                cur.execute("select * from emp_detail where e_id=%s",(self.var_emp_code.get()))
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error","This Employee is invalid,try with valid ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_detail` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`id_proof`=%s,`contact`=%s,`month`=%s,`year`=%s,`salary`=%s,`total_day`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`tds`=%s,`other`=%s,`total_deduction`=%s,`net_salary`=%s,`address`=%s,`salary_slip`=%s WHERE `e_id`=%s",
                    (                        
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_exp.get(),
                        self.var_proof.get(),
                        self.var_contact.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_tday.get(),
                        self.var_abs.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_tds.get(),
                        self.var_oth.get(),
                        self.var_ded.get(),
                        self.nt_sal,
                        self.txt_address.get('1.0', END),
                        self.var_emp_code.get()+".txt",
                        self.var_emp_code.get(),
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salary_reciept/'+str(self.var_emp_code.get())+".txt",'w',encoding="utf-8")
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("success","Record Updated Successfully")

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def add(self):
        if self.var_emp_code.get()=='' and self.var_name.get()=='' and self.var_email.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error","All Fields are required")
        else:  
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='empc')
                cur = con.cursor()

                cur.execute("select * from emp_detail where e_id=%s",(self.var_emp_code.get()))
                row = cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror("Error","This Employee Already Exist",parent=self.root)
                else:
                    cur.execute("insert into emp_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_exp.get(),
                        self.var_proof.get(),
                        self.var_contact.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_tday.get(),
                        self.var_abs.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_tds.get(),
                        self.var_oth.get(),
                        self.var_ded.get(),
                        self.nt_sal,
                        self.txt_address.get('1.0', END),
                        self.var_emp_code.get()+".txt"
                    )
                    )
                    con.commit()
                    con.close()
                    
                    file_=open('salary_reciept/'+str(self.var_emp_code.get())+".txt",'w',encoding="utf-8")
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("success","Record Added Successfully")
                    self.btn_print.config(state=NORMAL)

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')
    
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        self.btn_print.config(state=DISABLED)

        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_exp.set('')
        self.var_proof.set('')
        self.var_contact.set('')
        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_tday.set('')
        self.var_abs.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_tds.set('')
        self.var_oth.set('')
        self.var_ded.set('')
        self.var_net_salary.set('')
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,'')
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,self.sample)


    def show(self):
        try:
            con = pymysql.connect(host='localhost',user='root',password='',db='empc')
            cur = con.cursor()
            cur.execute("select * from emp_detail")
            rows = cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')

    #===================Emp_Frame==========================#

    def emp_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title(
            "Employee Payroll Management System | Developed By TBJ")
        self.root2.geometry("1300x600+120+100")
        self.root2.config(bg="white")
        title = Label(self.root2, text="All Employee Details", font=(
            "times new roman", 30, "bold"), bg="#262626", fg="white", anchor="w", padx=10).pack(side=TOP,fill=X)  
        self.root2.focus_force()

        scrolly = Scrollbar(self.root2, orient=VERTICAL)
        scrollx = Scrollbar(self.root2, orient=HORIZONTAL)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)

        self.employee_tree = ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'doj', 'dob', 'experience', 'id_proof', 'contact', 'month', 'year', 'salary', 'total_day', 'absent', 'medical', 'pf', 'tds', 'other', 'total_deduction', 'net_salary', 'address', 'salary_slip'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('doj',text='D.O.J.')
        self.employee_tree.heading('dob',text='D.O.B.')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('id_proof',text='Id Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('salary',text='Salary')
        self.employee_tree.heading('total_day',text='Total Day')
        self.employee_tree.heading('absent',text='Absent')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='P.F.')
        self.employee_tree.heading('tds',text='T.D.S.')
        self.employee_tree.heading('other',text='Other')
        self.employee_tree.heading('total_deduction',text='Total Deduction')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('salary_slip',text='Salary Slip')
        self.employee_tree['show']='headings'
        
        self.employee_tree.column('e_id',width=20)
        self.employee_tree.column('designation',width=50)
        self.employee_tree.column('name',width=60)
        self.employee_tree.column('age',width=20)
        self.employee_tree.column('gender',width=40)
        self.employee_tree.column('email',width=50)
        self.employee_tree.column('doj',width=30)
        self.employee_tree.column('dob',width=30)
        self.employee_tree.column('experience',width=30)
        self.employee_tree.column('id_proof',width=50)
        self.employee_tree.column('contact',width=40)
        self.employee_tree.column('month',width=20)
        self.employee_tree.column('year',width=20)
        self.employee_tree.column('salary',width=50)
        self.employee_tree.column('total_day',width=10)
        self.employee_tree.column('absent',width=10)
        self.employee_tree.column('medical',width=40)
        self.employee_tree.column('pf',width=40)
        self.employee_tree.column('tds',width=40)
        self.employee_tree.column('other',width=40)
        self.employee_tree.column('total_deduction',width=40)
        self.employee_tree.column('net_salary',width=40)
        self.employee_tree.column('address',width=40)
        self.employee_tree.column('salary_slip',width=20)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        
        self.root2.mainloop()
        
    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,"w",).write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print') 


    # def check_connection(self):
    #     try:
    #         con = pymysql.connect(host='localhost',user='root',password='',db='empc')
    #         cur = con.cursor()

    #         cur.execute("select * from emp_detail")
    #         rows = cur.fetchall()
    #         print(rows)

    #     except Exception as ex:
    #         messagebox.showerror("Error",f'Error due to:{str(ex)}')

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
