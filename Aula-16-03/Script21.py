from datetime import date, datetime

frutas = ["Jabuticaba", "Laranja", "Uva", "Banan"]
for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12}- Número de letras ={len(fruta): 3}"
    print(minha_fruta)

print()
print()

pi = 3.1415
meu_numero = f"O número Pi é {pi:1f}"
meu_numero_deslocado = f"O número de PI deslocado é {pi:4.1f}"
meu_numero_preciso = f"O número de PI preciso é {pi:7.4f}"
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()
print()

data = datetime.now()
minha_data = f"A data de hoje é {data}"
minha_data_formatada = f"A data de hoje formatada é {data:%d/%m/%Y}"
print(minha_data)
print(minha_data_formatada)
