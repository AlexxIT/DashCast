# DashCast for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

This [Home Assistant](https://www.home-assistant.io/) service allows you to cast a website to a Google [Chromecast](https://en.wikipedia.org/wiki/Chromecast).

**PS.** All thanks to [@stestagg](https://github.com/stestagg), developer of [DashCast](https://stestagg.github.io/dashcast/) app for Google Chromecast.

## Installation

**Method 1.** [HACS](https://hacs.xyz/) custom repo:

> HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: `AlexxIT/DashCast`, Category: Integration > Add > wait > DashCast > Install

**Method 2.** Manually copy `dash_cast` folder from [latest release](https://github.com/AlexxIT/DashCast/releases/latest) to `/config/custom_components` folder.

## Configuration

**Method 1.** GUI:

> Configuration > Integrations > Add Integration > **DashCast**

If the integration is not in the list, you need to clear the browser cache.

**Method 2.** YAML:

```yaml
dash_cast:
```

## Usage

New service `dash_cast.load_url`:

```yaml
service: dash_cast.load_url
data:
  entity_id: media_player.hall_tv
  url: https://www.home-assistant.io/
  force: true  # use this option if iframe blocking is enabled on the site
  reload_seconds: 60  # reload page every X seconds
```
