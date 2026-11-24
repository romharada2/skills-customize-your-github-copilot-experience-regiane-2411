# 📘 Assignment: Funções e Módulos

## 🎯 Objective

Criar funções em Python com parâmetros e valores de retorno, e organizar o código em módulos que podem ser importados em outros arquivos.

## 📝 Tasks

### 🛠️ Criar uma Função Simples

#### Descrição
Defina uma função que exibe uma mensagem de saudação e chame-a no programa principal.

#### Requisitos
O programa concluído deve:

- Definir a função `saudar()` sem parâmetros
- Exibir uma mensagem de saudação ao ser chamada
- Chamar `saudar()` pelo menos uma vez no programa principal

### 🛠️ Funções com Parâmetros e Retorno

#### Descrição
Crie funções que recebem dados, realizam um cálculo e devolvem o resultado com `return`.

#### Requisitos
O programa concluído deve:

- Definir a função `calcular_area_retangulo(largura, altura)` que retorna a área do retângulo
- Definir a função `calcular_media(notas)` que recebe uma lista de números e retorna a média
- Usar o valor retornado pelas funções para exibir os resultados

Exemplo de uso:

```python
area = calcular_area_retangulo(4, 3)
print(area)  # 12
```

### 🛠️ Organizar Funções em um Módulo

#### Descrição
Mova as funções para um arquivo separado e importe-as no programa principal.

#### Requisitos
O programa concluído deve:

- Criar um arquivo `calculadora.py` com as funções `calcular_area_retangulo` e `calcular_media`
- Importar essas funções em `main.py` usando `from calculadora import ...`
- Executar `main.py` sem erros e exibir os mesmos resultados da tarefa anterior
