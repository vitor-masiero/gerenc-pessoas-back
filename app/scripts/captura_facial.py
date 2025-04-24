import cv2
import numpy as np
import face_recognition
import mediapipe as mp

# Inicializa o detector do MediaPipe
mp_face_detection = mp.solutions.face_detection

def extract_face_from_frame(frame):
    """
    Detecta o rosto em um frame usando MediaPipe e recorta a imagem da face.
    """
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        # Converte a imagem para RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)

        if results.detections:
            # Pegamos o primeiro rosto detectado
            bbox = results.detections[0].location_data.relative_bounding_box
            h, w, _ = frame.shape
            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            width = int(bbox.width * w)
            height = int(bbox.height * h)

            # Garante que os limites estão dentro da imagem
            x = max(0, x)
            y = max(0, y)
            x2 = min(w, x + width)
            y2 = min(h, y + height)

            return frame[y:y2, x:x2]
    return None

def process_faces_with_face_recognition(frames):
    vectors = []

    for frame in frames:
        # Detecção e vetorização com face_recognition
        face_locations = face_recognition.face_locations(frame)

        if not face_locations:
            continue

        encodings = face_recognition.face_encodings(frame, face_locations)
        if encodings:
            vectors.append(encodings[0])

    if not vectors:
        return None

    return np.mean(vectors, axis=0).tolist()
