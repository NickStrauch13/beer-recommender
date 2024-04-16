# Beverage Recommendation System

## Introduction
This project develops a personalized beer recommendation system using the comprehensive dataset from [Kaggle's beer reviews](https://www.kaggle.com/datasets/rdoume/beerreviews). The system aims to help users discover beers they might like based on their taste preferences and similar users' ratings.

## Features
**Personalized Recommendations**: Tailor beer suggestions to individual user tastes.

**Rating System**: Users can rate beers on various attributes, improving recommendation accuracy.

**User Profile**s: Customizable user profiles that track taste preferences and rating history.

**Recommendation Engine**: Utilizes both collaborative filtering and content-based filtering techniques.

## To Run

### Installation - Steps to Run this Locally

Clone the repository to your local machine:
```
git clone https://github.com/NickStrach13/beverage-recommender.git
```
```
cd DUKE-RAG
```

Install the required Python libraries:
```
make install
```
OR
```
pip install requirements.txt
```

1. Extract [models](https://drive.google.com/drive/folders/10mZVUny6Aj0vQOdiCaFEtc06TC7HM3GE?usp=drive_link) in to `models/` folder
2. Set up python envoirnment and install requirements.txt
3. Start the server from root - `python src/app/server.py`
