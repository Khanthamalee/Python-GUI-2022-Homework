#EP.5 เดี๋ยวเขียนต่อกันจะยาวเลยแบ่งมาที่นี่
from tkinter import *
from tkinter import ttk,messagebox
from datetime import datetime
import csv
import webbrowser


def writetocsv(data,filename='data.csv'):
    #ใช้ with open() เพราะมันจะ close file ให้แทน
    with open(filename,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.title('แอพสั่งสินค้า-บ้านนาอุดม')
GUI.iconbitmap('malee.ico')

#Build ขึ้นมาแล้วให้หน้าต่าง GUI อยู่ตรงกลาง
W = 1100
H = 710
MW = GUI.winfo_screenwidth()
MH = GUI.winfo_screenheight()
SX = (MW/2)-(W/2)
SY = (MH/2)-(H/2)
SY = SY-50
GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
#GUI.geometry('1100x710')

#####MenuBar#####
menubar = Menu(GUI)
GUI.config(menu=menubar)

#Filemenu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)

def ExportDatabase():
    print('Export Database to CSV')
filemenu.add_command(label='Export',command=ExportDatabase)
filemenu.add_command(label='Exit',command=lambda:GUI.destroy())

#membermenu
membermenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Member',menu=membermenu)

#helpmenu
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)

#helpmenu-Contact Us
contact_url = 'https://www.facebook.com/macu.rnad'
helpmenu.add_command(label='Contact US',command=lambda:webbrowser.open(contact_url))

#helpmenu-About
def About():
    ABGUI = Toplevel()
    ABGUI.iconbitmap('malee.ico')
    W = 300
    H = 200
    MW = GUI.winfo_screenwidth()
    MH = GUI.winfo_screenheight()
    SX = (MW/2)-(W/2)
    SY = (MH/2)-(H/2)
    SY = SY-50
    ABGUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
    LAboutTP = Label(ABGUI,text='Na-udomShop Program',fg='blue',font=('Angsana New',30,'bold')).pack()
    LAboutPG = Label(ABGUI,text='พัฒนาโดย หนูมาลี บ้านนาอุดม',fg='orange',font=('Angsana New',20)).pack()
    ABGUI.mainloop()
helpmenu.add_command(label='About',command=About)



Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)

icon_tab1 = PhotoImage(file = 'tab3.png' )
icon_tab1_1 = PhotoImage(file = 'tab3.1.png')
icon_tab1_2 = PhotoImage(file = 'tab3.2.png')
icon_tab1_3 = PhotoImage(file = 'tab3.3.png')
icon_tab1_4 = PhotoImage(file = 'tab3.4.png')
icon_tab1_5 = PhotoImage(file = 'tab3.5.png')
icon_tab1_6 = PhotoImage(file = 'tab3.6.png')
icon_tab1_7 = PhotoImage(file = 'tab3.7.png')
icon_tab1_8 = PhotoImage(file = 'tab3.8.png')

Tab.add(T1,text='Na-udomShop',image=icon_tab1,compound='top')

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New',16))

SF1 = Frame(T1)
SF1.place(x=75,y=50)

allgoods = {}

product = {'Banana':{'name': 'กล้วย','price':30,'unit':'หวี'},'Cokle':{'name': 'หอยแครง','price':200,'unit':'กิโลกรัม'},'Fish':{'name': 'ปลานิล','price':100,'unit':'กิโลกรัม'},'Mango':{'name': 'มะม่วง','price':30,'unit':'กิโลกรัม'},'Corn':{'name': 'ข้าวโพ้ดหวาน','price':80,'unit':'กิโลกรัม'},'Rice':{'name': 'ข้าวหอมมะลิ','price':40,'unit':'กิโลกรัม'},'Mushroom':{'name': 'เห็ดนางฟ้า','price':60,'unit':'กิโลกรัม'},'Duck':{'name': 'เนื้อเป็ด','price':100,'unit':'กิโลกรัม'}}

