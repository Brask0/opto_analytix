# main.py - Point d'entrée du projet OptoAnalytix
# Ce script gère la configuration, l'acquisition, l'analyse et la sortie des données de capteurs optoélectroniques.

import argparse  # Pour la gestion des arguments en ligne de commande
import yaml       # Pour le chargement du fichier de configuration YAML
import time       # Pour la gestion du temps d'échantillonnage
from sensors import SENSOR_MAP  # Dictionnaire associant les types de capteurs à leur classe
from analysis import fft  # Module d'analyse (FFT)
from output import console           # Module de sortie console
from core import logger              # Module de gestion des logs


def main():
    # Analyse les arguments de la ligne de commande (permet de spécifier un fichier de config personnalisé)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    # Chargement du fichier de configuration YAML
    try:
        with open(args.config, 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print(f"Erreur lors du chargement du fichier de configuration: {e}")
        # Correction 4 : log aussi l'erreur
        import logging
        logging.basicConfig(level=logging.ERROR)
        logging.error(f"Erreur lors du chargement du fichier de configuration: {e}")
        return

    # Initialisation du logger (enregistre les logs dans un fichier et/ou la console)
    log = logger.setup_logger()

    # Initialisation du capteur, de la sortie et des paramètres d'acquisition
    try:
        SensorClass = SENSOR_MAP[config["sensor"]["type"]]  # Sélectionne la classe de capteur selon la config
        # Correction 2 : Placeholder ADC, à remplacer par une vraie instance ADC (ex: MCP3008)
        adc = None
        # Exemple d'intégration future :
        # from core.adc import MCP3008
        # adc = MCP3008(channel=config["sensor"].get("adc_channel", 0))
        sensor = SensorClass(channel=config["sensor"]["channel"], adc=adc)
        # Correction 3 : Préparer d'autres modules de sortie
        if config["output"]["type"] == "console":
            output = console
        # elif config["output"]["type"] == "file":
        #     from output import file_output
        #     output = file_output
        else:
            output = None
        sampling_rate = config["acquisition"]["sampling_rate"]  # Fréquence d'échantillonnage
        duration = config["acquisition"]["duration"]            # Durée d'acquisition
    except KeyError as e:
        log.error(f"Clé manquante dans la configuration: {e}")
        return

    # Boucle d'acquisition : lit les valeurs du capteur à la fréquence et durée spécifiées
    values = []
    total_samples = sampling_rate * duration
    for _ in range(total_samples):
        try:
            val = sensor.read()  # Lecture d'une valeur du capteur
            values.append(val)
        except Exception as e:
            log.error(f"Erreur lors de la lecture du capteur: {e}")
            continue
        # Correction 5 : Respect du taux d'échantillonnage
        time.sleep(1.0 / sampling_rate)

    # Analyse des données (optionnelle, selon la config)
    analysis_cfg = config.get("analysis", {})
    if analysis_cfg.get("fft"):  # Si l'analyse FFT est demandée
        result = fft.compute_fft(values, sampling_rate)
    else:
        result = values  # Sinon, on garde les valeurs brutes

    # Affichage ou sortie des résultats
    if output:
        output.display(result)
    else:
        print(result)
    log.info("Acquisition terminée")

# Point d'entrée du script
if __name__ == "__main__":
    main()
