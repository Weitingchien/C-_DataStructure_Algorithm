class Main:
    def __init__(self) -> None:
        self.files = [f'input10{i+1}.txt' for i in range(2)]
        self.remove_special_characters()
        self.add_serial_number()

    def add_serial_number(self):
        for i, val in enumerate(self.files):
            with open(val, 'r', encoding='utf-8') as f_r:
                data = f_r.readlines()
                header = data.pop(0)
                for i in range(len(data)):
                    data[i] = data[i].split('\n')
                    data[i] = f'{i+1}\t' + data[i][0]
                    data[i] = data[i] + '\n'

                data.insert(0, header)

            with open(val, 'w', encoding='utf-8') as f_w:
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

    def max_heap():
        pass


if __name__ == '__main__':
    main = Main()
