3) Os pares de instruções abaixo produzem o mesmo resultado? Imprima os valores abaixo, veja se algum deles (A, B ou C)
possuem valores diferentes nas versões 1 e 2, e caso sim, explique num comentário o motivo.

A1 ← (4/2)+(2/4)	e	A2 ← 4/2+2/4
B1 ← 4/(2+2)/4	e	B2 ← 4/2+2/4
C1 ← (4+2)*2-4	e	C2 ← 4+2*2-4


A =(4/2)+(2/4)
print(A)
A=4/2+2/4
print(A)
B=4/(2+2)/4
print(B)
B=4/2+2/4
print(B)
C=(4+2)*2-4
print(C)
C=4+2*2-4
print(C)
