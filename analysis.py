import pandas as pd


# add predicted probabilities to df_test
def add_predicted_proba(clf, df_test, X_test):
    probabilities = clf.predict_proba(X_test)
    df_test['probabilities'] = probabilities.tolist()
    return df_test


# wrong predictions
def wrong_predictions(clf, df_test, X_test, y_test):
    clf_predictions = clf.predict(X_test)
    wrong_indices = [i for i in range(len(y_test)) if y_test[i] != clf_predictions[i]]
    # add here indices for the correct guesses
    correct_indices = [i for i in range(len(y_test)) if i not in wrong_indices]
    df_wrong_predictions = df_test.iloc[wrong_indices, :]
    df_correct_predictions = df_test.iloc[correct_indices, :]
    return df_wrong_predictions, df_correct_predictions


# band / number of songs dataframe
def bands(df):
    song_counts = df['band'].value_counts()
    df_bands = pd.DataFrame(song_counts)
    df_bands_reset = df_bands.reset_index()
    df_bands_reset.columns = ['band', 'songs']
    df_bands = df_bands_reset.sort_values('band').reset_index(drop=True)
    return df_bands


def wrong_predictions_perband(df_wrong_predictions, df_bands):
    value_counts = df_wrong_predictions['band'].value_counts()
    df_val_counts = pd.DataFrame(value_counts)
    df_val_counts_reset = df_val_counts.reset_index()
    df_val_counts_reset.columns = ['band', 'wrong_predictions']
    df_val_counts = df_val_counts_reset.sort_values('band').reset_index(drop=True)

    df_wrong_predictions_perband = pd.merge(df_val_counts, df_bands, how='inner', on=['band'])
    df_wrong_predictions_perband['wrong_guesses_percentage'] = df_wrong_predictions_perband['wrong_predictions'] / \
                                                               df_wrong_predictions_perband['songs'] * 100
    df_wrong_predictions_perband = df_wrong_predictions_perband.sort_values('wrong_guesses_percentage')
    return df_wrong_predictions_perband


def bands_with_genre(df):
    df_genre = df[['band', 'genre']]
    df_genre = df_genre.drop_duplicates(subset=['band'])
    df_genre = df_genre.sort_values(by=['band'])
    return df_genre

def bands_songs_genre(df):
    df_bands = bands(df)
    df_genre = bands_with_genre(df)
    df_bands = df_bands.merge(df_genre, on='band', how='inner')
    return df_bands

def average_blackness(df):
    df_exploded = df.explode('probabilities').reset_index(drop=True)
    df_exploded = df_exploded[df_exploded.index % 2 != 0]
    return df_exploded['probabilities'].mean()


def average_deathness(df):
    df_exploded = df.explode('probabilities').reset_index(drop=True)
    df_exploded = df_exploded[df_exploded.index % 2 == 0]
    return df_exploded['probabilities'].mean()
