# import pprint
# d={i:chr(i) for i in range(1000+1)}
# pprint.pprint(d)

# open(r"D:\file_test.txt", "r+")
#
# print()
#
# f.tell()
# f.write("\n")
# f.seek(0)
# f.read()
# f.close()

import string
import pprint

with open(r"D:\hhgttg.txt", "r+") as f:
    content = f.read().lower()

with open(r"D:\stop2.txt", "r+") as w:
    stop_list = w.read().lower()



list_word = content.split()

word_stats = {}
for word in list_word:
    word = word.strip(string.punctuation)
    if word:
        if word in word_stats:
            word_stats[word] += 1
        else:
            word_stats[word] =1

#pprint.pprint(word_stats)

sorted(word_stats, key=word_stats.get, reverse=True)
pprint.pprint(word_stats)
