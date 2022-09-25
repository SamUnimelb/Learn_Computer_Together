.ORIG x3000
LEA R1 STARTSTR	;This is given by your question
		;That the start of the str's memory
		;is in R1. Use R1 as the address number.
ST R0 R0ORIGVAL
AND R7 R7 0
ADD R7 R7 15
ADD R7 R7 15
ADD R7 R7 15 ;For testing, change this number to 2 for printing real space.
ST R7 SPACEASCII

AND R7 R7 0
ADD R7 R7 6
ST R7 SCREENLEN

AND R7 R7 0 ;Prepare for counting length of the str.

COUNTSTRLEN	ADD R7 R7 1
		ADD R1 R1 1
		LDR R0 R1 0
BRp	COUNTSTRLEN
ST R7 STRLEN
ADD R7 R7 -6
BRzp	FIRSTSIX ;Str len >= 6, just print the first six and finish.

LD R7 STRLEN
ADD R7 R7 -5
BRz	FIRSTFIVE ;Str len == 5, just print the str with one space and finish.

LD R7 STRLEN
ADD R7 R7 -4
BRz	PRT4 ;Str len == 4, just print the str with 1 space + str + 1 space and finish.

LD R7 STRLEN
ADD R7 R7 -3
BRnz	PRLE3 ;Str len <= 3, just print the str with 2 spaces + str + the rest.

FIRSTSIX LEA R1 STARTSTR
OUTREST6  LDR R0 R1 0
	  PUTC
          LEA R7 STARTSTR
	  ADD R7 R7 6
          ADD R1 R1 1
	  NOT R7 R7
	  ADD R7 R7 1
          ADD R7 R1 R7
BRn	OUTREST6
BRnzp   FINISH

FIRSTFIVE LEA R1 STARTSTR
OUTREST5  LDR R0 R1 0
	  PUTC
          LEA R7 STARTSTR
	  ADD R7 R7 5
          ADD R1 R1 1
	  NOT R7 R7
	  ADD R7 R7 1
          ADD R7 R1 R7
BRn	  OUTREST5
LD R0 SPACEASCII
PUTC
BRnzp FINISH   

PRT4	  LD R0 SPACEASCII
          PUTC
	  LEA R1 STARTSTR
OUTREST4  LDR R0 R1 0
	  PUTC
          LEA R7 STARTSTR
	  ADD R7 R7 5
          ADD R1 R1 1
	  NOT R7 R7
	  ADD R7 R7 1
          ADD R7 R1 R7
BRn	  OUTREST4
LD R0 SPACEASCII
PUTC
BRnzp FINISH   

PRLE3	  LD R0 SPACEASCII
          PUTC
	  PUTC
	  LEA R1 STARTSTR
	  AND R7 R7 0 ;R7 for # of spaces.
	  LD R7 STRLEN
	  NOT R7 R7
	  ADD R7 R7 1
	  ADD R7 R7 4
	  ST R7 ENDSPACECT
          LDR R0 R1 0
OUTREST3  PUTC
          ADD R1 R1 1
          LDR R0 R1 0
	  BRp OUTREST3

LD R0 SPACEASCII	;Just print out the remaining space
LD R7 ENDSPACECT
AND R1 R1 0
ADD R1 R1 R7

REMSPACE PUTC
	 ADD R1 R1 -1
BRp REMSPACE

FINISH    LD R0 R0ORIGVAL
	  LEA R1 STARTSTR
          HALT

R0ORIGVAL .BLKW 1
ENDSPACECT .BLKW 1
STRLEN .BLKW 1
SPACEASCII .BLKW 1
SCREENLEN .BLKW 1
STARTSTR .STRINGZ "hhHHhHH"
.END