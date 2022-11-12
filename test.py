class WriteNumbersInFile:
    def __init__(self):
        self.name_file = 'E:/useful/English/New_words.txt'
        self.i = 0
        self.b = 1000
        #b = how much you want make?
        self.a = f'{self.i}. '
        # а = in what form will the numbers be made

    def to_write_in_file(self):
        with open(self.name_file, w, encoding='UTF-8') as file_object:
            while self.i < self.b:
                self.i += 1
                print(self.a)
                file_object.write(self.a)
