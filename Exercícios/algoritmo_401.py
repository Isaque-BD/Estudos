dados1 = []
dados2 = []
dados3 = []
milhas = []



texto = "MENU"
while True:
    print("\n",'*'*20,"\n",texto.center(20),"\n",'*'*20)
    print("\n1- Cadastro dos dados do cliente")
    print("2- Cadastro da milhagem do clinete")
    print("3- Lista a milhagem do cliente")
    print("4- Imprime os nomes que tem maior e menor milhagem")
    print("5- Imprime os nomes e as milhagens")
    print("6- Sair")
    op = int(input("\nEscolha uma opção: "))

    if op == 1:
        if dados1 < 50:
            for i in range(3):
                k = str(input("Nome: "))
                dados1.append(k)
                
                k = str(input("Endereço: "))
                dados2.append(k)
                
                k = str(input("Telefone: "))
                dados3.append(k)

        else: 
            print("\nArquivo cheio")
            break
    
    if op == 2:
        nome = str(input("Digite o nome da pessoa: "))
        if nome in dados1:
           
            milha1 = int(input("Digite a milhagem que deseja: "))
            milhas.append(milha1)
        else:
            print("Nome não encontrado")
            break
    
    if op == 3:
        print("Nome")