def UpdateTable():
    table.delete(*table.get_children())

    for i,m in enumerate(allgoods.values(),start=1):
        table.insert('','end',value=[i,m[0],m[1],m[2],m[3],m[4]])

Net = []
def AddGoods(name='Banana'):
    
    if name not in allgoods:
        allgoods[name]=[product[name]['name'],product[name]['price'],1,product[name]['unit'],product[name]['price']]
        Net.append(allgoods[name][1])
    else:
        quan = allgoods[name][2]+1
        total = quan * product[name]['price']
        allgoods[name]=[product[name]['name'],product[name]['price'],quan,product[name]['unit'],total]
        Net.append(allgoods[name][1])
    print(allgoods)
    print(sum(Net))
    v_result.set('{:,.2f}'.format(sum(Net)))
    UpdateTable()

def clear_all():
    global allgoods
    for item in table.get_children():
        table.delete(item)
    allgoods = {}
    v_result.set('0.00')
    trstamp = datetime.now().strftime(' %y%m%d%H%M%S ')
    v_transaction.set(trstamp)
    v_name.set('')
    v_phone.set('')
    v_id.set('')
    v_code.set('รหัสสมาชิก : {} '.format(trstamp))
    v_usertype.set('ทั่วไป')
    v_point.set('0.0')

    
    

    #Net.append(allgoods['Cokle'][4])

    #table.insert('','end',value=[1.,'กล้วย',30,30,900])

B1 = ttk.Button(SF1,text='กล้วยหอมทอง',image=icon_tab1_1,compound='top',command=lambda m = 'Banana': AddGoods(m))
B1.grid(row=0,column=0,ipadx=20,ipady=10)

B2 = ttk.Button(SF1,text='หอยแครง',image=icon_tab1_2,compound='top',command=lambda m = 'Cokle': AddGoods(m))
B2.grid(row=0,column=1,ipadx=20,ipady=10)

B3 = ttk.Button(SF1,text='ปลานิล',image=icon_tab1_3,compound='top',command=lambda m = 'Fish': AddGoods(m))
B3.grid(row=1,column=0,ipadx=20,ipady=10)

B4 = ttk.Button(SF1,text='มะม่วง',image=icon_tab1_4,compound='top',command=lambda m = 'Mango': AddGoods(m))
B4.grid(row=1,column=1,ipadx=20,ipady=10)

B5 = ttk.Button(SF1,text='ข้าวโพ้ดหวาน',image=icon_tab1_5,compound='top',command=lambda m = 'Corn': AddGoods(m))
B5.grid(row=2,column=0,ipadx=20,ipady=10)

B6 = ttk.Button(SF1,text='ข้าวหอมมะลิ',image=icon_tab1_6,compound='top',command=lambda m = 'Rice': AddGoods(m))
B6.grid(row=2,column=1,ipadx=20,ipady=10)

B7 = ttk.Button(SF1,text='เห็ดนางฟ้า',image=icon_tab1_7,compound='top',command=lambda m = 'Mushroom': AddGoods(m))
B7.grid(row=3,column=0,ipadx=20,ipady=10)

B8 = ttk.Button(SF1,text='เนื้อเป็ด',image=icon_tab1_8,compound='top',command=lambda m = 'Duck': AddGoods(m))
B8.grid(row=3,column=1,ipadx=20,ipady=10)


SF2 = Frame(T1)
SF2.place(x=400,y=50)

#ใส่ font ให้หัวตาราง Treeview.Heading
Tfont = ttk.Style()
Tfont.configure('Treeview.Heading',font=('Angsana New',18,'bold'))

#ใส่ rowheight=40 เพื่อเพิ่มความกว้างของแถว ถ้าไม่เพิ่มมันจะซ้อนกัน
Tfont.configure('Treeview',font=('Angsana New',16),background='light yellow',foreground='black',rowheight=40,fieldbackground='light yellow')


header = ['ลำดับ','รายการ','ราคา','จำนวน','หน่วย','รวม']
hwidth = [50,200,100,100,100,100]

