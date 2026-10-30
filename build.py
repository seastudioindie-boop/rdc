#!/usr/bin/env python3
"""Arma index.html (un solo archivo) a partir de src/."""
import json, pathlib
R = pathlib.Path(__file__).parent
html = (R/'src/app.html').read_text(encoding='utf-8')
geo = json.loads((R/'src/colombia-geo.json').read_text(encoding='utf-8'))
html = html.replace('/*__LEAFLET_CSS__*/', (R/'src/leaflet.min.css').read_text(encoding='utf-8'))
html = html.replace('/*__APP_CSS__*/', (R/'src/app.css').read_text(encoding='utf-8'))
html = html.replace('/*__GEO__*/null', json.dumps(geo, ensure_ascii=False, separators=(',', ':')))
html = html.replace('/*__APP_JS__*/', (R/'src/app.js').read_text(encoding='utf-8'))
# Versión fragmento para publicar como Artifact (el visor agrega doctype y head)
(R/'dist').mkdir(exist_ok=True)
(R/'dist/artifact.html').write_text(html, encoding='utf-8')
# Versión completa para GitHub Pages o para abrir desde el disco
full = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>\n'
        + html + '\n</html>\n')
(R/'index.html').write_text(full, encoding='utf-8')
print('index.html', round(len(full.encode())/1024), 'KB')
