#GUI-GUI-wikipedia.py

from tkinter import *
from tkinter import ttk,messagebox #ค่อยๆ import ตอนจะใช้ได้
#ควรอ่านตามลำดับเลข เพราะลุงสอนตามนั้น จะได้เข้าใจง่าย
import wikipedia # 35.7 เพื่อดึงข้อมูล wiki
#########CSV#########


# 32. การบ้านเพิ่มเวลาที่บันทึกลง CSV
from datetime import datetime

# 29. การสร้างฟังก์ชันเพื่อนำข้อมูลที่ต้องการบันทึกลง csv
import csv
def writetocsv(data):
    #ใช้ with open() เพราะมันจะ close file ให้แทน
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
 # 29.1 'a' ย่อมาจาก append
 # 29.2 'w' จะเขียนใหม่ทุกครั้งทับ file เดิม ใช้บางกรณี
 # 29.3 newline='' ทำให้บรรทัดมีการเคาะเว้นบรรทัด
 # 29.4 encoding='utf-8' ให้สามารถบันทึกภาษาไทยได้
 # 29.5 file คือ file ที่เราเปิดเข้ามา
 # 29.6 csv.writer() ดึง writer() มาจาก csv
 # 29.7 fw.writerow() คือ การบันทึกอะไรลงไปใน() csv

###########GUI#########
# 1. สร้างกล่อง GUI
GUI = Tk()

# 3. GUI มีชื่อว่า โปรแกรมคำนวนราคากุ้งและหอย
GUI.title('โปรแกรมคำนวนราคากุ้ง,หอย ,ค้นหาจาก Wikipedia และร้านค้า')

# 4. ขนาดของ GUI กว้าง 1000 ยาว 700 pixel
GUI.geometry('1000x700')

# 33. ต้องการสร้างแท็บให้กับ GUI
#################### สร้าง TAB #############
Tab = ttk.Notebook(GUI)
# 33.1 fill=BOTH,expand=1 คือการขยาย Tab
Tab.pack(fill=BOTH,expand=True)
# 33.2 T1 คือ TAB-1, T2 คือ TAB-2
T1 = Frame(Tab)
T2 = Frame(Tab)

T3 = Frame(Tab)

# 33.5 สร้าง logo เอา png ใส่ใน icon_tab1,icon_tab2
icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
icon_tab1_1 = PhotoImage(file='tab1.1.png')
icon_tab2_1 = PhotoImage(file='tab2.1.png')
icon_tab2_2 = PhotoImage(file='tab2.2.png')

icon_tab3 = PhotoImage(file='tab3.png')

# 33.6 เอา icon_tab1,icon_tab2 ใส่ลงใน Tab
# 33.7 compound='left' เอาภาพกุ้งใส่ทางด้านซ้ายของ tab
Tab.add(T1,text = ' กุ้ง,หอย ',image=icon_tab1,compound='left')
# 33.4 เอา T2 เข้าไปใน Tab
Tab.add(T2,text = 'Wiki ',image=icon_tab2,compound='left')

Tab.add(T3,text = ' Shop  ',image=icon_tab3,compound='left')

# 34. TAB-1 ของ กุ้ง,หอย
#################### TAB-1 กุ้ง,หอย #############

# 9. สร้างหัวข้อ ของกุ้ง
# 10. text คือ ข้อความ font คือ ประเภทตัวอักษร
# 34.1 T1 ย้าย กุ้ง,หอย ไปใส่ใน T1 เอา GUI ออก
L1 = Label(T1,text='จำนวนกุ้งในหน่วยกิโลกรัม (299 บาท ต่อกิโลกรัม)',font =('Angsana New',18))
L1.pack(pady=10)

# 14. ใช้ StringVar และ #สร้างตัวแปรพิเศษเอาไว้เก็บค่ากิโลกรัมของกุ้ง
v_kilo = StringVar()

# 24. สร้างเพิ่มทำการบ้านลุง ตัวแปรของหอย
h_kilo = StringVar()

