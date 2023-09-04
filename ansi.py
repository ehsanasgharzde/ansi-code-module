class fg:
    def __init__(self):
        self.black = '\033[30m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.orange = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[35m'
        self.cyan = '\033[36m'
        self.lightgrey = '\033[37m'
        self.darkgrey = '\033[90m'
        self.lightred = '\033[91m'
        self.lightgreen = '\033[92m'
        self.yellow = '\033[93m'
        self.lightblue = '\033[94m'
        self.pink = '\033[95m'
        self.lightcyan = '\033[96m'
 
class bg:
    def __init__(self):
        self.black = '\033[40m'
        self.red = '\033[41m'
        self.green = '\033[42m'
        self.orange = '\033[43m'
        self.blue = '\033[44m'
        self.purple = '\033[45m'
        self.cyan = '\033[46m'
        self.lightgrey = '\033[47m'

class style:
    def __init__(self):
        self.reset = '\033[0m'
        self.bold = '\033[01m'
        self.disable = '\033[02m'
        self.underline = '\033[04m'
        self.reverse = '\033[07m'
        self.strikethrough = '\033[09m'
        self.invisible = '\033[08m'