
"""
datasets.py
===========

Access geographical datasets.

Commands
--------
    list_datasets() : get a list of available datasets.
    dataset_metadata(dataset_name) : get metadata on specified
        dataset.
    load_dataset(dataset_name) : load dataset. Returns a numpy array.
"""

import csv
import codecs

from six.moves.urllib.request import urlopen

METADATA = {
    "sentiment": {
        "url": "https://drive.google.com/uc?export=download&id=1ainFBoDOGw8WigTH0iTHSUjQJOHMefKg",#http://127.0.0.1:8888/tree/util/sentiment.csv",  # noqa
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_00neg": {
        "url": "https://drive.google.com/uc?export=download&id=1xfRXV7k7-tMdu5k_tb3XdDfmPCgJXLa9", # noqa
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_00neu": {
        "url": "https://drive.google.com/uc?export=download&id=1s6q6TSW1xJ9xEh8nLfjpcLrAlR3iVk5d", # noqa
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_00pos": {
        "url": "https://drive.google.com/uc?export=download&id=1UbQm_eDmIkYSgJv1jWWBUBpniC_0Z3A7", # noqa
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_01neg": {
        "url": "https://drive.google.com/uc?export=download&id=1wOMVXly4_2z2MKUS9y81CJQQas5lfpj5", # noqa
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_01neu": {
        "url": "https://drive.google.com/uc?export=download&id=1cWWQ3ZEzDwPmd8QPAclHfqX5LoDLCBaS", # noqa
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_01pos": {
        "url": "https://drive.google.com/uc?export=download&id=1SSauGRepZJAUHC6Ca1FjhuUao7TsE1CL", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_02neg": {
        "url": "https://drive.google.com/uc?export=download&id=1YZYrrLMIYgxMgXKuuHlpnMaeeTNEHM7u", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_02neu": {
        "url": "https://drive.google.com/uc?export=download&id=1rhMZhTpze_2ROq-KFEMRY8-MPWKnS5Ob", # noqa        
            "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_02pos": {
        "url": "https://drive.google.com/uc?export=download&id=1VOilXJhiu1coopgg0DW3BP0U7sE7Spo7", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_03neg": {
        "url": "https://drive.google.com/uc?export=download&id=10TSGcdwVLmaT3AJ4ZEMguMxuVLYnp0yR", # noqa        
                "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_03neu": {
        "url": "https://drive.google.com/uc?export=download&id=1pY7jcmUWD8z5kV_VAlC108tGgr6Q9VoU", # noqa        
            "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_03pos": {
        "url": "https://drive.google.com/uc?export=download&id=1e5_QhpAZY1ucCS50OYGKtSY-deGBDH8M", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_04neg": {
        "url": "https://drive.google.com/uc?export=download&id=15xnLNWTzt12V_Pv-yZKLwpeu5_GohxkL", # noqa        
                "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_04neu": {
        "url": "https://drive.google.com/uc?export=download&id=1Cw_AZAIRoPnlnmN9dgaaSGDRzjGy7RQM", # noqa        
            "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_04pos": {
        "url": "https://drive.google.com/uc?export=download&id=1dildeidI5Nw-aWgGgoMEk0Dx104y0rdW", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_05neg": {
        "url": "https://drive.google.com/uc?export=download&id=1IE8FcOTBel3jgA7LgrmbW5992K3jgJ_s", # noqa        
                "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_05neu": {
        "url": "https://drive.google.com/uc?export=download&id=1Eh0ZLO9PKE8zxACJ1P6NlXjDCVFXe5ge", # noqa        
            "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_05pos": {
        "url": "https://drive.google.com/uc?export=download&id=1N5vRvRisC_5fWO3XyKJAq1m0URQFpbUo", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_06neg": {
        "url": "https://drive.google.com/uc?export=download&id=1pGrQLPsx-ykxh0n6Tf0ZKr1U45uVcV28", # noqa        
                "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_06neu": {
        "url": "https://drive.google.com/uc?export=download&id=1iR0YLJ3tnpjTUhstzY7WVYIOiskkkLcB", # noqa        
            "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_06pos": {
        "url": "https://drive.google.com/uc?export=download&id=1jXkWRsP2basnvoLrNOkGfxAwY8vza7M8", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_07neg": {
        "url": "https://drive.google.com/uc?export=download&id=1cPSHbvUeHO-B_AVWSS-hYcMmcaKd3RUp", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_07neu": {
        "url": "https://drive.google.com/uc?export=download&id=1ETJHvw9PNhHHlH05bU7f_zkJdJrOEChW", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_07pos": {
        "url": "https://drive.google.com/uc?export=download&id=1b3R5CViB_tnMLjIQCuhrZEVNHcwjCt2l", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_08neg": {
        "url": "https://drive.google.com/uc?export=download&id=1MpsT_VOkiXcZsb64ebtIqErm45TpSSv6", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_08neu": {
        "url": "https://drive.google.com/uc?export=download&id=1TCBRDISNhpWc0C2_3zFXM1J_WCh4KFci", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_08pos": {
        "url": "https://drive.google.com/uc?export=download&id=16ZynKiHWjIvLwvZ3ctXYnBReTJNB0mpR", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_09neg": {
        "url": "https://drive.google.com/uc?export=download&id=1G0EEoJrZ4DGe06-1YAp3NgSPHBBlIJs9", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_09neu": {
        "url": "https://drive.google.com/uc?export=download&id=1fMKzgeArhTrLJqZLqWNYlsAmbFZk-7nX", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_09pos": {
        "url": "https://drive.google.com/uc?export=download&id=1ecgPf6AovgtOITddANTGQqxSNBJjay8f", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_10neg": {
        "url": "https://drive.google.com/uc?export=download&id=1FePzJwTM8VtwKBtyPg1vI9tnY-1V88dH", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_10neu": {
        "url": "https://drive.google.com/uc?export=download&id=1UHOL3Ca5r9Rdhbz2zrF6QqvxPMMrzGlU", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_10pos": {
        "url": "https://drive.google.com/uc?export=download&id=1-ZXDsd0JFj0keT3INmJJONlHTT1TtumL", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_11neg": {
        "url": "https://drive.google.com/uc?export=download&id=1eXtSW0AR8PCzhHZ4oTTQ48AY6fp7TzVX", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_11neu": {
        "url": "https://drive.google.com/uc?export=download&id=13Z24mdzkXAqHa25BtWhzlNa-IzV6qjvc", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_11pos": {
        "url": "https://drive.google.com/uc?export=download&id=1yr8DkgdkROlC6Ql3STDGH2C6cJjKLtoP", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_12neg": {
        "url": "https://drive.google.com/uc?export=download&id=1WrfZ8-s-TGTYyAnpKcJ7t5rUGVlZieH-", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_12neu": {
        "url": "https://drive.google.com/uc?export=download&id=1Kwnz8BMKeRCOToTgn8pIbRpHq4ovLKR-", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_12pos": {
        "url": "https://drive.google.com/uc?export=download&id=1QXiRkjuMeaD2Dj_ifPjH2BBX28boOQIo", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_13neg": {
        "url": "https://drive.google.com/uc?export=download&id=1c-siXKVq69ydNlfdrXd4FNyA1kxx9ySz", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_13neu": {
        "url": "https://drive.google.com/uc?export=download&id=1hJi6claeGVAvo9qzi-2MvnPbBEGGc64I", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_13pos": {
        "url": "https://drive.google.com/uc?export=download&id=1wLoud4tkkz0lCkqIcAJ5-Xe3PJv7-N2x", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_14neg": {
        "url": "https://drive.google.com/uc?export=download&id=1Wb-aT8MZg6D6e7tuefywWoBfHa7YflBL", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_14neu": {
        "url": "https://drive.google.com/uc?export=download&id=1oNorRoylsB3b0KwPj_c1zPV3SkLU9a8G", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_14pos": {
        "url": "https://drive.google.com/uc?export=download&id=1i4xRpSgvhAMvTeMRpdml8as1d8gQ4-1w", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_15neg": {
        "url": "https://drive.google.com/uc?export=download&id=1v7vLQwGEzMG61t5GNClnmH9_c3H9yveg", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_15neu": {
        "url": "https://drive.google.com/uc?export=download&id=1ZzMsESRliqZrHWDIai2xKcORoDcyntE1", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_15pos": {
        "url": "https://drive.google.com/uc?export=download&id=1mV7EuQmlao7A6fQ02ItwxMMkqO-D7RIs", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_16neg": {
        "url": "https://drive.google.com/uc?export=download&id=1J5TYY1WakuP9F66VzeN6yHJMw4TTwWtH", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_16neu": {
        "url": "https://drive.google.com/uc?export=download&id=1L3Wd14aDsXGpfDve15ACKO2xjfCAB-CW", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_16pos": {
        "url": "https://drive.google.com/uc?export=download&id=1c239JgWyYxR5nkFuz1U8nPhcBQmK79-c", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_17neg": {
        "url": "https://drive.google.com/uc?export=download&id=1PXXFc590Ip_-rBKLtC6koby2kwngnLCU", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_17neu": {
        "url": "https://drive.google.com/uc?export=download&id=1aF-_bNAIjKFMZfVAyrgOq_umblKYKTLS", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_17pos": {
        "url": "https://drive.google.com/uc?export=download&id=1quReAyOwLuq6seMQhvhK4Yqm-AqGC7X3", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_18neg": {
        "url": "https://drive.google.com/uc?export=download&id=1U_jm8brafQXOb9nC-R9VW68mrCs3qKur", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_18neu": {
        "url": "https://drive.google.com/uc?export=download&id=1x74ixRRS96McUCb3rXFtA5yJgzLzdnoh", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_18pos": {
        "url": "https://drive.google.com/uc?export=download&id=1BoRofaGnsGgDWWNa8OWhOT7rLjmFWtF3", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_19neg": {
        "url": "https://drive.google.com/uc?export=download&id=1zMF7rHrzUC5GUCTD99NmdRBCcKC75qaB", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_19neu": {
        "url": "https://drive.google.com/uc?export=download&id=1hUyaNWl3daXNeP0GreYwvpBZOGd8ab6M", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_19pos": {
        "url": "https://drive.google.com/uc?export=download&id=1vTJXWHwvYdzEelBX-koEulIMMGt7S6Qm", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_20neg": {
        "url": "https://drive.google.com/uc?export=download&id=1EcPvxP_jmvxCiWGzuROYLeUkxHwnqCkz", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_20neu": {
        "url": "https://drive.google.com/uc?export=download&id=1YxVNh7VXPOszKzvS6SWMmfqKmCDsyARP", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_20pos": {
        "url": "https://drive.google.com/uc?export=download&id=1W6_oW7qzaO-3xuEgUvNiXhWWLjSwxhJQ", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_21neg": {
        "url": "https://drive.google.com/uc?export=download&id=1_i-hLf5jxbxJD871tpIr8BHOoxaPU4zI", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_21neu": {
        "url": "https://drive.google.com/uc?export=download&id=15OVzpfaYcdpX77VzoEWxYaewUBRPM0lC", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_21pos": {
        "url": "https://drive.google.com/uc?export=download&id=1-9sTxJUoWpkgWvOlLxy1dS8tkthHu_MO", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_22neg": {
        "url": "https://drive.google.com/uc?export=download&id=1FKuuWpDnawKamJxQCcUB8aFuN3crQ481", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_22neu": {
        "url": "https://drive.google.com/uc?export=download&id=1OhoP-LM8BdhzDxpgzvPtNVgiAFCUqjZO", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_22pos": {
        "url": "https://drive.google.com/uc?export=download&id=1-98HxbnfXdf3vp-rbZzKFu1VDfmwzEIi", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
            "sentiment_23neg": {
        "url": "https://drive.google.com/uc?export=download&id=1nAeymJPnvUW9sFacAItYShcMPwyZ9kD2", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
        "sentiment_23neu": {
        "url": "https://drive.google.com/uc?export=download&id=1kNy9OwtvhrcMyjeKy2rt4wCIDBkNo_Zp", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "sentiment_23pos": {
        "url": "https://drive.google.com/uc?export=download&id=1YJKbv2jcJlHJc2B6xJ1Ie6bO3X_JTWaQ", # noqa        
        "description": "Sentiment analysis values of English tweets worldwide",
        "headers": ["latitude", "longitude","negative","positive","neutral","compound"],
        "types": [float, float, float, float, float, float]
    },
    "taxi_rides": {
        "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/taxi_data.csv",  # noqa
        "description": "Taxi pickup location data in San Francisco",
        "headers": ["latitude", "longitude"],
        "types": [float, float]
    },
    "earthquakes": {
        "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/earthquakes.csv",  # noqa
        "description": ("All recorded earthquakes in 30 days "
                        "starting on 12th November 2014"),
        "headers": ["latitude", "longitude", "magnitude"],
        "types": [float, float, float]
    },
    "acled_africa": {
        "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/acled_africa.csv",  # noqa
        "description": "Recorded incidents of political violence in Africa",
        "source": "http://www.acleddata.com",
        "headers": ["latitude", "longitude"],
        "types": [float, float]
    },
    "london_congestion_zone": {
        "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/london_congestion_zone.csv",  # noqa
        "description": "Central part of the London congestion zone",
        "source": "https://www.google.com/maps/d/u/0/viewer?mid=1EnGO0p4-UuGlSMKyfRrMT21jfRs",  # noqa
        "headers": ["latitude", "longitude"],
        "types": [float, float]
    },
    "nuclear_plants": {
        "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/nuclear_power_plants.csv",  # noqa
        "description": "All nuclear power plants worldwide",
        "source": "IAEA (https://www.iaea.org/pris/)",
        "headers": ["latitude", "longitude"],
        "types": [float, float]
    },
    "starbucks_kfc_uk": {
        "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/starbucks_kfc_uk.csv",  # noqa
        "description": "All Starbucks and KFCs in the UK (September 2016)",
        "source": "http://ratings.food.gov.uk",
        "headers": ["latitude", "longitude", "chain_name"],
        "types": [float, float, str]
    },
    "gini": {
        "url": "https://s3-eu-west-1.amazonaws.com/jupyter-gmaps-examples/gini.csv",  # noqa
        "description": "GINI coefficient for most countries",
        "source": "https://www.cia.gov/library/publications/the-world-factbook/rankorder/2172rank.html",  # noqa
        "headers": ["country", "gini"],
        "types": [str, float]
    }
}


def _read_rows(f, column_types):
    f.readline()  # skip header line
    reader = csv.reader(codecs.iterdecode(f, "utf-8"))
    rows = []
    for row in reader:
#         print(row)
        typed_row = [
            column_type(cell) for column_type, cell in zip(column_types, row)
        ]
        rows.append(tuple(typed_row))
    return rows


def list_datasets():
    """
    List of datasets available
    """
    return METADATA.keys()


def dataset_metadata(dataset_name):
    """
    Information about the dataset

    This returns a dictionary containing a 'description',
    a list of the dataset headers and optionally information
    about the dataset source.

    :Examples:

    >>> dataset_metadata("earthquakes")
    {'description': 'Taxi pickup location data in San Francisco',
     'headers': ['latitude', 'longitude']}
    """
    metadata = METADATA[dataset_name].copy()
    del metadata["url"]
    return metadata


def load_dataset(dataset_name):
    """
    Fetch a dataset, returning an array of tuples.
    """
    url = METADATA[dataset_name]["url"]
    column_types = METADATA[dataset_name]["types"]
    
    f = urlopen(url)
    data = _read_rows(f, column_types)
    f.close()
    return data

def load_dataset_ff(dataset_name):
    """
    Fetch a dataset, returning an array of tuples.
    """
    url = METADATA[dataset_name]["url"]
    column_types = METADATA[dataset_name]["types"]
    
    f = open(url)
    data = _read_rows(f, column_types)
    f.close()
    return data

def load_dataset_as_df(dataset_name):
    """
    Fetch a dataset, returning a pandas dataframe.
    """
    import pandas as pd
    data = load_dataset(dataset_name)
    headers = dataset_metadata(dataset_name)["headers"]
    return pd.DataFrame(data, columns=headers)

def load_dataset_as_df_ff(dataset_name):
    """
    Fetch a dataset, returning a pandas dataframe.
    """
    import pandas as pd
    data = load_dataset_ff(dataset_name)
    headers = dataset_metadata(dataset_name)["headers"]
    return pd.DataFrame(data, columns=headers)