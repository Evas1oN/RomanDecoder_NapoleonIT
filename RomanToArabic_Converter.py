class Solution:
     def romanToInt(self, s: str) -> int:
        if (len(s) > 15 or len(s) == 0):
            return 'Превышено количество символов (макс. 15) или введена пустая строка'

        romans = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        notValid = {'DD':'M', 'LL':'C', 'VV': 'X'}

        for symbol in s:
            if (symbol not in romans.keys()):
                return 'Неизвестный символ: {0}'.format(symbol)

        counter = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                counter += 1
                if counter >= 3:
                    return 'В римской системе счисление недопустимо повторения одного и того же символа больше 3-х раз подряд.'
            else:
                counter = 0

            pair = s[i] + s[i - 1]
            if pair in notValid.keys():
                return 'Недопустим ввод {0}, используйте {1}'.format(pair, notValid[pair])
            
        result = 0
        prev = 0
        for symbol in reversed(s):
            if prev == 0: 
                result += romans[symbol]
            elif prev > romans[symbol]: 
                result -= romans[symbol]
            else: 
                result += romans[symbol]
            prev = romans[symbol]
        return result

while(True):
    print(Solution.romanToInt(Solution, input('Введите римское число: ')))