# 🤖 Automação de Cadastro de Produtos com Python e PyAutoGUI

Este projeto foi desenvolvido para demonstrar minha habilidade em criar um script para **automatizar tarefas operacionais e repetitivas** do dia a dia — seja na sua rotina pessoal ou no ambiente de trabalho — utilizando a linguagem Python. Utilizamos um banco com 293 fichas (cada ficha continha 7 colunas de itens, totalizando 2058 elementos) nos arquivos um arquivo pequeno, mas que já consumiria muito tempo e esforço pessoal. Foi um projeto construído durante o "intensivão" de Python da Hashtag Programação no ano de 2026.

> 📌 **Projeto de Portfólio / Estudo:** Esse processo foi feito para automatizar rotinas cansativas, eliminar erros de digitação e automação de fluxos de login e cadastro contínuo de dados.

---

## 💡 Sobre o Projeto

Já imaginou quanto tempo perde a realizar tarefas manuais todos os dias? 

Imagine que você tem que cadastrar produtos novos todos os dias, preencher um formulário constante e os campos são sempre os mesmos, preenchendo 4, 5, 6 ou até mais informações por cada um deles:
- **Processo Manual:** Leva horas, é extremamente cansativo e possui um risco elevado de erros (como digitar um valor errado ou colar uma informação no campo incorreto devido ao cansaço da repetição).
- **Processo Automatizado:** O script carrega uma base de dados em ficheiro CSV (`produtos.csv`), abre o navegador, efetua o login no sistema (sem Captcha) e realiza o cadastro de cada produto campo a campo de forma rápida e precisa.

---

## ⚡ Principais Benefícios da Automação

- ⏳ **Economia Massiva de Tempo:** Permite deixar a automação a correr enquanto foca a sua atenção em atividades estratégicas — ou até enquanto sai para o almoço e regressa com todos os registos concluídos!
- 🎯 **Redução Drástica de Erros:** Por usar uma lista pré-estabelecida, contanto que sua lista esteja correta, ele não fará um erro de digitação.
- 📈 **Aumento da Produtividade:** O script realiza essa tarefa em um "processo de máquina", que é muito mais veloz do que um humano conseguiria fazer.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **`pyautogui`:** Biblioteca para simular cliques do mouse, navegação do cursor, rolagem de tela e digitação no teclado.
- **`pandas`:** Leitura e estruturação dos dados provenientes da tabela `produtos.csv`.
- **`openpyxl`:** Suporte ao processamento de dados e tabelas em Python.
- **`time`:** Gestão de pausas e tempos de espera durante o carregamento de páginas.

---

## 🔄 Lógica de Funcionamento do Código

O fluxo de execução do script segue os seguintes passo:

1. **Abertura do Sistema:** O bot aciona o menu do sistema operativo, abre o navegador (eu utilizo o Brave, então troque por aquele que você utiliza) e acessa o endereço web que será feito o cadastro.
2. **Autenticação:** Clica no campo de entrada e preenche as credenciais de e-mail e senha para realizar o login.
3. **Leitura da Base de Dados:** Importa os dados contidos na tabela `produtos.csv`.
4. **Preenchimento Sequencial:** Interage com o formulário e preenche iterativamente todos os campos de cada produto:
   - Código
   - Marca
   - Tipo
   - Categoria
   - Preço Unitário
   - Custo
   - Observações (inclui verificação para ignorar valores nulos/`nan` do Python)
5. **Submissão e Repetição:** Submete o formulário, reposiciona a tela com uma rolagem (`scroll`) e repete o processo até concluir todos os registos.

---

## 📋 Pré-requisitos

Antes de executar a automação, certifique-se de ter instalado:

1. **Python 3.10+**
2. As bibliotecas indicadas no arquivo `requirements.txt`.
3. A base de dados `produtos.csv` acessível na pasta indicada no script.
4. O arquivo `auxiliar.py` serve para pegar a posição do mouse exato para o site que eu utilizei. Isso é totalmente substituível se você souber a posição ou encontrá-la de outra forma.

---

## 🔧 Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/zacmarques/AutomacaoPython_RPA.git](https://github.com/zacmarques/AutomacaoPython_RPA.git)