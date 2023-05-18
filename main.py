import views.zoo as zooView
import models.sistema as sistemaModel
import streamlit as st
if __name__ == '__main__':
    st.set_page_config(
        page_title="Zoológico RF",
        layout="wide"
    )

    sistema = sistemaModel.Sistema()
    zoo = zooView.Zoo()
    zoo.mostrarMenu(sistema)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
