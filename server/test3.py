from cita import cita
from PIL import Image
import cita as ct


app = cita()

ct.TOLERANCE = 0.45

"""
FIX THE DELETE STATEMENTS

"""

img = Image.open("unknown_faces/gg.jpg")
print(app.check_entry(img))
