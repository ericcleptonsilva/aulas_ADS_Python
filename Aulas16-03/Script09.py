
linhas = ["Conteudo da primeira linha", "\nConteudo da segunda linha"]

arquivo_escrita = open("date_writelines.txt", "w")

arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

