import copy  # 用來使用deepcopy函式


class Max_Heap:
    def __init__(self) -> None:
        self.result = []
        self.current_index = 0

    def swap(self, current_node, parent_node):
        temp = self.result[current_node]
        self.result[current_node] = self.result[parent_node]
        self.result[parent_node] = temp

    def max_heap(self):
        current_node = self.current_index - 1

        # 比較每個節點的學生數量，如果還小於上一層parent node，就繼續交換
        for i, val in enumerate(self.result):
            parent_node = round(i // 2) - 1
            # index小於0代表沒有這個parent node 所以要跳過這輪
            if(parent_node < 0):
                continue
            if(self.result[current_node]['number_of_students'] > self.result[parent_node]['number_of_students']):
                self.swap(current_node, parent_node)

        if(len(self.result) == 9):
            print(self.result)

    def push(self, data):
        self.result.append(data)
        self.current_index += 1

        if(len(self.result) < 2):
            return

        self.max_heap()


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
    def __init__(self) -> None:
        self.files = [f'input10{i+1}.txt' for i in range(2)]
        self.input101 = []
        self.input102 = []
        self.remove_special_characters()
        self.add_serial_number()
        self.read_file()
        self.max_heap_test()

    def read_file(self):
        for i, val in enumerate(self.files):
            with open(val, 'r', encoding='utf-8') as f_r:
                data = f_r.read().splitlines(True)
                data.pop(0)

                for j in range(len(data)):
                    data[j] = data[j].split('\t')
                for k in range(len(data)):
                    data[k][11] = data[k][11].replace('\n', '')  # 刪除最後一個換行符
                    school = School(data[k])
                    if i == 0:
                        self.input101.append(school.__dict__)
                    elif i == 1:
                        self.input102.append(school.__dict__)

    def add_serial_number(self):
        number_of_attributes = []  # 紀錄兩個.txt檔案添加序號總共有多少個屬性(未添加序號: 11個)

        for index, val in enumerate(self.files):
            with open(val, 'r', encoding='utf-8') as f_r:
                data = f_r.readlines()
                header = data.pop(0)
                number_of_attributes.append(len(data[0].split('\t')))

                if(number_of_attributes[index] < 12):
                    print('添加序號')
                    for i in range(len(data)):
                        data[i] = data[i].split('\n')
                        data[i] = f'{i+1}\t' + data[i][0]
                        data[i] = data[i] + '\n'

                    data.insert(0, header)

                    with open(val, 'w', encoding='utf-8') as f_w:
                        print('序號寫入')
                        f_w.writelines(data)

    def remove_special_characters(self):
        for i in self.files:
            with open(i, 'r', encoding='utf-8') as f_r:
                data = f_r.read().splitlines(True)
                data[0] = ''.join(s for s in data[0] if s.isalnum())  # 去除特殊字元
                data[1] = ''.join(s for s in data[1] if s.isalnum())
            if(data[0] == '大專校院各校科系別概況' and data[1] == '105學年度SY20162017'):
                print('Delete the first 2 lines')
                with open(i, 'w', encoding='utf-8') as f_w:
                    f_w.writelines(data[2:])

    def max_heap_test(self):
        test = [{'serial_number': 1, 'number_of_students': 20},
                {'serial_number': 2, 'number_of_students': 80}, {
                    'serial_number': 3, 'number_of_students': 50},
                {'serial_number': 4, 'number_of_students': 90}, {'serial_number': 5, 'number_of_students': 70}, {'serial_number': 6, 'number_of_students': 200}, {'serial_number': 7, 'number_of_students': 40}, {'serial_number': 8, 'number_of_students': 10}, {'serial_number': 9, 'number_of_students': 100}]
        temp = []  # 用來儲存只有序號與學生數的物件
        # 只要序號與學生數
        for i in range(len(self.input101)):
            temp.append(dict([('serial_number', self.input101[i]['serial_number']),
                        ('number_of_students', self.input101[i]['number_of_students'])]))
        # 字串轉整數型別
        for i, val in enumerate(temp):
            temp[i]['serial_number'] = int(temp[i]['serial_number'])
            temp[i]['number_of_students'] = int(temp[i]['number_of_students'])

        heap = Max_Heap()
        for i in test:
            heap.push(i)
        # print(temp)


if __name__ == '__main__':
    main = Main()
