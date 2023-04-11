import cv2

cap = cv2.VideoCapture(0)

while True:
    # captura a imagem da câmera
    ret, frame = cap.read()

    # exibe a imagem em uma janela
    cv2.imshow('Webcam', frame)

    # espera por uma tecla
    key = cv2.waitKey(1)

    # se a tecla 'q' for pressionada, interrompe o loop
    if key == ord('q'):
        break

# libera os recursos da câmera
cap.release()

# fecha todas as janelas
cv2.destroyAllWindows()
