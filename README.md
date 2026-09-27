# 📊 Programa de Pesquisa de Satisfação

Um sistema interativo em console desenvolvido em Python para coletar, validar e analisar dados de pesquisas de satisfação de atendimento ao cliente de forma dinâmica e automatizada.

🚀 Sobre o Projeto
O Programa de Pesquisa de Satisfação foi criado para automatizar o processo de coleta de opiniões de clientes. O sistema valida dados de entrada em tempo real (como nomes, idades e opções de avaliação), calcula porcentagens estatísticas das respostas e exibe um relatório consolidado ao final de cada sessão, permitindo também reiniciar o ciclo quantas vezes o usuário desejar.

📸 Demonstração do Programa
Veja abaixo o programa rodando no terminal e exibindo o resultado final da pesquisa:

PESQUISA DE SATISFAÇÃO DE ATENDIMENTO 

Quantas pessoas serão entrevistadas nesta pesquisa? 10
Iniciando pesquisa com 10 clientes.

--- Entrevistado 1 de 10 ---
Digite o nome do cliente: alexandre
Digite a idade do cliente: 51
Opinião sobre o atendimento:
 [1] EXCELENTE
 [2] BOM
 [3] RUIM
Digite o número correspondente (1, 2 ou 3): 1
...
      RESULTADO FINAL DA PESQUISA    
Total de entrevistados nesta sessão: 10
a) Quantidade de respostas “EXCELENTE”: 4 (40.0%)
   Quantidade de respostas “BOM”: 4 (40.0%)
b) Quantidade de respostas “RUIM”: 2 (20.0%)

Deseja realizar uma nova pesquisa? (s/n): n
Encerrando o programa de pesquisas. Obrigado!

🛠️ Tecnologias Utilizadas

 Python: Linguagem principal utilizada para toda a lógica de programação, tratamento de exceções e manipulação de fluxo.

  Fórmula Utilizada para o CálculoPara obter a porcentagem de cada categoria de resposta (Excelente, Bom, Ruim), o programa utiliza a seguinte fórmula matemática em proporção:

  $$\text{Porcentagem} = \left( \frac{\text{Quantidade da Resposta}}{\text{Total de Entrevistados}} \right) \times 100$$

  O valor final é formatado para exibir apenas uma casa decimal ($\text{:.1f}\%$).
  
  ⚙️ Funcionalidades

  ✨ Validação Robusta: Impede entradas inválidas usando blocos try/except e loops condicionais.

  🔄 Sessões Múltiplas: Permite rodar várias pesquisas consecutivas sem precisar reiniciar o script manualmente.

  📋 Relatório Detalhado: Apresenta contagens absolutas e relativas (percentuais) de cada nível de satisfação.

  📥 Como Executar o Programa
Siga os passos abaixo para rodar o projeto em sua máquina:

Pré-requisitos: Certifique-se de ter o Python instalado em seu computador.

Baixar o código: Salve o código principal com o nome pesquisa.py em uma pasta de sua preferência.

Abrir o terminal: Abra o terminal (CMD, PowerShell ou terminal do VS Code) na pasta onde salvou o arquivo.

Executar: Digite o comando abaixo e aperte Enter:

python pesquisa.py

📄 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizá-lo, modificá-lo e melhorá-lo!

Desenvolvido com Python.