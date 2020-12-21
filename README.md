# DashCast for Home Assistant

This Home Assistant service allows you to cast a website to a Google Chromecast.


Installation with HACS can be done by adding the repository using the "Add Custom Repository"
feature. You must also add a top-level line to your `configuration.yaml` enabling this service.

```yaml
dash_cast:
```


Пример использования:
Usage example:

```yaml
script:
  show_weather:
    alias: Покажи погоду
    sequence:
      - service: dash_cast.load_url
        data:
          entity_id: media_player.hall_tv
          url: http://yandex.ru/pogoda/moscow
          force: true
```
