from cryptography.fernet import Fernet
from time import sleep
import os
import pyfiglet

menu_options = {
    1: 'Generate a key',
    2: 'Encrypt file',
    3: 'Decrypt file',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key])

def option1():

    os.system('cls')
    sleep(2)
    print("Generating the key...")
    sleep(2)
    #gerar a chave
    key = Fernet.generate_key()

    #salvar arquivo da chave  =   (nome do arquivo / como quer salvar (codigo binario BW))
    with open('MyKey.key','wb') as file:
        file.write(key) # o que vai ter escrito no arquivo? a chave :) 

    if os.path.isfile('MyKey.key'):
        print("Key created successfully" + '\n')
    else:
        print("There was a failure, try again" + '\n')
    sleep(2)


def option2():

    os.system('cls')
    sleep(2)

    if os.path.isfile('MyKey.key'):

        print("Checking the key...")
        # ler a chave
        key = ''
        with open('MyKey.key', 'rb') as file: #quando abrir o arquivo key, ele ira ler como binario 'read bin"
            key = file.read()
        
        files = input("Select the file: ")
        data = '' # ler os dados do arquivo 

        if os.path.isfile(files):
            with open(files, 'rb') as file: #quando abrir o arquivo key, ele ira ler como binario 'read bin"
                data = file.read()
            # encriptar o arquivo 
            print("Encrypting the file...")
            sleep(2)
            
            #Pegar o nome do arquivo
            split_tup = os.path.splitext(files) 
            file_name = split_tup[0] 
            file_extension = split_tup[1] 
            file_final = file_name + "Encry" + file_extension
            
            f = Fernet(key)
            encryptdata = f.encrypt(data)
            # salvar o arquivo encriptado

            with open(file_final, 'wb') as file:
                file.write(encryptdata)

            if os.path.isfile(file_final):
                print("Successfully encrypted file" + '\n')
            else:
                print("File encryption error")
            
            sleep(2)

        else:
            print("File not found")
    else:
        print("Key file not found")

def option3():
    
    os.system('cls')
    sleep(2)

    if os.path.isfile('MyKey.key'):
        # ler a chave
        key = ''
        with open('MyKey.key', 'rb') as file: #quando abrir o arquivo key, ele ira ler como binario 'read bin"
            key = file.read()
        

        files = input("Select the file: ")

        if os.path.isfile(files):

            # ler o arquivo
            encryptdata = ''
            with open(files, 'rb') as file: #quando abrir o arquivo key, ele ira ler como binario 'read bin"
                encryptdata = file.read()
            
            #Pegar o nome do arquivo
            split_tup = os.path.splitext(files) 
            file_name = split_tup[0] 
            file_extension = split_tup[1] 
            file_final = file_name + "Decry" + file_extension

            # decodificar
            f = Fernet(key)
            decryptData = f.decrypt(encryptdata)
            
            with open(file_final, 'wb') as file:
                file.write(decryptData)

            if os.path.isfile(file_final):
                print("file decrypted successfully" + '\n')
            else:
                print("Error decrypting file")
            
            sleep(2)
        
        else: 
            print("File not found")

    else:
        print("Key file not found")

    #salvar
result = pyfiglet.figlet_format("EncryptFile", font = "slant")
print(result + "\n")

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        #Verifique qual opção foi inserida e aja de acordo
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')