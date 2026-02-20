import os
import time
os.system('clear')
# Cores ANSI
C = "\033[1;36m" # Ciano
W = "\033[1;37m" # Branco
Y = "\033[1;33m" # Amarelo
N = "\033[0m"    # Reset

def banner():
    os.system('clear')
    print(f"{C}##########################################################{N}")
    print(f"{C}#                                                        #{N}")
    # PAINEL em letras grandes
    print(f"{C}#  {W}██████╗  █████╗ ██╗███╗   ██╗███████╗██╗          {C}#{N}")
    print(f"{C}#  {W}██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║          {C}#{N}")
    print(f"{C}#  {W}██████╔╝███████║██║██╔██╗ ██║█████╗  ██║          {C}#{N}")
    print(f"{C}#  {W}██╔═══╝ ██╔══██║██║██║╚██╗██║██╔══╝  ██║          {C}#{N}")
    print(f"{C}#  {W}██║     ██║  ██║██║██║ ╚████║███████╗███████╗     {C}#{N}")
    print(f"{C}#  {W}╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝     {C}#{N}")
    # TL começando embaixo do L (alinhado à direita)
    print(f"{C}#                                                        #{N}")
    print(f"{C}#                    {W}████████╗██╗                {C}#{N}")
    print(f"{C}#                    {W}╚══██╔══╝██║                {C}#{N}")
    print(f"{C}#                    {W}   ██║   ██║                {C}#{N}")
    print(f"{C}#                    {W}   ██║   ██║                {C}#{N}")
    print(f"{C}#                    {W}   ██║   ███████╗           {C}#{N}")
    print(f"{C}#                    {W}   ╚═╝   ╚══════╝           {C}#{N}")
    print(f"{C}#                                                        #{N}")
    print(f"{C}##########################################################{N}")
    print(f"{C}#  {W}v(1.0)                             {Y}by J4XBOOST  {C}#{N}")
    print(f"{C}##########################################################{N}")
    print("\n")

if __name__ == "__main__":
    banner()
