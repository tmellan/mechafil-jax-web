import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)

st.write("# 👋 Welcome to Filecoin's CryptoEconomics Explorer!")

st.sidebar.success("Select a Page above.")

st.markdown(
    """
    ### Introduction
    This web-app implements a digital twin of the Filecoin Economy. It can be used to forecast all the components underlying Filecoin's circulating supply (i.e., minting, vesting, locking, and burning), based on a set of parameters that encode storage provider behavior.
    The model is best suited to test a hypothesis about how a change in storage provider behavior will impact the main drivers of circulating supply. It can also be used to test changes in certain economic parameters of Filecoin.
    To learn more about the model assumptions and design, you can refer to:
     1. Our [GitHub repository](https://github.com/protocol/mechafil-jax).
     2. Our paper on [Agent Based Modeling of the Filecoin Economy](https://arxiv.org/pdf/2307.15200.pdf), published at Chainscience 2023. Section 3 details the modeling of the digital twin.
    
    ### How to use this app
    
    **👈 Select "Supply Exploration" from the sidebar** to get started. 
    
    In that page, you will see three slider bars allow you to configure the storage provider behavior that you want to test. You can change these parameters to see how they impact the main drivers of circulating supply.
    The three parameters are:
        - RB Onboarding Rate - This is the amount of raw-byte power that is onboarded every day onto the network.
        - Renewal Rate - This is the percentage of sectors which are expiring that are renewed.
        - FIL+ Rate - This is the percentage of onboarded data that is FIL+.
    
    Once these values are configured, click the "Forecast" button. The digital-twin runs in the background, taking into account both historical data pulled directly from the Filecoin blockchain and the mechanistic laws defining the various aspects of Filecoin's circulating supply to forecast 
    these statistics for the next 365 days. The results are displayed in the form of a graph, which you can download as a PNG file by clicking the "Download" button.

    ### Want to learn more?

    - Check out [CryptoEconLab](https://cryptoeconlab.io)

    - Engage with us on [X](https://x.com/cryptoeconlab)
"""
)