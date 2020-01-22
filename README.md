# DashCast for Home Assistant

Пример использования.

```yaml
service:
  show_weather:
    alias: Покажи погоду
    sequence:
      - service: dash_cast.load_url
        data:
          entity_id: media_player.hall_tv
          url: http://yandex.ru/pogoda/moscow
          force: true
```