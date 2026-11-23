# Controle Financeiro (Linha de Comando)

Aplicativo de linha de comando em Python para organizar as finanças pessoais. Com ele, o usuário registra receitas e despesas e consulta o saldo atual, tudo por um menu interativo no terminal.

Projeto desenvolvido para a **Atividade Prática – AV2**, aplicando funções (`def`) para organizar cada funcionalidade do sistema.

## Integrantes

- Manoel de Moura Filho
- José Vinicius Barbosa

## Funcionalidades

| Opção | Descrição |
|---|---|
| 1 | **Adicionar receita**: registra uma descrição e um valor de entrada |
| 2 | **Adicionar despesa**: registra uma descrição e um valor de saída |
| 3 | **Ver saldo**: mostra o total de receitas, o total de despesas e o saldo |
| 4 | **Sair**: encerra o programa |

O programa valida o valor digitado: aceita vírgula ou ponto como separador decimal e recusa textos, zero e números negativos.

## Como executar

1. Tenha o [Python 3](https://www.python.org/downloads/) instalado.
2. Baixe o arquivo `NOME_DO_ARQUIVO.py` deste repositório.
3. No terminal, dentro da pasta do arquivo, execute:

```bash
python NOME_DO_ARQUIVO.py
```

## Exemplo de uso

```
=== CONTROLE FINANCEIRO ===
1) Adicionar receita
2) Adicionar despesa
3) Ver saldo
4) Sair
Escolha uma opção: 1
Descrição da receita: Salário
Valor (R$): 1500,50
Receita de R$ 1500.50 adicionada!
```

## Conceitos aplicados

- Funções com `def` (uma para cada funcionalidade)
- Retorno de valores com `return`
- Estruturas condicionais: `if`, `elif` e `else`
- Estrutura de repetição `while` para manter o menu ativo
- Entrada e saída de dados com `input()` e `print()`
- Listas e dicionários para armazenar os lançamentos
- Tratamento de erros com `try` / `except`

## Observação

Os dados ficam guardados apenas na memória enquanto o programa está aberto. Ao sair, as informações são perdidas.
