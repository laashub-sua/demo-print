import fitz


def do_convert(file_path):
    doc = fitz.open(file_path)
    file_path = file_path[:-4] + '.jpg'
    for pg in range(doc.pageCount):
        page = doc[pg]
        zoom = 4.0
        rotate = int(0)
        trans = fitz.Matrix(zoom, zoom).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG(file_path)
        break
    return file_path
