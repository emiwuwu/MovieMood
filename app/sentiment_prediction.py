# Import necessary libraries
import pickle
import tensorflow as tf

# Define parameters for the model
MAX_NUM_WORDS = 100000
MAX_SEQUENCE_LEN = 250
MODEL_PATH = 'Models/sentiment_analysis_model.h5'

# Load the saved model
model = tf.keras.models.load_model(MODEL_PATH)

# Load the tokenizer
with open('Models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


# Define a function to decode sentiment based on the score
def decode_sentiment(score):
    return "Positive" if score >= 0.4 else "Negative"


# Define a function to predict sentiment for a list of texts
def predict(text_list):
    predicted_labels = []
    for text in text_list:
        # Tokenize the input text
        tokens = tf.keras.preprocessing.text.text_to_word_sequence(text)
        tokens = [tokenizer.word_index[word]
                  if word in tokenizer.word_index else 0 for word in tokens]

        # Pad and preprocess the tokenized text
        x_test = tf.keras.preprocessing.sequence.pad_sequences(
            [tokens], maxlen=MAX_SEQUENCE_LEN)

        # Predict sentiment score and decode it
        score = model.predict(x_test)[0]
        label = decode_sentiment(score)
        predicted_labels.append(label)

    return predicted_labels