# 5. สร้างช่องด้วย E1 = Entry(GUI)
# 8. ทำให้กรอบสวยงามด้วย ttk.Entry(GUI)
# 9. ทำให้ช่องใหญ่และใส่ font ตามต้องการ ttk.Entry(GUI,font=('ชื่อ font',ขนาด font))
# 10. ทำให้จำนวนช่องกรอกกว้าง 10 ตัวอักษรด้วย width = 10
# 11. ทำให้ข้อความเขียนจากทางด้านขวา justify='right'
# 15. อย่าลืมเอา v_kilo = StringVar() โดย textvariable = v_kilo
# ในกรณีที่เรากรองตัวเลขลงมาจะเป็น textvariable ชื่อ v_kilo เป็นชนิด StringVar() 
# 34.1 T1 ย้าย กุ้ง,หอย ไปใส่ใน T1 เอา GUI ออก
E1 = ttk.Entry(T1,textvariable = v_kilo,width=10,font=('impact',20),justify='right')
E1.pack(pady = 5)

# 23. สร้างหัวข้อ ของหอย
# 34.1 T1 ย้าย กุ้ง,หอย ไปใส่ใน T1 เอา GUI ออก
L2 = Label(T1,text='จำนวนหอยในหน่วยกิโลกรัม(100 บาท ต่อกิโลกรัม)',font =('Angsana New',18))
L2.pack(pady=10)

# 25. สร้างช่องไว้กรอกจำนวนกิโลกรัมของหอย 
# 34.1 T1 ย้าย กุ้ง,หอย ไปใส่ใน T1 เอา GUI ออก
E2 = ttk.Entry(T1,textvariable = h_kilo,width=10,font=('impact',20),justify='right')
E2.pack(pady = 5)

# 12. สร้างฟังก์ชันโชว์ว่ากำลังคำนวนใน idle ยังไง และทำหน้าป๊อปอัพ
def Calc(event=None): # 23. event=None ที่ฟังชันนี้
    print('กำลังคำนวณ...กรุณารอสักครู่')
    # 16. .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar จะยังรันได้ไม่ตรงตามต้องการ
    #ถ้าใช้ kilov = v_kilo.get() ต้องใช้ float ครอบ
    kilov = float(v_kilo.get())

    # 26. .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar จะยังรันได้ไม่ตรงตามต้องการ
    #ถ้าใช้ kiloh = h_kilo.get() ต้องใช้ float ครอบ
    kiloh = float(h_kilo.get())
    print(kilov * 299)
    print(kiloh * 100)
    
    # 19. คำนวนตัวเลขราคากุ้งที่ลูกค้าต้องจ่ายแล้วเอาไปใส่ใน messagebox.showinfo
    cal_resultv = kilov*299

    # 27. คำนวนตัวเลขราคาหอยที่ลูกค้าต้องจ่ายแล้วเอาไปใส่ใน messagebox.showinfo
    cal_resulth = kiloh*100

    # 28. คำนวนตัวเลขราคาหอยที่ลูกค้าต้องจ่ายแล้วเอาไปใส่ใน messagebox.showinfo
    cal_sum = cal_resultv + cal_resulth
    print(cal_sum)
    # 30. นำตัวแปรกุ้งและหอยมาใส่ใน data
    # 32. การบ้านเพิ่มเวลาที่บันทึกลง CSV
    yy = datetime.now()
    Tyear = yy.year + 543
    Tdate = yy.strftime('%d/%m')
    Ttime = yy.strftime('%H:%M:%S')
    print('year',Tyear)
    print('day',Tdate)
    print('time',Ttime)
    data = ['วันที่ {}/{} เวลา {}\nกุ้ง จำนวน {} กิโลกรัม ราคา {:,.2f} บาท\nหอย จำนวน {} กิโลกรัม ราคา {:,.2f} บาท\nรวมเป็นเงิน {:,.2f} บาn\n'.format(Tdate,Tyear,Ttime,kilov,cal_resultv,kiloh,cal_resulth,cal_sum)]
    # 31. เรียกฟังชันก์เข้ามาใช้งาน
    writetocsv(data)
    

    # 17. ทำให้ข้อความเป็นป๊อปอัพบอกว่าต้องจ่ายตังเท่าไหร่
    # 18. title = 'รวมราคาทั้งหมด',text = 'ราคาหอยและกุ้งรวมเป็นเงิน {:,.2f} บาท แบ่งเป็น กุ้ง {:,.2f} บาท และ หอย {:,.2f} บาท'.format(cal_sum,cal_resultv,cal_resulth)'
    # 20. การเอา float ไปใส่ใน str ใช้ '{)'.format(ชื่อ float)
    # 21. :.2f คือ จำนวนทศนิยม 2 ตำแหน่ง >> :,.2f คือ จำนวนทศนิยม 2 ตำแหน่ง และ , ทุกสามหลัก
    messagebox.showinfo('รวมราคาทั้งหมด','ราคาหอยและกุ้งรวมเป็นเงิน {:,.2f} บาท แบ่งเป็น กุ้ง {:,.2f} บาท และ หอย {:,.2f} บาท'.format(cal_sum,cal_resultv,cal_resulth))
    
