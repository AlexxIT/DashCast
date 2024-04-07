from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.core import ServiceCall, HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.entity_component import DATA_INSTANCES
from pychromecast import Chromecast
from pychromecast.controllers.dashcast import DashCastController

DOMAIN = "dash_cast"

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    dashs = {}

    async def play_media(call: ServiceCall):
        entity_ids = call.data.get(ATTR_ENTITY_ID)
        kwargs = {
            k: v
            for k, v in call.data.items()
            if k in ("url", "force", "reload_seconds")
        }

        for entity in hass.data[DATA_INSTANCES]["media_player"].entities:
            if entity.entity_id not in entity_ids:
                continue

            dash: DashCastController = dashs.get(entity.entity_id)
            if not dash:
                chromecast: Chromecast = getattr(entity, "_chromecast")
                if chromecast:
                    dashs[entity.entity_id] = dash = DashCastController()
                    chromecast.register_handler(dash)
                else:
                    return

            dash.load_url(**kwargs)

    hass.services.async_register(DOMAIN, "load_url", play_media)

    return True


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    return True
