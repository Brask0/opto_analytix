# core/adc.py
"""
Module ADC pour Raspberry Pi utilisant le MCP3008 via SPI.
"""
import spidev
import time

class MCP3008:
    def __init__(self, spi_bus=0, spi_device=0, vref=3.3):
        self.vref = vref
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 1350000

    def read(self, channel):
        """
        Lit la valeur analogique sur le canal donné (0-7).
        Retourne une valeur entre 0 et 1023 (10 bits).
        """
        if not 0 <= channel <= 7:
            raise ValueError("Le canal doit être entre 0 et 7")
        # Protocole MCP3008 :
        # 1er octet : start bit (1)
        # 2e octet : single-ended (1), channel (3 bits), 0 (4 bits)
        # 3e octet : 0
        cmd = [1, (8 + channel) << 4, 0]
        r = self.spi.xfer2(cmd)
        value = ((r[1] & 3) << 8) | r[2]
        return value

    def read_voltage(self, channel):
        """
        Retourne la tension mesurée sur le canal (en volts).
        """
        raw = self.read(channel)
        return raw * self.vref / 1023.0

    def close(self):
        self.spi.close()
