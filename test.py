class WriteNumbersInFile():
    def __init__(self):
        self.name_file = 'New_words.txt'
        self.i = 0
        self.b = 1000
        #b = how much you want make?
        self.a = '. '
        self.answer = str(self.i + self.a)

    def make_numbers(self):
        while self.i < self.b:
            self.i += 1
            print(self.answer)

        def to_write_in_file(self):
            with open(self.name_file, a, encoding='UTF-8') as file_object:
                file_object.write(answer)
