# import streamlit as st
import pandas as pd


data = pd.read_csv("./training_data.csv", delimeter=":")
print(data.head())