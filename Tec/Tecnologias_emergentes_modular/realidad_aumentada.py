import cv2
import numpy as np
import os

def menu_ar():
    try:
        while True:
            opt = input(
                "Seleccione una operación:\n"
                "1 -> Generar marcadores ArUco\n"
                "2 -> Leer marcadores ArUco (Realidad Aumentada)\n"
                "0 -> Salir\n"
                "Opción: "
            ).strip()

            if opt == '1':
                generador_aruco()
            elif opt == '2':
                realidad_aumentada()
            elif opt == '0':
                print("Fin AR")
                break
            else:
                print("Seleccione una opción válida (0, 1, 2).")
    except KeyboardInterrupt:
        print("\nInterrupción detectada. Saliendo del menú.")
    except EOFError:
        print("\nEntrada no disponible. Saliendo del menú.")


def generador_aruco():
    output_dir = "marcadores"
    os.makedirs(output_dir, exist_ok=True)
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    for id_marker in range(6):
        img = cv2.aruco.generateImageMarker(aruco_dict, id_marker, 400)
        cv2.imwrite(f"{output_dir}/marker_{id_marker}.png", img)
    print(" Marcadores generados exitosamente!")


def realidad_aumentada():
    # Usa la carpeta correcta y nombres reales de tus imágenes
    base_path = 'imagen/'

    imagenes = {
        0: cv2.imread(base_path + 'Cebra.jpg'),
        1: cv2.imread(base_path + 'Curi.jpg'),
        2: cv2.imread(base_path + 'Oso.jpeg'),
        3: cv2.imread(base_path + 'Tigre.jpg'),
        4: cv2.imread(base_path + 'Tucan.jpg'),
        5: cv2.imread(base_path + 'venado.jpg')
    }

    for id_img, img in imagenes.items():
        if img is None:
            print(f" Error: No se pudo cargar la imagen asociada al ID {id_img}. Verifica que exista el archivo correctamente.")
            return

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        corners, ids, _ = detector.detectMarkers(frame)

        if ids is not None:
            for corner, marker_id in zip(corners, ids.flatten()):
                if marker_id in imagenes:
                    img_to_overlay = imagenes[marker_id]
                    pts_dst = np.array(corner[0], dtype="float32")
                    h, w = img_to_overlay.shape[:2]
                    pts_src = np.array([
                        [0, 0],
                        [w - 1, 0],
                        [w - 1, h - 1],
                        [0, h - 1]
                    ], dtype="float32")

                    matrix, _ = cv2.findHomography(pts_src, pts_dst)
                    warped_image = cv2.warpPerspective(img_to_overlay, matrix, (frame.shape[1], frame.shape[0]))
                    mask = np.zeros(frame.shape[:2], dtype="uint8")
                    cv2.fillConvexPoly(mask, pts_dst.astype(int), 255)
                    frame = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
                    frame = cv2.add(frame, warped_image)

        cv2.imshow('Realidad Aumentada', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    menu_ar()
