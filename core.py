import datetime

def lerArquivo(nome):
    arq = open('dados.txt', "r")
    linhas = arq.readlines()
    result = []
    for l in linhas:
        result.append(l.replace('\n', ''))
    arq.close()
    return result

def obtemParticipantes(dados):
    participantes = []
    for d in dados:
        if "," in d:
            individual = d.split(",")
            participantes.append(individual)
    return participantes

def dateTime():

    x = datetime.datetime.now()
    d = x.strftime("%d")
    m = x.strftime("%b")
    a = x.strftime("%Y")
    h=x.strftime("%X")
    print(f"DATA: {d}/{m}/{a}   HORA:{h}")

#-----------------------------------------------------------
entrada = lerArquivo("dados.txt")
dados = obtemParticipantes(entrada)
#----------------------------------------------------------
def remove_repetidos(dados):
    l = []
    for i in dados:
        if i not in l:
            l.append(i)
    l.sort()
    return l

# -------- OPÇÃO 0 E CONTIDA EM 1 -------------
def valorGenero():
    l_gen = []
    for i in range(len(dados)):
        for j in range(len(dados[i][0])):
            l_gen.append(dados[i][0])

    fem = 0
    masc = 0

    for i in l_gen:
        if i == "F":
            fem = fem+1
        if i == "M":
            masc = masc+1

    pcentf = int((fem/len(l_gen))*100)
    pcentm = int((fem/len(l_gen))*100)
    
    return pcentm,pcentf,l_gen

# ------- OPÇÃO 1 ----------------------------------------------------------- 

#------------ PORCENTAGEM POR IDADE-----------------------------------------
def faixaEtaria():   
    jovens=[]
    adultos=[]
    idosos=[]
    l_age=[]

    for i in range(len(dados)):
        for j in range(len(dados[i][1])):
            l_age.append(int(dados[i][1]))
            l_age = remove_repetidos(l_age)

    for i in l_age:
        if i in range(0,19):
            idade = int(i)
            jovens.append(idade)
        if i in range(20,59):
            idade = int(i)
            adultos.append(idade)
        if i in range(60,999):
            idade = int(i)
            idosos.append(idade)
        
    pcent_jovens = int((len(jovens)/len(l_age))*100)
    pcent_adultos = int((len(adultos)/len(l_age))*100)
    pcent_idosos = int((len(idosos)/len(l_age))*100)

    return pcent_jovens,pcent_adultos,pcent_idosos,jovens,adultos,idosos


#-------------------------Placebo ou não--------------------------
def vacina_placebo():
    
    l_placebo=[]

    for i in range(len(dados)):
        for j in range(len(dados[i][2])):
            dado = dados[i][2]
            l_placebo.append(dado)

    pcent_vacina = int((l_placebo.count("V")/len(l_placebo))*100)
    pcent_placebo = int((l_placebo.count("P")/len(l_placebo))*100)

    return pcent_vacina,pcent_placebo,l_placebo

#----------------------Contração de COVID?------------------------
def contracaoCovid():

    l_contracao = []

    for i in range(len(dados)):
        for j in range(len(dados[i][3])):
            c_covid = dados[i][3]
            l_contracao.append(c_covid)

    pcent_s = int((l_contracao.count("S")/len(l_contracao))*100)
    pcent_n = int((l_contracao.count("N")/len(l_contracao))*100)

    return pcent_s,pcent_n,l_contracao
 

#  ---------- Opção 2 -- EFICÁCIA GERAL DA VACINA -------------------
def eficaciaGeral():

    v = vacina_placebo()
    c=contracaoCovid()

    v=v[2]
    c=c[2]

    a=0
    b=0

    for i in range(len(v)):
        if v[i] == "P" and c[i] == "S":
            a +=1
        if v[i] == "V" and c[i] == "S":
            b +=1

    e = (a - b)*100/a

    return e,v,c

#---------------Opção 3 --------------Eficácia geral por idade -------------------------------------
def eficaciaIdade():
    aj = len([p for p in dados if p[2] == 'P' and p[3] == 'S' and int(p[1]) <= 19 ])   
    bj = len([p for p in dados if p[2] == 'V' and p[3] == 'S' and int(p[1]) <= 19 ])
    eficaciaj = 100 * (aj - bj) / aj
    eficacia_J =  int(round(eficaciaj, 2))

    aa = len([p for p in dados if p[2] == 'P' and p[3] == 'S' and int(p[1]) <= 59 and int(p[1]) >= 20])   
    ba = len([p for p in dados if p[2] == 'V' and p[3] == 'S' and int(p[1]) <= 59 and int(p[1]) >= 20])
    eficacia_a = 100 * (aa - ba) / aa
    eficacia_A =  int(round(eficacia_a, 2))

    ai = len([p for p in dados if p[2] == 'P' and p[3] == 'S' and int(p[1]) >= 60])   
    bi = len([p for p in dados if p[2] == 'V' and p[3] == 'S' and int(p[1]) >= 60])
    eficacia_i = 100 * (ai - bi) / ai
    eficacia_I =  int(round(eficacia_i, 2))

    #print(eficacia_J, eficacia_A,eficacia_I)
    print(aj,bj,'\n',aa,ba,'\n',ai,bi)
    print(dados)
    return eficacia_J,eficacia_A,eficacia_I
    

#--------Opção 4 ----------Eficácio por Gênero
def eficaciaGenero():

    lista = dados

    af = len([p for p in lista if p[2] == 'P' and p[3] == 'S' and p[0] == "F"])   
    bf = len([p for p in lista if p[2] == 'V' and p[3] == 'S' and p[0] == "F"])
    eficacia = 100 * (af - bf) / af
    eficacia_F =  int(round(eficacia, 2))

    am = len([p for p in lista if p[2] == 'P' and p[3] == 'S' and p[0] == "M"])   
    bm = len([p for p in lista if p[2] == 'V' and p[3] == 'S' and p[0] == "M"])
    eficacia = 100 * (am - bm) / am
    eficacia_M =  int(round(eficacia, 2))

    return eficacia_F, eficacia_M

