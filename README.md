[![CI](https://github.com/NickStrauch13/beverage-recommender/actions/workflows/python-ci.yml/badge.svg)](https://github.com/NickStrauch13/beverage-recommender/actions/workflows/python-ci.yml)
# Beverage Recommendation System

<p align="center">
    <img src="./data/readmepic.png" width="200">
</p>

In this project, we developed a beverage recommendation system utilizing both deep learning and traditional machine learning approaches to cater to diverse user preferences. We implemented Neural Collaborative Filtering (NCF) for a personalized and dynamic recommendation experience, alongside Singular Value Decomposition (SVD) to provide a robust baseline using matrix factorization techniques. The system aims to enhance user discovery of beers by effectively matching individual tastes with novel and appealing beer options.

## To Run

The run the application locally, follow these steps:
1. Clone the repository to your local machine.
2. Create a virtual python environment using `python -m venv venv`.
3. Activate the virtual environment using `source venv/bin/activate` for mac/linux or `venv\Scripts\activate` for windows.
4. Install the project requirements using `pip install -r requirements.txt`.
5. Download the models [here](https://drive.google.com/drive/folders/10mZVUny6Aj0vQOdiCaFEtc06TC7HM3GE?usp=drive_link) and place them in the `models/` directory in the project root.
6. Run the application from the root directory using `python .src/app/server.py`.

## Data

The [dataset](https://www.kaggle.com/datasets/rdoume/beerreviews) user for this project features an extensive variety of over 100 different beer styles and more than 66,000 unique beers, each accompanied by user ratings. These beers originate from over 6,000 breweries, showcasing a wide range of brewing coverage. Additionally, the dataset includes reviews from more than 33,000 beer enthusiasts, providing a rich and diverse foundation for our recommendation system to analyze and predict user preferences effectively. This broad and detailed dataset ensures robust training and testing of our models, enhancing the accuracy and relevance of the recommendations generated.

## Approaches

**Naive** - Returned the highest rated items as prediction.

**SVD** - Singular Value Decomposition to build latent vectors 

**NCF** - Neural Collaborative Filerting utilizing deep learning to train model based on user + item embeddings.

## Evaluation
The evaluation results indicate that both the Neural Collaborative Filtering (NCF) and Singular Value Decomposition (SVD) algorithms significantly outperform the naive baseline, demonstrating lower values in Root Mean Square Error (RMSE) and Mean Absolute Error (MAE). Notably, NCF shows a slightly better performance compared to SVD, suggesting its effectiveness in providing more accurate and personalized beer recommendations.

| Algorithm | RMSE  | MAE   |
|-----------|-------|-------|
| NCF       | 0.606 | 0.452 |
| SVD       | 0.614 | 0.455 |
| Naive     | 0.796 | 0.525 |


## Project Structure

```
├── .devcontainer
├── .github
├── data
├── models
├── src
│   ├── app
│   │   ├── static
│   │   ├── templates
│   ├── notebooks
│   ├── scripts
├── .gitignore
├── Makefile
├── README.md
├── requirements.txt
├── setup.sh
```


