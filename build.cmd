pyrcc5 -o resources.py resources.qrc
pyi-makespec -F  -w  main.py

pyinstaller --clean main.spec -y