from keras.models import load_model


def load_from_model(name_path):
    model = load_model(name_path)
    return model


def show_summary(model):
    model.summary()


def process_keras_model(name_path):
    print("calling process_keras_mode...")
    model = load_from_model(name_path)
    show_summary(model)
