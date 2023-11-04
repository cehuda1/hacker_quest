import streamlit as st
import base64

###############################################
#
#
#               FUNCTIONS DEFINITION
#
#
################################################

# this little function helps us to clear text input by storing variable in temp
# counter +1 is a part of a neat trick to introduce focus on text field (explained further in the code)
def clear(ss_variable):
    st.session_state["temp"] = st.session_state[ss_variable]
    st.session_state[ss_variable] = ""
    st.session_state["counter"] += 1


# before changing scene you have to clear out the temp
def temp_clear():
    st.session_state["temp"] = ""


# function restarting session state
# in the future can be used for randomization


def restart_session():

    st.session_state["health"] = 100
    st.session_state["mana"] = 80
    st.session_state["gold"] = 5
    st.session_state["place"] = "introScene"
    st.session_state["sheep_anger"] = 0
    st.session_state["forest_trip"] = 0
    st.session_state["sword"] = 0
    st.session_state["dragon_alive"] = 1
    st.session_state["dragon_hp"] = 20
    st.session_state["scenes_counter"] = {
        "intro_counter": 0,
        "cave_counter": 0,
        "trip_counter": 0,
        "elf_counter": 0,
    }
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <style>
                .hidden-audio {{
                    display: none;
                }}
            </style>
            <audio class="hidden-audio" controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )