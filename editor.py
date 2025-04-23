import pyray as rl
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import time

# Inizializzazione della finestra
rl.init_window(800, 600, "Contatore di Parole con Raylib")

# Variabili per il testo
input_text = ""

# Funzione per contare le parole

# Ciclo principale
while not rl.window_should_close():
    # Start del frame
    rl.begin_drawing()
    rl.clear_background(rl.DARKBLUE)
    #scrivi il testo digiotato sullo schermo
    rl.draw_text(input_text,60,60,20,rl.GREEN)
    # Aggiungi i caratteri digitati
    for key in range(32, 127):  # Caratteri ASCII stampabili
        if rl.is_key_pressed(key):
            input_text += chr(key)
    # Gestisci il tasto backspace per cancellare l'ultimo carattere
    if rl.is_key_pressed(rl.KEY_BACKSPACE) and len(input_text) > 0:
        input_text = input_text[:-1]  # Rimuovi l'ultimo carattere

    # Gestisci il tasto spazio per aggiungere uno spazio
    if rl.is_key_pressed(rl.KEY_SPACE):
        input_text += ' '  # Aggiungi uno spazio
    # Fine del frame
    rl.end_drawing()

# Chiusura della finestra
rl.close_window()
