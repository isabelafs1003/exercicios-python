# 9. Crie um programa para ler o tamanho de um arquivo em GBytes e a velocidade de download de uma rede em Mbits por segundo. Após as leituras, calcular e mostrar o tempo em minutos gasto para transferir o arquivo pela rede.
# 1 Byte = 8 bits
# 1 GByte = 1024 MBytes

print("\nCalcule o tempo gasto para um Download: ")

tam = int(input("\nTamanho do Arquivo (GByte): "))
vel = int(input("\nVelocidade da Rede (Mbits/s): "))

tam_mb = tam * 1024 * 8 # converte o tamanho em Mbit
ts = tam_mb // vel # tempo em segundos (apenas o valor inteiro para descartar os décimos de seg)
tm = ts // 60 # calcula os minutos
ts %= 60 # calcula os segundos que restaram (ts = ts % 60)

print(f'\nTempo gasto de download = {tm} min e {ts} seg')
