arquivo = open("text2.txt")

conteudo = arquivo.read()
print("Todo conteúdo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Releitura de todo conteúdo do arquivo")
print(repr(conteudo_releitura))

arquivo.close()

arquivo_reaberto = open("text2.txt")

conteudo_reaberto = arquivo_reaberto.read()
print("Todo conteúdo do arquivo novamente")
print(repr(conteudo_reaberto), '\n')


arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Todo conteúdo do arquivo após o seek")
print(repr(conteudo_seek), '\n')

arquivo_reaberto.close()
