//Program for division num1 / num2
//e.g. num1 = 10, num2 = 5, num1 / num2 = 
.ORIG x3000
LD R1, xF
LD R2, xF
AND R3, R3, 0 ;Store divsor
ADD R3, R2, 0
AND R4, R4, 0 ;Store result.
ADD R4, R4, 1
NOT R3, R2 ;R1 - R2
ADD R3, R3, 1
ADD R1, R1, R3
BRp -5
BRz 1 //Jump to HALT and R4 is the result
ADD R4, R4, -1
HALT
.END