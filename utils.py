import qrcode
from PIL import Image, ImageFont, ImageDraw
from PySide2.QtWidgets import QTableWidgetItem


def createQrId(guid, data):
    qr = qrcode.make(guid)
    qr = qr.resize((250, 250))

    output = Image.new("RGB", (800, 450), (255, 255, 255))
    output.paste(qr, (500, 150))

    Font = ImageFont.truetype("Georgia.ttf", 50)
    Brush = ImageDraw.Draw(output)

    Brush.text((50, 50), "XYZ Library", font=Font, fill=(0, 0, 0))

    Font = ImageFont.truetype("Georgia.ttf", 25)

    offset = 300 // len(data)
    i = 0
    for key in data:
        Brush.text(
            (50, 150 + i * offset),
            f"{key}: {data[key]}",
            font=Font,
            fill=(0, 0, 0)
        )
        i += 1

    return output


def addDataToTable(table, headers, data):
    table.setRowCount(0)
    table.setColumnCount(0)

    for i in range(len(headers)):
        table.insertColumn(i)
    table.setHorizontalHeaderLabels(headers)

    j = 0
    for row in data:
        table.insertRow(j)
        i = 0
        for x in row:
            table.setItem(j, i, QTableWidgetItem(x))
            i += 1
        j += 1


if __name__ == "__main__":
    from PIL import ImageShow
    data = {
        "First Name": "Monish",
        "Last Name": "Sudhagar",
        "Gender": "Male",
        "Date of Joining": "2020/11/01",
        "Role": "Librarian"
    }
    ID = createQrId("c3f9d130-8524-4699-9b40-4e0f7d5bd4f5", data)
    ImageShow.show(ID)
