

class Calculator:
    def sum(self,string):
        if string == '':
            return 0
        elif ',' in string or ':' in string or '&' in string:
            string = string.replace(':',',')
            string = string.replace('&',',')
            numbers = string.split(',')
            total = 0
            for num in numbers:
                total = total + int(num)
            return total
        else:
            return int(string)

