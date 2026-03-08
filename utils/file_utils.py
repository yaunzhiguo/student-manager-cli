from utils.logger import logger

def load_data(filename):
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                data = line.split(",")

                if len(data) != 2:
                    continue

                name = data[0]
                score = float(data[1])

                student = {
                    "name": name,
                    "score": score
                }

                students.append(student)

        print("数据加载成功")

    except FileNotFoundError:
        print("没有找到数据文件，已创建空列表")

    except Exception as e:
        print("读取文件失败：", e)
        logger.error("读取学生文件失败")

        

    return students

def save_data(filename, students):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for student in students:
                line = student["name"] + "," + str(student["score"]) + "\n"
                file.write(line)

        print("数据保存成功")

    except Exception as e:
        print("保存文件失败：", e)