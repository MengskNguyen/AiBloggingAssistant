import streamlit as st

from Modules.generate_blog_module import create_generate_blog_chain
from Modules.generate_img_module import create_img_module
from Modules.translator_module import translator_module

# Streamlit State
if "disable" not in st.session_state:
    st.session_state.disable = True

# Front end layout
st.set_page_config(layout="wide")

st.title("Blogging Assistant: Your AI Writing Companion")
st.subheader("Craft perfect blogs with the help of AI powered by GPT-4o")

with st.sidebar:
    st.title("Input your blog details")
    st.subheader("Enter details of the blog you want to generate")

    blog_title = st.text_input("Blog Title")

    keywords = st.text_area("Keywords (comma-separated)")

    num_words = st.slider("Number of words", min_value=250, max_value=1000, step=250)

    generate_img = st.checkbox("Generate image bases on keywords")

    translate = st.checkbox("Translate to Vietnamese")

    if blog_title and keywords:
        st.session_state.disable = False
    else:
        st.session_state.disable = True

    generate_btn = st.button("Generate", disabled=st.session_state.disable)

    if generate_btn:
        print("Generating blog ...")
        generated_blog = create_generate_blog_chain({
            "title": blog_title,
            "words_count": num_words,
            "keywords": keywords
        })
        print("Finished generate blog ...")
        if "generated_blog" in st.session_state:
            del st.session_state.generated_blog
            st.session_state.generated_blog = generated_blog
        else:
            st.session_state.generated_blog = generated_blog

        if translate:
            print("Translating blog ...")
            translated_blog = translator_module({
                "content": st.session_state.generated_blog,
                "language": "Vietnamese"
            })
            print("Finished translate blog ...")
            if "translated_blog" in st.session_state:
                del st.session_state.translated_blog
                st.session_state.translated_blog = translated_blog
            else:
                st.session_state.translated_blog = translated_blog

    if generate_img:
        print("Generating image ...")
        img_url = create_img_module({
            "keywords": keywords
        })
        print("Finished generate image ...")
        if "image_url" in st.session_state:
            del st.session_state.image_url
            st.session_state.image_url = img_url
        else:
            st.session_state.image_url = img_url


if "image_url" in st.session_state:
    st.image(st.session_state.image_url)

if "generated_blog" in st.session_state:
    st.divider()
    st.write(st.session_state.generated_blog)

if "translated_blog" in st.session_state:
    st.divider()
    st.write(st.session_state.translated_blog)


