import sys


class Heap:
    def __init__(self, mode) -> None:
        self.mode = mode
        self.result = []
        # self.current_index = 0

    def display(self):
        print(
            f"root: serial_number: {self.result[0]['serial_number']} number_of_graduates_in_the_last_year: {self.result[0]['number_of_graduates_in_the_last_year']}"
        )

        temp = []  # 儲存所有節點的學生數
        left_parent_node_index = []
        common_difference = 2
        bottom = 0

        # bottom
        for i in range(len(self.result)):
            temp.append(self.result[i]["number_of_graduates_in_the_last_year"])
            if i == len(self.result) - 1:
                bottom = self.result[i]

                print(
                    f"bottom: serial_number: {bottom['serial_number']} number_of_graduates_in_the_last_year: {bottom['number_of_graduates_in_the_last_year']}"
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
                # print(f"left_parent_node_index: {left_parent_node_index}")
                if left_parent_node_index[i] > len(self.result) - 1:
                    left_parent_node_index.pop()
                    # print(f"left_parent_node_index.pop(): {left_parent_node_index}")
                    break

        print(
            f"leftmost bottom: serial_number: {self.result[left_parent_node_index[len(left_parent_node_index)-1]]['serial_number']} number_of_graduates_in_the_last_year: {self.result[left_parent_node_index[len(left_parent_node_index)-1]]['number_of_graduates_in_the_last_year']}"
        )

        # Max heap , Min heap, Min_Max heap
        if self.mode == 1:
            print(f"Max heap: {temp}")
        elif self.mode == 2:
            print(f"Min heap: {temp}")
        elif self.mode == 3:
            print(f"Min_Max heap: {temp}")

    def swap(self, current_node_index, parent_node_index):
        temp = self.result[current_node_index]
        self.result[current_node_index] = self.result[parent_node_index]
        self.result[parent_node_index] = temp

    def heap(self):
        current_node_index = len(self.result) - 1
        parent_node_index = int((current_node_index - 1) / 2)

        if self.mode == 1:  # max heap
            while (parent_node_index >= 0) and (
                self.result[current_node_index]["number_of_graduates_in_the_last_year"]
                > self.result[parent_node_index]["number_of_graduates_in_the_last_year"]
            ):
                self.swap(current_node_index, parent_node_index)
                # 繼續往上層比較
                current_node_index = parent_node_index
                parent_node_index = int((current_node_index - 1) / 2)

        elif self.mode == 2:  # min heap
            while (parent_node_index >= 0) and (
                self.result[current_node_index]["number_of_graduates_in_the_last_year"]
                < self.result[parent_node_index]["number_of_graduates_in_the_last_year"]
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


class Min_Max_Heap(Heap):
    def __init__(self, mode) -> None:
        super().__init__(mode)
        self.current_level = 0

    def reheap(self, parent_node_index, current_node_index):
        grandparent_node_index = int((parent_node_index - 1) / 2)
        if grandparent_node_index < 0:
            return
        if (
            self.result[current_node_index]["number_of_graduates_in_the_last_year"]
            < self.result[grandparent_node_index][
                "number_of_graduates_in_the_last_year"
            ]
        ):
            print(
                f"(reheap) current_node_index: {current_node_index} grandparent_node_index: {grandparent_node_index}"
            )
            self.swap(current_node_index, grandparent_node_index)
            current_node_index = grandparent_node_index
            grandparent_node_index = int((grandparent_node_index) - 1 / 2)
            self.reheap(grandparent_node_index, current_node_index)

    def is_max_level(self, current_node_index):
        self.current_level = 0  # 初始化，避免重複新增時累加
        while current_node_index > 0:
            current_node_index = int((current_node_index - 1) / 2)
            self.current_level += 1
        return self.current_level % 2 != 0

    def min_max_heap(self, size):
        current_node_index = size - 1
        is_max_level = self.is_max_level(current_node_index)
        parent_node_index = int((current_node_index - 1) / 2)

        if (is_max_level) and self.result[current_node_index][
            "number_of_graduates_in_the_last_year"
        ] < self.result[parent_node_index]["number_of_graduates_in_the_last_year"]:
            print("Max level:當前節點小於父節點")
            print(
                f"current_node_index: {current_node_index} -> current_node: {self.result[current_node_index]['number_of_graduates_in_the_last_year']}, parent_node_index: {parent_node_index} parent_node: {self.result[parent_node_index]['number_of_graduates_in_the_last_year']}"
            )
            # print(f"current_node_index: {current_node_index}")
            self.swap(current_node_index, parent_node_index)
            current_node_index = parent_node_index
            parent_node_index = int((parent_node_index - 1) / 2)
            self.reheap(parent_node_index, current_node_index)

        elif (
            not is_max_level
            and self.result[current_node_index]["number_of_graduates_in_the_last_year"]
            > self.result[parent_node_index]["number_of_graduates_in_the_last_year"]
        ):
            print("Min level:當前節點大於父節點")
            print(
                f"current_node_index: {current_node_index} -> current_node: {self.result[current_node_index]['number_of_graduates_in_the_last_year']}, parent_node_index: {parent_node_index} parent_node: {self.result[parent_node_index]['number_of_graduates_in_the_last_year']}"
            )
            self.swap(current_node_index, parent_node_index)
            parent_node_index = int((current_node_index - 1) / 2)
            self.reheap(parent_node_index, current_node_index)
        """
        elif (
            not is_max_level
            and self.result[current_node_index]["number_of_graduates_in_the_last_year"]
            < self.result[parent_node_index]["number_of_graduates_in_the_last_year"]
        ):
            print(
                "Min level:當前節點小於父節點(進一步檢查是否小於祖父節點)"
            )  # 小於父節點不需要交換，但是要進一步判斷是否小於祖父節點，如果比祖父節點小就需要跟祖父節點作交換
            parent_node_index = int((parent_node_index - 1) / 2)
            self.reheap(parent_node_index, current_node_index)
        """

    def push(self, el):
        self.result.append(el)

        size = len(self.result)

        if size < 2:
            return

        self.min_max_heap(size)


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
        self.temp = self.input_filter()

        if self.mode != 3:
            self.heap()
        elif self.mode == 3:
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

    def input_filter(self):
        temp = []  # 用來儲存只有序號與學生數的物件
        # 只要序號與學生數
        if self.file_number == 101:
            for i in range(len(self.input101)):
                temp.append(
                    dict(
                        [
                            ("serial_number", self.input101[i]["serial_number"]),
                            (
                                "number_of_graduates_in_the_last_year",
                                self.input101[i][
                                    "number_of_graduates_in_the_last_year"
                                ],
                            ),
                        ]
                    )
                )

            # 字串轉整數型別
            for i, val in enumerate(temp):
                temp[i]["serial_number"] = int(temp[i]["serial_number"])
                temp[i]["number_of_graduates_in_the_last_year"] = int(
                    temp[i]["number_of_graduates_in_the_last_year"]
                )

        elif self.file_number == 102:
            for i in range(len(self.input102)):
                temp.append(
                    dict(
                        [
                            ("serial_number", self.input102[i]["serial_number"]),
                            (
                                "number_of_graduates_in_the_last_year",
                                self.input102[i][
                                    "number_of_graduates_in_the_last_year"
                                ],
                            ),
                        ]
                    )
                )
            # 字串轉整數型別
            for i, val in enumerate(temp):
                temp[i]["serial_number"] = int(temp[i]["serial_number"])
                temp[i]["number_of_graduates_in_the_last_year"] = int(
                    temp[i]["number_of_graduates_in_the_last_year"]
                )

        print(temp)
        return temp

    def heap(self):
        """
        test = [{'serial_number': 1, 'number_of_graduates_in_the_last_year': 3},
                {'serial_number': 2, 'number_of_graduates_in_the_last_year': 2}, {
                    'serial_number': 3, 'number_of_graduates_in_the_last_year': 1},
                {'serial_number': 4, 'number_of_graduates_in_the_last_year': 5}, {'serial_number': 5, 'number_of_graduates_in_the_last_year': 4}]
        for i in test:
            heap.push(i)
        """

        heap = Heap(self.mode)

        for i in self.temp:
            heap.push(i)

        heap.display()

    def min_max_heap(self):
        min_max_heap = Min_Max_Heap(self.mode)

        test = [
            {"serial_number": 1, "number_of_graduates_in_the_last_year": 18},
            {"serial_number": 2, "number_of_graduates_in_the_last_year": 5},
            {"serial_number": 3, "number_of_graduates_in_the_last_year": 14},
            {"serial_number": 4, "number_of_graduates_in_the_last_year": 20},
            {"serial_number": 5, "number_of_graduates_in_the_last_year": 45},
            {"serial_number": 6, "number_of_graduates_in_the_last_year": 33},
            {"serial_number": 7, "number_of_graduates_in_the_last_year": 8},
            {"serial_number": 7, "number_of_graduates_in_the_last_year": 11},
            {"serial_number": 7, "number_of_graduates_in_the_last_year": 1},
        ]
        for i in test:
            min_max_heap.push(i)

        """
        for i in self.temp:
            min_max_heap.push(i)
        """

        min_max_heap.display()


if __name__ == "__main__":
    heap_construction = int(
        input(
            "0. quit\n1. Build a max heap\n2. Build a min heap\n3. Build a min max heap\n"
        )
    )
    file_number = int(input("Input a file number: (101 or 102)\n"))

    if heap_construction == 0 or file_number != 101 and file_number != 102:
        sys.exit("quit")
    elif heap_construction != 0:
        main = Main(file_number, heap_construction)
