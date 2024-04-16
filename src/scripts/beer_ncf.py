import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.optimizers import Adam

def load_data_and_fit_encoders():
    '''
    Load the data and fit the encoders
    '''
    df = pd.read_csv('../../data/beer_reviews.csv')

    ndf = df[['review_profilename', 'beer_beerid', 'review_overall']]

    ndf.dropna()

    # Create a dictionary mapping beer IDs to names
    beer_id_to_name = pd.Series(df.beer_name.values, index=df.beer_beerid).to_dict()

    # Encode 'review_profilename' and 'beer_beerid'
    user_encoder = LabelEncoder()
    item_encoder = LabelEncoder()

    ndf['user_encoded'] = user_encoder.fit_transform(ndf['review_profilename'])
    ndf['item_encoded'] = item_encoder.fit_transform(ndf['beer_beerid'])

        
    # Split the dataset
    train, test = train_test_split(ndf, test_size=0.2, random_state=42)

    return ndf, train, test


def create_ncf(num_users, num_items, embedding_size, layer_sizes=[64, 32, 16, 8]):
    '''
    Create a Neural Collaborative Filtering model
    '''
    # Input layers
    user_input = layers.Input(shape=(1,))
    item_input = layers.Input(shape=(1,))

    # Embeddings layers
    user_embedding_gmf = layers.Embedding(num_users, embedding_size, embeddings_initializer='he_normal',
                                          embeddings_regularizer=tf.keras.regularizers.l2(1e-6))(user_input)
    user_embedding_gmf = layers.Flatten()(user_embedding_gmf)

    item_embedding_gmf = layers.Embedding(num_items, embedding_size, embeddings_initializer='he_normal',
                                          embeddings_regularizer=tf.keras.regularizers.l2(1e-6))(item_input)
    item_embedding_gmf = layers.Flatten()(item_embedding_gmf)

    user_embedding_mlp = layers.Embedding(num_users, embedding_size, embeddings_initializer='he_normal',
                                          embeddings_regularizer=tf.keras.regularizers.l2(1e-6))(user_input)
    user_embedding_mlp = layers.Flatten()(user_embedding_mlp)

    item_embedding_mlp = layers.Embedding(num_items, embedding_size, embeddings_initializer='he_normal',
                                          embeddings_regularizer=tf.keras.regularizers.l2(1e-6))(item_input)
    item_embedding_mlp = layers.Flatten()(item_embedding_mlp)

    # GMF part
    gmf_mul = layers.Multiply()([user_embedding_gmf, item_embedding_gmf])

    # MLP part
    mlp_concat = layers.Concatenate()([user_embedding_mlp, item_embedding_mlp])
    mlp = mlp_concat
    for layer_size in layer_sizes:
        mlp = layers.Dense(layer_size, activation='relu')(mlp)

    # Concatenate GMF and MLP parts
    concat = layers.Concatenate()([gmf_mul, mlp])

    # Final prediction layer scaled to 0-5 range
    output = layers.Dense(1, activation='linear')(concat)
    output = layers.Lambda(lambda x: x * 5)(output)

    model = Model(inputs=[user_input, item_input], outputs=output)
    model.compile(optimizer=Adam(learning_rate=0.00005), loss='mse', metrics=['mae'])

    return model

def train_model(model,train):
    '''
    Train the model
    '''
    # Preparing the data   
    x_train = [train['user_encoded'].values, train['item_encoded'].values]
    y_train = train['review_overall'].values

    # Training the model
    history = model.fit(x_train, y_train, batch_size=128, epochs=1, validation_split=0.2)

    return model

def test_model(model,test):
    '''
    Test the model
    '''
    # Preparing the data
    x_test = [test['user_encoded'].values, test['item_encoded'].values]
    y_test = test['review_overall'].values  # Use actual ratings

    # Evaluate the model using regression metrics
    test_loss, test_mae = model.evaluate(x_test, y_test)
    print(f'Test MSE: {test_loss}, Test MAE: {test_mae}')


def main():
    '''
    Main function
    '''

    # Load the data and fit the encoders
    ndf, train, test = load_data_and_fit_encoders()


    # Instantiate and train the model
    num_users = ndf['user_encoded'].nunique()
    num_items = ndf['item_encoded'].nunique()
    embedding_size = 256
    model = create_ncf(num_users, num_items, embedding_size)
    model = train_model(model,train)
    test_model(model,test)
