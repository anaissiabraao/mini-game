import random
import os

class PortoExQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "1) Quando foi fundada a companhia?",
                "options": [
                    "1. 2011",
                    "2. 2013",
                    "3. 2008",
                    "4. 2007",
                    "5. 2005"
                ],
                "correct": 3  # Index of correct answer (0-based)
            },
            {
                "question": "2) Quais desses serviços são oferecidos?",
                "options": [
                    "1. Serviços advocatícios",
                    "2. Serviços empresariais",
                    "3. Serviços logísticos",
                    "4. Serviços de taxidriver",
                    "5. Serviços navais"
                ],
                "correct": 2
            },
            {
                "question": "3) Qual é a pessoa que aparece na homepage da empresa?",
                "options": [
                    "1. Ana Elícia",
                    "2. Fabrício",
                    "3. Marlon Marques",
                    "4. José Aguinaldo",
                    "5. Isadora"
                ],
                "correct": 3
            },
            {
                "question": "4) Quantos serviços oferecemos pela homepage?",
                "options": [
                    "1. TRANSPORTE ECONÔMICO, TRANSPORTE PERSONALIZADO, TRANSPORTE EXPRESSO e SERVIÇOS LOGÍSTICOS",
                    "2. TRANSPORTE DE CARGA, TRANSPORTE ADUANEIRO, TRANSPORTE ENTRE BASES e ARMAZENAGEM",
                    "3. TRANSPORTE DE VEÍCULOS (CEGONHA), TRANSPORTE DE CARGA PESADA (HEAVYLIFT), TRANSPORTE ADUANEIRO (NAVIO) e TRANSPORTE AÉREO",
                    "4. SERVIÇOS LOGÍSTICOS GERAIS",
                    "5. TRANSPORTE DE CARGAS GERAIS, TRANSPORTE DE CARGA VALIOSA, TRANSPORTE DE CARGA FRACIONADA e TRANSPORTE DEDICADO"
                ],
                "correct": 0
            },
            {
                "question": "5) Quais serviços são oferecidos no transporte personalizado?",
                "options": [
                    "1. Contêiner, DTA (Declaração de Trânsito Aduaneiro), Lotação e Veículo plataforma",
                    "2. Entregas em shopping, Cargas Anvisa, Entregas em locais com grades de horário e Armazenagem",
                    "3. Entregas sem agendamento fixo (possível antecipação), Crossdocking, Etiquetagem e Separação",
                    "4. Cargas Anvisa e Cargas com valor agregado",
                    "5. Nenhuma das alternativas"
                ],
                "correct": 0
            },
            {
                "question": "6) O que são cargas LTL e FTL?",
                "options": [
                    "1. LTL (Less Than Truckload): Refere-se ao transporte de cargas menores que não ocupam a totalidade do espaço ou da capacidade de peso de um caminhão. Nesse caso, a carga de um cliente é combinada com cargas de outros clientes no mesmo veículo, otimizando custos. É ideal para envios de pequeno a médio porte, como pallets ou caixas.\n   FTL (Full Truckload): Envolve o transporte de uma carga que ocupa todo o espaço ou a capacidade total de peso do caminhão, destinada a um único cliente. É usada para grandes volumes ou quando a carga exige entrega direta.",
                    "2. LTL (Lotação de Tranporte Leve): Refere-se ao transporte de cargas leves, ou seja, cargas que não possuem alto valor e demandas expressas. Isso significa que a carga tem prioridade baixa e por esse motivo pode aguardar durante a transferência entre bases. FTL (Transporte Fracionado de Lotações): Refere-se a cargas que são fracionadas, por isso não há paletes serão sempre lotações batidas. Onde não há organização e proporções de clientes isso quer dizer que são diversos clientes."
                ],
                "correct": 0
            },
            {
                "question": "7) O que significa a lógica FIFO?",
                "options": [
                    "1. Federação Internacional de Organizações Futurísticas",
                    "2. First In First Out (Primeiro a entrar, primeiro a sair)",
                    "3. First Input Finally Output (Primeira Entrada, Finalmente Saída)"
                ],
                "correct": 1
            }
        ]
        self.score = 0

    def clear_screen(self):
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')

    def show_header(self):
        self.clear_screen()
        print("=" * 50)
        print("           QUIZ PORTOEX           ")
        print("=" * 50)
        print(f"Pontuação: {self.score}/{len(self.questions)}\n")

    def run_quiz(self):
        random.shuffle(self.questions)  # Shuffle questions for variety
        
        for i, q in enumerate(self.questions, 1):
            self.show_header()
            print(f"Pergunta {i}/{len(self.questions)}:")
            print(q["question"])
            print()
            
            for option in q["options"]:
                print(option)
            
            while True:
                try:
                    answer = int(input("\nSua resposta (número da opção): ")) - 1
                    if 0 <= answer < len(q["options"]):
                        break
                    else:
                        print(f"Por favor, digite um número entre 1 e {len(q['options'])}")
                except ValueError:
                    print("Por favor, digite apenas números.")
            
            if answer == q["correct"]:
                print("\n✅ Resposta correta!")
                self.score += 1
            else:
                print(f"\n❌ Resposta incorreta. A resposta correta era a opção {q['correct'] + 1}.")
            
            input("\nPressione Enter para continuar...")
        
        self.show_results()
    
    def show_results(self):
        self.show_header()
        print("=== RESULTADO FINAL ===")
        percentage = (self.score / len(self.questions)) * 100
        print(f"\nVocê acertou {self.score} de {len(self.questions)} perguntas!")
        print(f"Pontuação: {percentage:.1f}%")
        
        if percentage == 100:
            print("\n🎉 Excelente! Você é um expert em PortoEx! 🎉")
        elif percentage >= 70:
            print("\n👍 Bom trabalho! Você conhece bem a PortoEx!")
        elif percentage >= 50:
            print("\n😊 Bom trabalho, mas há espaço para melhorar!")
        else:
            print("\n📚 Continue aprendendo sobre a PortoEx!")
        
        print("\nObrigado por jogar o Quiz PortoEx!")

if __name__ == "__main__":
    quiz = PortoExQuiz()
    quiz.run_quiz()
