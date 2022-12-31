import socket
import sys

def  main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso!")

    HostLocalizado = input("Digitie o Host ou IP desejado: ")
    PortaLocalizada = input("Digite a porta desejada: ")

    try:
        s.connect((HostLocalizado, int(PortaLocalizada)))
        print("Cliente TCP conectado: " + HostLocalizado + " e na Porta: " + PortaLocalizada)
        s.shutdown(1)
    except socket.error as e:
        print("Host não conectado:" + HostLocalizado + " - Porta: " +PortaLocalizada)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == " main ":
    main()
