def status(nome, nota1, nota2):

    media = (nota1+nota2)/2
    if media > 6:
        print("Aluno ",nome,"aprovado!! com media %.2f"%media)
    elif media >= 4 and media <=6:
        print("Aluno ",nome," em verificação complementar!! com media %.2f"%media)
    else:
        print("Aluno ",nome," reprovado!! com media %.2f" %media)
    return media
