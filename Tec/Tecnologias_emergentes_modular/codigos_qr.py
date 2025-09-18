import qrcode  # Para generar el código QR
import cv2     # Para leer código QR desde imagen o cámara

def gen_qr():
    """Genera un código QR a partir de una URL digitada (imagen o video)"""
    data = input("Digite el enlace al que debe dirigir el código QR (ej: https://...): ").strip()

    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crear imagen
    img = qr.make_image(fill="black", back_color="white")
    img.save("codigo_qr.png")
    print("Código QR generado y guardado como 'codigo_qr.png'")

def leer_qr_img():
    """Lee un código QR desde una imagen guardada"""
    imagen = cv2.imread("codigo_qr.png")
    if imagen is None:
        print("No se pudo cargar la imagen 'codigo_qr.png'. Verifica que exista.")
        return

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(imagen)

    if data:
        print("Contenido del QR detectado:")
        print(data)
    else:
        print("No se detectó ningún código QR en la imagen.")

def leer_qr_cam():
    """Lee un código QR usando la cámara"""
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    print("Escaneando... presiona 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            cv2.polylines(frame, [bbox.astype(int)], True, (0, 255, 0), 2)
            if data:
                print("QR detectado:", data)

        cv2.imshow("Escáner QR", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def menu_qr():
    try:
        while True:
            opt = input(
                "\nSeleccione una opción:\n"
                "1 -> Generar QR desde URL\n"
                "2 -> Leer QR desde imagen\n"
                "3 -> Leer QR desde cámara\n"
                "0 -> Salir\n"
                "Opción: "
            ).strip()

            if opt == '1':
                gen_qr()
            elif opt == '2':
                leer_qr_img()
            elif opt == '3':
                leer_qr_cam()
            elif opt == '0':
                print("Fin del programa.")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except EOFError:
        print("\nEntrada no disponible. Saliendo.")

if __name__ == "__main__":
    menu_qr()
