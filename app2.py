import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# ✅ Place `st.set_page_config()` at the top
st.set_page_config(page_title="🍽️ Restaurant Recommender", layout="wide")

st.image("Restaurant_banner.jpg", use_column_width=True)  # Header Banner

with st.sidebar:
    st.title("🍴 Explore Restaurants")
    st.markdown("### 🔎 Get personalized recommendations for restaurants!")
    st.info("📍 Select a restaurant and find the best alternatives nearby.", icon="ℹ️")
    st.markdown("---")
    st.write("👨‍🍳 **Powered by AI & Machine Learning**")

# Load dataset (Replace with actual loading method)
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset.csv")  # Replace with actual dataset path
    df['Restaurant Name'] = df['Restaurant Name'].str.strip().str.lower()
    return df

df = load_data()

# Load pre-trained KNN model
@st.cache_resource
def load_model():
    knn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    feature_matrix = np.random.rand(len(df), 5)  # Replace with actual feature matrix
    knn_model.fit(feature_matrix)
    return knn_model, feature_matrix

knn_model, feature_matrix = load_model()

# Function to find closest match
def get_closest_match(restaurant_name, df):
    matches = df[df['Restaurant Name'].str.contains(restaurant_name, case=False, na=False)]['Restaurant Name'].unique()
    return matches[0] if len(matches) > 0 else None

# Function to get recommendations
def get_recommendations(restaurant_name, df, model, feature_matrix):
    closest_match = get_closest_match(restaurant_name, df)
    
    if closest_match is None:
        return None, f"⚠️ No restaurant found with the name '{restaurant_name}'!"

    idx = df[df['Restaurant Name'] == closest_match].index[0]
    distances, indices = model.kneighbors([feature_matrix[idx]])

    recommended_restaurants = df.iloc[indices[0][1:]]
    return recommended_restaurants[['Restaurant Name', 'Aggregate rating', 'Cuisines']], None

# Streamlit UI
st.title("🍽️ Restaurant Recommendation System")
st.subheader("🔍 Find the best restaurants based on your preferences!")

# ✅ Use selectbox instead of text input
restaurant_options = sorted(df['Restaurant Name'].unique())
selected_restaurant = st.selectbox("Select a Restaurant", restaurant_options)

if st.button("Get Recommendations"):
    if selected_restaurant:
        recommendations, error = get_recommendations(selected_restaurant.lower(), df, knn_model, feature_matrix)
        if error:
           st.warning(error)
        else:
           st.success(f"✅ Restaurants similar to '{selected_restaurant.title()}':")
    
    # Improve table styling with Streamlit columns
    for _, row in recommendations.iterrows():
        with st.expander(f"🍽️ {row['Restaurant Name']}"):
            st.write(f"**⭐ Rating:** {row['Aggregate rating']} / 5.0")
            st.write(f"🍜 **Cuisines:** {row['Cuisines']}")
            st.write("---")

    else:
        st.error("Please select a restaurant!")

# Footer
st.markdown("---")
st.markdown("🔗 Created by *Aniket*  | AI-Powered by Machine Learning")
st.markdown(
    """
    <div style="text-align: center; color: white; background-color: #FF4B4B; padding: 10px; border-radius: 10px;">
        <h4>🍕 Built with ❤️ by Aniket | AI-Powered Restaurant Recommendations 🍽️</h4>
    </div>
    """,
    unsafe_allow_html=True
)
