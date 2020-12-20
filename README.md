# DashCast for Home Assistant

Эта служба Home Assistant позволяет транслировать веб-сайт на Google Chromecast.
This Home Assistant service allows you to cast a website to a Google Chromecast.

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
