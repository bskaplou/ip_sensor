import logging
from homeassistant.helpers.entity import Entity
from pythonping import ping

logger = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    entities = []
    for name, ip in config['hosts'].items():
        entities.append(IPSensor(name, ip))

    add_entities(entities)

class IPSensor(Entity):
    def __init__(self, name, ip):
        self._name = name
        self._ip = ip
        self._state = None
        self._is_on = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def state_attributes(self):
        return {'ip_address': self._ip}

    @property
    def device_class(self):
        return 'connectivity'

    @property
    def is_on(self):
        return self._is_on

    def update(self):
        result = ping(self._ip, count=1, timeout=0.1)
        self._is_on = result.success()
        self._state = 'on' if result.success() else 'off'
