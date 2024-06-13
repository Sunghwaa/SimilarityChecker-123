class LengthChecker:
    def check(self, str1, str2):
        if self.is_length_same(str1, str2):
            return 60

        if self.is_length_diff_more_than_twice(str1, str2):
            return 0

        return self.calc_score(str1, str2)

    def is_length_same(self, str1, str2):
        return len(str1) == len(str2)

    def is_length_diff_more_than_twice(self, str1, str2):
        return len(str1) >= len(str2) * 2 or len(str1) * 2 <= len(str2)

    def calc_score(self, str1, str2):
        return int((1 - (len(str1) - len(str2)) / len(str2)) * 60)
