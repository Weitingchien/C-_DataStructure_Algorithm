class School:
    def __init__(self, number, name, department_number, department_name, day_or_night, degree, number_of_students, number_of_teachers, number_of_graduates_in_the_last_year, county, system_type) -> None:
        self.number = number
        self.name = name
        self.department_number = department_number
        self.department_name = department_name
        self.day_or_night = day_or_night
        self.degree = degree
        self.number_of_students = number_of_students
        self.number_of_teachers = number_of_teachers
        self.number_of_graduates_in_the_last_year = number_of_graduates_in_the_last_year
        self.county = county
        self.system_type = system_type

    def __repr__(self) -> str:
        return f'學校代碼: {self.number} 學校名稱: {self.name} 科系代碼: {self.department_number} 科系名稱: {self.department_name} 日間∕進修別:{self.day_or_night} 等級別: {self.degree} 學生數: {self.number_of_students} 教師數: {self.number_of_teachers} 上學年度畢業生數: {self.number_of_graduates_in_the_last_year} 縣市名稱: {self.county} 體系別: {self.system_type}'


class Main:
    def __init__(self) -> None:
        self.files = [f'input00{i+1}.txt' for i in range(3)]
        self.remove_special_characters()
        self.input001 = []
        self.input002 = []
        self.input003 = []
        self.read_file()

    def read_file(self):
        for i, val in enumerate(self.files):
            with open(val, 'r', encoding='utf-8') as f_r:
                if i == 0:
                    data = f_r.read().splitlines(True)
                    data.pop(0)

                    for j in range(len(data)):
                        data[j] = data[j].split('\t')  # 指定\t為分隔符，並且它會回傳list
                    for k in range(len(data)):
                        data[k][10] = data[k][10].replace(
                            '\n', '')  # 刪除最後一個換行符
                    # test
                    school = School(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
                    print(school)

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

    def insertion_sort(self):
        pass


if __name__ == '__main__':
    main = Main()
