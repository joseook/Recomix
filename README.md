
# Anime and Music Recommendation System

This project is an Anime and Music recommendation system developed in Python. It utilizes advanced natural language processing (NLP) and machine learning techniques to provide personalized recommendations for Anime shows and Music tracks based on user preferences.

## Requirements

- Python 3.x
- Libraries: `numpy`, `pandas`, `scikit-learn`, `nltk`, `gensim`, `keras`, `sqlite3`, `PyInquirer`, `textblob`, `beautifulsoup4`

## Project Structure

```
RecoMix/
│
├── anime_scripts/
│   ├── main_anime.py               # Main script for Anime recommendations
│   ├── utils/                      # Module containing project utilities
│   │   ├── database_operations.py   # Functions for database management
│   │   ├── data_preprocessing.py    # Functions for data preprocessing
│   │   ├── feature_extraction.py    # Functions for feature extraction
│   │   ├── feedback.py             # User feedback collection and storage
│   │   ├── input_validators.py     # User input validators
│   │   └── model.py                # Algorithms for recommendation calculation
│   
│
├── music_scripts/
│   ├── main_music.py               # Main script for Music recommendations
│   ├── utils/                      # Module containing project utilities
│   │   ├── database_operations.py   # Functions for database management
│   │   ├── data_preprocessing.py    # Functions for data preprocessing
│   │   ├── feature_extraction.py    # Functions for feature extraction
│   │   ├── feedback.py             # User feedback collection and storage
│   │   ├── input_validators.py     # User input validators
│   │   └── model.py                # Algorithms for recommendation calculation
│   └── ...
│
├── styles/                         # Custom style files
│   ├── menu_style_music.py         # Style for music interactive menus
│   └── menu_style_animes.py         # Style for anime
│
└── README.md                       # Project documentation
```

## How to Use

1. **Installing Dependencies**:
   Ensure that all the necessary libraries are installed. You can do this by running the following command in the project's root directory:

   ```bash
   pip install -r requirements.txt
   ```

2. **Anime Recommendation**:
   To start Anime recommendations, run the following command in the `anime_scripts` folder:

   ```bash
   python main_anime.py
   ```

   The system will present an interactive menu where users can choose from various recommendation options.

3. **Music Recommendation**:
   To initiate Music recommendations, run the following command in the `music_scripts` folder:

   ```bash
   python main_music.py
   ```

   Similar to Anime, the system will present an interactive menu to select recommendation options.

## User Feedback

The system allows users to provide feedback on recommendations, contributing to continuous system improvement. Feedback is stored in a structured manner in a database for future analysis.

## Final Thoughts

This project provides a solid and flexible foundation for developing high-quality recommendation systems. You can customize and expand the system by adding additional features and fine-tuning recommendation models as needed.

Enjoy exploring new Anime shows and Music tracks with your personalized Anime and Music Recommendation System!

## Notes: 
Ensure that the required data, such as CSV files and embedding models, are present in the appropriate folders before running the recommendation system. Additionally, make sure Python virtual environments (venv) are set up correctly to avoid dependency conflicts.

---
