import os
import math


def main():
    path = "data/"
    iem_files = os.listdir(path)
    file = ""

    new_frequency_list = []
    new_dB_list = []
    for i in range(0, 1425):
        new_frequency_list.append(math.pow(10, 3 * i / 1264 + 1))

    # for frequency in new_frequency_list:
    #     print(frequency)
    # print(len(new_frequency_list))
    for iem_file in iem_files:
        file_name, file_ext = os.path.splitext(iem_file)
        if file_ext == "":
            continue

        old_frequency_list = []
        old_dB_list = []
        temp_string = ""

        file = open(path + iem_file, "r")
        # print(file)
        for line in file.readlines():
            if line == "":
                continue

            frequency, dB = line.strip().split(",")
            old_frequency_list.append(frequency)
            old_dB_list.append(dB)

        for i in range(0, len(old_dB_list)):
            temp_string += str(new_frequency_list[i]) + \
                "," + str(old_dB_list[i]) + "\n"

        file = open(path + iem_file, "w")
        file.write(temp_string.strip())

    file.close()


if __name__ == '__main__':
    main()
