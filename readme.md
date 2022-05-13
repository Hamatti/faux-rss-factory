# Faux RSS Factory

A Python app that has a plugin interface to scrape individual blogs that don't provide an RSS feed.

## General workflow idea

### Parsing with plugins

See [plugins/readme.md](plugins/readme.md) for documentation on how to build plugins.

### Storage

SQLite database against which we can match and tag if something is new.

### WebUI

Simple web UI that shows all the new blog posts.
