import sys


class Min_Max_Heap(Heap):
    def __init__(self) -> None:
        super().__init__()
        self.current_level = 0
    
    def is_max_level(self, current_node_index):
        while(current_node_index > 0):
            current_node_index = int((current_node_index - 1) / 2)
            self.current_level += 1
        return self.current_level % 2 != 0
    
    def reheap_up_max():
        pass

    def reheap_up_min():
        pass


    def min_max_heap(self, size):
        current_node_index = size - 1
        is_max_level = self.is_max_level(current_node_index)
        parent_node_index = int((current_node_index - 1) / 2)
        if((is_max_level) and self.result[current_node_index]["number_of_students"] < self.result[parent_node_index]["number_of_students"]):
            self.swap(current_node_index, parent_node_index)



    def push(self, el):
        self.result.append(el)

        size = len(self.result)

        if size < 2:
            return

        self.min_max_heap(size)


class Heap:
    def __init__(self, mode) -> None:
        self.mode = mode
        self.result = []
        #self.current_index = 0

    def display(self):
        print(
            f"root: serial_number: {self.result[0]['serial_number']} number_of_students: {self.result[0]['number_of_students']}"
        )

        temp = []  # 儲存所有節點的學生數
        left_parent_node_index = []
        common_difference = 2
        bottom = 0

        # bottom
        for i in range(len(self.result)):
            temp.append(self.result[i]["number_of_students"])
            if i == len(self.result) - 1:
                bottom = self.result[i]

                print(
                    f"bottom: serial_number: {bottom['serial_number']} number_of_students: {bottom['number_of_students']}"
                )

        # leftmost bottom
        for i in range(len(self.result)):
            if i == 0 or i == 1:
                left_parent_node_index.append(i)
            else:
                if i != 2:
                    common_difference *= 2  # 固定公差
                left_parent_node_index.append(
                    left_parent_node_index[i - 1] + common_difference
                )
                if left_parent_node_index[i] > len(self.result):
                    left_parent_node_index.pop()
                    break

        print(
            f"leftmost bottom: serial_number: {self.result[left_parent_node_index[len(left_parent_node_index)-1]]['serial_number']} number_of_students: {self.result[left_parent_node_index[len(left_parent_node_index)-1]]['number_of_students']}"
        )

        # Max heap or Min heap
        if self.mode == 1:
            print(f"Max heap: {temp}")
        elif self.mode == 2:
            print(f"Min heap: {temp}")

    def swap(self, current_node_index, parent_node_index):
        temp = self.result[current_node_index]
        self.result[current_node_index] = self.result[parent_node_index]
        self.result[parent_node_index] = temp

    def heap(self):
        current_node_index = len(self.result) - 1
        parent_node_index = int((current_node_index - 1) / 2)

        if self.mode == 1:  # max heap
            while (parent_node_index >= 0) and (
                self.result[current_node_index]["number_of_students"]
                > self.result[parent_node_index]["number_of_students"]
            ):
                self.swap(current_node_index, parent_node_index)
                # 繼續往上層比較
                current_node_index = parent_node_index
                parent_node_index = int((current_node_index - 1) / 2)

        elif self.mode == 2:  # min heap
            while (parent_node_index >= 0) and (
                self.result[current_node_index]["number_of_students"]
                < self.result[parent_node_index]["number_of_students"]
            ):
                self.swap(current_node_index, parent_node_index)
                # 繼續往上層比較
                current_node_index = parent_node_index
                parent_node_index = int((current_node_index - 1) / 2)

    def push(self, data):
        self.result.append(data)
        size = len(self.result)

        if size < 2:
            return

        self.heap()


class School:
    def __init__(self, data) -> None:
        self.serial_number = data[0]
        self.number = data[1]
        self.name = data[2]
        self.department_number = data[3]
        self.department_name = data[4]
        self.day_or_night = data[5]
        self.degree = data[6]
        self.number_of_students = data[7]
        self.number_of_teachers = data[8]
        self.number_of_graduates_in_the_last_year = data[9]
        self.county = data[10]
        self.system_type = data[11]


