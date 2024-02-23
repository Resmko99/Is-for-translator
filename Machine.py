import tensorflow as tf
import numpy as np



def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def prepare_data(input_sentences, target_sentences, input_tokenizer, target_tokenizer, max_len):
    input_seq = input_tokenizer.texts_to_sequences(input_sentences)
    target_seq = target_tokenizer.texts_to_sequences(target_sentences)

    input_seq = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=max_len, padding='post')
    target_seq = tf.keras.preprocessing.sequence.pad_sequences(target_seq, maxlen=max_len, padding='post')

    decoder_target_data = np.zeros((len(target_seq), max_len), dtype=np.int)
    for i, seq in enumerate(target_seq):
        decoder_target_data[i] = np.roll(seq, -1)

    return input_seq, target_seq, decoder_target_data



max_len = 50
num_samples = 1000

input_data = read_data('en.txt')[:num_samples]
target_data = read_data('ru.txt')[:num_samples]


input_tokenizer = tf.keras.preprocessing.text.Tokenizer()
input_tokenizer.fit_on_texts(input_data)
target_tokenizer = tf.keras.preprocessing.text.Tokenizer()
target_tokenizer.fit_on_texts(target_data)

encoder_input_data, decoder_input_data, decoder_target_data = prepare_data(input_data, target_data, input_tokenizer,
                                                                           target_tokenizer, max_len)

print("Размерность encoder_input_data:", encoder_input_data.shape)