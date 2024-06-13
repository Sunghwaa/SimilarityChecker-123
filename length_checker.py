class LengthChecker:
    def check(self, str1, str2):
        if len(str1) >= len(str2) * 2 or len(str1) * 2 <= len(str2):
            return 0
