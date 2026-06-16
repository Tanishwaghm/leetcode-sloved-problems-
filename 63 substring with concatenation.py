from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_freq = Counter(words)
        result = []

        # try different starting offsets
        for i in range(word_len):

            left = i
            seen = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):

                word = s[j:j + word_len]

                if word in word_freq:

                    seen[word] += 1
                    count += 1

                    # shrink window if word frequency exceeded
                    while seen[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # valid window found
                    if count == word_count:
                        result.append(left)

                        # move left forward to search next match
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result
