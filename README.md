# 🍽️ Restaurant Recommendation System

This project is a machine learning–based **Restaurant Recommendation System** that suggests similar restaurants based on user selection. It uses **K-Nearest Neighbors (KNN)** and a pre-computed **feature matrix** to recommend the top 5 alternatives for any given restaurant, based on factors like rating, cuisine, and more.

The app is fully interactive, deployed using **Streamlit**, and designed with user experience in mind.

---

## 📌 Table of Contents

- [🔍 Overview](#-overview)
- [📁 Dataset Description](#-dataset-description)
- [🧠 ML Pipeline](#-ml-pipeline)
- [💻 Streamlit App Features](#-streamlit-app-features)
- [📊 Sample Input/Output](#-sample-inputoutput)
- [⚙️ Installation & Run Locally](#️-installation--run-locally)
- [📁 Project Structure](#-project-structure)
- [📦 Requirements](#-requirements)
- [🚀 Future Enhancements](#-future-enhancements)
- [🧠 Learnings](#-learnings)
- [📬 Contact](#-contact)
- [📝 License](#-license)

---

## 🔍 Overview

This project provides an intuitive interface for users to:
- Select a restaurant from a list
- Get top 5 similar restaurants using a KNN model
- View rating, cuisine, and other details for recommendations

The project is useful for:
- Food delivery platforms
- Restaurant search engines
- Academic ML deployments

---

## 📁 Dataset Description

The dataset used in this project contains the following key features:

| Feature               | Description                                   |
|-----------------------|-----------------------------------------------|
| `Restaurant Name`     | Name of the restaurant                        |
| `Aggregate rating`    | Average user rating (0–5 scale)               |
| `Cuisines`            | Type(s) of cuisine served                     |
| `Locality`, `City`    | Geographical area (not used in model)         |
| Other columns         | Additional metadata available                 |

---

## 🧠 ML Pipeline

### ✅ Model: K-Nearest Neighbors (KNN)

- **Input:** Feature matrix (preprocessed from the dataset)
- **Algorithm:** NearestNeighbors from `sklearn`
- **Distance metric:** Euclidean
- **Neighbors:** 6 (top 5 recommendations shown)

### ✅ Feature Engineering:
- Feature matrix was built using numerical + encoded features like:
  - Cuisine frequencies
  - Location clusters
  - Ratings
- Precomputed and stored in `feature_matrix.pkl`

---

## 💻 Streamlit App Features

- 📊 **Restaurant selection dropdown**
- 🤖 **AI-based recommendations**
- 📍 View rating & cuisine of recommended restaurants
- 💅 Custom layout with sidebar and footer
- ✅ Responsive and easy-to-use interface

---

## 📊 Sample Input/Output


Selected Restaurant: Biryani Blues

✅ Recommendations:
1. Behrouz Biryani — ⭐ 4.4 — 🍜 Mughlai, Biryani
2. Dum Safar Biryani — ⭐ 4.1 — 🍜 Hyderabadi
3. Biryani By Kilo — ⭐ 4.0 — 🍜 North Indian, Biryani
4. Paradise Biryani — ⭐ 3.9 — 🍜 Andhra, Biryani
5. Hyderabadi Express — ⭐ 3.8 — 🍜 Hyderabadi, Fast Food

### ▶️ How to Run the App

# 1️⃣ Clone the repository
git clone https://github.com/your-username/restaurant-recommender.git
cd restaurant-recommender

# 2️⃣ (Optional) Create a virtual environment
python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit app
streamlit run app2.py

##🗂️ Project Structure:
<br>
-restaurant-recommender
<br>
├── app.py                    (Streamlit frontend interface)<br>
├── app2.py                   (Streamlit application)<br>
├── features.ipynb            (Feature engineering and model training)<br>
├── Dataset .csv              (Input restaurant dataset)<br>
├── feature_matrix.pkl        (Precomputed feature matrix)<br>
├── knn_model.pkl             (Trained KNN model)<br>
├── Restaurant_banner.jpg     (App header banner)<br>
├── README.md                 (Project documentation)<br>
├── requirements.txt           (Python dependencies)<br>

##📦 Requirements:
<br>
-Python 3.7+ <br>
-pandas<br>
-numpy<br>
-scikit-learn<br>
-streamlit<br>
-pickle

##📚 Learnings & Takeaways<br>
1.Content-based filtering using KNN<br>
2.Feature engineering on restaurant metadata<br>
3.UI/UX design using Streamlit,br>
4.Optimizing real-time ML inference with preloaded models<br>

##🚀 Future Improvements<br>
1.Include filters by rating, cuisine, or price<br>
2.Use cosine similarity or hybrid recommendation techniques<br>
3Include restaurant images or maps<br>
4.Add NLP-based review sentiment similarity<br>

##🤝 Contributing<br>
Pull requests and suggestions are welcome. For major changes, please open an issue first to discuss what you would like to change.

##📬 Contact:<br>
-Author: Aniketanand Sandipkumar<br>
📧 [Email-Id](aniketanand2712@gmail.com)<br>
🔗 [LinkedIn](www.linkedin.com/in/aniketanand-sandipkumar-8475ab258)<br>
[App link](https://restraunt-recommendation-system-qpuqi3rhwpv8appr2tgxrd.streamlit.app)

