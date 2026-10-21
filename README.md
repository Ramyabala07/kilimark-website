# Kilimark website prototype

Landing page prototype for Kilimark rice (Sastha Ayyanar Modern Rice Mill, Madurai), designed by PTJ.

## Files

- `index.src.html`: source of the page (HTML, CSS and JS in one file, English and Tamil copy).
- `build.py`: inlines the SVG icons and writes `index.html` (the complete page, served by GitHub Pages) and `artifact.html` (the same page as a fragment, for the Claude artifact).
- `assets/img/`: photos, pack images, brand logos, illustrations and the mill video loop. Photo credits are in `assets/img/credits.json`.

## Work on it

```bash
python3 build.py
python3 -m http.server 8765
```

Then open http://localhost:8765/.

Live site: https://ramyabala07.github.io/kilimark-website/

Edit `index.src.html` and run `build.py` again after each change.
