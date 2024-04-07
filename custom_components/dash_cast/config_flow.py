from homeassistant.config_entries import ConfigFlow

from . import DOMAIN


class ConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    async def async_step_import(self, user_input=None):
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(title="DashCast", data={})
