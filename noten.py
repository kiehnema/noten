import streamlit as st
import pandas as pd

st.set_page_config(page_title="Notenapp", page_icon="📊")

st.title("📊 Notenapp für Schüler")

# Session State initialisieren
if "noten" not in st.session_state:
    st.session_state.noten = pd.DataFrame(columns=["Fach", "Note"])

st.subheader("➕ Note eingeben")

fach = st.text_input("Fach")
note = st.number_input(
    "Note (0–15 Punkte)",
    min_value=0.0,
    max_value=15.0,
    step=0.5
)

if st.button("Hinzufügen"):
    if fach.strip() == "":
        st.warning("Bitte ein Fach eingeben.")
    else:
        neue_zeile = pd.DataFrame(
            [{"Fach": fach, "Note": note}]
        )
        st.session_state.noten = pd.concat(
            [st.session_state.noten, neue_zeile],
            ignore_index=True
        )
        st.success("Note gespeichert ✅")

st.divider()

st.subheader("📋 Übersicht der Noten")

if st.session_state.noten.empty:
    st.info("Noch keine Noten eingegeben.")
else:
    st.dataframe(st.session_state.noten, use_container_width=True)

    durchschnitt = st.session_state.noten["Note"].mean()

    st.metric(
        label="📈 Durchschnitt",
        value=round(durchschnitt, 2)
    )

    if st.button("🗑️ Alle Noten löschen"):
        st.session_state.noten = st.session_state.noten.iloc[0:0]
        st.experimental_rerun()
