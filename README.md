# 📊 Programa de Pesquisa de Satisfação

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

<p align="center">
  Um sistema interativo em console desenvolvido em Python para coletar, validar e analisar dados de pesquisas de satisfação de atendimento ao cliente de forma dinâmica e automatizada.
</p>

---

## 🚀 Sobre o Projeto

O **Programa de Pesquisa de Satisfação** foi criado para automatizar o processo de coleta de opiniões de clientes. O sistema valida dados de entrada em tempo real (como nomes, idades e opções de avaliação), calcula porcentagens estatísticas das respostas e exibe um relatório consolidado ao final de cada sessão, permitindo também reiniciar o ciclo quantas vezes o usuário desejar.

---

## 🛠️ Tecnologias Utilizadas

*   [![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/) **Python**: Linguagem principal utilizada para toda a lógica de programação, tratamento de exceções e manipulação de fluxo.

---

## 📐 Fórmula Utilizada para o Cálculo

Para obter a porcentagem de cada categoria de resposta (Excelente, Bom, Ruim), o programa utiliza a seguinte fórmula matemática em proporção:

$$\text{Porcentagem} = \left( \frac{\text{Quantidade da Resposta}}{\text{Total de Entrevistados}} \right) \times 100$$

O valor final é formatado para exibir apenas uma casa decimal ($\text{:.1f}\%$).

---

## ⚙️ Funcionalidades

*   ✨ **Validação Robusta**: Impede entradas inválidas usando blocos `try/except` e loops condicionais.
*   🔄 **Sessões Múltiplas**: Permite rodar várias pesquisas consecutivas sem precisar reiniciar o script manualmente.
*   📋 **Relatório Detalhado**: Apresenta contagens absolutas e relativas (percentuais) de cada nível de satisfação.

---

## 📥 Como Executar o Programa

Siga os passos abaixo para rodar o projeto em sua máquina:

1. **Pré-requisitos**: Certifique-se de ter o [Python](https://www.python.org/) instalado em seu computador.
2. **Baixar o código**: Salve o código principal com o nome `pesquisa.py` em uma pasta de sua preferência.
3. **Abrir o terminal**: Abra o terminal (CMD, PowerShell ou terminal do VS Code) na pasta onde salvou o arquivo.
4. **Executar**: Digite o comando abaixo e aperte `Enter`:

```bash
python pesquisa.py
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para utilizá-lo, modificá-lo e melhorá-lo!

---

<p align="center">Desenvolvido com 💙 e Python.</p>