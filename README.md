# IP Sensor

This is a simple implementation of binary sensor which checks the presense of IP address in network.

### Installation

Copy this folder to `<config_dir>/custom_components/ip_sensor/`.

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
binary_sensor:
  platform: ip_sensor
  scan_interval: 5
  hosts:
    router: 192.168.2.1        # device => binary_sensor.router
    toshiba_tv: 192.168.2.149  # device => binary_sensor.toshiba_tv
```
