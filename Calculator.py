AMPERSAND = '&'
TWO_POINTS = ':'
COMMA = ','
EMPTY_STRING = ''


class Calculator:
    def sum(self,string):
        if string == EMPTY_STRING:
            return 0
        elif COMMA in string or TWO_POINTS in string or AMPERSAND in string:
            string = string.replace(TWO_POINTS, COMMA)
            string = string.replace(AMPERSAND, COMMA)
            numbers = string.split(COMMA)
            total = 0
            for num in numbers:
                total = total + int(num)
            return total
        else:
            return int(string)

