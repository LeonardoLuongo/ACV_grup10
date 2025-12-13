import os
from ultralytics import SAM

# 1. Definisci il percorso della cartella (come nel tuo screenshot)
# Modifica l'inizio del percorso se necessario
path_to_img_folder = os.path.join("dataset", "tracking-2023", "train", "SNMOT-060", "img1")

# 2. Carica il modello SAM 2 (scaricherà automaticamente 'sam2_b.pt' se non ce l'hai)
# 'sam2_b.pt' è la versione base (veloce). Usa 'sam2_l.pt' se vuoi più precisione (più lento).
model = SAM("sam2_b.pt")

# 3. Esegui il Tracking
# Ultralytics gestisce le cartelle di immagini automaticamente come video.
# bboxes=None e text="..." dice al modello cosa cercare.
results = model(
    source=path_to_img_folder,
    name="tracking_result", # nome della cartella dove salverà i risultati
    save=True,              # Salva il video/immagini con le annotazioni
    stream=True,             # Importante per i video/sequenze lunghe per non saturare la RAM
    device=0        # Usa la GPU se disponibile
)

# 4. Loop per processare e visualizzare (opzionale, per vedere in diretta)
# Per attivare il tracking testuale con SAM2, spesso bisogna fornire il prompt al primo frame.
# Nota: L'implementazione attuale di SAM2 in Ultralytics è ancora in evoluzione per i prompt testuali puri su video.
# Il metodo più robusto con SAM2 è fornire un punto o un box iniziale, ma proviamo l'approccio automatico.

for result in results:
    # Se vuoi visualizzare a schermo ogni frame mentre elabora
    result.show()