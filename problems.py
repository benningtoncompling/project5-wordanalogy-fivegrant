class Problem:
    def __init__(self, elements):
        self.base_pair = (elements[0], elements[1])
        try:
            self.sec_pair = (elements[2], elements[3])
        except:
            self.sec_pair = [elements[2], None]

    def __eq__(self, compare):
        return self.base_pair == compare.base_pair and \
         self.sec_pair == compare.sec_pair

    def __lt__(self, compare):
        return self.sec_pair[1] == None and compare.sec_pair[1] != None

    def __str__(self):
        return " ".join([
         str(self.base_pair[0]), str(self.base_pair[1]), 
         str(self.sec_pair[0]), str(self.sec_pair[1])]) + '\n'

    def quick_check(self, compare):
        return self.sec_pair[1] == compare.sec_pair[1]

    def blind(self):
        return Problem([self.base_pair[0], self.base_pair[1], self.sec_pair[0]])

    def solve(self, solution):
        self.sec_pair = (self.sec_pair[0], solution)

