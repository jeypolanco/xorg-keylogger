
#!/bin/bash

pid=$1

strace -s 1000 -xx -p $pid -e trace=recvfrom |&
grep --line-buffered -o '.*32$'              |
grep -o '\".*\"'                             |
sed 's/\"//g'                                |
grep --line-buffered "^.x03"                 |
./xkyc2char.py                               ;
