
# 🧠 Porypy

> Um bot modular em Python para o Discord com foco em **organização pessoal**, **planejamento financeiro** e **gestão de metas**, incluindo a jornada até o **primeiro imóvel**.

<br><br>

## ✨ Visão Geral

O **Porypy** é um bot de organização pessoal que roda no Discord, permitindo ao usuário registrar tarefas, definir metas, acompanhar finanças e planejar sua vida — tudo de forma acessível, conversando diretamente com um bot.

🎯 **Objetivo inicial:** auxiliar pessoas que desejam comprar seu primeiro imóvel a se organizarem financeiramente e por metas.  
⚙️ **Escopo atual:** expandido para cobrir organização pessoal e planejamento de rotina.

<br><br>

## 🖼️ Identidade Visual

**Ícone oficial do Porypy:**

<img src="assets/porypy_icon.svg" alt="Porypy Icon" width="100" />
<img src="assets/porypy_icon_with_checklist.svg" alt="Porypy Icon" width="100" />

<br><br>

## 📁 Estrutura do Projeto

```
PorypyBot/
│
├── bot.py               # Ponto de entrada para o bot
├── core/                # Contém o código principal do bot
│   ├── client.py        # Cliente do bot, com a definição do comando e eventos
│   │   config.py        # Configurações, incluindo o token
│   └── __init__.py      # Marca a pasta como um módulo
│
├── extensions/          # Contém as extensões de comandos (comandos personalizados)
│   └── commands/
│       ├── __init__.py  # Marca a pasta como um módulo      
│       └── basic.py     # Comandos básicos (exemplo: !ping, !help)
│
├── Dockerfile           # Arquivo para construção da imagem Docker
├── docker-compose.yml   # Docker Compose para facilitar execução com Docker
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos para ignorar no controle de versão
└── README.md            # Documentação do projeto
```

<br><br>

## 🧩 Funcionalidades

### ✅ Já Implementadas
| Ícone | Módulo | Descrição |
|------|--------|-----------|
| ⚙️ | `core.py` | Comandos utilitários (ping, ajuda) |

### 🚧 Em Desenvolvimento
| Ícone | Módulo | Descrição |
|------|--------|-----------|
| 📝 | `tasks.py` | Gerenciamento de tarefas |
| 🏠 | `housing.py` | Cadastro e comparação de imóveis |
| 🎯 | `goals.py` | Definição de metas e progresso |
| 📅 | `planner.py` | Adição de eventos e lembretes |
| 💰 | `finances.py` | Rastreamento de entradas e despesas |
| 🗒️ | `notes.py` | Anotações rápidas |
| 🧑‍💼 | `settings.py` | Personalização do bot por usuário |
| 🌐 | `config.py` | Suporte a múltiplos servidores e usuários |

<br><br>

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Propósito |
|-----------|-----------|
| ![Python](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg) | Lógica do bot |
| ![Discord.py](https://img.shields.io/badge/discord.py-2.x-blue?logo=discord&style=flat-square) | Biblioteca principal |
| ![SQLite](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg) | Armazenamento de dados local |
| ![Docker](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg) | Empacotamento do projeto |
| [APScheduler](https://apscheduler.readthedocs.io/en/latest/) | Agendador de lembretes |
---

## 🧭 Escopo Expandido

Além da busca pelo primeiro imóvel, o bot se propõe a:

- ✅ Ajudar no planejamento pessoal de rotina
- ✅ Manter finanças organizadas com controle simples
- ✅ Permitir acompanhamento de metas de curto e longo prazo
- ✅ Gerenciar links, eventos e observações úteis
- ✅ Operar totalmente via comandos no Discord

<br><br>

## 🚀 Como Rodar Localmente

```bash
git clone https://github.com/seu-usuario/porypy.git
cd porypy
docker build -t porypy .
docker run --env-file .env porypy
```

> 💡 Configure o seu token e prefixo em `config.py`

<br><br>

## 📌 Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para detalhes.

<br><br>

## 💬 Contato

Desenvolvido por **[Mateus-Mota]**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/mateusmotaa/)  
[![Discord](https://img.shields.io/badge/Discord-Bot_Porypy-5865F2?logo=discord&style=flat-square)](https://discord.com/oauth2/authorize?client_id=1368781797428695090)

---
