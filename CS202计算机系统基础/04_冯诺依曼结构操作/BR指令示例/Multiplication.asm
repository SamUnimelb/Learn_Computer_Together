//Store positive num1 at x3010 and positive num2 at x3011
//Calculate num1 * num2 and store it to R2
.ORIG x3000
LD R0 xF //RO = 2
LD R1 xF //R1 = 16
AND R2, R2, 0
ADD R2, R2, R0 //R2 = 20
ADD R1, R1, -1 //R1 = 0
BRp -3
TRAP x25
.END