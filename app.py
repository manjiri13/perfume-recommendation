import pickle
import streamlit as st
import requests


def recommend(perfume):
    index = perfumes[perfumes['Name'] == perfume].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_perfume_names = []
    recommended_perfume_posters = []
    recommended_perfume_desc = []
    recommended_perfume_note = []
    recommended_perfume_brand=[]
    recommended_perfume_price=[]
    for i in distances[1:6]:
        
        # perfume_id = perfumes.iloc[i[0]].index()
        recommended_perfume_posters.append(perfumes.iloc[i[0]].img)
        recommended_perfume_names.append(perfumes.iloc[i[0]].Name)
        recommended_perfume_desc.append(perfumes.iloc[i[0]].Description)
        recommended_perfume_note.append(perfumes.iloc[i[0]].Notes)
        recommended_perfume_brand.append(perfumes.iloc[i[0]].Brand)
        recommended_perfume_price.append(perfumes.iloc[i[0]].price)

    return recommended_perfume_names,recommended_perfume_posters,recommended_perfume_desc,recommended_perfume_note,recommended_perfume_brand,recommended_perfume_price


st.header('Perfume Recommender System')
perfumes = pickle.load(open('perfume-_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

perfume_list = perfumes['Name'].values
selected_per = st.selectbox(
    "Type or select a perfume from the dropdown",
    perfume_list
)

if st.button('Show Recommendation'):
    recommended_perfume_names,recommended_perfume_posters,recommended_perfume_desc,recommended_perfume_note,recommended_perfume_brand,recommended_perfume_price = recommend(selected_per)
    st.header('Recommended Perfumes:')
    
    
    for i in range(5):
        with st.container():
            st.subheader(recommended_perfume_names[i])
            st.markdown('**_Image_**')
            st.image(recommended_perfume_posters[i],width=150)
            st.write('**_Rs_**', recommended_perfume_price[i], '/-')
            st.write('Brand:', recommended_perfume_brand[i])
            with st.expander("More Info"):
                st.markdown('**_Description_**.')
                st.write(recommended_perfume_desc[i])
                st.markdown('**_Notes_**.')
                st.write(recommended_perfume_note[i])

