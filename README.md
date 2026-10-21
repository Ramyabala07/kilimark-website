# Kilimark website prototype

Landing page prototype for Kilimark rice (Sastha Ayyanar Modern Rice Mill, Madurai), designed by PTJ.

## Files

- `index.src.html`: source of the page (HTML, CSS and JS in one file, English and Tamil copy).
- `build.py`: inlines the SVG icons and writes `index.html` (the published page) and `_preview.html` (a local preview with a doctype wrapper).
- `assets/img/`: photos, pack images, brand logos, illustrations and the mill video loop. Photo credits are in `assets/img/credits.json`.

## Work on it

```bash
python3 build.py
python3 -m http.server 8765
```

Then open http://localhost:8765/_preview.html.

Edit `index.src.html` and run `build.py` again after each change.
