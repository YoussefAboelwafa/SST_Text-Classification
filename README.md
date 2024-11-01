# Text Classification

Sentiment Classification into five distinct classes using the Stanford Sentiment Treebank (SST) dataset using two different classification models: Naive Bayes & Logistic Regression.

## Dataset

The SST dataset consists of labeled sentences with sentiment scores, where scores closer to 0 indicate negative sentiment and scores closer to 1 indicate positive sentiment. To simplify the classification task, the sentiment scores are mapped to five categories as follows:

- **0 to 0.2 (inclusive):** Very Negative
- **0.2 to 0.4 (inclusive):** Negative
- **0.4 to 0.6 (inclusive):** Neutral
- **0.6 to 0.8 (inclusive):** Positive
- **0.8 to 1.0 (inclusive):** Very Positive

## Model Architecture

**Logistic Regression**: A linear model for binary classification that can be extended to multiclass classification using the One-vs-Rest (OvR) strategy.

**Stochastic Gradient Descent (SGD)**: An optimization algorithm used to train the logistic regression model.

## Training Process

The training process involves the following steps:

1. **Tokenization**: Convert sentences into tokens.
2. **Bigrams Extraction**: Extract bigrams from the tokenized sentences.
3. **Feature Matrix Generation**: Generate a feature matrix for the training dataset using the extracted bigrams.
4. **Feature Filtering**: Filter features for validation and test datasets to match the training features.
5. **Model Training**: Train the models using the training dataset and validate using the validation dataset.
6. 
## Testing and Evaluation

- The models are evaluated using the test dataset.
- The evaluation metrics include accuracy, precision, recall, and F1-score.

## Results

The results of the models are logged using Comet.ml for tracking and visualization.
![Comet Experiments](https://www.comet.com/youssefaboelwafa/nlp-lr/view/new/panels)

![train_accuracy,val_accuracy VS step](https://github.com/user-attachments/assets/03072ad6-2f4c-4e08-a6f6-e406bb4fef1f)
![train_loss,val_loss VS step](https://github.com/user-attachments/assets/d955e37e-0d4e-4ee0-80d6-c82b960e51af)


