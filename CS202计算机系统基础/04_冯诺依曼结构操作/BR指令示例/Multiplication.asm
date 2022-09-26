//Calculate num1 * num2 and store the result to R3
//num1 and num2 can be any integers ranging between xFFFD ~ xFD
//e.g. num1 = 4, num2 = 5, num1 * num2 = 20;
//e.g. num1 = -4, num2 5, num1 * num2 = -20;
//e.g. num1 = 4, num2 = -5, num1 * num2 = -20;
//e.g. num1 = -4, num2 -5, num1 * num2 = 20;

.ORIG x3000
AND R3 R3 0 ;R3 to store results of the calculation.
AND R4 R4 0 ;R4 to calculate number of neg factors.
LD R1 NUM1
BRz 	CLEANUP
BRp	GETR2
NOT R1 R1
ADD R1 R1 1
ADD R4 R4 1

GETR2	LD R2 NUM2
	BRz	CLEANUP
	BRp	CALCULATE
NOT R2 R2
ADD R2 R2 1
ADD R4 R4 1

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
EOP HALT

NUM1 .BLKW 1
NUM2 .BLKW 1
.END