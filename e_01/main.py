import pandas as pd





class main:
    def __init__(self) -> None:
        self.remove_text()
        first_text_file = pd.read_csv('input001.txt', sep="\t")
        print(first_text_file)
        #print(first_text_file.iloc[1: , :])
    
    def remove_text(self):
        files = [f'input00{i+1}.txt' for i in range(3)]
        for i in files:
            with open(i, 'r', encoding='utf-8') as f_r:
                data = f_r.read().splitlines(True)
                data[0] = ''.join(s for s in data[0] if s.isalnum())
                print(repr(data[0]))
    
        




if __name__ == '__main__':
    main = main()
    # print(main)