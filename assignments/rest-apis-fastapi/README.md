# 📘 Assignment: Criando APIs REST com FastAPI

## 🎯 Objective

Construir uma API REST com FastAPI para criar, consultar, atualizar e remover itens, usando modelos Pydantic para validar os dados.

## 📝 Tasks

### 🛠️ Criar a API e Endpoints de Leitura

#### Descrição
Crie a aplicação FastAPI e implemente os endpoints que listam e consultam os itens armazenados em memória.

#### Requisitos
O programa concluído deve:

- Ter um endpoint `GET /items` que retorna todos os itens
- Ter um endpoint `GET /items/{item_id}` que retorna um item específico
- Retornar status `404` quando o `item_id` não existir

### 🛠️ Adicionar Itens com Validação

#### Descrição
Crie um modelo Pydantic para os dados de um item e use-o para cadastrar novos itens.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic com os campos `name` (texto), `price` (número maior que zero) e `in_stock` (booleano)
- Ter um endpoint `POST /items` que cria um item e retorna status `201`
- Retornar status `422` automaticamente quando os dados enviados forem inválidos

Exemplo de corpo da requisição:

```json
{
  "name": "Caneta",
  "price": 2.5,
  "in_stock": true
}
```

### 🛠️ Atualizar e Remover Itens

#### Descrição
Implemente as operações de atualização e remoção, mantendo as respostas de erro consistentes.

#### Requisitos
O programa concluído deve:

- Ter um endpoint `PUT /items/{item_id}` que substitui os dados de um item existente
- Ter um endpoint `DELETE /items/{item_id}` que remove um item e retorna status `204`
- Retornar status `404` nas operações de atualização e remoção quando o item não existir
