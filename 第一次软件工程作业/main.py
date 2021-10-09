import sys

import cal_sim_cosine as cal


def main():
    try:
        file_name1 = sys.argv[1]
        file_name2 = sys.argv[2]
        file_name3 = sys.argv[3]

        result = cal.cal_sim_cosine(file_name1, file_name2)

        result_file = open(file_name3, "a", encoding="utf-8")
        result_file.writelines(str(result) + "\n")
        result_file.close

        print("结果请查看" + file_name3 + "文件")

    except IndexError as e:
        print(e)
        sys.exit(1)
    except IOError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
