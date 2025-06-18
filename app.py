import streamlit as st
from PIL import Image


#https://social-caption-uroyf7rnzwv2rcbasyld5n.streamlit.app/

from model.caption_generator import generate_caption
from utils.rewrite import rewrite_caption


st.set_page_config(
    page_title="Social Status Caption AI",
    layout="centered",
    page_icon="📸"
)

st.title("📸 Social Status Caption AI")
st.caption("Generate personalized captions for whatsapp instagram and twitter")

platform=st.selectbox("Select Platform", ["Instagram", "Twitter","WhatsApp"])
style=st.selectbox("Select Caption Style", ["Funny", "Romantic", "Deep", "Savage"])

uploaded_file=st.file_uploader("Upload The Image", type=["jpg","jpeg","png"])

if uploaded_file:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Thinking...."):
            try:
                base_caption=generate_caption(image)
                final_caption=rewrite_caption(base_caption,platform,style)

                st.subheader("Your Caption")
                st.code(final_caption, language="markdown")

            except Exception as e:
                st.error(f"Something wrong happened: {e}")
else:
    st.info(" Upload an image to get started ")