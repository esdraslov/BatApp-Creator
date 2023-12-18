import PyAutoGui as pg
import os
import components.appDetector

layout = [[pg.Text("Projects")],
    [pg.Button("open", key="-OP-"), pg.Button("new", key="-NEW-"), pg.Button("manage")]
]

window = pg.Window("Projects - BatApp Creator", layout)
