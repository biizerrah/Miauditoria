# 🐈 MiauDitoria - Sistema de Gerenciamento de Gatinhos

Este projeto é um sistema simples de gerenciamento de cadastro de gatinhos desenvolvido em **Python**. Ele permite realizar as operações básicas de **CRUD** (Criação, Leitura/Listagem, Consulta e Remoção) de registros, organizando os dados por sexo (Macho e Fêmea).

## 💡 Visão Geral e Estrutura de Dados

O sistema utiliza estruturas de dados nativas do Python para armazenar os registros em memória:

* **Dicionário Principal (`todos_os_gatos`):** Separa os gatinhos por gênero, usando as chaves `'f'` (Fêmea) e `'m'` (Macho).
* **Listas:** Usadas para armazenar os registros dentro de cada categoria de sexo.
* **Tuplas:** Cada registro individual de gatinho é armazenado como uma tupla `(Nome, Cor)`.

A estrutura em memória tem o seguinte formato:

```python
todos_os_gatos = {
    'f': [
        ('luna', 'branca'), 
        ('nina', 'laranja')
    ],
    'm': [
        ('frajola', 'preto e branco'),
        ('thor', 'cinza')
    ]
}
 ```

## 🚀 Como Rodar o Projeto
Para executar este projeto em sua máquina, siga os passos abaixo:

 - 1. Pré-requisitos: 
Certifique-se de ter o Python 3 instalado em seu sistema operacional.

 -  2. Clonar o Repositório:
Abra seu terminal ou prompt de comando e clone o projeto:

```
git clone https://github.com/biizerrah/Miauditoria
```

 - 3. Executar o Programa:
Execute o script principal usando o Python:

```
python main.py
```
O menu interativo será exibido no console, permitindo que você navegue pelas opções.

## ⚙️ Funcionalidades (Menu Principal)

| Opção | Comando | Descrição |
| :---: | :------ | :-------- |
| **1** | Cadastrar Item | ➕ Adiciona um novo gatinho (Nome, Cor, Sexo) ao sistema. |
| **2** | Listar Itens | 📋 Exibe todos os gatinhos cadastrados, separados por Macho e Fêmea. |
| **3** | Consultar Item | 🔍 Busca e exibe os detalhes de um gatinho específico pelo nome. |
| **4** | Remover Item | 🗑️ Remove um gatinho da lista pelo nome. |
| **5** | Sair | 🚪 Encerra o programa. |



Project - Tati Bezerra