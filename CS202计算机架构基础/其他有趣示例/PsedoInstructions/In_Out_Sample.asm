.ORIG x3000
LEA R1 MYSTRING ; R1 for storing the address of the input char.
LOOP	GETC
	PUTC
	STR R0 R1 0
	ADD R1 R1 1
	ADD R0 R0 -10
BRp LOOP
LEA R1 MYSTRING
PRINT	LDR R0 R1 0
	PUTC
	ADD R1 R1 1
	ADD R0 R0 0
BRp PRINT

MYSTRING .BLKW 1
.END
