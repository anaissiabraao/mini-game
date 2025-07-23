# Quiz PortoEx

Um jogo de quiz interativo sobre a PortoEx, desenvolvido para testar conhecimentos sobre os serviços e informações da empresa.

## 🚀 Como Executar Localmente

1. Certifique-se de ter o Python 3.8+ instalado
2. Clone este repositório
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Execute o servidor:
   ```
   python server.py
   ```
5. Acesse no navegador: http://localhost:8080

## 🛠️ Estrutura do Projeto

```
.
├── static/                 # Arquivos estáticos (HTML, CSS, JS, imagens)
│   ├── index.html         # Página principal do quiz
│   ├── styles.css         # Estilos do quiz
│   ├── script.js          # Lógica do quiz
│   └── portoex-logo.png   # Logo da PortoEx
├── server.py             # Servidor Python
├── mini_game.py          # Versão em console do jogo (opcional)
├── requirements.txt      # Dependências do Python
└── README.md            # Este arquivo
```

## 🚀 Como Implantar no Render

1. Crie uma nova conta no [Render](https://render.com/)
2. Clique em "New" e selecione "Web Service"
3. Conecte seu repositório do GitHub
4. Configure as seguintes configurações:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:CORSRequestHandler`
5. Clique em "Create Web Service"

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
