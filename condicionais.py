def verificar_maioridade():
    idade = int(input("Qual é a sua idade?"))

    if(idade >= 18):
        print("Maior idade.")
    else:
        print("Menor idade.")
    
verificar_maioridade()