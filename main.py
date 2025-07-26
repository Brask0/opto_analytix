import argspace
import yaml
from sensors import SENSOR_MAP
from analysis import fft, smoothing
from outpu import consol, web_server
from core import logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    log = logger.setup_logger()

    # Sensor setup
    SensorClass = SENSOR_MAP[config["sensor"]["type"]]
    sensor = SensorClass(channel = config["sensor"]["channel"], adc=None)   # Init ADC avant

    # Output setup
    output = console if config["output"]["type"] == "console" else web_server

    # Acquisition
    sampling_rate = config["acquisition"]["duration"]
    values = []

    for _ in range(sampling_rate * duration):
        val = sensor.read()
        values.append(val)

    if config["analysis"].get("fft"):
        result = fft.compute_fft(values, sampling_rate)

    else:
        result = values

    output.display(result)
    log.info("Acquisition terminée")

if __name__ == "__main__":
    main()
