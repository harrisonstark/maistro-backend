import tensorflow as tf
import numpy as np

labels = [
    'admiration',
    'amusement',
    'anger',
    'annoyance',
    'approval',
    'caring',
    'confusion',
    'curiosity',
    'desire',
    'disappointment',
    'disapproval',
    'disgust',
    'embarrassment',
    'excitement',
    'fear',
    'gratitude',
    'grief',
    'joy',
    'love',
    'nervousness',
    'neutral',
    'optimism',
    'pride',
    'realization',
    'relief',
    'remorse',
    'sadness',
    'surprise',
]

VALENCE_MAP = {
    'admiration': 0.6,
    'amusement': 0.5,
    'anger': 0.1,
    'annoyance': 0.3,
    'approval': 0.6,
    'caring': 0.6,
    'confusion': 0.4,
    'curiosity': 0.4,
    'desire': 0.4,
    'disappointment': 0.3,
    'disapproval': 0.2,
    'disgust': 0.2,
    'embarrassment': 0.4,
    'excitement': 0.7,
    'fear': 0.1,
    'gratitude': 0.6,
    'grief': 0.1,
    'joy': 0.9,
    'love': 0.9,
    'nervousness': 0.4,
    'optimism': 0.5,
    'pride': 0.7,
    'realization': 0.4,
    'relief': 0.7,
    'remorse': 0.3,
    'sadness': 0.2,
    'surprise': 0.5,
    'neutral': 0.5,
}

AROUSAL_MAP = {
    'admiration': 0.4,
    'amusement': 0.2,
    'anger': 0.9,
    'annoyance': 0.6,
    'approval': 0.3,
    'caring': 0.3,
    'confusion': 0.5,
    'curiosity': 0.2,
    'desire': 0.5,
    'disappointment': 0.2,
    'disapproval': 0.3,
    'disgust': 0.5,
    'embarrassment': 0.5,
    'excitement': 0.7,
    'fear': 0.9,
    'gratitude': 0.7,
    'grief': 0.9,
    'joy': 0.9,
    'love': 0.5,
    'nervousness': 0.4,
    'optimism': 0.2,
    'pride': 0.4,
    'realization': 0.7,
    'relief': 0.2,
    'remorse': 0.2,
    'sadness': 0.7,
    'surprise': 1.0,
    'neutral': 0.5,
}

#PRELIMINARY METHOD!!! ideally should have the saved model loaded elsewhere
def predict_emotion(text):
    binary = tf.saved_model.load('bin.tf') #change this to int.tf to use the other model, its not much better in terms of accuracy though i think
    array = binary.serve(tf.constant([text])).numpy()
    emotion_index = array.argmax()
    emotion = labels[emotion_index] 
    return VALENCE_MAP[emotion], AROUSAL_MAP[emotion]



