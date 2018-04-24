# import tkinter
#
# #tkinter._test() 测试
#
# def showLabel():
#     global baseFrame
#     lb = tkinter.Label(baseFrame, text="显示Label") #标签
#     lb.pack()
#
# baseFrame = tkinter.Tk()
# baseFrame.wm_title("Label Test") #标题
# btn = tkinter.Button(baseFrame, text="Show Label", command=showLabel) #按钮
# btn.pack() #布局
# baseFrame.mainloop() #消息循环

# import tkinter
#
# def baseLabel(event):
#     global baseFrame
#     print("我被点击了")
#     lb = tkinter.Label(baseFrame, text="谢谢点击")
#     lb.pack()
#
# baseFrame = tkinter.Tk()
# lb = tkinter.Label(baseFrame, text="模拟按钮")
# lb.bind("<Button-1>", baseLabel) #绑定消息与处理函数
# lb.pack()
#
# baseFrame.mainloop()

import tkinter

baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)
for item in ['File', 'Edit', 'View', 'About']:
    menubar.add_command(label=item)
baseFrame['menu'] = menubar
baseFrame.mainloop()