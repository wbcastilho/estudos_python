# Em python prefira o padrão EAFP

# Maneira errada
# LBYL
# Look before you leap
# Verifique antes de agir
if Path(caminho_do_arquivo).exists():
    with open(caminho_do_arquivo) as f:
        f.do_something()
else:
    print("O arquivo não existe!")

# Maneira correta
# EAFP
# Easy Ask Forgiveness than permission
# É melhor pedir perdão do que permissão
try:
    with open(caminho_do_arquivo) as f:
        f.do_something()
except FileNotFoundError:
    print("O Arquivo não existe!")

