#!/usr/bin/python -u

class KeyConverter:

    def xkeycodes(self):
        return{
            24:"q",
            25:"w",
            26:"e",
            27:"r",
            28:"t",
            29:"y",
            30:"u",
            31:"i",
            32:"o",
            33:"p",
            38:"a",
            39:"s",
            40:"d",
            41:"f",
            42:"g",
            43:"h",
            44:"j",
            45:"k",
            46:"l",
            52:"z",
            53:"x",
            54:"c",
            55:"v",
            56:"b",
            57:"n",
            58:"m",
    }
    
    def convert(self, value):
        keycodes = self.xkeycodes()
        if value in keycodes:
            return keycodes[value]
        else:
            return None

import sys

def main():
    for x in iter(sys.stdin.readline, ""):
        print KeyConverter().convert(int(x.split("\\x")[2], 16))

if __name__ == "__main__":
    main()
