## OptoAnalytix

Plateforme d'acquisition et d'analyse de signaux optoélectroniques pour Raspberry Pi 3 A+ (OS Lite).

### Installation

1. Cloner le dépôt
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurer le fichier `config.yaml`

### Utilisation

```bash
python main.py --config config.yaml
```

### Dépendances principales

- PyYAML
- numpy
- (Ajouter d'autres selon les modules utilisés)

### Objectifs

- Acquisition fiable de signaux
- Analyse FFT, lissage, etc.
- Sortie console, fichier, etc.
- Extensible et optimisé pour Raspberry Pi
