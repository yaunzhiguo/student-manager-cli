from models.student import create_student
from utils.helpers import get_grade, is_valid_score
from utils.file_utils import save_data
from utils.logger import logger

def add_student(students, filename):
    name = input("请输入学生姓名: ").strip()

    if name == "":
        print("姓名不能为空")
        return

    for student in students:
        if student["name"] == name:
            print("该学生已存在")
            return

    try:
        score = float(input("请输入学生成绩: "))
    except ValueError:
        print("成绩输入无效")
        return

    if not is_valid_score(score):
        print("成绩必须在 0 到 100 之间")
        return

    student = create_student(name, score)
    students.append(student)
    save_data(filename, students)
    print("学生添加成功")

    logger.info(f"添加学生: {name} 成绩: {score}")


def find_student(students):
    name = input("请输入要查找的学生姓名: ").strip()

    if name == "":
        print("姓名不能为空")
        return

    for student in students:
        if student["name"] == name:
            print("找到学生")
            print("姓名:", student["name"])
            print("成绩:", student["score"])
            print("等级:", get_grade(student["score"]))
            return

    print("没有找到该学生")

    logger.info(f"查询学生: {name}")


def show_students(students):
    if len(students) == 0:
        print("当前没有学生数据")
        return

    index = 1
    for student in students:
        print(f"学生 {index}")
        print("姓名:", student["name"])
        print("成绩:", student["score"])
        print("等级:", get_grade(student["score"]))
        print("-" * 20)
        index += 1


def delete_student(students, filename):
    name = input("请输入要删除的学生姓名: ").strip()

    if name == "":
        print("姓名不能为空")
        return

    for student in students:
        if student["name"] == name:
            students.remove(student)
            save_data(filename, students)
            print("删除成功")
            return

    print("没有找到该学生")

    logger.info(f"删除学生: {name}")


def update_student(students, filename):
    name = input("请输入要修改的学生姓名: ").strip()

    if name == "":
        print("姓名不能为空")
        return

    for student in students:
        if student["name"] == name:
            print("当前成绩:", student["score"])

            try:
                new_score = float(input("请输入新的成绩: "))
            except ValueError:
                print("成绩输入无效")
                return

            if not is_valid_score(new_score):
                print("成绩必须在 0 到 100 之间")
                return

            student["score"] = new_score
            save_data(filename, students)
            print("成绩修改成功")
            return

    print("没有找到该学生")

    logger.info(f"修改成绩: {name} -> {new_score}")


def statistics(students):
    if len(students) == 0:
        print("当前没有学生数据")
        return

    total = 0
    max_score = students[0]["score"]
    min_score = students[0]["score"]
    max_name = students[0]["name"]
    min_name = students[0]["name"]

    excellent_count = 0
    pass_count = 0
    fail_count = 0

    for student in students:
        score = student["score"]
        total += score

        if score > max_score:
            max_score = score
            max_name = student["name"]

        if score < min_score:
            min_score = score
            min_name = student["name"]

        if score >= 90:
            excellent_count += 1
            pass_count += 1
        elif score >= 60:
            pass_count += 1
        else:
            fail_count += 1

    average = total / len(students)

    print("学生总人数:", len(students))
    print("总分:", total)
    print("平均分:", average)
    print("最高分:", max_score, "学生:", max_name)
    print("最低分:", min_score, "学生:", min_name)
    print("优秀人数:", excellent_count)
    print("及格人数:", pass_count)
    print("不及格人数:", fail_count)
