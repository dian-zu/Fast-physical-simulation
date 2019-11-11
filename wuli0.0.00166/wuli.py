import os
import tkinter
from tkinter import ttk 
import tkinter.messagebox
from pyphysicssandbox import *
import tkinter.colorchooser  as cc

WIN_WIDTH = 800
WIN_HT = 600
base = static_box((0, 600), WIN_WIDTH, 10)
base.color = Color("black")
base = static_box((0, -10), WIN_WIDTH, 10)
base.color = Color("black")
window("Physical Simulator", WIN_WIDTH, WIN_HT)
gravity(0.0, 500.0)

t = tkinter.Tk()#初始化对象，t


class tishi(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
 
    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tkinter.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
 
        label = tkinter.Label(tw, text=self.text, justify=tkinter.LEFT,
                      background="#ffffe0", relief=tkinter.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
 
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            
          
def createtishi( widget, text):
    toolTip = tishi(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


def callback():
	res = tkinter.messagebox.askokcancel('关闭','确定退出(退出后数据清空)？')
	if res ==True:
		t.quit()
	else:
		pass

def caidan(*args):
	tkinter.messagebox.showinfo('彩蛋','你点我干什么？')
	tkinter.messagebox.showinfo('彩蛋','我不是彩蛋。')
	tkinter.messagebox.showwarning('彩蛋','等等！')
	tkinter.messagebox.showinfo('彩蛋','为什么我的标题写着“彩蛋”？！')
	tkinter.messagebox.showinfo('彩蛋','（电阻居然暴露了我。。。）')
	tkinter.messagebox.showinfo('彩蛋','好吧我是彩蛋，不要告诉别人')
	t.quit()

def caidan2(*args):
	tkinter.messagebox.showinfo('彩蛋','您好。。。')
	tkinter.messagebox.showinfo('彩蛋','我是。。。。')
	tkinter.messagebox.showwarning('彩蛋','等等！')
	tkinter.messagebox.showinfo('彩蛋','你怎么找到我的')
	tkinter.messagebox.showinfo('彩蛋','我藏得这么隐秘')
	tkinter.messagebox.showinfo('彩蛋','好吧我是彩蛋，不要告诉别人')
	t.quit()

w = 500#宽变量：165
h = 335#高变量：400
ws = 0#屏幕位置x系坐标变量：200
hs=200#屏幕位置y系坐标变量：200
t.title('物理快模拟-未选择')#设置窗口名称为：物理快模拟
t.geometry('%dx%d+%d+%d'%(w,h,ws,hs))#设置窗口的高，宽，X坐标，Y坐标
t.resizable(0,0)#设置窗口不能最大化
t.iconbitmap('wuli.ico')

menubar = tkinter.Menu(t)

menuc = tkinter.Menu(menubar)

yesno = tkinter.IntVar(value=0)
X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
def canvas_cao():
	global yesno,X,Y

	caogao = tkinter.Toplevel()
	caogao.title('画板草稿')
	caogao.iconbitmap('wuli.ico')
	caogao.geometry('800x600+50+50')

	canvas = tkinter.Canvas(caogao, bg='white', width=800, height=600,cursor='pencil')
	canvas.pack()

	def pen_d(event):
		yesno.set(1)
		X.set(event.x)
		Y.set(event.y)
	canvas.bind('<Button-1>', pen_d)

	def pen_u(event):
		canvas.create_line(X.get(), Y.get(), event.x, event.y,width=5)
		X.set(event.x)
		Y.set(event.y)
	canvas.bind('<B1-Motion>', pen_u)
menuc.add_command(label='草稿画板',command=canvas_cao)
menuc.add_separator()

xian_tf = tkinter.IntVar()
xian_menu = menuc.add_checkbutton(label='启用线条工具',variable=xian_tf)

menuc.add_separator()

menubar.add_cascade(label='工具',menu=menuc)

menuw = tkinter.Menu(menubar)

wrap_tf = tkinter.IntVar()
wrap_menu = menuw.add_checkbutton(label='页面滚动',variable=wrap_tf)

menuw.add_separator()

def tk_info():
	info_ui = tkinter.Toplevel()
	info_ui.title('页面设置')
	info_ui.iconbitmap('wuli.ico')
	info_ui.geometry('500x400+10+10')

	info_frame = tkinter.LabelFrame(info_ui,text='页面设置')
	info_frame.place(x = 5,y = 5,width = 490,height = 100)

	root_x_lb = tkinter.Label(info_frame,text='页面x设置：')
	root_x_lb.place(x = 5,y = 5)

	root_x_en_var = tkinter.StringVar()
	root_x_en = tkinter.Enterbox(info_ui)

	root_y_lb = tkinter.Label(info_frame,text='页面y设置：')
	root_y_lb.place(x = 5,y = 45)
tk_cmd = menuw.add_command(label='页面设置',command=tk_info)

menuw.add_separator()

menubar.add_cascade(label='设置',menu=menuw)
'''#########################################################公告
#******************一定注意*****************'''
def gonggao():
	tkinter.messagebox.showinfo('2019.10.27更新公告','1.优化菜单\n2.“帮助”上线\n3.修复了若干BUG\n4.UI微微调整\n5.增加状态栏\n6.增加了异常控制\n--祝您使用愉快')
menubar.add_command(label = '公告',command=gonggao)
'''#########################################################版本号
#******************一定注意******************'''
menug = tkinter.Menu(menubar)
menug.add_command(label = '版本状态：内测')
menug.add_command(label = '版本号：0.0.00165')
menug.add_separator()

menug.add_command(label = '内测状态：开源')
menug.add_separator()

menug.add_command(label = '制作：电阻')
menug.add_command(label = '版权：极速程式项目应用')
menug.add_separator()

menubar.add_cascade(label='关于',menu=menug)

def bangzhu():
	bangzhu_ui = tkinter.Toplevel()
	bangzhu_ui.title('帮助')
	bangzhu_ui.geometry('257x150+100+100')
	bangzhu_ui.iconbitmap('wuli.ico')
	bangzhu_ui.resizable(0,0)

	bz_n = ttk.Notebook(bangzhu_ui)

	yuan_bz = tkinter.Frame(bz_n)
	ju_bz = tkinter.Frame(bz_n)
	xian_bz = tkinter.Frame(bz_n)
	caogao_bz = tkinter.Frame(bz_n)

	bz_n.add(yuan_bz,text='添加圆形')
	bz_n.add(ju_bz,text='添加多边形')
	bz_n.add(xian_bz,text='添加线段')
	bz_n.add(caogao_bz,text='使用草稿')

	yuan_label = tkinter.Message(yuan_bz,width=210,text='       添加圆形，圆形是物理模拟中必不可少的元素，而添加圆形非常简单，写出圆心的坐标即可，适当的调整大小和重量！')
	yuan_label.place(x=5,y=5)
	ju_label = tkinter.Message(ju_bz,width=210,text='       添加多边形，一些特殊图形经常出现在实验，而添加多边形只需要写出多边形的每个顶点的坐标即可，适当的调整重量！')
	ju_label.place(x=5,y=5)
	xian_label = tkinter.Message(xian_bz,width=210,text='       添加线段，这里的线段是反重力的，可以当做边缘使用！只需要写出端点的坐标。')
	xian_label.place(x=5,y=5)
	caogao_label = tkinter.Message(caogao_bz,width=210,text='       需要大量计算？不用，直接用草稿，在上面涂鸦，快速画出你要做的实验，表上数，更方便实验。')
	caogao_label.place(x=5,y=5)

	bz_n.pack(padx=10,pady=10,fill=tkinter.BOTH,expand=tkinter.TRUE)

menubar.add_command(label = '帮助',command=bangzhu)

menubar.add_command(label = "退出", command = callback)

t.config(menu = menubar)

zhong_or_bs = tkinter.StringVar()
zhong_or_bs.set('设置大小：')
label_2d = tkinter.StringVar()
label_2d.set('未选择2D图形')
zt_2d = tkinter.StringVar()
zt_2d.set('未添加2D图形')

data_2d = []
color = '#ff0000'
#————————————————#
#————————————————#
#————————————————#
#————————————————#
#————————————————#

group = tkinter.LabelFrame(t, text='2D图形选择：',padx=5, pady=5)
group.place(x=5, y=5,width = 200,height=500)

label = tkinter.Label(group,text='请选择：',font=r'C:\Windows\Fonts\华文琥珀')
label.place(x=10,y=5)

label = tkinter.Label(group,text='极速程式项目',font=('方正舒体',23),fg = 'blue',cursor='gumby')
label.place(x=5,y=25,width=180)

label.bind('<Button-2>',caidan)
label.bind('<Button-3>',caidan2)

def yuan():
	zhong_or_bs.set('设置大小：')
	label1.place_forget()
	t.title('物理快模拟-添加圆形')

	group4 = tkinter.LabelFrame(group1,text='设置角度:',padx=5,pady=5)
	group4.place(x=5,y=0,width=260,height=50)

	jiaodu = tkinter.Spinbox(group4,from_=1,to=360)
	jiaodu.pack()

	group3 = tkinter.LabelFrame(group1,text='设置坐标：',padx=5,pady=5)
	group3.place(x=5,y=60,width=260,height=100) 

	x_label = tkinter.Label(group3,text='x坐标：')
	x_label.place(x=5,y=13)

	yuan_x = tkinter.StringVar()
	x = tkinter.Spinbox(group3,from_=0,to=800,textvariable=yuan_x)
	x.pack(pady=10)

	x_label = tkinter.Label(group3,text='y坐标：')
	x_label.place(x=5,y=43)

	yuan_y = tkinter.StringVar()
	y = tkinter.Spinbox(group3,from_=0,to=600,textvariable=yuan_y)
	y.pack()

	def colors():
		global color
		color = cc.askcolor()[1]
	color_return = tkinter.Button(group1,text='选择颜色…',command=colors)
	color_return.place(x=3, y=170,width = 135,height=40)

	def done():
		try:
			ball1 = ball((int(yuan_x.get()), int(yuan_y.get())), int(bs.get()),int(zhong_bs.get()))
			ball1.color = Color(color)
			ball1.wrap = bool(wrap_tf.get())
			zt_2d.set('圆形 重量：{} 大小：{} 颜色：{} {}'.format(zhong_bs.get(),bs.get(),color,(int(yuan_x.get()),int(yuan_y.get()))))
			tkinter.messagebox.showinfo('成功','添加成功')
		except:
			zt_2d.set('失败：错误！')
	color_return = tkinter.Button(group1,text='确定添加',command=done)
	color_return.place(x=145, y=170,width = 120,height=40)

b2=tkinter.Button(group,text='添加圆形',command=yuan)
b2.place(x=10, y=80,width = 175,height=40)

def san():
	san_xy = []
	zhong_or_bs.set('(不可用)')
	label1.place_forget()	
	t.title('物理快模拟-添加多边形')

	group4 = tkinter.LabelFrame(group1,text='坐标操作:',padx=5,pady=5)
	group4.place(x=5,y=0,width=260,height=50)

	cmd = ttk.Combobox(group4)
	cmd.place(x=0,y=0,width=120,height=20)
	cmd['value']=san_xy

	def ju_new():

		san_x.set(0)
		san_y.set(0)
	return_ju = tkinter.Button(group4,text = '新建',command=ju_new)
	return_ju.place(x = 125,y = 0,width = 60,height = 20)
	# jiaodu = tkinter.Spinbox(group4,from_=1,to=360)
	# jiaodu.pack()

	def ju_return():
		san_xy.append((int(san_x.get()),int(san_y.get())))
		cmd['value'] = san_xy
		cmd.current(len(san_xy)-1)
	return_ju = tkinter.Button(group4,text = '确定添加',command=ju_return)
	return_ju.place(x = 190,y = 0,width = 60,height = 20)

	group3 = tkinter.LabelFrame(group1,text='设置端点坐标：',padx=5,pady=5)
	group3.place(x=5,y=60,width=260,height=100)

	x_label = tkinter.Label(group3,text='x坐标：')
	x_label.place(x=5,y=13)
	san_x = tkinter.StringVar()
	x = tkinter.Spinbox(group3,from_=0,to=800,textvariable=san_x)
	x.pack(pady=10)

	x_label = tkinter.Label(group3,text='y坐标：')
	x_label.place(x=5,y=43)
	san_y = tkinter.StringVar()
	y = tkinter.Spinbox(group3,from_=0,to=600,textvariable=san_y)
	y.pack()

	def colors():
		global color
		color = cc.askcolor()[1]
	color_return = tkinter.Button(group1,text='选择颜色…',command=colors)
	color_return.place(x=3, y=170,width = 135,height=40)

	def done():
		global color
		if xian_tf.get() == 1:
			try:
				if len(tuple(san_xy)) >=3:
					odd_shape = polygon(tuple(san_xy),int(zhong_bs.get()))
					odd_shape.color = Color(color)
					odd_shape.wrap = bool(wrap_tf.get())
					zt_2d.set('多边形 重量：{} 颜色：{} {}'.format(zhong_bs.get(),color,tuple(san_xy)))
					tkinter.messagebox.showinfo('成功','添加成功')
				else:
					line=static_line(tuple(san_xy)[0], tuple(san_xy)[1], 5)
					line.color=Color(color)
					zt_2d.set('线条')
					tkinter.messagebox.showinfo('成功','添加成功')
			except:
				zt_2d.set('失败：错误！')
		else:
			try:
				odd_shape = polygon(tuple(san_xy),int(zhong_bs.get()))
				odd_shape.color = Color(color)
				odd_shape.wrap = bool(wrap_tf.get())
				zt_2d.set('多边形 重量：{} 颜色：{} {}'.format(zhong_bs.get(),color,tuple(san_xy)))
				tkinter.messagebox.showinfo('成功','添加成功')
			except:
				zt_2d.set('失败：错误！')
	color_return = tkinter.Button(group1,text='确定添加',command=done)
	color_return.place(x=145, y=170,width = 120,height=40)

b3=tkinter.Button(group,text='添加多边形',command=san)
b3.place(x=10, y=130,width = 175,height=40)

group5 = tkinter.LabelFrame(group,text='图形物理设置')
group5.place(y=170,x=5,width=180,height=85)

bs = tkinter.StringVar()#设置字符串变量：v
bs = tkinter.Spinbox(group5,from_=5,to=200,width=10,textvariable=bs)
bs.place(x=70,y=1)

bs_label= tkinter.Label(group5,textvariable=zhong_or_bs)
bs_label.place(x=0,y=1)

zbs = tkinter.StringVar()#设置字符串变量：v
zhong_bs = tkinter.Spinbox(group5,from_=10,to=5000,width=10,textvariable=zbs)
zhong_bs.place(x=70,y=41)

bs_label= tkinter.Label(group5,text='设置重力：')
bs_label.place(x=0,y=41)
#————————————————#
#————————————————#
#————————————————#
#————————————————#
#————————————————#

group1 = tkinter.LabelFrame(t, text='调试区域：',padx=5, pady=5)
group1.place(x=210, y=5,width = 285,height=240)

label1 = tkinter.Label(group1,textvariable=label_2d,fg='red')
label1.place(x = 0,y=0)

def label_233_bind(*args):
	if zt_2d.get() != '未添加2D图形' and zt_2d.get() != '失败：错误！' and zt_2d.get() != '打开失败，请确定上一个图形是否添加成功！':
		label233_ui = tkinter.Toplevel()
		label233_ui.title('自动化工具')
		label233_ui.iconbitmap('wuli.ico')
		label233_ui.geometry('500x400+0+200')

		set_gongneng = ttk.Notebook(label233_ui)

		dingzi = tkinter.Frame(set_gongneng)
		zidongzhou = tkinter.Frame(set_gongneng)

		set_gongneng.add(dingzi,text = '固定钉')
		set_gongneng.add(zidongzhou,text = '自动轴')
		set_gongneng.pack(padx=10,pady=10,fill=tkinter.BOTH,expand=tkinter.TRUE)
	else:
		zt_2d.set('打开失败，请确定上一个图形是否添加成功！')
label233 = tkinter.Label(t,textvariable=zt_2d,bd=1,relief=tkinter.SUNKEN,anchor=tkinter.W)  # anchor left align W -- WEST
label233.pack(side=tkinter.BOTTOM,fill=tkinter.X)
label233.bind('<Button-1>', label_233_bind)
createtishi(label233,'点击为上一个图形开启自动化工具')
#————————————————#
#————————————————#
#————————————————#
#————————————————#
#————————————————#
def start():
	try:
		data_2d = []
		run(True)
	except:
		tkinter.messagebox.showerror('Error','Error!Try to restart this application!')
		t.quit()
done=tkinter.Button(t,text='开始演示…',command=start)
done.place(x=210, y=250,width = 285,height=40)

#————————————————#
#————————————————#
#————————————————#
#————————————————#
#————————————————#
t.protocol('WM_DELETE_WINDOW',callback)

tkinter.mainloop()

	 #//////////////////////////#
	##//  制作:       谢谢     \\##
	##//  电阻小弟    使用     \\##
	 #\\\\\\\\\\\\\\\\\\\\\\\\\\\#
	 #######       ##     ##
	 #3   ##       ##     ##
	 ##    ##      ##     #6
	 ##     #.     ##     ##
	 ##    ##       ### ###
	 ##   ##          ### ##
	 #####                ##
	 ##           ##      ##
	 ##            ##     ##
	 ##              #####.2