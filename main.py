import keyboard

# Funkcija, ki se sproži ob pritisku tipke
def on_key_press(event):
    print(f'Pritisnjena tipka: {event.name}')

# Registriramo funkcijo, ki "posluša" tipke
keyboard.on_press(on_key_press)

# Program teče dokler ne pritisnemo ESC
keyboard.wait('esc')