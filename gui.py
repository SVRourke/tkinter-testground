import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('500x300')
window.title("Accutrack")
window.grid()

# pb = ttk.Progressbar(
#     window,
#     orient='horizontal',
#     mode='indeterminate',
#     length=280
# )
# pb.grid()

sensorFrame = tk.Frame(master=window, height=100, width=600, relief='sunken')
sensorFrame.grid(column=0, row=0, columnspan=6)

sensorFrameTitle = tk.Label(master=sensorFrame, text="Sensor")
sensorFrameTitle.pack(padx=5, pady=5)

# sensorConnectButton = tk.Button(
#     text="Connect",
#     height=1,
#     master=sensorFrame
# )
# sensorConnectButton.pack()

# sensorCalibrateButton = tk.Button(
#     text="Calibrate",
#     height=1,
#     master=sensorFrame
# )
# sensorCalibrateButton.pack()

# sensorDisconnectButton = tk.Button(
#     text="Disconnect",
#     height=1,
#     master=sensorFrame
# )
# sensorDisconnectButton.pack()

window.mainloop()
