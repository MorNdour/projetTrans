import time
import board
import adafruit_dht
import psutil

def temperatureHumidite():
    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
    sensor = adafruit_dht.DHT11(board.D17)
    global temp
    global humididy
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        sensor.exit()
    time.sleep(2.0)
    return temp,humidity

print(temperatureHumidite())
