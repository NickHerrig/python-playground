import sys
import re
import collections


if __name__=="__main__":
    WORD_RE = re.compile(r'\w+')

    dd = collections.defaultdict(list)
    nd = {}

    with open(sys.argv[1], encoding='utf-8') as f:
        for line_no, line in enumerate(f, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                nd.setdefault(word, []).append(location)
                dd[word].append(location)

        print(dd)
        print(nd)
