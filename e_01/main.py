import pandas as pd

class main:
    def __init__(self) -> None:
        first_text_file = pd.read_csv('input001.txt', sep="\t")
        print(first_text_file)
    pass



if __name__ == '__main__':
    main = main()
    # print(main)