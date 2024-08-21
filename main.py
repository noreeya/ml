import streamlit as st
import seaborn as sns
df = sns.load_dataset('iris')
df
st.sidebar.title('Classifier')
classifier = st.sidebar.selectbox('Classifier', ('KNN', 'SVM', 'DT', 'RF', 'NN'))
