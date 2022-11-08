print("Seja Bem vindo ao nosso Jogo!!")
user = input("Quer começar? [S/N]")
print(user)

if user != "S":
    quit() 
    


score = 0

print("Começando...")
print("Quem criou a microsoft?\n(A)Bill Gate\n(B)Linus Torvalds\n(C)Steve jobs")
user_1 = input("Respostas: ")

if user_1 == "A":
    print("Resposta Correta 🥳")
    score = score + 1
else:
    print("Incorreta 😥")
    
    
print("Vamos para segunda Pergunta?...")
user = input("Quer começar? [S/N]")
print(user)

if user != "S":
    quit() 

    
print("Quem Criou o Linux?\n(A)Bill Gate\n(B)Linus Torvalds\n(C)Steve jobs")
user_2 = input("Respostas: ")

if user_2 == "B":
    print("Resposta Correta 🥳")
    score = score + 1
else:
    print("Incorreta 😥")
    
    
print("Vamos para Terceira Pergunta?...")
user = input("Quer começar? [S/N]")
print(user)

if user != "S":
    quit() 

    
print("Quem Criou a Apple?\n(A)Bill Gate\n(B)Linus Torvalds\n(C)Steve jobs")
user_3 = input("Respostas: ")

if user_3 == "C":
    print("Resposta Correta 🥳")
    score = score + 1
else:
    print("Incorreta 😥")
    
print(f"Quiz Acabou... Sua Pontuação foi: {score}/3!!")
    
    
    