table = ttk.Treeview(SF2,columns=header,show='headings',height=11)
table.pack()

#ให้ตัวหนังสืออยู่ตรงกลางโดย anchor=CENTER
for hd,hw in zip(header,hwidth):
	table.heading(hd,text=hd,anchor=CENTER)
	table.column(hd,width=hw,anchor=CENTER)

SF3 = Frame(T1)
SF3.place(x=910,y=430)

L1 = Label(SF3,text='ยอดสุทธิ(บาท)',font =('Angsana New',16))
L1.pack(ipadx=20,ipady=5)

v_result = StringVar()
v_result.set('0.00')
result = Label(SF3,textvariable=v_result,font=('Angsana New',16))
result.pack() 

B9 = ttk.Button(SF2,text='CLEAR ALL.',command=clear_all)
B9.pack(ipadx=20,ipady=10,pady = 5)

#Transaction ID หรือเลขที่ออเดอร์

v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S')
v_transaction.set(trstamp)

LTR  = Label(T1,textvariable=v_transaction,font=('Angsana New',18),background='white').place(x=940,y=5)
LTR_title  = Label(T1,text=' เลขที่ออเดอร์ :',font=('Angsana New',18),background='white').place(x=842,y=5)

LTR_member  = Label(T1,text=' เบอร์โทรสมาชิก :  ',font=('Angsana New',18),background='white').place(x=400,y=5)

v_id = StringVar()
E1 = Entry(T1,textvariable=v_id,width=15,selectborderwidth=20,font=('Angsana New',20),justify='center')
E1.place(x=525,y=5)



#สร้างปุ่มเพื่อบันทึกข้อมูลลง CSV

FB = Frame(T1)
FB.place(x=800,y=530)


def AddTransaction():
    global idmember
    stamp = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction,stamp,allgoods)
    for m in allgoods.values():
        m.insert(0,transaction)
        m.insert(1,stamp)
        writetocsv(m,'Reciept.csv')
    idmember = str(v_id.get())
    memberpoint = sum(Net)/50
    print(idmember,memberpoint)
    clear_all() #เคลียข้อมูลหลังจากกดบันทึก

    messagebox.showinfo('Point','สมาชิก {} ได้รับเต้มเพิ่ม {} '.format(idmember,memberpoint))
    UpdateTable_Member()
    print('allmember',allmember)
     
    Sumpoint = float(allmember[idmember][3])+float(memberpoint)
    print('allmember[idmember][3]',allmember[idmember][3])
    print('Sumpoint',Sumpoint)
    print('allmember',allmember)
    allmember[idmember][3]=Sumpoint
    print('allmember',allmember)
    UpdateCSV(list(allmember.values()),'Member.csv')
    UpdateTable_Member()
   

Bsave = ttk.Button(FB,text='บันทึกคำสั่งซื้อ',command=AddTransaction)
Bsave.pack(ipadx=20,ipady=10)

#History New windows
def Historywindow(event=None):
    HIS = Toplevel() #คล้าย GUI = Tk() เพราะ Tk() ใช้ได้แค่ครั้งเดียวต่อหน้าต่างหลัก
    HIS.geometry('950x600')

    L_title = Label(HIS,text='ประวัติการสั่งซื้อ',font=('Angsana New',18,'bold')).pack()

    header = ['เลขที่ออเดอร์','วันที่และเวลา','รายการ','ราคา','จำนวน','หน่วย','รวม']
    hwidth = [100,150,200,100,100,100,100]

    table_history = ttk.Treeview(HIS,columns=header,show='headings',height=11)
    table_history .pack()

    #ให้ตัวหนังสืออยู่ตรงกลางโดย anchor=CENTER
    for hd,hw in zip(header,hwidth):
        table_history.heading(hd,text=hd,anchor=CENTER)
        table_history.column(hd,width=hw,anchor=CENTER)
    #Update from CSV
    with open('Reciept.csv',newline='',encoding = 'utf-8') as file:
        fr = csv.reader(file) #file reader
        for row in fr:
            table_history.insert('',0,value=row)
    HIS.mainloop()

