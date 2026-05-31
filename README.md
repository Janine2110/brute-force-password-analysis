# Análise da Complexidade de Senhas com Força Bruta

## Sobre o Projeto

Este projeto foi desenvolvido como parte dos meus estudos em Cibersegurança para demonstrar como a complexidade de uma senha influencia diretamente a quantidade de combinações possíveis e o tempo necessário para um ataque de força bruta.

O programa gera todas as combinações possíveis para senhas de 4 caracteres utilizando diferentes conjuntos de caracteres e mede o tempo necessário para percorrer cada conjunto.

## Metodologia

Foram realizados três testes:

1. Apenas números (`0-9`)
2. Apenas letras (`a-z`, `A-Z`)
3. Letras, números e símbolos

Em cada cenário, o script gerou todas as combinações possíveis e registrou o tempo de execução.

## Resultados

| Conjunto de Caracteres     | Caracteres Disponíveis | Combinações Geradas |    Tempo |
| -------------------------- | ---------------------: | ------------------: | -------: |
| Apenas números             |                     10 |              10.000 | 0,0063 s |
| Apenas letras              |                     52 |           7.311.616 | 0,5095 s |
| Letras, números e símbolos |                     94 |          78.074.896 | 4,4604 s |

## Análise

Os resultados mostram como o número de combinações cresce rapidamente à medida que aumentamos a quantidade de caracteres disponíveis para formar uma senha.

Embora todos os testes tenham utilizado senhas de apenas 4 caracteres, a inclusão de letras, números e símbolos aumentou significativamente o espaço de busca e o tempo necessário para gerar todas as combinações possíveis.

Esse comportamento demonstra por que senhas mais complexas são mais resistentes a ataques de força bruta.

## Tecnologias Utilizadas

* Python 3
* itertools
* string
* time

## Conclusão

A segurança de uma senha não depende apenas de sua aparência complexa, mas principalmente da quantidade de combinações possíveis que um invasor precisa testar. Quanto maior o conjunto de caracteres utilizado, maior será o esforço computacional necessário para descobrir a senha por meio de força bruta.
