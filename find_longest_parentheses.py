class LongestValidParentheses(object):
    def longest_valid_parentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_open = self.find_first(s)
        last_close = self.find_last(s)
        s = s[first_open:last_close+1]
        is_valid = self.validate_str(s)
        while is_valid != 0:
            if is_valid > 0:
                first_open = self.find_first(s, occurence=2)
                s = s[first_open:]
            else:
                last_close = self.find_last(s, occurence=2)
                s = s[:last_close+1]
            is_valid = self.validate_str(s)
        return s

    def find_first(self, x, occurence = 1):
        found = 0
        for i in range(len(x)):
            if x[i] == '(':
                found += 1
                if found == occurence:
                    return i

    def find_last(self, x, occurence = 1):
        found = 0
        for i in range(len(x) - 1, 0, -1):
            if x[i] == ')':
                found += 1
                if found == occurence:
                    return i

    def validate_str(self, x):
        valid_prace = 0
        for i in x:
            if i == '(':
                valid_prace += 1
            elif i == ')':
                valid_prace -= 1
            if valid_prace < 0:
                return valid_prace
        return valid_prace

# x=LongestValidParentheses()
# print(x.longest_valid_parentheses('(()))'))
# (())
# print(x.longest_valid_parentheses(')()())'))
# ()()
