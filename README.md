# Intrusion warning
- Reference from MiAI channel: https://www.youtube.com/watch?v=fd0WrwnPhtg&t=1199s
- Using YOLOv5

# Instruction
- Clone repository
```
git clone https://github.com/npk7264/Intrusion-warning.git
```
- Move to folder Intrusion-warning, install packages in requirements.txt
```
pip install -r requirements.txt
```
- Run
```
python main.py
```
- Blue is restricted area, Pink is object. Red dot is centroid of bounding box, if red dot in restricted area, display 'ALARM' text

<img src="https://github.com/npk7264/Intrusion-warning/assets/90046327/0149164c-1791-4c6e-8d9e-b65a0366c1b9"  width="500">
