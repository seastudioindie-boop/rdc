# R.D.C · Plataforma de información climática

Reto 2 de **TECNOHACK 2026** (SENA TecnoParque Bogotá + IDEAM). Equipo S.E.A.

La plataforma ubica cada estación en su coordenada sobre un mapa GIS de Colombia y muestra sus datos.

## Qué pide el reto y dónde está

| Requisito del IDEAM | En R.D.C |
| --- | --- |
| Página de login que autentique usuarios | Pantalla de ingreso con usuario y contraseña. Las contraseñas se guardan cifradas (PBKDF2-SHA-256, 150 000 iteraciones, sal por usuario). Se bloquea 30 s después de 5 intentos fallidos. |
| Al ingresar, mapa GIS de Colombia | Mapa Leaflet con los 32 departamentos y Bogotá D.C. Coordenadas en vivo del cursor (decimal y grados-minutos-segundos) y el departamento debajo. |
| Crear estación con coordenadas y verla en el mapa | Botón **Nueva estación**: nombre, código, tipo, latitud y longitud (decimal o 4°36'35"N). También se puede tocar el mapa. Círculo = meteorológica, cuadrado = pluviométrica, rombo = hidrológica. |
| Al hacer clic en la estación, ver sus variables | Ventana emergente con cada variable, su último valor y la fecha. |
| Crear variables: precipitación, temperatura, humedad, presión, viento, radiación | Catálogo con los códigos que usa Polaris: PREC, TEMA, HUMA, PRES, VELV, DIRV, RADG. También variables propias (por ejemplo, nivel del río). |
| Cargar un CSV y ver los datos en la estación | Botón **Cargar datos CSV** con revisión antes de guardar. Acepta CSV de Excel en español, el CSV de TRIADA PLUVIO y el ejemplo de una línea de la reunión. |
| Datos en una base de datos | IndexedDB, la base de datos del navegador. Respaldo y restauración en JSON. |
| Lluvia cada 10 minutos (forma de trabajo del IDEAM) | Gráficas en datos crudos o agregados cada 10 min: la lluvia se suma, las demás variables se promedian y la dirección del viento usa promedio circular. |

## Lo que la hace distinta

- **Funciona sin internet.** El mapa vectorial de Colombia va dentro de la página. Si la red del evento falla, la plataforma sigue funcionando, incluso abierta desde una USB.
- **Departamento automático.** Al escribir las coordenadas, la plataforma dice en qué departamento cae la estación y avisa si las coordenadas quedan fuera de Colombia (el error típico es olvidar el signo menos de la longitud).
- **Altitud y municipio con un botón.** La altitud viene del modelo de elevación Copernicus GLO-90 (vía Open-Meteo) y el municipio de OpenStreetMap (Nominatim). Ambos necesitan internet.
- **Lectura inteligente del CSV.** Reconoce el separador (coma, punto y coma o tabulador), la coma decimal, fechas día/mes/año y fecha y hora en columnas separadas. También reconoce nombres de columnas en español o en inglés.
- **Control de calidad.** Los valores fuera de rango (por ejemplo, humedad de 104 %) se guardan como dato crudo pero quedan marcados. Así lo hace el IDEAM antes de validar.
- **Estados como en Polaris.** Cada estación queda en línea, con retraso, en alerta, en mantenimiento o desconectada. Si llovió en los últimos 10 minutos, el marcador muestra ondas.
- **Bitácora.** Registra quién hizo qué y cuándo: ingresos, estaciones creadas, archivos cargados.

### Novedades de las versiones 1.2 a 1.4

- **Nombre nuevo:** la plataforma se llama **R.D.C**. Las cuentas y los datos ya guardados se conservan, y los respaldos con el nombre anterior se pueden restaurar.
- **Ingreso solo con cuenta.** Para entrar hay que registrarse. La pantalla tiene dos pestañas, *Ingresar* y *Crear cuenta*, y cualquier persona puede crear su cuenta en cualquier momento. El acceso de invitado de la versión 1.2 se retiró.
- **Ingreso más claro:** botón para ver la contraseña, medidor de fortaleza al crear cuenta, avisos en el campo que falla e indicador de carga mientras se cifra la contraseña.
- **Animaciones sobrias:** el mapa del ingreso se dibuja departamento por departamento y cada tanto una estación "reporta" con una onda. Al entrar, la plataforma aparece con un fundido. Con *movimiento reducido* activado en el sistema, todo aparece quieto.

### Novedades de la versión 1.1

- **Capa de isoyetas** (una isoyeta es la línea que une los puntos con la misma cantidad de lluvia). Interpola la lluvia de las últimas 24 h entre las estaciones activas (distancia inversa, potencia 2) y dibuja las curvas de 1, 5, 10, 20, 35 y 50 mm, recortadas a Colombia. Cada estación influye hasta 170 km. Al pasar el cursor, el recuadro de coordenadas muestra la lluvia estimada en ese punto. Se activa en *Capas y leyenda* o con la tecla `i`. Es una guía visual y no reemplaza el análisis del IDEAM.
- **Indicadores de la red** en la barra superior: estaciones, cuántas están en línea, alertas y la mayor lluvia de 24 h. En celular aparecen arriba de la lista.
- **Filtros** por tipo de estación y por estado. Las estaciones que no cumplen el filtro se atenúan en el mapa.
- **Leyenda del mapa** con las formas por tipo y los colores por estado, más una escala gráfica en kilómetros.
- **Minigráficas** de las últimas 24 h en cada variable de la estación.
- **Comparar estaciones.** Superpone en la misma gráfica la serie de otra estación. Para la lluvia compara el acumulado.
- **Rosa de los vientos** (16 rumbos) con la dirección predominante y la velocidad media.
- **Tabla** con los últimos 12 registros de la estación.
- **Red de ejemplo** de 11 estaciones en ciudades reales (Quibdó, Barranquilla, Leticia, Pasto, Neiva y otras) con series sintéticas marcadas como *datos de ejemplo*. Incluye una estación hidrológica con nivel del río y casos de cada estado: alerta, retraso y mantenimiento.
- **Atajos de teclado:** `/` buscar, `n` nueva estación, `f` encuadrar la red, `i` isoyetas, `t` tema, `?` ayuda. No se activan mientras se escribe en un campo.
- **Accesibilidad:** el foco queda dentro de las ventanas de confirmación, `Esc` las cierra y el foco vuelve al botón que las abrió. Cada 30 s se actualizan los estados y el "hace X min".

## Probarla en un minuto

1. Descarga la carpeta completa del proyecto.
2. Abre `index.html` con doble clic en **Chrome o Edge**. No hace falta instalar nada ni tener internet.
3. Crea una cuenta en la pestaña *Crear cuenta* (nombre, usuario y contraseña de 8 o más caracteres).
4. Pulsa **Cargar red de ejemplo** para crear 11 estaciones con datos de las últimas 24 horas, o pulsa **Nueva estación**.
5. En *Capas y leyenda* (arriba a la izquierda del mapa) activa **Isoyetas**.
6. Abre una estación, pulsa **Cargar datos CSV** y arrastra un archivo de la carpeta `ejemplos/`.

> La cuenta y los datos quedan guardados **en ese navegador de ese computador**. Para llevarlos a otro equipo usa *Usuario ▾ → Respaldo de datos*.

## Publicarla gratis en GitHub Pages (paso a paso, sin instalar nada)

1. Entra a [github.com](https://github.com) e inicia sesión (o crea una cuenta gratis).
2. Arriba a la derecha pulsa **+** y luego **New repository**.
3. Nombre: `rdc`. Marca **Public**. Pulsa **Create repository**.
4. En la página del repositorio vacío pulsa el enlace **uploading an existing file**.
5. Arrastra **todo el contenido** de la carpeta del proyecto: `index.html`, `README.md`, `build.py` y las carpetas `ejemplos`, `vendor` y `src`. Escribe un mensaje como "Primera versión" y pulsa **Commit changes**.
6. Ve a **Settings** y luego a **Pages** (en el menú de la izquierda).
7. En *Build and deployment*, en **Source** elige **Deploy from a branch**. En **Branch** elige `main` y la carpeta `/ (root)`. Pulsa **Save**.
8. Espera uno o dos minutos y recarga esa página. Arriba aparece el enlace, con la forma `https://TU-USUARIO.github.io/rdc/`.
9. Abre el enlace, crea la cuenta y listo. Con internet ya aparecen las capas de calles, relieve y satélite.

Cada vez que cambien algo, suben el archivo de nuevo (**Add file → Upload files**) y GitHub Pages se actualiza solo. Ese historial de cambios sirve de bitácora del código, como pidió la organización.

## Conectar TRIADA PLUVIO (Reto 1)

El ESP32-CAM crea su propia red WiFi y guarda los datos en un CSV con estas columnas:

```
fecha_hora,precipitacion_mm,intensidad_mm_h,precip_peso_mm,gotas_min,acumulado_dia_mm,estado
```

R.D.C reconoce ese formato solo:

| Columna | Se guarda como |
| --- | --- |
| `precipitacion_mm` | PREC, precipitación (mm) |
| `intensidad_mm_h` | INTP, intensidad de lluvia (mm/h) |
| `precip_peso_mm` | PPES, precipitación por peso (celda de carga) |
| `gotas_min` | GOTA, gotas por minuto (piezo) |
| `acumulado_dia_mm` | no se carga, porque se calcula |
| `estado` | estado reportado por el equipo (SECO, LLUVIA, ALERTA_LLUVIA…) |

Para llevar los datos a la plataforma:

1. Conecta el computador o el celular a la red **TRIADA-PLUVIO** (clave `lluvia2026`).
2. Abre `http://192.168.4.1/csv`. Se descarga `lluvia.csv`.
3. En R.D.C, abre la estación, pulsa **Cargar datos CSV** y arrastra el archivo.
4. Revisa la tabla de vista previa y pulsa **Guardar en la estación**.

El botón *Traer CSV de 192.168.4.1* intenta leerlo directamente. Cuando la plataforma se abre desde GitHub Pages (https), el navegador bloquea esa lectura por seguridad, porque la estación habla http. En ese caso se usa el método de descargar y arrastrar, que siempre funciona.

## Formatos de CSV que acepta

Los archivos de `ejemplos/` cubren cada caso:

| Archivo | Formato |
| --- | --- |
| `estacion-completa.csv` | Las 7 variables, una fila cada 10 min, coma y punto decimal |
| `excel-colombia.csv` | Como lo guarda Excel en español: punto y coma, coma decimal, fecha `28/10/2026` y hora en otra columna |
| `triada-pluvio.csv` | El formato de TRIADA PLUVIO, una fila por minuto |
| `una-linea.csv` | `Precipitación 0.0, temperatura 18, presión atmosférica 750`, el ejemplo literal de la reunión. Pide la fecha y la hora al cargarlo. |
| `variable-valor.csv` | Formato largo: `fecha,variable,valor` |

## Limitaciones conocidas

- Los datos y las cuentas viven en el navegador. Es una prueba de concepto para el reto; para una red real del IDEAM el siguiente paso es un servidor con base de datos compartida (por ejemplo PostgreSQL con PostGIS) y que cada estación envíe sus datos por internet.
- Las capas de calles, relieve y satélite, la altitud y el municipio necesitan internet. El resto funciona sin conexión.
- Probada con 78 pruebas automáticas en Chromium (escritorio y celular, tema claro y oscuro). Los servidores de calles (Esri), relieve (OpenTopoMap), satélite (Esri), altitud (Open-Meteo) y municipio (Nominatim) se verificaron respondiendo el 29 de octubre de 2026. Para abrirla desde el disco usen Chrome o Edge.
- Las isoyetas con pocas estaciones son muy aproximadas: entre más estaciones activas, más fiel es la superficie.

## Estructura

```
index.html            la plataforma completa (un solo archivo)
vendor/               Leaflet 1.9.4 local, por si no hay internet
ejemplos/             CSV de prueba
src/                  código fuente: app.html, app.css, app.js, límites de Colombia
build.py              vuelve a armar index.html desde src/ (python3 build.py)
```

## Fuentes y créditos

- [Leaflet 1.9.4](https://leafletjs.com) (licencia BSD-2-Clause, en `vendor/LICENSE-leaflet.txt`).
- Límites departamentales: [Natural Earth](https://www.naturalearthdata.com) 1:10m, *Admin 1 – States, Provinces* (dominio público), simplificados a ~1 km.
- Calles: Esri World Street Map (Esri, HERE, Garmin, © [OpenStreetMap](https://www.openstreetmap.org/copyright)). Relieve: [OpenTopoMap](https://opentopomap.org) (CC-BY-SA). Satélite: Esri World Imagery. Se descartó CARTO porque desde 2026 sus mapas piden clave y sin ella muestran una marca de agua.
- Altitud: [Open-Meteo Elevation API](https://open-meteo.com/en/docs/elevation-api), basada en Copernicus DEM GLO-90.
- Municipio: [Nominatim](https://nominatim.org) de OpenStreetMap.
- Códigos de variables tomados del visor Polaris del IDEAM mostrado en la reunión del 22 de octubre de 2026.
