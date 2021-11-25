import core as c
import time 


def menu():
    
    print("Resultados pesquisa COVID 19")
    print("Escolha umas das opçoes a baixo")
    c.dateTime()
    print('\n')
    op = ["Percentuais por gênero.","Todos os Percentuais","Eficácia geral da vacina","Eficácia por faixa etária","Eficácia por gênero","Sair"]
    for i in range(6):
        print("[",i,"]", " - ",op[i],)
    print("\n")
    

while True:

    print("\n")
    menu()
    select = int(input("Digite sua opção: "))
    texo_saida = "Porcentagem de participantes por gênero;"

    print()
    
    if select == 5:
        break
    if select not in [0,1,2,3,4,5]:
        txt=len("DIGITE UMA OPÇÃO VÁLIDA!")
        print("*"*txt)
        print("DIGITE UMA OPÇÃO VÁLIDA!")
        print("*"*txt)

    if select == 0:
        d = c.valorGenero()
        f = d[0]
        m = d[1]
        print("*"*len(texo_saida))
        print(f"OPÇÃO {select}\n{texo_saida}")
        print("*"*len(texo_saida))
        print(f"FEMININO  = {f}%\nMASCULINO = {m}%\n")
        print("*"*len(texo_saida))

    if select == 1:
        genero=c.valorGenero()
        por_idade=c.faixaEtaria()
        vacina=c.vacina_placebo()
        contracao=c.contracaoCovid()
        print("*"*102)
        print("OPÇÃO ",select)
        print("*"*102)
        print(f"=> Percentuais por gênero:\n    {genero[0]}% FEMININO\n    {genero[1]}% MASCULINO.")
        print(f"=> Percentuais por idade:\n    {por_idade[0]}% => JOVENS.\n    {por_idade[1]}% => ADULTOS.\n    {por_idade[2]}% => IDOSOS.")
        print(f"=> Percentual de vacina x placebo:\n    {vacina[0]}% TOMARAM VACINA.\n    {vacina[1]}% TOMARAM PLACEBO.")
        print(f"=> Percentual de quem contraiu Covid e não contraiu:\n    {contracao[0]}% SIM => CONTRAIRAM COVID\n    {contracao[1]}% NÂo => NÃO CONTRAIRAM COVID.")
        print("*"*102,"\n")
    
    if select == 2:
        eficacia = c.eficaciaGeral()
        eficacia = int(eficacia[0])
        texto = len("A eficácia geral da vacina foi de       ")
        print("*"*texto)
        print("OPÇÃO ",select)
        print("*"*texto)
        print(f"EFICÁCIA GERAL: {eficacia} %.\n")
        print("*"*texto)

    if select == 3:
        e_age = c.eficaciaIdade()
        e_J = e_age[0]
        e_A = e_age[1]
        e_I = e_age[2]
        texto = len("Eficácia por faixa etária:")
        print("*"*texto)
        print("OPÇÃO ",select)
        print("*"*texto)
        print(f"JOVENS  {e_J}%.\nADULTOS {e_A}%.\nIDOSOS  {e_I}%.")
        print("*"*texto)
        continue

    if select == 4:
        ef = c.eficaciaGenero()
        ef_F = ef[0]
        ef_M = ef[1]
        texto = len("A eficácia por gênero:")
        print("*"*texto)
        print("OPÇÃO ",select)
        print("*"*texto)
        print(f"SEXO FEMININO {ef_F}%.\nSEXO MASCULINO {ef_M}%")
        print("*"*texto)
        continue
    time.sleep(3)

