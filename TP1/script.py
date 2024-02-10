data_dict = {} # (column , atleta_id) -> data

file = open("emd.csv", "r")

header = file.readline().rstrip('\n')
column_names = header.split(",")

for line in file:
    data = line.rstrip('\n').split(",")
    if (len(data) != len(column_names)):
        print("Invalid line: " + line)
        continue
    for i in range(len(data)):
        data_dict[(column_names[i], data[0])] = data[i]

file.close()

modalidades = set()
for (column, atleta_id) in data_dict:
    if column == "modalidade":
        modalidades.add(data_dict[(column, atleta_id)])
modalidades = sorted(modalidades)

aptos = 0
inaptos = 0
for (column, atleta_id) in data_dict:
    if column == "resultado":
        if data_dict[(column, atleta_id)] == "true":
            aptos += 1
        else:
            inaptos += 1
percentagem_aptos = aptos / (aptos + inaptos) * 100
percentagem_inaptos = inaptos / (aptos + inaptos) * 100

escaloes = {} # escalão -> lista de atletas
for (column, atleta_id) in data_dict:
    if column == "idade":
        idade = int(data_dict[(column, atleta_id)])
        escalao = (idade // 5) * 5
        nome_atleta = data_dict[("nome/primeiro", atleta_id)] + " " + data_dict[("nome/último", atleta_id)]
        if escalao not in escaloes:
            escaloes[escalao] = []
        escaloes[escalao].append(nome_atleta)

print()
print("Atletas por escalão:")
file = open("resultados.txt", "w")
file.write("Atletas por escalão:\n")
for escalao in sorted(escaloes):
    percentagem = round(len(escaloes[escalao]) / (aptos + inaptos) * 100,2)
    file.write(str(escalao) + " - " + str(escalao + 4) + " (" + str(len(escaloes[escalao])) + ' - ' + str(percentagem) + "%)" + ":\n")
    print(str(escalao) + " - " + str(escalao + 4) + " (" + str(len(escaloes[escalao])) + ' - ' + str(percentagem) + "%)" + ":")
    for atleta in escaloes[escalao]:
        file.write("- " + atleta + "\n")
        print("- " + atleta)
    file.write("\n")
    print()

print("Modalidades: " + ", ".join(modalidades))
print()
print("Aptos: " + str(aptos) + " (" + str(percentagem_aptos) + "%)")
print()
print("Inaptos: " + str(inaptos) + " (" + str(percentagem_inaptos) + "%)")
print()

file.write("\n")
file.write("Modalidades: " + ", ".join(modalidades) + "\n")
file.write("\n")
file.write("Aptos: " + str(aptos) + " (" + str(percentagem_aptos) + "%)\n")
file.write("\n")
file.write("Inaptos: " + str(inaptos) + " (" + str(percentagem_inaptos) + "%)\n")

print("Resultados guardados no ficheiro 'resultados.txt'")