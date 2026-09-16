# Xeno Publishers Website

Static GitHub Pages website for Xeno Publishers.

## Files
- `index.html` — homepage
- `about.html` — publisher/about page
- `downloads.html` — game downloads
- `patch-notes.html` — all-game patch notes
- `support.html` — player support
- `terms.html` — terms and services
- `maintenance.html` — maintenance screen
- `maintenance.js` — global maintenance switch
- `404.html` — custom GitHub Pages 404
- `style.css` — global design
- `script.js` — navigation and reveal animations

## Maintenance mode
Open `maintenance.js` and change:

`const MAINTENANCE_MODE = false;`

to `true`. Every page that loads the script will redirect to `maintenance.html`.

## APK
In `downloads.html`, replace `DOWNLOAD_APK_URL_HERE` with the real APK download URL when ready.
