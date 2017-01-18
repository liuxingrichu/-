#!/urs/bin/env python
# -*- coding:utf-8 -*-

import re

#添加员工信息
def add(request):
    request = re.split("[(),']", request.strip())
    obj = []
    for i in request:
        if i:
            obj.append(i)

    save_data()
    phone = False
    count = 0
    with open("staff_table.txt.bak", "r", encoding="utf-8") as f1,\
        open("staff_table.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            if obj[3] not in line:
                f2.write(line)
                count += 1
            else:
                f2.write(line)
                phone = True
                count += 1
        if phone:
            return False
        else:
            obj[0] = str(count+1)
            f2.write("\n")
            f2.write(",".join(obj))
            return True

#删除员工信息
def delete(request):
    obj = re.split("[=']", request.strip())[-2]
    save_data()
    with open("staff_table.txt.bak", "r", encoding="utf-8") as f1,\
        open("staff_table.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            if line.startswith(obj):
                continue
            else:
                f2.write(line)

#更新员工信息
def update(request):
    request = re.split("'", request.strip())
    obj = []
    for i in range(4):
        if i%2:
            obj.append(request[i])

    save_data()
    with open("staff_table.txt.bak", "r", encoding="utf-8") as f1,\
        open("staff_table.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            info = line.strip().split(",")
            if info[4] == obj[1]:
                info[4] = obj[0]
                f2.write(",".join(info))
                f2.write("\n")
            else:
                f2.write(line)

#查询员工信息
def query(request):
    request = request.strip().split()
    if "*" in request:
        if "LIKE" not in request:
            read_data(4, "IT", request)
        else:
            read_data(5, "2013", request)
    else:
        read_data(2, 22, request)

#数据备份
def save_data():
    with open("staff_table.txt", "r", encoding="utf-8") as f1,\
        open("staff_table.txt.bak", "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line)

#数据读取
def read_data(position, obj, request):
    count = 0
    print("-"*50)
    with open("staff_table.txt", "r", encoding="utf-8") as f1:
        for line in f1:
            info = line.strip().split(",")
            if "*" in request:
                if "LIKE" not in request:
                    if info[position] == obj:
                        print(" ".join(info))
                        count += 1
                else:
                    if info[position].startswith(obj):
                        print(" ".join(info))
                        count += 1
            else:
                if int(info[position]) > obj:
                    print("%-10s   %3s" % (info[1], info[2]))
                    count += 1
    print("-"*50)
    print("共计：%s 条" % count)


#task = "SELECT name,age FROM staff_table WHERE age > 22"
#task = "SELECT  * FROM staff_table WHERE dept = 'IT'"
#task = "SELECT * FROM staff_table WHERE enroll_date LIKE '2013'"
#task = "INSERT INFO staff_table VALUES ('Alex Zhou','18','13789456129','IT','2016-01-01')"
#task = "DELETE FROM staff_table staff_id = '2'"
#task = "UPDATE staff_table SET dept = 'Market' WHERE dept = 'IT'"


def main():
    exit_flag = False
    while not exit_flag:
        task = input(">>")
        if task.startswith("SELECT"):
            query(task)
        elif task.startswith("INSERT"):
            result = add(task)
            if result:
                print("Add success")
            else:
                print("Add fail, because phone is exist")
        elif task.startswith("DELETE"):
            delete(task)
            print("Delete success")
        elif task.startswith("UPDATE"):
            update(task)
            print("Update success")
        elif task == "q":
            exit_flag = True


if __name__ == '__main__':
    main()
