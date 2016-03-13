

class Calculator:
    def sum(self,string):
        if string == '':
            return 0
        elif ',' in string:
            numbers = string.split(',')
            total = 0
            for num in numbers:
                total = total + int(num)
            return total
        else:
            return int(string)

