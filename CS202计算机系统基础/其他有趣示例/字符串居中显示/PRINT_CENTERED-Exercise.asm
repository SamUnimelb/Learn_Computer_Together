.ORIG x3000
LEA R1 STARTSTR	;This is given by your question
		;That the start of the str's memory
		;is in R1. Use R1 as the address number.
AND R2 R2 0	;R2 used to store the length of the str
AND R4 R4 0
ADD R4 R4 R1	;Store the original address being loaded to R1.
AND R0 R0 0	;Clean output.
ADD R0 R0 15
ADD R0 R0 15
ADD R0 R0 2	;Got a space.
	
CHECKLEN    ADD R2 R2 1
	    ADD R1 R1 1
            LDR R3 R1 0	;R3 to store and check the content of R1.
	    BRp CHECKLEN ;When sth. positive loaded to R3, the str is not ended.

ADD R2 R2 -4
BRz £¿£¿£¿£¿	
BRn £¿£¿£¿£¿

AND R2 R2 0	;R2 is useless in this case and can be recollected.
ADD R2 R2 ?

PRINTLONGSTR	????  ;There are 4 lines of codes here,
		????  ;and please simulate PRINTSTR to finish.
		????
		????
BRzp	PRINTLONGSTR
BRnzp	???

TWOSPACE PUTC
         PUTC
BRnzp PRINTSTR		

ONESPACE	PUTC
BRnzp	PRINTSTR

PRINTSTR	LDR R0 R4 0;
		PUTC
		ADD R4 R4 1
BRp	PRINTSTR
EOP HALT
STARTSTR .STRINGZ "hhHh" ;Test string can be entered here.
.END