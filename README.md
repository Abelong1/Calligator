# Calligator

A study buddy for electronics fundamentals: Ohm's Law, resistor color codes, Boolean algebra, Karnaugh maps, series/parallel R and L/C, voltage and current dividers, plus a notepad.

Responsive installable web app (PWA). Works offline once loaded.

## Files
- `index.html` — the built app (React bundled in, no build step needed to host)
- `manifest.json`, `sw.js`, `icon-*.png` — install + offline support
- `src/CalligatorApp.jsx` — source

## Rebuild after editing the source
```
npm i react@18.3.1 react-dom@18.3.1 esbuild@0.24
python3 build.py
```
