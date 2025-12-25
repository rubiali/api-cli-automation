# API CLI Automation

CLI em Python para consumo de uma API pública via linha de comando, com suporte a
limite de resultados, logging e salvamento opcional em arquivo JSON.

Projeto focado em demonstrar organização de código, consumo de APIs REST
e automação simples em Python.

---

## Tecnologias

- Python 3.8+
- Requests
- python-dotenv
- logging (stdlib)

---

## Funcionalidades

- Consumo de API pública via HTTP
- Execução via terminal (CLI)
- Limite de resultados por argumento
- Salvamento opcional em arquivo JSON
- Tratamento de erros
- Logs informativos

---

## Estrutura do Projeto

api-cli-automation/
├── cli.py
├── services.py
├── storage.py
├── config.py
├── logger.py
├── requirements.txt
└── README.md

---

## Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/rubiali/api-cli-automation.git
cd api-cli-automation
```

### 2. Criar ambiente virtual (opcional, recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate   # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

---

## Exemplos de uso

### Executar normalmente
```bash
python cli.py
```

### Limitar quantidade de resultados
```bash
python cli.py --limit 3
```

### Salvar resultado em arquivo JSON
```bash
python cli.py --limit 5 --save users.json
```

---

## Configuração

A URL da API pode ser configurada via variável de ambiente:

```env
API_URL=https://jsonplaceholder.typicode.com/users
```

Caso não seja definida, o projeto utiliza um valor padrão.

---
