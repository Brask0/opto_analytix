import logging

def setup_logger(name="opto"):
    logging.basicConfig(level=logging.INFO,
                        format = '[%(asctime)s] %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("data/logs/log.txt"), logging.StreamHandler()])
    return logging.getLogger(name)
