from utils.file_utils import load_data, save_data
from services.student_service import add_student, find_student, show_students
from services.student_service import delete_student, update_student, statistics
from utils.logger import logger

FILENAME = "data/students.txt"


def menu():
    print("\n====== 学生成绩管理系统 ======")
    print("1. 添加学生")
    print("2. 查找学生")
    print("3. 显示所有学生")
    print("4. 删除学生")
    print("5. 修改学生成绩")
    print("6. 成绩统计")
    print("7. 保存数据")
    print("8. 重新加载数据")
    print("0. 退出系统")
    print("============================")


def main():
    students = load_data(FILENAME)

    while True:
        menu()
        choice = input("请输入你的选择: ").strip()

        if choice == "1":
            add_student(students, FILENAME)
        elif choice == "2":
            find_student(students)
        elif choice == "3":
            show_students(students)
        elif choice == "4":
            delete_student(students, FILENAME)
        elif choice == "5":
            update_student(students, FILENAME)
        elif choice == "6":
            statistics(students)
        elif choice == "7":
            save_data(FILENAME, students)
        elif choice == "8":
            students = load_data(FILENAME)

        elif choice == "0":
            save_data(FILENAME, students)
            print("感谢使用学生成绩管理系统，再见！")
            logger.info("系统退出")

            break
        else:
            print("输入无效，请重新选择")


if __name__ == "__main__":
    main()

logger.info("系统启动")