GUI.bind('<F1>',Historywindow)

###### สร้าง tab สมาชิก #################

T2 = Frame(Tab)

icon_tab2  = PhotoImage(file = 'tab2.3.png')

Tab.add(T2,text='Members',image=icon_tab2,compound='top')

SFapply = Frame(T2)
SFapply.place(x=75,y=15)

LApply = Label(SFapply,text=' แบบฟอร์มสมัครสมาชิก ',font=('Angsana New',18,'bold'),background='light pink',foreground='black')
LApply.pack(pady=10,ipadx=20,ipady=10)


v_code = StringVar()
v_code.set('รหัสสมาชิก : {} '.format(trstamp))
LCode2=Label(SFapply,textvariable=v_code,font=('Angsana New',20)).pack()

LName  = Label(SFapply,text=' ชื่อ-นามสกุล :  ',font=('Angsana New',18))
LName.pack()

v_name = StringVar()
EName = ttk.Entry(SFapply,textvariable=v_name ,width=25,font=('Angsana New',18),justify='center')
EName.pack()

LPhone  = Label(SFapply,text=' เบอร์โทรศัพท์ :  ',font=('Angsana New',18))
LPhone.pack()

v_phone = StringVar()
EPhone = ttk.Entry(SFapply,textvariable=v_phone,width=25,font=('Angsana New',18),justify='center')
EPhone.pack()

def EMember(GUI,text,font=('Angsana New',18)):
    v_strvar = StringVar()
    Title_member = Label(GUI,text=text,font=font).pack()
    Entry_member = ttk.Entry(GUI,textvariable=v_strvar,width=25,font=font,justify='center')
    return(v_strvar,Title_member,Entry_member)

v_point,Title_point,Entry_point = EMember(SFapply,'แต้ม :')
v_point.set('0.0')
Entry_point.pack()

v_usertype,Title_usertype,Entry_usertype = EMember(SFapply,'ประเภทสมาชิก :')
v_usertype.set('ทั่วไป')
Entry_usertype.pack()



def MemberSave():
    membername = v_name.get()
    memberphone = v_phone.get()
    memberID = trstamp
    memberpoint = v_point.get()
    memberusertype = v_usertype.get()
    membersum = [memberID,membername,memberphone,memberpoint,memberusertype]
    writetocsv(membersum,'Member.csv')
    table_member.insert('',0,value=[memberID,membername,memberphone,memberpoint,memberusertype])
    print(membersum)
    UpdateTable_Member()
    clear_all()

Bsubmit = ttk.Button(T2,text='สมัคร',command=MemberSave)
Bsubmit.place(x=100,y=460)

def EditMember():
    code = v_phone.get()
    print('code',code)
    #allmember[code][0]=v_code.get()[14:]
    allmember[code][1]=v_name.get()
    allmember[code][2]=v_phone.get()
    allmember[code][3]=v_point.get()
    allmember[code][4]=v_usertype.get()

    UpdateCSV(list(allmember.values()),'member.csv')
    UpdateTable_Member()
    print('EditMember :',allmember[code][0],allmember[code][1],allmember[code][2],allmember[code][3],allmember[code][4])

    BEdit.state(['disabled'])
    Bsubmit.state(['!disabled'])
    clear_all()

BEdit = ttk.Button(T2,text='แก้ไข',command=EditMember)
BEdit.place(x=190,y=460)


'''def PointAdd():
    IDpointAdd = v_id.get()
    print('idmember',idmember)
PointAdd()

BNew = ttk.Button(SFapply,text='ใหม่',command=PointAdd)
BEdit.pack()'''


SFtable = Frame(T2)
SFtable.place(x=330,y=25)

LMemberlist  = Label(SFtable,text='    รายชื่อสมาชิก   ',font=('Angsana New',20,'bold'),background='light yellow')
LMemberlist.pack()