print ("")
print ("")
print ("=====================================================================================")
print (f"{C}<––––[ZPHISHER]{Y}-------------[01]")
print (f"{C}<––––[MAXPHISHER]{Y}-----------[02]")
print (f"{C}<––––[NMAP]{Y}-----------------[03]")
print (f"{C}<––––[RED_WAWK]{Y}-------------[04]")
print (f"{C}<––––[HAMMER]{Y}---------------[05]")
print ("=====================================================================================")
print ("")
print ("                           SAIR                    [00]")
print ("")
print (f"{C}<≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈KALI [06]≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print (f"{C}<≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ARCH [07]≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print (f"{C}<≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈DEBIAN [08]≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print (f"{C}<≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈UBUNTU [09]≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print ("=====================================================================================")
print ("")
print ("")
n1 = input(">>>  ")
if n1 == "01" or n1 == "1":
   os.system('pkg update -y && pkg upgrade -y && pkg install git php curl openssh -y && git clone --depth=1 https://github.com/htr-tech/zphisher.git && cd zphisher && chmod +x zphisher.sh && ./zphisher.sh')
elif n1 == "02" or n1 == "2":
    os.system('pkg update && pkg upgrade -y && pkg install python git php curl -y && termux-setup-storage && git clone https://github.com/KasRoudra/MaxPhisher && cd MaxPhisher && pip install -r files/requirements.txt && python maxphisher.py')
elif n1 == "03" or n1 == "3":
    os.system('nmap --help')
elif n1 == "04" or n1 == "4":
    os.system(' git clone https://github.com/Tuhinshubhra/RED_HAWK.git; cd RED_HAWK; php rhawk.php')
elif n1 == "05" or n1 == "5":
    os.system('pkg install python git -y && git clone https://github.com/cyweb/hammer && cd hammer && python hammer.py -h')
    time.sleep(1)
    print (f"{Y}EX: cd hammer && python hammer.py{N}")
elif n1 == "06" or n1 == "6":
    os.system('pkg install wget -y && wget -O install-nethunter-termux https://offs.ec/2MceZWr && chmod +x install-nethunter-termux && ./install-nethunter-termux')
elif n1 == "07" or n1 == "7":
    os.system('pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && chmod +x arch.sh && ./arch.sh')
    print(f'''{Y}🛠️ GUIA BLACKARCH NO TERMUX (2026)
1. INICIAR O SISTEMA
./start-arch.sh -> Executa o Arch Linux após instalado.

2. ATUALIZAR TUDO
pacman -Syu -> Atualiza pacotes e o núcleo do sistema.

3. BAIXAR O INSTALADOR BLACKARCH
curl -O https://blackarch.org/strap.sh -> Baixa o script de conversão.

4. ATIVAR REPOSITÓRIOS
chmod +x strap.sh && ./strap.sh -> Transforma o Arch em BlackArch.

5. LISTAR CATEGORIAS
pacman -Sg | grep blackarch -> Mostra grupos (ex: sniffing, spoofing).

6. VER TODAS AS FERRAMENTAS
pacman -Sgg | grep blackarch -> Lista todas as ferramentas (+2800).

7. BUSCAR UMA FERRAMENTA
pacman -Ss [nome] -> Procura uma ferramenta específica.

8. INSTALAR FERRAMENTA
pacman -S [nome] -> Baixa e instala a ferramenta escolhida.

9. REMOVER FERRAMENTA
pacman -Rns [nome] -> Remove a ferramenta e sobras inúteis.

10. LIMPAR MEMÓRIA
pacman -Sc -> Limpa o cache para economizar espaço no celular''')
elif n1 == "08" or n1 == "8":
    os.system('pkg update && pkg upgrade -y && pkg install proot-distro -y && proot-distro install debian && proot-distro login debian')
    print (f'''{Y}🐧 GUIA DEBIAN NO TERMUX (2026)
1. INICIAR O SISTEMA
./start-debian.sh -> Executa o Debian após a instalação.

2. ATUALIZAR REPOSITÓRIOS
apt update -> Atualiza a lista de pacotes disponíveis.

3. ATUALIZAR O SISTEMA
apt upgrade -y -> Instala as versões mais novas dos programas.

4. BUSCAR UMA FERRAMENTA
apt search [nome] -> Procura se uma ferramenta existe no Debian.

5. INSTALAR FERRAMENTA
apt install [nome] -y -> Baixa e instala a ferramenta (ex: nmap).

6. REMOVER FERRAMENTA
apt remove [nome] -> Desinstala o programa escolhido.

7. REMOVER SOBRAS
apt autoremove -> Apaga dependências que não servem mais para nada.

8. LIMPAR O CACHE
apt clean -> Apaga os arquivos de instalação para liberar espaço.

9. VER PACOTES INSTALADOS
dpkg --list -> Lista tudo que você já instalou no sistema.

10. INSTALAR O BÁSICO (RECOMENDADO)
apt install git python3 curl wget nano -y -> Instala o kit básico de sobrevivência.

💡 DICA DE OURO PARA DEBIAN:
Diferente do BlackArch, o Debian não vem com repositórios de "hacking" por padrão. Se você quiser as ferramentas do Kali Linux dentro do Debian, você precisa adicionar os repositórios do Kali manualmente no arquivo /etc/apt/sources.list.

Quer que eu te mande o comando para transformar esse Debian em um "Kali Minimal" adicionando as fontes oficiais?''')
elif n1 == "09" or n1 == "9":
    os.system('pkg update && pkg upgrade -y && pkg install proot-distro -y && proot-distro install ubuntu && proot-distro login ubuntu')
    print (f'''{Y}GUIA UBUNTU NO TERMUX (2026)
ENTRAR NO SISTEMA
proot-distro login ubuntu -> Acessa o terminal do Ubuntu após a instalação.

REINICIAR O AMBIENTE
exit && proot-distro login ubuntu -> Simula um reboot, fechando e abrindo o sistema para aplicar mudanças.

ATUALIZAR REPOSITÓRIOS
apt update -> Lê a lista de servidores para saber quais programas têm novas versões.

ATUALIZAR O SISTEMA COMPLETO
apt upgrade -y -> Baixa e instala todas as atualizações de segurança de 2026 de uma vez.

INSTALAR O KIT SOBREVIVÊNCIA
apt install git python3 python3-pip micro curl wget -y -> Instala o básico para programar e baixar arquivos.

BUSCAR UMA FERRAMENTA
apt search [nome] -> Verifica se o programa que você quer existe nos repositórios oficiais.

INSTALAR UMA FERRAMENTA
apt install [nome] -y -> Baixa e instala qualquer programa (Ex: apt install nmap -y).

REMOVER E LIMPAR TUDO
apt remove [nome] && apt autoremove -> Desinstala o programa e apaga as "sobras" que não servem mais.

LIBERAR ESPAÇO EM DISCO
apt clean -> Apaga os instaladores (.deb) baixados para economizar memória do celular.

VER PROCESSOS ATIVOS
top -> Mostra em tempo real o que o Ubuntu está rodando e quanto de RAM está usando.

💡 DICA DE OURO PARA UBUNTU:
O Ubuntu no Termux roda como Root por padrão, o que significa que você tem poder total. Se você precisar de uma ferramenta que só existe no ecossistema Python (muito comum em 2026), use o comando pip install [nome] logo após instalar o Python no passo 5.

Se o sistema reclamar de "externally-managed environment", use o parâmetro --break-system-packages ao final do comando pip.

Quer que eu te mande a sequência de comandos para transformar esse Ubuntu em um servidor Web completo (Nginx + PHP) para rodar sites no seu celular?''')
