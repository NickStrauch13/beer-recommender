# Beverage Recommendation System

A recommendation system for beers based on a set of user ratings. Built using a database of various reviews from [kaggle](https://www.kaggle.com/datasets/rdoume/beerreviews). 

## To Run

1. Extract [models](https://drive.google.com/drive/folders/10mZVUny6Aj0vQOdiCaFEtc06TC7HM3GE?usp=drive_link) in to `models/` folder
2. Set up python envoirnment and install requirements.txt
3. Start the server from root - `python src/app/server.py`

## Approaches

**Naive** - Returned the highest rated items as prediction.

**SVD** - Singular Value Decomposition to build latent vectors 

**NCF** - Neural Collaborative Filerting utilizing deep learning to train model based on user + item embeddings.

| Algorithm | RMSE  | MAE   |
|-----------|-------|-------|
| NCF       | 0.606 | 0.452 |
| SVD       | 0.614 | 0.455 |
| Naive     | 0.796 | 0.525 |


## Repo Structure

```
├── .devcontainer
├── .github
├── data
├── models
├── src
    ├── app
        ├── static
        ├── templates
    ├── notebooks
    ├── scripts
├── .gitignore
├── Makefile
├── README.md
├── requirements.txt
├── setup.sh
```