header = ['รหัสสมาชิก','ชื่อ-นามสกุล','เบอร์โทรศัพท์','แต้ม','ประเภทสมาชิก']
hwidth = [100,200,150,100,150]

table_member = ttk.Treeview(SFtable,columns=header,show='headings',height=10)
table_member.pack(pady=5)

#ให้ตัวหนังสืออยู่ตรงกลางโดย anchor=CENTER
for hd,hw in zip(header,hwidth):
    table_member.heading(hd,text=hd,anchor=CENTER)
    table_member.column(hd,width=hw,anchor=CENTER)

def UpdateCSV(data,filename='data.csv'):
    with open(filename,'w',newline='',encoding = 'utf-8') as file:
        fw = csv.writer(file)
        fw.writerows(data)
def DeleteMember(event=None):
    select = table_member.selection()
    if len(select) != 0:
        data = table_member.item(select)['values']
        print('data',data)
        A = str('0{}'.format(data[2]))
        print('data[2]',A)
        del allmember[A]
        UpdateCSV(list(allmember.values()),'Member.csv')
        UpdateTable_Member()
    else:
        messagebox.showwarning('คุณไม่ได้เลือกรายการ','กรุณาเลือกรายการที่ต้องการลบ')
table_member.bind('<Delete>',DeleteMember)




'''def writetocsvrefresh():
    with open('Member.csv',newline='',encoding = 'utf-8') as file:
        fr = csv.reader(file) #file reader
        for row in fr:
            table_member.insert('',0,value=row)

BRefresh = ttk.Button(SFtable, text="Show the members",command =writetocsvrefresh, width=6) 
BRefresh.pack(pady=15,ipadx=40,ipady=10)'''

def UpdateMemberInfo(event=None):
    select = table_member.selection()
    if len(select) != 0:
        code = '0{}'.format(str(table_member.item(select)['values'][2]))
        print(code)
        print(allmember[code])
        memberinfo = allmember[code]
        v_code.set('รหัสสมาชิก : {} '.format(memberinfo[0]))
        v_name.set(memberinfo[1])
        v_phone.set(memberinfo[2])
        v_point.set(memberinfo[3])
        v_usertype.set(memberinfo[4])
        BEdit.state(['!disabled'])
        Bsubmit.state(['disabled'])
    else:
        messagebox.showwarning('คุณไม่ได้เลือกรายการ','กรุณาเลือกรายการที่ต้องการแก้ไข')
table_member.bind('<Double-1>',UpdateMemberInfo)


Allpoint = {}
last_member = ''
allmember = {}
def UpdateTable_Member():
    global last_member
    with open('Member.csv',newline='',encoding = 'utf-8') as file:
        fr = csv.reader(file) #file reader
        table_member.delete(*table_member.get_children())
        for row in fr:
            table_member.insert('',0,value=row)
            code = row[2] #ดึงรหัสสมาชิก
            allmember[code]=row
            Allpoint[row[2]] = row
    print('Allpoint',Allpoint)
    print('Last row: ',row)
    last_member = row[0]
    print('---',len(allmember),'---',allmember)
    #Oldpoint.set(Allpoint['0834532277'][3])

####Pop Up Menu### 
member_rcmenu = Menu(GUI,tearoff=0)
member_rcmenu.add_command(label='Dalete',command = DeleteMember)
member_rcmenu.add_command(label='Update',command = UpdateMemberInfo)

'''def popup():
    member_rcmenu.post(event.x_root,event.y_root)'''
table_member.bind('<Button-3>',lambda event : member_rcmenu.post(event.x_root,event.y_root))  


def SearchName():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print('name',name)
    url = 'https://www.google.com/search?q={}'.format(name)
    webbrowser.open(str(url))
member_rcmenu.add_command(label='Search Name',command = SearchName)

BEdit.state(['disabled'])
UpdateTable_Member()
GUI.mainloop()