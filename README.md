# Report: Mobile Recommendation System Using Cosine Similarity and K-Nearest Neighbors (KNN)

## Dataset Description

The dataset comprises various features of mobile phones, including:
- **Name**: Model of the mobile phone
- **Rating**: Average user rating
- **Price Rs**: Price in Indian Rupees
- **RAM Gb**: RAM capacity
- **ROM Gb**: ROM capacity
- **Expandable GB**: Expandable storage
- **Size Cm/Inch**: Dimensions
- **Camera MP**: Camera resolution
- **Battery Mah**: Battery capacity
- **Processor**: Processor type
- **Image**: Mobile image

## Data Preprocessing

Data preprocessing involved:
- **Handling Missing Values**: Missing values for features like Rating and Expandable GB were assigned default values (0). String values in Price were corrected.
- **Label Encoding**: Categorical data such as Processor Brand was encoded numerically.
- **Normalization**: Feature scaling and normalization were applied to ensure consistent data ranges.

## Exploratory Data Analysis (EDA)

Key insights include:
- **Price and Rating**: Positive correlation between price and rating.
- **Feature Relationships**: RAM, ROM, and camera features positively correlated with ratings and prices, while screen size and battery capacity showed inverse relationships.

## Methodology

1. **Cosine Similarity**:
   - **Feature Extraction**: Numerical representation of mobile attributes.
   - **Feature Vector Construction**: Mobile products represented as feature vectors.
   - **Similarity Calculation**: Computed cosine similarity between products.
   - **Top-N Recommendations**: Recommended items based on highest similarity scores.
   - **Benefits**: Intuitive and robust to feature magnitudes; however, it is sensitive to data sparsity.

2. **K-Nearest Neighbors (KNN)**:
   - **Data Preprocessing**: Conversion of categorical features to numerical values.
   - **Feature Extraction**: Transformation of textual data into numerical vectors.
   - **Model Training**: KNN model trained with features such as Brand, RAM, ROM, and Battery.
   - **Recommendation Generation**: Used cosine similarity to find and recommend similar items.
   - **Benefits**: Simple, versatile, and handles non-linear data; however, it is computationally expensive and sensitive to noisy data.

## Experimental Results and Analysis

The KNN algorithm, tested on a system with AMD Ryzen 5 CPU and 1024 GB memory, demonstrated satisfactory performance. Proper feature preprocessing and merging improved the recommendation quality. The KNN model provided personalized suggestions effectively, with results closely matching user inputs and offering slight variations for broader recommendations.

## Conclusion and Future Work

The study successfully demonstrated the effectiveness of combining Cosine Similarity and KNN for mobile recommendations. While the system provided accurate and personalized suggestions, limitations include dependency on comprehensive data and the need for ongoing updates. Future work will explore incorporating additional techniques like collaborative filtering and matrix factorization to enhance recommendation accuracy and coverage.
