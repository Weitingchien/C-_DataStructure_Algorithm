import pandas as pd


class main:
    def __init__(self) -> None:
        self.remove_text()
        first_text_file = pd.read_csv('input001.txt', sep="\t")
        print(first_text_file)

    def remove_text(self):
        files = [f'input00{i+1}.txt' for i in range(3)]
        for i in files:
            with open(i, 'r', encoding='utf-8') as f_r:
                data = f_r.read().splitlines(True)
                data[0] = ''.join(s for s in data[0] if s.isalnum())  # 去除特殊字元
                data[1] = ''.join(s for s in data[1] if s.isalnum())
            if(data[0] == '大專校院各校科系別概況' and data[1] == '105學年度SY20162017'):
                print('Delete the first 2 lines')
                with open(i, 'w', encoding='utf-8') as f_w:
                    f_w.writelines(data[2:])


if __name__ == '__main__':
    main = main()
    # print(main)
