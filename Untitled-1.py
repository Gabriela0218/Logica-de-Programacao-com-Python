"""Ter um convite VIP.
Estar na lista de convidados.
Ser um membro do clube. 
"""
convite_vip = input("Você possui convite VIP? (sim/não): ")

na_lista = input("Você está na lista de convidados? (sim/não): ")         

membro_clube = input("Você é um membro do clube? (sim/não): ")  

if convite_vip == "sim" or na_lista == "sim" or membro_clube == "sim":

     print ("Bem-vindo(a) ao evento!")

else:
    print("Desculpe, você não pode entrar no evento!")