# crie uma função que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def calcule_media(nota1,nota2,nota3):
    media = (nota1 + nota2+ nota3)/3
    return media

def verificar_media(media):
    if media >7:
        return "aprovado"
    else:
        return "reprovado"

nota1 = float(input("digite a 1º nota: "))
nota2 = float(input("digite a 2º nota: "))
nota3 = float(input("digite a 3º nota: "))

resultado_media = calcule_media(nota1,nota2,nota3)
print(resultado_media)

resultado_final = verificar_media(resultado_media)
print(resultado_final)

