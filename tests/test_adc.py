# Test du module MCP3008 (nécessite le matériel connecté)
import pytest
from core.adc import MCP3008

def test_adc_read():
    adc = MCP3008()
    value = adc.read(0)
    assert 0 <= value <= 1023
    adc.close()

def test_adc_voltage():
    adc = MCP3008()
    voltage = adc.read_voltage(0)
    assert 0.0 <= voltage <= adc.vref
    adc.close()

# Pour exécuter : pytest tests/test_adc.py
# Nécessite un MCP3008 connecté sur SPI0 (GPIO du Raspberry Pi)
