import dlib
import numpy as np
import face_recognition_models
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)

        face_descriptor = facerec.compute_face_descriptor(
            image_np,
            shape,
            1
        )

        encodings.append(np.array(face_descriptor))

    return encodings


def train_classifier():
    """
    No SVM classifier is needed.

    Face recognition is done by comparing
    the new face embedding with embeddings
    stored in the database.
    """

    st.cache_resource.clear()
    return True


def predict_attendance(class_image_np):

    # ---------------------------------
    # 1. Get face embedding from camera
    # ---------------------------------

    encodings = get_face_embeddings(class_image_np)

    detected_student = {}

    if len(encodings) == 0:
        return detected_student, [], 0

    # ---------------------------------
    # 2. Get all registered students
    # ---------------------------------

    all_students = get_all_students()

    if not all_students:
        return detected_student, [], len(encodings)

    # ---------------------------------
    # 3. Get stored face embeddings
    # ---------------------------------

    students_with_embeddings = []

    for student in all_students:

        embedding = student.get("face_embedding")

        if embedding:

            try:
                stored_embedding = np.array(
                    embedding,
                    dtype=np.float64
                )

                if stored_embedding.shape == (128,):

                    students_with_embeddings.append(
                        (
                            student["student_id"],
                            stored_embedding
                        )
                    )

            except Exception:
                continue

    # No registered face embeddings
    if not students_with_embeddings:
        return detected_student, [], len(encodings)

    # ---------------------------------
    # 4. Compare camera face with
    #    every registered student
    # ---------------------------------

    resemblance_threshold = 0.60

    all_ids = [
        student_id
        for student_id, _ in students_with_embeddings
    ]

    for encoding in encodings:

        best_student_id = None
        best_distance = float("inf")

        for student_id, stored_embedding in students_with_embeddings:

            distance = np.linalg.norm(
                stored_embedding - encoding
            )

            if distance < best_distance:
                best_distance = distance
                best_student_id = student_id

        # ---------------------------------
        # 5. Accept match only if distance
        #    is within threshold
        # ---------------------------------

        if (
            best_student_id is not None
            and best_distance <= resemblance_threshold
        ):

            detected_student[best_student_id] = True

    return detected_student, all_ids, len(encodings)