# 6. สร้างปุ่มด้วย B1 = Button(GUI,text='ต้องจ่ายค่ากุ้งและหอยจำนวน')
# 7. ทำให้ปุ่มสวย B1 = ttk.Button(GUI,text='ต้องจ่ายค่ากุ้งและหอยจำนวน')
# 13. เชื่อมปุ่ม B1 กับ def Calc(): เพื่อให้ปรากฏข้อความเมื่อคลิก
# 34.1 T1 ย้าย กุ้ง,หอย ไปใส่ใน T1 เอา GUI ออก
B1 = ttk.Button(T1,text='  ต้องจ่ายค่ากุ้งและหอยจำนวน  ',image=icon_tab1_1,compound='left',command=Calc)
B1.pack(ipadx = 30,ipady= 15,pady = 15)

# 22. หากมีการกดปุ่มใน keyboard '<Return>' คือ enter ตัวไหนให้กลับไปที่ def Calc(event=None):
E1.bind('<Return>',Calc) # 23. ต้องใส่คำว่า event=None ไว้ในฟังชันด้วย เดี๋ยวลุงมาอธิบาย EP หน้า

#################### TAB-2 Wiki #############
# 35. TAB-2 Wiki

FONT1 = ('Angsana New',18)

# 35.1 สร้างหัวข้อของช่องค้นหาข้อมูล และ T2 ย้าย Wiki ไปใส่ใน T2 เอา GUI ออก
L2 = Label(T2,text='ค้นหาข้อมูลจาก Wikipedia',font =FONT1)
L2.pack(pady=5)
# 35.2 สร้างช่องค้นหาข้อมูล และ T2 ย้าย Wiki ไปใส่ใน T2 เอา GUI ออก
# 35.4 เอาตัวแปร v_search ใส่ใน textvariable
v_search = StringVar()
E1 = ttk.Entry(T2,textvariable = v_search,width=70,font=FONT1,justify='center')
E1.pack(pady = 5)

v_link = StringVar()

# 35.7 พิมพ์เป็นภาษาไหนก็ได้จะผลการค้นหาเป็นภาษาไทย
wikipedia.set_lang("th")

# 35.6 สร้างฟังชันในการค้นหาข้อมูล wikipedia
def WikiFind():
    # 35.6.3 ตรวจสอบถ้ามันค้นหาไม่ได้ให้โชว์ except
    try:
        # 35.6.1 ดึงข้อความจากช่องกรอกมา
        wiki_find = v_search.get()
        #text = wikipedia.summary(wiki_find)
        #เฉลยการบ้านจากลุงให้ทำ link ดูข้อมูลเพิ่มเติม เลยดึงเป็นเพจมาเลยจาก wikipedia
        text = wikipedia.page(wiki_find)
        print(wiki_find,' : ',text)
        # 35.6.2 เอา text ใส่ใน v_result แต่มันไม่ตัดคำให้ ข้อมูลจะโชว์ที่ค้นหาแทน --------Result--------- หลังจากคลิก Button 
        # 35.6.4 text[:1000] ตัวอักษรน้อยกว่า 1000
        #เฉลยการบ้านจากลุงให้ทำ link ดูข้อมูลเพิ่มเติม ดึงข้อมูลส่วน content มาไม่เอา title
        v_result.set(text.content[:1000])
        print('URL',text.url)
        #เฉลยการบ้านจากลุงให้ทำ link ดูข้อมูลเพิ่มเติม เอา text.url ใส่ในตัวแปร v_link
        v_link.set(text.url)
            
    except:
        v_result.set('ไม่มีข้อมูลกรุณา ค้นหาข้อมูลใหม่')

# 35.3. สร้างปุ่ม และ T2 ย้าย Wiki ไปใส่ใน T2 เอา GUI ออก
B1 = ttk.Button(T2,text='ค้นหา',image=icon_tab2_2,compound = 'left',command=WikiFind)
B1.pack(pady = 5)

#เฉลยการบ้านจากลุงให้ทำ link ดูข้อมูลเพิ่มเติม import เพื่อเปิด url
import webbrowser

#เฉลยการบ้านจากลุงให้ทำ link ดูข้อมูลเพิ่มเติม สร้างฟังชันก์เปิดลิงค์
def Resultpage2():
    webbrowser.open(v_link.get())


