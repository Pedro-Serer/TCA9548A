# Feito por Pedro Serer

import smbus

linha_i2c = 1 # Número do barramento
barramento_i2c = smbus.SMBus(linha_i2c)

############################################
#                                          #
#  Função que escaneia a rede I2C na porta #
#  informada.                              #
#                                          #
############################################

def tca_reader(tca_endereco, porta, endereco):
    barramento_i2c.write_byte(tca_endereco, (1 << porta))
    
    try:
        barramento_i2c.write_quick(endereco)
        return "Endereço " + str(hex(endereco)) + " encontrado!"
    
    except:
        return "Não existe o endereço " + str(hex(endereco)) + " na porta " + str(porta)


print(tca_reader(0x70, 5, 0x6d))
