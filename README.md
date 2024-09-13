# Máquina de Turing

Esta implementação da Máquina de Turing foi feito como projeto de Teoria da Computação na [UENP](https://uenp.edu.br/).

## Sobre 

Máquina de Turing realizada em python.  O simulador processa o estado inicial, o estados final e as transições do _arquivo.json_. Depois processa o arquivo _entrada.txt_, então é realizado o processamento, e por fim, o resultado da simulação é exibido no terminal. Se a entrada é aceita, o terminal mostrará **1**, caso contrário, mostrará **0**, e a fita depois de processada é escrita do no arquivo _saida.txt_.


- Exemplo do arquivo JSON _arquivo.json_

```json
{
    "initial" : 0,
    "final" : [4],
    "white" : "_",
    "transitions" : [
        {"from": 0, "to": 1, "read": "a", "write": "A", "dir":"+1"},
        {"from": 1, "to": 1, "read": "a", "write": "a", "dir":"+1"},
        {"from": 1, "to": 1, "read": "B", "write": "B", "dir":"+1"},
        {"from": 1, "to": 2, "read": "b", "write": "B", "dir":"-1"},
        {"from": 2, "to": 2, "read": "B", "write": "B", "dir":"-1"},
        {"from": 2, "to": 2, "read": "a", "write": "a", "dir":"-1"},
        {"from": 2, "to": 0, "read": "A", "write": "A", "dir":"+1"},
        {"from": 0, "to": 3, "read": "B", "write": "B", "dir":"+1"},
        {"from": 3, "to": 3, "read": "B", "write": "B", "dir":"+1"},
        {"from": 3, "to": 4, "read": "_", "write": "_", "dir":"-1"}      
    ]
}
```

- Exemplo do arquivo TXT de entrada _entrada.txt_

```txt
aaaaaabbbbbb
```

- Exemplo do arquivo TXT de saída _saida.txt_

```txt
AAAAAABBBBBB_
```

## Como usar

Para clonar o repositório

```bash
   git clone https://github.com/RafaelTomazGraciano/Maquina_de_Turing.git
```

Abra o terminal na pasta que está o repositório e então digite:

```bash
  python main.py 
```
