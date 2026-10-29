#!/usr/bin/env python3

import sys

words = sys.argv[1:]

if not words:
    print("none")
else:
    for word in words:
        if not word.endswith("ism"):
            print(word + "ism")