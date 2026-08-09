@echo off
ping -n 40 127.0.0.1 >nul
echo ---- pages build ----
gh api repos/Kaminczak/genre-machine/pages/builds/latest --jq .status
echo ---- http codes ----
curl -s -o nul -w "index: %%{http_code}\n" https://kaminczak.github.io/genre-machine/
curl -s -o nul -w "audio: %%{http_code}\n" https://kaminczak.github.io/genre-machine/assets/audio/pigs_08_western.wav
curl -s -o nul -w "image: %%{http_code}\n" https://kaminczak.github.io/genre-machine/assets/images/pigs_01_original.webp
curl -s -o nul -w "data:  %%{http_code}\n" https://kaminczak.github.io/genre-machine/data/scripts-generated.js