# 35.5 สร้างตัวแปรเพื่อเก็บค่าให้โชว์ผลการค้นหา
v_result = StringVar()
v_result.set('--------Result---------')
# 35.6 wraplength=600 ตัดข้อความที่ 600 ตัวอักษร
result = Label(T2,textvariable=v_result,wraplength=600,font=('Angsana New',14))
result.pack() 

#เฉลยการบ้านจากลุงให้ทำ link ดูข้อมูลเพิ่มเติม ทำปุ่มและเมื่อคลิกให้ลิงค์เข้า wiki หน้าที่เราค้นหา
B2 = ttk.Button(T2,text='ข้อมูลเพิ่มเติม',image=icon_tab2_1,compound = 'left',command=Resultpage2)
B2.pack(pady = 5)


#####################TAB-3#######################
icon_tab3_1 = PhotoImage(file='tab3.1.png')
icon_tab3_2 = PhotoImage(file='tab3.2.png')
icon_tab3_3 = PhotoImage(file='tab3.3.png')
icon_tab3_4 = PhotoImage(file='tab3.4.png')
icon_tab3_5 = PhotoImage(file='tab3.5.png')
icon_tab3_6 = PhotoImage(file='tab3.6.png')

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New',16))

SF1 = Frame(T3)
SF1.place(x=25,y=25)

#ROW0
allgoods = {}

product = {'Banana':{'name':'กล้วย','price':25},'Cokle':{'name':'หอยแครง','price':180},'Fish':{'name':'ปลานิล','price':80},'Mango':{'name':'มะม่วง','price':30},'Corn':{'name':'ข้าวโพ้ด','price':50},'Rice':{'name':'ข้าวหอมมะลิ','price':16}}

def UpdateTable():
    table.delete(*table.get_children())

    for i,m in enumerate(allgoods.values(),start=1):
        table.insert('','end',value=[i,m[0],m[1],m[2],m[3]])


def AddGoods(name='Banana'):
    if name not in allgoods:
        allgoods[name]=[product[name]['name'],product[name]['price'],1,product[name]['price']]
    else:
        quan = allgoods[name][2]+1
        total = quan * product[name]['price']
        allgoods[name]=[product[name]['name'],product[name]['price'],quan,product[name]['price']]
    print(allgoods)
    #table.insert('','end',value=[1.,'กล้วย',30,30,900])

def Goods1():
    AddGoods('Banana')
    UpdateTable()

def Goods2():
    AddGoods('Cokle')
    UpdateTable()

def Goods3():
    AddGoods('Fish')
    UpdateTable()

def Goods4():
    AddGoods('Mango')
    UpdateTable()

def Goods5():
    AddGoods('Corn')

def Goods6():
    AddGoods('Rice')
    UpdateTable()


B1 = ttk.Button(SF1,text='กล้วย',compound='top',image=icon_tab3_1,command=Goods1)
B1.grid(row=0,column=0,ipadx=20,ipady=10)

B2 = ttk.Button(SF1,text='หอยแครง',compound='top',image=icon_tab3_2,command=Goods2)
B2.grid(row=0,column=1,ipadx=20,ipady=10)

#ROW1
B3 = ttk.Button(SF1,text='ปลานิล',compound='top',image=icon_tab3_3,command=Goods3)
B3.grid(row=1,column=0,ipadx=20,ipady=10)

B4 = ttk.Button(SF1,text='มะม่วง',compound='top',image=icon_tab3_4,command=Goods4)
B4.grid(row=1,column=1,ipadx=20,ipady=10)

#ROW2
B5 = ttk.Button(SF1,text='ข้าวโพ้ด',compound='top',image=icon_tab3_5,command=Goods5)
B5.grid(row=2,column=0,ipadx=20,ipady=10)

B6 = ttk.Button(SF1,text='ข้าวหอมมะลิ',compound='top',image=icon_tab3_6,command=Goods6)
B6.grid(row=2,column=1,ipadx=20,ipady=10)

#สร้างตาราง
SF2 =Frame(T3)
SF2.place(x=400,y=25)

header = ['Time','Order','Price','Quantity','Total']
hwidth = [50,200,100,100,100]

table = ttk.Treeview(SF2,columns=header,show='headings',height=27)
table.pack()

for hd,hw in zip(header,hwidth):
    table.heading(hd,text=hd)
    table.column(hd,width=hw)

# 2. ทำให้หน้าจอกราฟฟิกโชว์ตลอด
GUI.mainloop()
