   # projeto integrado

import random

lista_codigo = []
lista_nome = []
lista_email = []
lista_telefone = []
lista_curso = []

while 3 == 3:
    esc = int(input("1 - cadastro \n" + "2 - consulta \n" + "3 - finalizar programa \n"))

    if esc == 1:
        codigo = random.randint(100,400)
        lista_codigo.append(codigo)

        nome = input("digite o nome: \n")
        lista_nome.append(nome)

        email = input("digite o email: \n")
        lista_email.append(email)

        telefone = input("digite o telefone: \n")
        lista_telefone.append(telefone)

        curso = input("digite o curso: \n")
        lista_curso.append(curso)

        print("matricula: {} \n".format(lista_codigo) + "Nome: {} \n".format(lista_nome) + "Telefone: {} \n".format(
        lista_telefone)
          + "Email: {} \n".format(lista_email) + "curso: {} \n".format(lista_curso))
    elif esc == 2:
        print("matricula: {} \n".format(lista_codigo) + "Nome: {} \n".format(lista_nome) + "Telefone: {} \n".format(lista_telefone)
                + "Email: {} \n".format(lista_email) + "curso: {} \n".format(lista_curso))

    else:
        print("final do programa")
        break
