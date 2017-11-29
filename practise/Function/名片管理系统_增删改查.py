#使用列表装名片--内存
card_infos = [] # 存储的字符改成--字典
def read_doc():
    '读取文本内容'
    global card_infos
    doc = open('test.txt','a+')
    doc.seek(0)
    result = doc.read()
    doc.close()
    if len(result) != 0 :
        result = eval(result)
        card_infos = result # 把文本中的表单加入
    return_name()
def write_doc():
    '写入文本内容'
    global card_infos
    doc = open('test.txt','w')
    card_infos = str(card_infos)
    doc.write(card_infos)
    doc.close()
def cardInfo():
    '显示系统大体信息'
    print("="*50)
    print("\t名片管理系统1.1")
    print("\t1.添加名片")
    print("\t2.删除名片")
    print("\t3.修改名片")
    print("\t4.查找名片")
    print("\t5.显示名片")
    print("\t6.退出名片管理系统")
    print("="*50)
def addname():
    '添加名片'
    global card_infos
    name = input("请输入您要添加的姓名:")
    qq = input("请输入您要添加的qq:")
    phone = input("请输入您要添加的电话:")
    #把信息添加到字典
    name_info = {}
    name_info["name"] = name
    name_info["qq"] = qq
    name_info["phone"] = phone
    card_infos.append(name_info)
    print("当前人数如下:")
    print("="*40)
    for card in card_infos :
        print(card)
def del_name():
    '根据内容删除名片的某个信息'
    global card_infos
    name = input("请输入您要删除的姓名:")#李四
    flage = 0#0没有此人1，有此人
    i = 0
    for name_info in card_infos :
        #删除姓名
        if name_info.get("name") == name:
            #删除该字典
            #card_infos.remove(name_info)
            del card_infos[i]
            #del name_info
            print("已经删除:%s" % name)
            flage = 1
            break
        else :
            #print("没有此人:%s" % name)
            flage = 0
        i += 1
    if flage == 0:
        print("没有此人:%s" % name)
    #打印当前列表的信息
    print("当前人数如下:")
    print("="*40)
    for card in card_infos :
        print(card) 
def change_name():
    '修改名片'
    global card_infos
    name = input("请输入您要修改的姓名:")
    flage = False#True有此人，False没有此人
    for name_info in card_infos :
        #删除姓名
        if name_info.get("name") == name:
            #修改该字典
            new_name = input("你要修改成新的姓名:")
            name_info["name"] = new_name
            print("已经把%s修改成:%s" % (name,new_name))
            flage = True
            break
        else :
            flage = False
    if flage :
        pass
    else:    
        print("没有你要修改的人:%s" % name)
    #打印当前列表的信息
    print("当前人数如下:")
    print("="*40)
    for card in card_infos :
        print(card)
def find_name():
    '查找名片'
    global card_infos
    name = input("请输入您要查找的姓名:")
    flage = 0
    for name_dic in card_infos:
        if name_dic['name'] == name:
            print('你找到了%s' % name)
            flage == 1
        else:
            flage == 0
    if flage == 0:
        print("%s不在系統中" % name)
def return_name():
    '顯示名片'
    global card_infos
    print("当前人如下:")
    print("姓名\tqq\t电话")
    for name_info in card_infos :
        print("%s\t%s\t%s" % (name_info["name"],name_info["qq"],name_info["phone"]))
    print("")  
def main():
    '名片系統主程序'
    while True:
        num = input("请输入上面提示的编号:")
        if num.isdigit():#判断是否都是数字
            print("你输入的编号是%s" % num)
            if num == "1" :#添加名片
                addname()
            elif num == "2" :#删除名片
                del_name()
            elif num == "3" :#修改名片
                change_name()
            elif num == "4" :#查找名片
                find_name()
            elif num == "5" :#显示名片
                return_name()
            elif num == "6" :#退出名片管理系统
                break
            else :
                print("亲，好像你输入的编号错了!")
        else:
            print("亲,请输入正确的编号!")
cardInfo()
read_doc()
main()
write_doc()
