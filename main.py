from flet import (
    Page,
    Theme,
    AppBar,
    Icon,
    icons,
    Text,
    colors,
    Image,
    TextField,
    ResponsiveRow,
    Column,
    Container,
    FilledButton,
    app
)

import pyqrcode 
import png 
from time import sleep

def main(page: Page):
    page.title = "Aditya's QR code generator"
    page.window.height = 720
    page.window.width = 360
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme = Theme("lightblue")
    page.theme_mode = "light"

    page.appbar=AppBar(
        leading=Icon(icons.QR_CODE_SCANNER),
        leading_width=30,
        title=Text("Adi QRcode-generator"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
        )

    

    def generate(e):
        box.controls.clear()
        page.update()
        sleep(1)
        url = pyqrcode.create(inp.value)
        path = f'/storage/emulated/0/Download/{inp.value[:7]}.png'
        url.png(path, scale = 6)
        t1 = Text("generating...")
        box.controls.append(t1)
        page.update()
        sleep(2)
        t2 = Text("generating done!")
        qrcode = Image(src=path,tooltip=inp.value)
        box.controls.append(t2)
        box.controls.append(qrcode)
        page.update()

        
    
    inp = TextField(label="Enter url here")
    btn = FilledButton("Generate",on_click=lambda e:generate(e))
    box = Column()
    cont = Container(content=box)

    page.add(
        ResponsiveRow(
            [inp,btn],
            alignment="center",
        ),cont)
    
app(main)
