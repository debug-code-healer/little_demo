import os

def add():
    all_student = []
    print("开始信息的输入!")
    for i in range(1000000):
        count = 0
        ccount = 0
        mm = str("student")+str(i)
        mm = []
        while True:
            ccount += 1
            name = str(input("请输入此人的名字:"))
            for ch in name:
                if '\u4e00' <= ch <= '\u9fff':
                    count += 1 
            if count == len(name):
                mm.append(name)
                break
            else:
                print("姓名输入错误,请重新输入!")
                continue
            

        while True:
            age = eval(input("请输入此人的年龄:"))
            if 1<=age<=100:
                mm.append(age)
                break
            else:
                print("年龄输入错误,请重新输入!")
                continue

        while True:
            telephone = str(input("请输入此人的电话号码:"))
            if len(telephone)==11:
                mm.append(telephone)
                break
            else:
                print("电话号码输入错误,请重新输入!")
                continue

        while True:
            email = str(input("请输入此人的邮箱:"))
            if "@" in email and "." in email:
                mm.append(email)
                break
            else:
                print("邮箱输入错误,请重新输入!")
                continue
        
        all_student.append(mm)
        
        
        print("是否要继续输入:")
        n = eval(input("1.继续 2.退出"))
        if n == 2:
            return all_student,ccount
            break
        else:
            continue


def find(all,count):
    while True:
        n = str(input("请输入要查找联系人的姓名:"))
        for m in range(count):
            if all[m][0] == n:
                print(all[m])
            else:
                print("未查找到此人!")
        print("是否继续查找其他人:")
        m = eval(input("1.是 2.否"))
        if m == 1:
            continue
        else:
            break

def delete(all,count):
    while True:
        n = str(input("请输入要删除的联系人姓名:"))
        for m in range(count):
            if all[m][0] == n:
                del all[m]
                print("删除联系人完成!")
            else:
                print("未查找到此人!")
        print("是否继续删除其他人:")
        m = eval(input("1.是 2.否"))
        if m == 1:
            continue
        else:
            break

def revise(all,count):
    while True:
        n = str(input("请输入要修改的的联系人姓名:"))
        dcount = 0
        if count == 0:
            print("通讯录中没有任何联系人!")
            break
        for m in range(count):
            if all[m][0] == n:
                print("请问您要修改此联系人的哪个信息:")
                mm = eval(input("1.姓名 2.年龄 3.电话号码 4.邮箱"))
                if mm ==1:
                    while True:
                        new_name = str(input("请输入新姓名:"))
                        for ch in new_name:
                            if '\u4e00' <= ch <= '\u9fff':
                                dcount += 1 
                        if dcount == len(new_name):
                            all[m][0] = new_name
                            break
                        else:
                            print("姓名输入错误,请重新输入!")
                            continue
                elif mm == 2:
                    while True:
                        new_age = eval(input("请输入新的年龄:"))
                        if 1<=new_age<=100:
                            all[m][1] == new_age
                            break
                        else:
                            print("年龄输入错误,请重新输入!")
                            continue
                elif mm == 3:
                    while True:
                        new_telephone = str(input("请输入新的电话号码:"))
                        if len(new_telephone)==11:
                            all[m][2] =  new_telephone
                            break
                        else:
                            print("电话号码输入错误,请重新输入!")
                            continue                    
                elif mm == 4:


                    while True:
                        new_email = str(input("请输入新邮箱:"))
                        if "@" in new_email and "." in new_email:
                            all[m][3] = new_email
                            break
                        else:
                            print("邮箱输入错误,请重新输入!")
                            continue 
                else:
                    print("没有此操作!")
            else:
                print("未查找到此人!")
        print("是否继续修改其他人:")
        m = eval(input("1.是 2.否"))
        if m == 1:
            continue
        else:
            break
            
        
    



def main():
    while True:
        print("==通讯录管理系统==")
        print("1.新建\n2.查询\n3.删除\n4.修改")
        n = eval(input("请选择你要进行的操作:"))
        if n == 1:
            all,count = add()
        elif n ==2:
            find(all,count)
        elif n == 3:
            delete(all,count)
        else:
            revise(all,count)
        print("是否要继续进行操作:\n")
        m = eval(input("1.继续\n2.结束"))
        if m == 1:
            continue
        else:
            exit()
main()
    
