import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.stoggle import stoggle
from streamlit_extras.metric_cards import style_metric_cards
import time
import random
import game_scenes
import game_def

# additional components from https://extras.streamlit.app/

# -------------- app config ---------------

st.set_page_config(page_title="Harcke's Quest Journey", page_icon="⚔")
game_def.autoplay_audio('audio/medival1.mp3')


# define external css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


###############################################
#
#
#           VARIABLES DEFINITION
#
#
################################################

# variable responsible for checking if player provided his name and game can be started
start = False

# set session states
# this is streamlit specific. For more contex please check streamlit documenation

if "health" not in st.session_state:
    st.session_state["health"] = 100
if "mana" not in st.session_state:
    st.session_state["mana"] = 80
if "gold" not in st.session_state:
    st.session_state["gold"] = 5
if "place" not in st.session_state:
    st.session_state["place"] = "introScene"
if "sheep_anger" not in st.session_state:
    st.session_state["sheep_anger"] = 0
if "sword" not in st.session_state:
    st.session_state["sword"] = 0
if "dragon_alive" not in st.session_state:
    st.session_state["dragon_alive"] = 1
if "dragon_hp" not in st.session_state:
    st.session_state["dragon_hp"] = 20
if "temp" not in st.session_state:
    st.session_state["temp"] = ""
if "counter" not in st.session_state:
    st.session_state["counter"] = 0
if "scenes_counter" not in st.session_state:
    st.session_state["scenes_counter"] = {
        "intro_counter": 0,
        "cave_counter": 0,
        "trip_counter": 0,
        "elf_counter": 0,
    }


###############################################
#
#
#               GAME ENGINE
#
#
################################################

# ---------------- CSS ----------------

local_css("style.css")

# ----------------- game start --------


welcome = st.empty()
welcome.title("Welcome to Hacker Quest, Adventure!")


# hero base statistics

player_name_container = st.empty()
player_name_container.text_input(
    "Masukkan nama dan tekan enter untuk memulai petualangan", key="player_name"
)

main_text_container = st.empty()
# main_text_container.caption("Create your own adventure visit [GitHub](https://github.com/TomJohnH/streamlit-dungeon)")


# if st.button("Start"):
#     if st.session_state.player_name != "":
#         player_name_container.empty()
#         main_text_container.empty
#         start = True
#         while start is True:
#             with st.spinner('Wait for it...'):
#                 time.sleep(5)
#                 st.success('Done!')
if st.session_state.player_name != "":
    player_name_container.empty()

    main_text_container.empty()
    
    # progress_text = "Operation in progress. Please wait."
    # my_bar = st.progress(0, text=progress_text)

    # for percent_complete in range(100):
    #     time.sleep(0.01)
    #     my_bar.progress(percent_complete + 1, text=progress_text)
    # time.sleep(1)
    # my_bar.empty()
    start = True

# START THE GAME

if start:
    game_def.autoplay_audio('audio/sword.mp3')
    # delete welcome
    welcome.empty()

    if st.session_state.place == "introScene":
        time.sleep(1.5)
        game_scenes.introScene()
    elif st.session_state.place == "sheepScene":
        game_scenes.sheepScene()
    elif st.session_state.place == "southpathScene":
        game_scenes.southpathScene()
    elif st.session_state.place == "elfScene":
        game_scenes.elfScene()
    elif st.session_state.place == "caveScene":
        game_scenes.caveScene()
    elif st.session_state.place == "poScene":
        game_scenes.poScene()
    elif st.session_state.place == "dragonScene":
        game_scenes.dragonScene()
    elif st.session_state.place == "libraryScene":
        game_scenes.libraryScene()

    # player stats

    # col1 = st.columns(1)
    # # col1, col2, col3 = st.columns(3)
    # col1.metric(label="Health", value=st.session_state.health, delta=0)
    # # col2.metric(label="Mana", value=st.session_state.mana, delta=0)
    # # col3.metric(label="Gold", value=st.session_state.gold, delta=0)
    # style_metric_cards(
    #     background_color="#black", border_color="#21212f", border_left_color="#21212f"
    # )

    # if st.session_state["sword"] == 1:
    #     st.write("🗡️ sword equipped")

# this part of the code focuses input on text window
# please note that counter is required - for streamlit specific it does not work without it

components.html(
    f"""
        <div>some hidden container</div>
        <p>{st.session_state.counter}</p>
        <script>
            var input = window.parent.document.querySelectorAll("input[type=text]");
            for (var i = 0; i < input.length; ++i) {{
                input[i].focus();
            }}
    </script>
    """,
    height=0,
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# MainMenu {visibility: hidden;}

# ------------ footer  ---------------------------

# st.markdown(
#     f"""
#     <div class="bpad" id="bpad">
#     <a href="https://cehuda.id" style="color: grey; text-decoration:none;">
#     <div class="coffee_btn" >
#     <img src="https://raw.githubusercontent.com/tailwindlabs/blog.tailwindcss.com/master/public/mstile-70x70.png" style="max-width:20px;margin-right:10px;">
#     Visit Our Web</a></div></div>""",
#     unsafe_allow_html=True,
# )
