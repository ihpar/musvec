from sklearn.manifold import TSNE
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.rad2deg(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))


def reduce_dimensions(wv, perplexity=2, n_iter=1000):
    num_dimensions = 2

    vectors = np.asarray(wv.vectors)
    labels = np.asarray(wv.index_to_key)

    tsne = TSNE(n_components=num_dimensions,
                perplexity=perplexity, n_iter=n_iter)

    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    return x_vals, y_vals, labels


def create_angle_matrix(wv):
    angles_dict = {}
    for current in wv.key_to_index:
        # if current == UNK_TAG:
        #     continue

        angles_dict[current] = {}
        for pitch in wv.key_to_index:
            # if pitch == UNK_TAG:
            #     continue

            angle = round(angle_between(wv[current], wv[pitch]), 2)
            angles_dict[current][pitch] = angle

    return angles_dict
