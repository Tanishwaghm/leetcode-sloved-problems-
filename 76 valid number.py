class Solution(object):
    def isNumber(self, s):

        s = s.strip()

        num_seen = False
        num_after_e = True
        dot_seen = False
        e_seen = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                num_seen = True
                num_after_e = True

            elif ch in ['+', '-']:
                # sign only allowed at start or after e
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            elif ch == '.':
                # dot not allowed after e or second time
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            elif ch in ['e', 'E']:
                # must have number before e
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False

            else:
                return False

        return num_seen and num_after_e
