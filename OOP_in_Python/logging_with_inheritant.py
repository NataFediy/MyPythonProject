import time


class WriteFile(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_line(self, text):
        fh = open(self.file_name, 'a')
        fh.write(text + '\n')
        fh.close()


class LogFile(WriteFile):
    def write(self, this_line):
        date_str = time.strftime('%a %b %d %H:%M:%S %Y')
        self.write_line('{0}   {1}'.format(date_str, this_line))


class DelimFile(WriteFile):
    def __init__(self, file_name, delim):
        super(DelimFile, self).__init__(file_name)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)


log = LogFile('log.txt')
# mydelim = DelimFile('data.csv', ',')
log.write('this is alog  message')
log.write('this is another message')
# mydelim.write(['a', 'b', 'c', 'd'])
# mydelim.write(['1', '2', '3', '4'])
log.write('Next message')
