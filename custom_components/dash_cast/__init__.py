from homeassistant.components.media_player import DOMAIN as MP_DOMAIN
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.core import ServiceCall
from homeassistant.helpers.entity_component import DATA_INSTANCES

from pychromecast.controllers.dashcast import DashCastController

DOMAIN = 'dash_cast'


async def async_setup(hass, hass_config):
    dashs = {}

    async def play_media(call: ServiceCall):
        entity_ids = call.data.get(ATTR_ENTITY_ID)
        url = call.data.get('url')
        force = call.data.get('force', False)

        for entity in hass.data[DATA_INSTANCES][MP_DOMAIN].entities:
            if entity.entity_id in entity_ids:
                dash = dashs.get(entity.entity_id)
                if not dash:
                    dashs[entity.entity_id] = dash = DashCastController()
                    entity._chromecast.register_handler(dash)
                dash.load_url(url, force)

    hass.services.async_register(DOMAIN, 'load_url', play_media)

    return True


async def async_setup_entry(hass, entry):
    return True
