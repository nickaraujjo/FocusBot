import json
import os

def entender_pergunta(pergunta, dados):
    pergunta = pergunta.lower().strip()

    for chave in dados:
        if chave in pergunta:
            return chave, dados[chave]

    return None, None

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def carregar_materias():
    try:
        with open("data/materias.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_materias(materias):
    with open("data/materias.json", "w") as arquivo:
        json.dump(materias, arquivo, indent=4)

def carregar_tarefas():
    try:
        with open("data/tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return {}

def salvar_tarefas(tarefas):
    with open("data/tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

#MENU PRINCIPAL

def menu():

    print("📚 Olá, Eu sou o Focus!")
    print(" Seu assistente pessoal de estudos ✨")
    print(" Estou aqui para ajudar você a organizar seus estudos, criar planos de estudo personalizados e fornecer dicas para melhorar seu foco e produtividade. 🚀")

    nome = input("\nQual é o seu nome: ")
    limpar_tela()

    print(f"\nPrazer em te conhecer, {nome}! 😊")
    print("\nVamos começar! O que você gostaria de fazer hoje? 🤔")
    
    materias = carregar_materias()
    tarefas = carregar_tarefas()
    
    with open("data/conceitos.json", "r") as arquivo:
        dados = json.load(arquivo)

    while True:
    
            print("Escolha uma opção:")
            print("\n1. Criar um plano de estudo personalizado")
            print("2. Obter dicas para melhorar o foco e a produtividade")
            print("3. Ver matérias")
            print("4. Adicionar matéria")
            print("5. Fazer um teste de conhecimento")
            print("6. Gerenciar tarefas")
            print("7. Aprender um conceito")
            print("8. Sair")

            escolha = input("\nDigite o número da opção desejada: ")
            limpar_tela()

    #===========
    #PLANO DE ESTUDO
    #===========
            
            if escolha == "1":
                print("\nVamos criar um plano de estudo personalizado! 📅")
                        
                if not materias:
                    print("⚠️ Adicione matérias primeiro!")
                else:
                    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

                    print("\n📅 Seu plano de estudos:")
                    for i in range(len(materias)):
                        dia = dias[i % len(dias)]
                        print(f"{dia} → {materias[i]}")
                #===========
                #DICAS
                #===========
            elif escolha == "2":
                    print("\nAqui estão algumas dicas para melhorar o foco e a produtividade: 💡")
                    print("- Estabeleça metas claras e alcançáveis")
                    print("- Use técnicas de Pomodoro para gerenciar seu tempo")
                    print("- Faça pausas regulares para descansar a mente")
                    print("- Mantenha uma alimentação saudável e durma bem")
                    print("\nDigite 'Enter' para voltar ao menu principal.")
                    input()
                    limpar_tela()

                  
                # ========================
                # VER MATÉRIAS
                # ========================
            elif escolha == "3":
                    if not materias:
                        print("\nNenhuma matéria adicionada ainda. 😔")
                    else:
                        print("\nSuas matérias: 📚")
                        for m in materias:
                            print(f"- {m}")
                           
            
                # ========================
                # ADICIONAR MATÉRIA
                # ========================
                            
            elif escolha == "4":
                    print("\nVamos adicionar uma nova matéria! 📚")
                    materia = input("Digite o nome da nova matéria: ")
                        
                    if materia in materias:
                       print(f"\nA matéria '{materia}' já está cadastrada. 😔")
                    else:
                        materias.append(materia)
                        salvar_materias(materias)
                        print(f"\nMatéria '{materia}' adicionada com sucesso! ✅")
                        input("\nPressione Enter para continuar...")
                        limpar_tela()

                

                # ========================
                # QUIZ
                # ========================
            elif escolha == "5":
                print("\nVamos fazer um teste de conhecimento! 🧠")
                acertos = 0

            # PERGUNTA 1
                print("\n1-) O que significa Phishing?")
                print("a- Um tipo de vírus de computador")
                print("b- Uma tentativa de engano para obter informações sensíveis")
                print("c- Um sistema de proteção de redes")

                resposta = input("Digite a letra correta: ").lower()

                if resposta == "b":
                            print("✅ Resposta correta!")
                            acertos += 1
                else:
                            print("❌ Resposta incorreta.")
                            print("✔ Resposta certa: b- Uma tentativa de engano para obter informações sensíveis")

                            # PERGUNTA 2
                            print("\n2-) O que é um firewall?")
                            print("a- Um dispositivo de segurança que monitora o tráfego de rede")
                            print("b- Um tipo de ataque hacker")
                            print("c- Um programa de edição de texto")

                            resposta = input("Digite a letra correta: ").lower()

                if resposta == "a":
                        print("✅ Resposta correta!")
                        acertos += 1
                else:
                        print("❌ Resposta incorreta.")
                        print("✔ Resposta certa: a- Um dispositivo de segurança que monitora o tráfego de rede")

                    # RESULTADO FINAL
                        print(f"\n🎯 Você acertou {acertos} de 2 perguntas!")
                        input("\nPressione Enter para continuar...")
                        limpar_tela()
                        

            elif escolha == "6":

                while True:

                        print("\n📌 MENU DE TAREFAS")
                        print("1. Adicionar tarefa")
                        print("2. Ver tarefas")
                        print("3. Voltar")

                        opcao = input ("Escolha: ")

                        # ADICIONAR TAREFA
                        if opcao == "1":
                            if not materias:
                                print("⚠️ Cadastre matérias primeiro!")
                                continue

                            print("\nEscolha a matéria:")
                            for i, m in enumerate(materias):
                                print(f"{i+1}. {m}")

                            escolha_materia = int(input("Número: ")) - 1

                            if 0 <= escolha_materia < len(materias):
                                materia = materias[escolha_materia]

                                tarefa = input("Digite a tarefa: ")

                                if materia not in tarefas:
                                    tarefas[materia] = []

                                tarefas[materia].append(tarefa)
                                salvar_tarefas(tarefas)

                                print("✅ Tarefa adicionada!")
                            else:
                                print("❌ Opção inválida.")
                                input("\nPressione Enter para continuar...")
                                limpar_tela()

                        # VER TAREFAS
                        elif opcao == "2":
                            if not tarefas:
                                print("⚠️ Nenhuma tarefa cadastrada.")
                            else:
                                print("\nSuas tarefas:")
                                for m, t_list in tarefas.items():
                                    print(f"\n📚 {m}:")
                                    for t in t_list:
                                        print(f" - {t}")
                            input("\nPressione Enter para continuar...")
                            limpar_tela()

                        # VOLTAR
                        elif opcao == "3":
                            break

                        else:
                            print("❌ Opção inválida.")
                            input("\nPressione Enter para continuar...")
                            limpar_tela()

            elif escolha == "7":
                print("\n📚 Modo conversa ativado (digite 'sair' para voltar)")

                while True:
                    pergunta = input("\nVocê: ")

                    if pergunta.lower() == "sair":
                        break
                   

                    chave, resposta = entender_pergunta(pergunta, dados)

                    if resposta:
                        print(f"\n🤖 Sobre {chave}: {resposta}")
                    else:
                        print("\n🤖 Ainda nao entendi muito bem... tente outra forma.")
                        print(dados)
                    input("\nPressione Enter para continuar...")
                    limpar_tela()
                
                # SAIR
                # ========================

            elif escolha == "8":
                print("\nEspero que esteja gostando de usar o Focus! Até a próxima! 👋")
                break

            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida. ❌")
menu()

def materias_menu():
# Lista para guardar as matérias
    materias = []

    while True:
        print("\nO que deseja fazer?")
        print("1. Adicionar matéria")
        print("2. Ver matérias")
        print("3. Criar tarefa para uma matéria")
        print("4. Voltar ao menu principal")
        print("5. Sair")

        escolha = input("\nDigite o número da opção desejada: ")

        if escolha == "1":
            materia = input("\nDigite o nome da nova matéria: ")
            materias.append(materia)
            print(f"\nMatéria '{materia}' adicionada com sucesso! ✅")

        elif escolha == "2":
            if materias:
                print("\nMatérias disponíveis:")
                for idx, materia in enumerate(materias, start=1):
                    print(f"{idx}. {materia}")
                else:
                    print("\nNenhuma matéria cadastrada ainda. 😔")
                    materias_menu()

        elif escolha == "3":
            if materias:
                print("\nEscolha a matéria para criar uma tarefa:")
                for idx, materia in enumerate(materias, start=1):
                    print(f"{idx}. {materia}")
                materia_escolhida = int(input("\nDigite o número da matéria: "))
                if 1 <= materia_escolhida <= len(materias):
                    tarefa = input("\nDigite o nome da tarefa: ")
                    print(f"\nTarefa '{tarefa}' criada para a matéria '{materias[materia_escolhida - 1]}'! ✅")
                else:
                    print("\nNúmero de matéria inválido. ❌")
        elif escolha == "4":
            menu()
            break
        elif escolha == "5":
            print("\nEspero que esteja gostando de usar o Focus! Até a próxima! 👋")
            break