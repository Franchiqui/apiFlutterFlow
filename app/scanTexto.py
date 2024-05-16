import cv2
import pytesseract

def scanTexto_func():
    return text('scaner')

# Cargar la imagen
img = cv2.imread('image_path')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbrales para convertir a una imagen binaria
threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Establecer la ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'

# Establece el idioma del texto
text = pytesseract.image_to_string(img, config='--psm 10 lang=es')

# Extraer texto usando pytesseract
text = pytesseract.image_to_string(threshold_img)

# Mostrar las imágenes en escala de grises y de umbral.
cv2.imshow("gris", gray)
cv2.imshow("umbral", threshold_img)

# Guarda el texto capturado en el archivo 'resultado.txt'
with open('resultado.txt', 'w') as f: f.write(text)

# Imprime el texto extraído
print(text)

# Agregue un retraso para mantener la ventana abierta
cv2.waitKey(0)  # Espere a que se presione una tecla antes de cerrar la ventana.
cv2.destroyAllWindows()  # cerrar todas las ventanas

