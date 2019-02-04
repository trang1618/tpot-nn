import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=None)

# Average CV score on the training set was:0.5415391498881432
exported_pipeline = make_pipeline(
    PCA(iterated_power=5, svd_solver="randomized"),
    MLPClassifier(activation="tanh", alpha=0.001, learning_rate="invscaling", learning_rate_init=0.9, momentum=0.9, solver="adam")
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)