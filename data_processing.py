import pdf2image.exceptions
import pytesseract
from PIL.Image import DecompressionBombError
from pdf2image import convert_from_path
import glob
import cvttext as sc
import aspose.words as aw
import imghandler as ts

all_files = glob.glob(r"files\*")
#print(len(all_files))
#i = 0
#j=0
#Key is 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
for file in all_files:
    if '.pdf' in str(file):
        try:
            pages = convert_from_path(file, 350)
        except (ValueError, pdf2image.exceptions.PDFPageCountError, pdf2image.exceptions.PDFSyntaxError, DecompressionBombError):
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
            ts.rmv_imgs()
    elif '.jpg' in str(file):
        try:
            txt = sc.convert_txt(str(file))
        except (pytesseract.TesseractError, FileNotFoundError, OSError, AttributeError):
            print("An error occurred:")
        else:
            with open("C:/Users/hp/PycharmProjects/bigdataProject/texts/" + str(file)[6:] + ".txt", "w",
                      encoding="utf8") as my_output_file:
                my_output_file.write(txt)
                my_output_file.close()
    elif '.JPG' in str(file):
        try:
            txt = sc.convert_txt(str(file))
        except (pytesseract.TesseractError, FileNotFoundError, OSError, AttributeError):
            print("An error occurred:")
        else:
            with open("C:/Users/hp/PycharmProjects/bigdataProject/texts/" + str(file)[6:] + ".txt", "w",
                      encoding="utf8") as my_output_file:
                my_output_file.write(txt)
                my_output_file.close()
    elif '.jpeg' in str(file):
        try:
            txt = sc.convert_txt(str(file))
        except (pytesseract.TesseractError, FileNotFoundError, OSError, AttributeError):
            print("An error occurred:")
        else:
            with open("C:/Users/hp/PycharmProjects/bigdataProject/texts/" + str(file)[6:] + ".txt", "w",
                      encoding="utf8") as my_output_file:
                my_output_file.write(txt)
                my_output_file.close()
    elif '.JPEG' in str(file):
        try:
            txt = sc.convert_txt(str(file))
        except (pytesseract.TesseractError, FileNotFoundError, OSError, AttributeError):
            print("An error occurred:")
        else:
            with open("C:/Users/hp/PycharmProjects/bigdataProject/texts/" + str(file)[6:] + ".txt", "w",
                      encoding="utf8") as my_output_file:
                my_output_file.write(txt)
                my_output_file.close()
    elif '.doc' in str(file):
        try:
            doc = aw.Document(str(file))
        except RuntimeError:
            print("reading issue!!!")
        else:
            options = aw.saving.ImageSaveOptions(aw.SaveFormat.JPEG)
            # loop through pages and convert them to PNG images
            i = 0
            for pageNumber in range(doc.page_count):
                options.page_set = aw.saving.PageSet(pageNumber)
                i += 1
                doc.save("images/" + str(i) + "_page.jpeg", options)
            images = glob.glob(r"images/*")
            txt = ''
            for img in images:
                name = str(img)
                txt = txt + sc.convert_txt(name)
            with open("texts/" + str(file)[6:] + ".txt", "w", encoding="utf8") as my_output_file:
                my_output_file.write(txt)
                my_output_file.close()
            ts.rmv_imgs()
