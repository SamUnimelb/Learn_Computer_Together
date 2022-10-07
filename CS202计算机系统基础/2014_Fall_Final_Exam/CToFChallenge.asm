;This is the program to transfer temperature in integer (16 bits) from 
;Celcius to Fahrenheit. 
;
; The Celcius values are ranging from -273 to 3640 Celcius
; Celcius value is stored in memory address NUM1 to fill. 
; Calculation result will be stored in R3 in the end. 
; Following the formula F = 1.8C + 32 = 9 * C / 5 + 32
;
//Calculate num1 * 9 and store the result to R3
//num1 and num2 can be any integers ranging between -273 ~ 3640

.ORIG x3000
ST R1 R1VAL
ST R2 R2VAL
ST R3 R3VAL
ST R4 R4VAL
AND R3 R3 0 ;R3 to store results of the calculation.
AND R4 R4 0 ;R4 to calculate number of neg factors.
LD R1 NUM1
BRz 	CLEANUP
BRp	GETR2
NOT R1 R1
ADD R1 R1 1
ADD R4 R4 1

GETR2	AND R2 R2 0
	ADD R2 R2 9

CALCULATE	ADD R3 R3 R2
		ADD R1 R1 -1
BRp CALCULATE

ADD R4 R4 -1
BRnp	CLEANUP
NOT R3 R3
ADD R3 R3 1

CLEANUP AND R2 R2 0
	AND R1 R1 0
	AND R4 R4 0

//END OF MULTIPLICATION

AND R1 R1 0
AND R4 R4 0
ADD R1 R3 0
BRp ONGO
ADD R4 R4 1 ;R4 = 1 means R1 is -
NOT R1 R1
ADD R1 R1 1
ONGO AND R3 R3 0 ;Store result in R3

LD R2 NUM3 ; Store divisor and reminder in R2
NOT R2 R2
ADD R2 R2 1
    
CALCULATEDIV   ADD R3 R3 1 
	    ADD R1, R1, R2
BRp CALCULATEDIV
BRz GETRET
ADD R3 R3 -1

GETRET ADD R4 R4 -1
       BRn EOP
       NOT R3 R3
       ADD R3 R3 1

EOP	LD R2 CONST
	ADD R3 R2 R3
	ADD R0 R3 0
	LD R1 R1VAL
	LD R2 R2VAL
	LD R3 R3VAL
	LD R4 R4VAL
	HALT	; End of program.

NUM1 .BLKW 1
NUM2 .FILL 9
NUM3 .FILL 5
CONST .FILL 32
R1VAL .BLKW 1
R2VAL .BLKW 1
R3VAL .BLKW 1
R4VAL .BLKW 1
.END
