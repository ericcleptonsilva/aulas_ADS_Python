arquivo_escrita = open("date_write.txt", "w")

arquivo_escrita.write("Conteúdo na primeira linha")
arquivo_escrita.write("\nConteúdo na segunda linha")
print("conteúdo adicionado com sucesso!")

arquivo_escrita.close()