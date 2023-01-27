import time
import random


class School:
    def __init__(self, data) -> None:
        self.number = data[0]
        self.name = data[1]
        self.department_number = data[2]
        self.department_name = data[3]
        self.day_or_night = data[4]
        self.degree = data[5]
        self.number_of_students = data[6]
        self.number_of_teachers = data[7]
        self.number_of_graduates_in_the_last_year = data[8]
        self.county = data[9]
        self.system_type = data[10]
    """
    def __repr__(self):
        return {'學校代碼': self.number, '學校名稱': self.name, '科系代碼': self.department_number, '科系名稱': self.department_name, '日間∕進修別': self.day_or_night, '等級別': self.degree, '學生數': self.number_of_students, '教師數': self.number_of_teachers, '上學年度畢業生數': self.number_of_graduates_in_the_last_year, '縣市名稱': self.county, '體系別': self.system_type}
    """


class Main:
    def __init__(self) -> None:
        self.files = [f'input00{i+1}.txt' for i in range(3)]
        self.remove_special_characters()
        self.input001 = []
        self.input002 = []
        self.input003 = []
        self.input001_average_execution_time = []
        self.input002_average_execution_time = []
        self.input003_average_execution_time = []
        self.read_file()
        self.convert_string_to_int()
        # ---------------------- test ----------------------
        self.list_A = []
        self.generate_a_list_of_random_numbers()
        self.convert_string_to_int()
        # ---------------------- test ----------------------

    def convert_string_to_int(self):
        for a in range(len(self.input001)):
            self.input001[a]['number_of_graduates_in_the_last_year'] = int(
                self.input001[a]['number_of_graduates_in_the_last_year'])
        for b in range(len(self.input002)):
            self.input002[b]['number_of_graduates_in_the_last_year'] = int(
                self.input002[b]['number_of_graduates_in_the_last_year'])
        for c in range(len(self.input003)):
            self.input003[c]['number_of_graduates_in_the_last_year'] = int(
                self.input003[c]['number_of_graduates_in_the_last_year'])

    def read_file(self):
        for i, val in enumerate(self.files):
            with open(val, 'r', encoding='utf-8') as f_r:
                data = f_r.read().splitlines(True)
                data.pop(0)

                for j in range(len(data)):
                    data[j] = data[j].split('\t')  # 指定\t為分隔符，並且它會回傳list
                for k in range(len(data)):
                    data[k][10] = data[k][10].replace('\n', '')  # 刪除最後一個換行符
                    school = School(data[k])
                    if i == 0:
                        self.input001.append(school.__dict__)
                    elif i == 1:
                        self.input002.append(school.__dict__)
                    elif i == 2:
                        self.input003.append(school.__dict__)

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

    def average_execution_time_insertion_sort(self):
        for i in range(10):
            start = time.time()
            self.insertion_sort(1)
            end = time.time()
            elapsed_time = end-start
            self.input001_average_execution_time.append(elapsed_time)
        for i in range(10):
            start = time.time()
            self.insertion_sort(2)
            end = time.time()
            elapsed_time = end-start
            self.input002_average_execution_time.append(elapsed_time)
        for i in range(10):
            start = time.time()
            self.insertion_sort(3)
            end = time.time()
            elapsed_time = end-start
            self.input003_average_execution_time.append(elapsed_time)
        print('------------------------Insertion sort------------------------------------------------')
        print(
            f'Average execution time of input001.txt: {sum(self.input001_average_execution_time)/10}')
        print(
            f'Average execution time of input002.txt: {sum(self.input002_average_execution_time)/10}')
        print(
            f'Average execution time of input003.txt: {sum(self.input003_average_execution_time)/10}')
        print('--------------------------------------------------------------------------------------')

    def average_execution_time_merge_sort(self):
        for i in range(10):
            start = time.time()
            self.merge_sort(1)
            end = time.time()
            elapsed_time = end-start
            self.input001_average_execution_time.append(elapsed_time)
        for i in range(10):
            start = time.time()
            self.merge_sort(2)
            end = time.time()
            elapsed_time = end-start
            self.input002_average_execution_time.append(elapsed_time)
        for i in range(10):
            start = time.time()
            self.merge_sort(3)
            end = time.time()
            elapsed_time = end-start
            self.input003_average_execution_time.append(elapsed_time)
        print('------------------------Merge sort------------------------------------------------')
        print(
            f'Average execution time of input001.txt: {sum(self.input001_average_execution_time)/10}')
        print(
            f'Average execution time of input002.txt: {sum(self.input002_average_execution_time)/10}')
        print(
            f'Average execution time of input003.txt: {sum(self.input003_average_execution_time)/10}')

    def insertion_sort(self, file):
        if (file == 1):
            for i in range(len(self.input001)-1):
                for j in range(i+1, 0, -1):
                    if(self.input001[j]['number_of_graduates_in_the_last_year'] > self.input001[j-1]['number_of_graduates_in_the_last_year']):
                        temp = self.input001[j-1]
                        self.input001[j-1] = self.input001[j]
                        self.input001[j] = temp
            return self.input001
        elif(file == 2):
            for i in range(len(self.input002)-1):
                for j in range(i+1, 0, -1):
                    if(self.input002[j]['number_of_graduates_in_the_last_year'] > self.input002[j-1]['number_of_graduates_in_the_last_year']):
                        temp = self.input002[j-1]
                        self.input002[j-1] = self.input002[j]
                        self.input002[j] = temp
            return self.input002
        elif(file == 3):
            for i in range(len(self.input003)-1):
                for j in range(i+1, 0, -1):
                    if(self.input003[j]['number_of_graduates_in_the_last_year'] > self.input003[j-1]['number_of_graduates_in_the_last_year']):
                        temp = self.input003[j-1]
                        self.input003[j-1] = self.input003[j]
                        self.input003[j] = temp
            return self.input003

    def merge(self, left, right):
        temp = []
        while(len(left) > 0 and len(right) > 0):
            if(right[0]['number_of_graduates_in_the_last_year'] > left[0]['number_of_graduates_in_the_last_year']):
                temp.append(right.pop(0))
            else:
                temp.append(left.pop(0))

        if (len(left)):
            temp = temp + left
        else:
            temp = temp + right

        return temp

    def merge_sort(self, file):
        if(file == 1):
            if(len(self.input001) < 2):
                return self.input001

            mid = len(self.input001) // 2
            left_array = self.input001[:mid]
            right_array = self.input001[mid:]
            return self.merge(self.merge_sort_test(left_array), self.merge_sort_test(right_array))
        elif(file == 2):
            if(len(self.input002) < 2):
                return self.input002

            mid = len(self.input002) // 2
            left_array = self.input002[:mid]
            right_array = self.input002[mid:]
            return self.merge(self.merge_sort_test(left_array), self.merge_sort_test(right_array))
        elif(file == 3):
            if(len(self.input003) < 2):
                return self.input003

            mid = len(self.input003) // 2
            left_array = self.input003[:mid]
            right_array = self.input003[mid:]
            return self.merge(self.merge_sort_test(left_array), self.merge_sort_test(right_array))

    def generate_a_list_of_random_numbers(self):
        self.list_A = [i for i in range(10000)]
        list_A_random = random.sample(self.list_A, len(self.list_A))
        self.list_A = list_A_random

    def insertion_sort_test(self):
        for i in range(len(self.list_A)-1):
            for j in range(i+1, 0, -1):
                if(self.list_A[j] > self.list_A[j-1]):
                    temp = self.list_A[j-1]
                    self.list_A[j-1] = self.list_A[j]
                    self.list_A[j] = temp
        return self.list_A

    def merge_sort_test(self, array):
        if(len(array) < 2):
            return array

        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        return self.merge(self.merge_sort_test(left_array), self.merge_sort_test(right_array))


if __name__ == '__main__':
    main_insertion_sort = Main()
    main_merge_sort = Main()

    main_insertion_sort.average_execution_time_insertion_sort()
    main_merge_sort.average_execution_time_merge_sort()

    # ---------------------- test ----------------------
    """
    start = time.time()
    print(main.insertion_sort_test())
    end = time.time()
    elapsed_time = end-start
    print(elapsed_time)
    main.merge_sort_test([5, 1, 8, 6, 9])
    """
    # ---------------------- test ----------------------
