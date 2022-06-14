; Store positive num1 at x3010 and positive num2 at x3011
; Calculate num1 * num2 and store it to R2
;
; Use .FILL to fill up a specific value.
; Use .BLKW to set a memory address to have the value to be filled. 
;
.ORIG x3000
LD R0 NUM1
LD R1 NUM2
AND R2, R2, 0
LOOP ADD R2, R2, R0
     ADD R1, R1, -1
BRp LOOP
TRAP x25
NUM1 .BLKW 1 ; Num1 to be filled up here.
NUM2 .BLKW 2 ; Num2 to be filled up here.
.END