# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:09:26 2020

@author: kvija
"""

import streamlit as st
import requests

def main():
    st.title('Sentence Length Frequency')
    #user inputs
    textlink = st.sidebar.text_input("Text Link")
    button_was_clicked = st.sidebar.button("Submit")
    if button_was_clicked:
        st.write("For text link: " + textlink)
        #Run Sentence Frequency cloud function 
        freq_link = "https://us-central1-vijaysai.cloudfunctions.net/sent_freq?link="+textlink
        freq_dist = requests.get(freq_link)
        
        #Run Plot Histogram cloud function 
        plot_funclink = "https://us-central1-vijaysai.cloudfunctions.net/plot_hist?data="+freq_dist.text+"&link="+textlink
        plot_link = requests.get(plot_funclink)
        
        #Display Frequency Output
        st.write("Frequency distribution of sentence lengths: (Format - {Sentence length: Number of occurrences})")
        st.write(freq_dist.text)
        
        #Display histogram image
        st.image(plot_link.text,width=650)
        
if __name__ == '__main__':
    main()