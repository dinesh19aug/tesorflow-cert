from sklearn.datasets import load_boston
import pandas as pd
from tensorflow import keras
import tensorflow as tf

boston = load_boston();
print(load_boston().feature_names)

boston_df = pd.DataFrame(boston.data)

boston_df.columns = boston.feature_names
boston_price_df = pd.DataFrame(boston.target)
boston_room_df = boston_df['RM']


#define model

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
#compile model
model.compile(optimizer='sgd',loss='mean_squared_error')

#train the model
model.fit(boston_room_df,boston_price_df, batch_size=5, epochs=500)

#predict
print(model.predict([7.0]))
