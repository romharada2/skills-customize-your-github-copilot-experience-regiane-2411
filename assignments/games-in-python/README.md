
# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Construir o clássico jogo de adivinhar palavras em Python, praticando manipulação de strings, loops, condicionais e seleção aleatória.

## 📝 Tasks

### 🛠️ Selecionar a Palavra e Exibir o Progresso

#### Descrição
Escolha uma palavra aleatória de uma lista predefinida e mostre ao jogador o progresso atual, com as letras ocultas representadas por `_`.

#### Requisitos
O programa concluído deve:

- Selecionar palavras aleatoriamente de uma lista predefinida
- Exibir a palavra oculta no formato `_ _ _`, com as letras já adivinhadas reveladas

Exemplo de saída:

```text
Palavra: _ _ _ _ _ _
```

### 🛠️ Receber Palpites e Controlar as Tentativas

#### Descrição
Leia as letras digitadas pelo jogador, atualize o progresso e controle quantas tentativas incorretas ainda restam.

#### Requisitos
O programa concluído deve:

- Aceitar palpites de letras do usuário
- Atualizar e mostrar o progresso sempre que uma letra correta for informada
- Rastrear e exibir o número de tentativas incorretas restantes

### 🛠️ Encerrar o Jogo e Exibir o Resultado

#### Descrição
Defina quando a partida termina e informe ao jogador se ele venceu ou perdeu.

#### Requisitos
O programa concluído deve:

- Encerrar quando a palavra for adivinhada completamente
- Encerrar quando as tentativas incorretas se esgotarem
- Exibir mensagem de vitória ou de derrota ao final da partida