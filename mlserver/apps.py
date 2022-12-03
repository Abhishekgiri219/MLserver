from django.apps import AppConfig
import pickle


class MlserverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mlserver'

    model = pickle.load(
        open("C:/Users/Abhishek Giri/Documents/iot/mlserver/mlmodel/collision_detection_NB_model_2.sav", "rb"))
