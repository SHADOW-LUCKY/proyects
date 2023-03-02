"""
10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato
"""
subsidio=[0,0.6,0.4,0.15,1,1,1,1,1,1,1]
consumo_kw_mes=float(input("ud cuantos kw consume en el mes?: "))
valor_kw=400
mes_consumo=input("mes de consumo?: ")
estrato = subsidio[int(input("estrato? (max 10): "))]

consumototal = (valor_kw * estrato) * mes_consumo

print(f"el valor a pagar por concepto de energía eléctrica es: {consumototal} en el mes: {mes_consumo}")

