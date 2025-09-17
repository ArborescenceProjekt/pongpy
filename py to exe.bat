@echo off
pyinstaller --onefile --noconsole ^
  --add-data "Sounds;Sounds" ^
  --add-data "Images;Images" ^
  main.py