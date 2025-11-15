#Nova's Magical Pink Wishes

import openai
import streamlit as st
import random

#
openai.api_key = "sk-proj-Mwb8by8PKEEOL...."

prompts = [
    "un vœu ",
    "un souhait",
    "un vœu adorable.",
    "un message.",
]

st.title("Nova's Magical Pink Wishes 🌸✨")
st.markdown("Bienvenue dans l'univers magique de Nova, où chaque souhait devient réalité!")

user_wish = st.text_input("Quel est ton souhait aujourd'hui ? ✨", "")

def generate_wish(user_wish):
    prompt = random.choice(prompts)
    if user_wish:
        prompt += f" Mon souhait : {user_wish}"

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un générateur de vœux mignons et magiques."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Erreur lors de la génération du vœu : {e}")
        return None

if user_wish:
    wish = generate_wish(user_wish)
    if wish:
        st.write(f"✨ Voici ton vœu magique : {wish}")
else:
    st.markdown("Si tu ne sais pas quoi souhaiter, voici un souhait aléatoire pour toi ! 🌟")
    random_wish = generate_wish("")
    if random_wish:
        st.write(f"✨ {random_wish}")