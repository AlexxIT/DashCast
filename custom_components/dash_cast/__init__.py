import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.core import ServiceCall, HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.entity_component import DATA_INSTANCES
from pychromecast import Chromecast
from pychromecast.controllers.dashcast import DashCastController

DOMAIN = "dash_cast"

LOAD_URL_SCHEMA = cv.make_entity_service_schema(
    {
        vol.Required("url"): cv.string,
        vol.Optional("force", default=False): cv.boolean,
        vol.Optional("reload_seconds", default=0): cv.positive_int,
    }
)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    dashs = {}

    async def play_media(call: ServiceCall):
        kwargs = dict(call.data)
        entity_ids = kwargs.pop(ATTR_ENTITY_ID)

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

    hass.services.async_register(DOMAIN, "load_url", play_media, LOAD_URL_SCHEMA)

    return True


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    return True
