//This program is able to perform division
//of any 2 given integers whose absolute value
//ranges from x0 ~ x7FFF.

//The program gets result in R3, reminder in R2.
//The signal of the reminder depends on the nominator.
//e.g. num1 = 11, num2 = 5, num1 / num2 = 2...1
//e.g. num1 = -11, num2 = 5, num1 / num2 = -2...-1
//e.g. num1 = 11, num2 = -5, num1 / num2 = -2...1
//e.g. num1 = -11, num2 = -5, num1 / num2 = 2...-1

.ORIG x3000
AND R3 R3 0 ;Store result in R3

; If both are +, R4 = 0
; If ONLY NUM2 is -, R4 = 1
; If ONLY NUM1 is -, R4 = 2
; If both are -, R4 = 3

AND R4 R4 0
LD R2 NUM2 ; Store divisor and reminder in R2
BRz MGZERODIV
BRp GETDEN ; Jump to get denominator R1
ADD R4 R4 1; R2 negative number originally
NOT R2 R2  ; Make it positive number
ADD R2 R2 1	

GETDEN	LD R1 NUM1
	BRz   SETR20
	BRnp  KEEPGETR1
SETR20	AND R2 R2 0
	BRz EOP

KEEPGETR1    BRp   NEGATE
	     ADD R4 R4 2	;R1 negative number originally
	     NOT R1 R1	;Make it positive number
	     ADD R1 R1 1
	     BRp   NEGATE
        
MGZERODIV	LD R0 ZERODIVERR	;If divisor is 0,
		LEA R1 ZERODIVERR	;Manage to output the exception.
	OUTPUT  PUTC
		ADD R1 R1 1
		LDR R0 R1 0
BRp	OUTPUT
BRz	EOP

NEGATE NOT R2 R2
       ADD R2 R2 1
    
CALCULATE   ADD R3 R3 1 
	    ADD R1, R1, R2
BRz CLEANR2 //No reminder and division finished!
BRp CALCULATE
BRn GETREM

CLEANR2	AND R2 R2 0
BRz MGSIG

GETREM  ADD R3 R3 -1
	NOT R2 R2
	ADD R2 R2 1
	ADD R2 R1 R2
BRp	MGSIG

MGSIG	ADD R4 R4 -1
	BRnz GETRET
	NOT R2 R2
	ADD R2 R2 1	
GETRET	ADD R4 R4 1
	BRz EOP
	ADD R4 R4 -3
	BRz EOP
	NOT R3 R3
	ADD R3 R3 1
	
EOP	HALT	; End of program.

NUM1 .BLKW 1
NUM2 .BLKW 1
ZERODIVERR .STRINGZ "Divide by 0 exception!"
.END
