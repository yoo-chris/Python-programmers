import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import AdamW
from PIL import Image
import numpy as np
from  utils import *
from vit_structure import *
import logging
import time
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

device = 'cuda' if tf.config.list_physical_devices('GPU') else 'cpu'
N_classes = 9

logger.debug(f"device: {device}")

# s3에서 파일 불러오기

if len(os.listdir('/home/ubuntu/murok_ai_backend/weights/')) < 4:
    classes = ['strawberry', 'cucumber', 'tomato', 'pepper']
    for c in classes:
        download_weights(c)
        logger.debug(f"Downloaded {c} weight file from S3")
else:
    logger.debug("Weight files already downloaded")


def create_model(crop_type):
    h5_file = get_weight_by_crop(crop_type)
    logger.debug(f"h5_file: {h5_file}")
    model = tf.keras.models.load_model(h5_file)
    logger.debug(f"Model loaded")
    return model

# 모델 가중치 미리 불러오기
with tf.keras.utils.custom_object_scope({'Patches': Patches, 'PatchEncoder': PatchEncoder, 'AdamW': AdamW}):
    strawberry_model = load_model(get_weight_by_crop('strawberry'), compile=False)
    cucumber_model = load_model(get_weight_by_crop('cucumber'), compile=False)
    tomato_model = load_model(get_weight_by_crop('tomato'), compile=False)
    pepper_model = load_model(get_weight_by_crop('pepper'), compile=False)


def get_model_by_crop(crop_type):
    # crop_type에 따라 미리 로드된 모델 선택
    if crop_type == 'strawberry':
        return strawberry_model
    elif crop_type == 'cucumber':
        return cucumber_model
    elif crop_type == 'tomato':
        return tomato_model
    elif crop_type == 'pepper':
        return pepper_model
    else:
        raise ValueError("Invalid crop_type")


def load_and_preprocess_image(image_path):
    logger.debug("Loading and preprocessing image...")  
    # 이미지 로드 및 전처리
    image = Image.open(image_path).convert("RGB")
    image = tf.convert_to_tensor(np.array(image))
    image = tf.image.resize(image, [128, 128])
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)

    # 배치 차원 추가
    image = tf.expand_dims(image, 0)
    logger.debug("Image loaded and preprocessed successfully.")
    return image


def diagnose(image_path, crop_type):
    logger.info("Starting diagnosis...")
    start_time = time.time()
    # 이미지 로드 및 전처리
    image = load_and_preprocess_image(image_path)
    # 모델 호출
    model = get_model_by_crop(crop_type) 
    logger.debug(f"Get {crop_type} model")
# 추론 
    with tf.GradientTape(persistent=True) as tape:
        tape.watch(image)
        outputs = model(image)
        outputs = tf.stop_gradient(outputs)
    logger.debug(f"Completed Inference")
    # 상위 3개의 클래스 및 확률 추출
    top_classes = tf.math.top_k(outputs, k=3).indices.numpy()[0].tolist()
    
    # 클래스를 병명으로 변환
    disease_map = get_disease_map()
    label_map = get_label_map(crop_type)
    
    # 병명 코드 구하기
    code_list = [label_map[i] for i in top_classes]
    
    # 병명 코드로부터 병명 구하기
    top_diseases = [disease_map[code] for code in code_list]
    logger.debug(f"top diseases: {top_diseases}")
    # 각 클래스의 확률값 추출
    softmax = tf.keras.layers.Softmax(axis=1)
    probabilities = softmax(outputs)[0].numpy()
    top_probabilities = [probabilities[class_label] for class_label in top_classes]
    top_probabilities = [float(probability) for probability in top_probabilities]

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Diagnosis completed in {elapsed_time} seconds.")
    return top_diseases, top_probabilities