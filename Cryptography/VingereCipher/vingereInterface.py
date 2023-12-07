import sys
sys.path.append("C:\\Users\\justa\\Documents\\Coding\\Public\\CodingFolder\\Cryptography")

import cryptotools as ct
import tkinter as tk
import vingereChiSquared as vingere

# create window
window = tk.Tk(className = " Vingere Cipher Decoder")

cv = tk.Canvas(window, width = 750, height = 500)
cv.grid()



# show window
window.mainloop()
