"""try:
    pages = convert_from_path(file, 350)
except ValueError:
    print("issue!!!")
else:
    i = 1
    for page in pages:
        image_name = str(file)[6:] + str(i) + ".jpg"
        page.save('images/' + image_name, "JPEG")
        i = i + 1
    images = glob.glob(r"images\*")
    txt = ''
    for img in images:
        name = str(img)
        txt = txt + sc.convert_txt(name)
    with open("C:/Users/hp/PycharmProjects/bigdataProject/texts/" + str(file)[6:] + ".txt", "w",
              encoding="utf8") as my_output_file:
        my_output_file.write(txt)
        my_output_file.close()
    ts.rmv_imgs()"""
try:
    txt = sc.convert_txt(str(file))
except (pytesseract.TesseractError, FileNotFoundError, OSError, AttributeError):
    print("An error occurred:")
else:
    with open("C:/Users/hp/PycharmProjects/bigdataProject/texts/" + str(file)[6:] + ".txt", "w",
              encoding="utf8") as my_output_file:
        my_output_file.write(txt)
        my_output_file.close()