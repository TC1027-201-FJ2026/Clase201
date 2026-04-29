import os
import pandas as pd


desktop_path = os.path.expanduser("C:/Users/gnisimura/Downloads")

df = pd.read_excel(desktop_path + "/vendedores-1.xlsx", sheet_name="gc_QRO.PM3000.5.1813.18212_full")

print(df)