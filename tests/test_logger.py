# Test du module core.logger
from core import logger

def test_logger_setup():
    log = logger.setup_logger()
    log.info("Test info")
    log.error("Test error")
    assert log is not None