class Main:
    def __init__(self, file_number, mode) -> None:
        self.mode = mode
        self.file_number = file_number
        self.files = [f"input10{i}.txt" for i in range(1, 3)]
        self.input101 = []
        self.input102 = []
        self.remove_special_characters()
        self.add_serial_number()
        self.read_file()
        # Max heap or Min heap
        self.heap()
        # min max heap
        if self.mode == 3:
            self.min_max_heap()

    def read_file(self):
        for i, val in enumerate(self.files):
            with open(val, "r", encoding="utf-8") as f_r:
                data = f_r.read().splitlines(True)
                data.pop(0)

                for j in range(len(data)):
                    data[j] = data[j].split("\t")
                for k in range(len(data)):
                    data[k][11] = data[k][11].replace("\n", "")  # 刪除最後一個換行符
                    school = School(data[k])
                    if i == 0:
                        self.input101.append(school.__dict__)
                    elif i == 1:
                        self.input102.append(school.__dict__)

    def add_serial_number(self):
        number_of_attributes = []  # 紀錄兩個.txt檔案添加序號總共有多少個屬性(未添加序號: 11個)

        for index, val in enumerate(self.files):
            with open(val, "r", encoding="utf-8") as f_r:
                data = f_r.readlines()
                header = data.pop(0)
                number_of_attributes.append(len(data[0].split("\t")))

                if number_of_attributes[index] < 12:
                    print("添加序號")
                    for i in range(len(data)):
                        data[i] = data[i].split("\n")
                        data[i] = f"{i+1}\t" + data[i][0]
                        data[i] = data[i] + "\n"

                    data.insert(0, header)

                    with open(val, "w", encoding="utf-8") as f_w:
                        print("序號寫入")
                        f_w.writelines(data)

    def remove_special_characters(self):
        for i in self.files:
            with open(i, "r", encoding="utf-8") as f_r:
                data = f_r.read().splitlines(True)
                data[0] = "".join(s for s in data[0] if s.isalnum())  # 去除特殊字元
                data[1] = "".join(s for s in data[1] if s.isalnum())
            if data[0] == "大專校院各校科系別概況" and data[1] == "105學年度SY20162017":
                print("Delete the first 2 lines")
                with open(i, "w", encoding="utf-8") as f_w:
                    f_w.writelines(data[2:])

    def heap(self):
        """
        test = [{'serial_number': 1, 'number_of_students': 3},
                {'serial_number': 2, 'number_of_students': 2}, {
                    'serial_number': 3, 'number_of_students': 1},
                {'serial_number': 4, 'number_of_students': 5}, {'serial_number': 5, 'number_of_students': 4}]
        """
        temp = []  # 用來儲存只有序號與學生數的物件
        # 只要序號與學生數
        if self.file_number == 101:
            for i in range(len(self.input101)):
                temp.append(
                    dict(
                        [
                            ("serial_number", self.input101[i]["serial_number"]),
                            (
                                "number_of_students",
                                self.input101[i]["number_of_students"],
                            ),
                        ]
                    )
                )
            # 字串轉整數型別
            for i, val in enumerate(temp):
                temp[i]["serial_number"] = int(temp[i]["serial_number"])
                temp[i]["number_of_students"] = int(temp[i]["number_of_students"])

        elif self.file_number == 102:
            for i in range(len(self.input102)):
                temp.append(
                    dict(
                        [
                            ("serial_number", self.input102[i]["serial_number"]),
                            (
                                "number_of_students",
                                self.input102[i]["number_of_students"],
                            ),
                        ]
                    )
                )
            # 字串轉整數型別
            for i, val in enumerate(temp):
                temp[i]["serial_number"] = int(temp[i]["serial_number"])
                temp[i]["number_of_students"] = int(temp[i]["number_of_students"])

        heap = Heap(self.mode)
        # min_heap = Min_Heap()
        # print(temp)
        for i in temp:
            heap.push(i)

        """
        for i in test:
            heap.push(i)
        """
        heap.display()

    def min_max_heap():
        min_max_heap = Min_Max_Heap()
        test = [
            {"serial_number": 1, "number_of_students": 45},
            {"serial_number": 2, "number_of_students": 40},
            {"serial_number": 3, "number_of_students": 19},
            {"serial_number": 4, "number_of_students": 5},
            {"serial_number": 5, "number_of_students": 10},
            {"serial_number": 6, "number_of_students": 50},
            {"serial_number": 7, "number_of_students": 34},
            {"serial_number": 8, "number_of_students": 13},
            {"serial_number": 9, "number_of_students": 28},
            {"serial_number": 10, "number_of_students": 31},
            {"serial_number": 11, "number_of_students": 18},
            {"serial_number": 12, "number_of_students": 32},
            {"serial_number": 13, "number_of_students": 15},
        ]
        for i in test:
            min_max_heap.push(i)


if __name__ == "__main__":
    heap_construction = int(
        input(
            "0. quit\n1. Build a max heap\n2. Build a min heap\n3. Build a min max heap"
        )
    )
    file_number = int(input("Input a file number: (101 or 102)\n"))

    if heap_construction == 0 or file_number != 101 and file_number != 102:
        sys.exit("quit")
    elif heap_construction != 0:
        main = Main(file_number, heap_construction)
