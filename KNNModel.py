import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
# Load the dataset

import tkinter as tk
global user_input
user_input = pd.DataFrame({
    
    'RAM Gb': [6],
    'ROM Gb': [128],
    'Battery Mah': [6000],
    'Brand' : 'Samsung'
})

abcd = {}

def submit():
    brand = brand_entry.get()
    ram = int(ram_entry.get())
    rom = int(rom_entry.get())
    battery = int(battery_entry.get())
    global abcd
    mobile_data = {
        
        'RAM': ram,
        'ROM': rom,
        'Battery': battery,
        'Brand': brand
    }
    abcd = mobile_data
    

root = tk.Tk()
root.title('Mobile Data Input')

brand_label = tk.Label(root, text='Brand:')
brand_label.pack()
brand_entry = tk.Entry(root)
brand_entry.pack()

ram_label = tk.Label(root, text='RAM:')
ram_label.pack()
ram_entry = tk.Entry(root)
ram_entry.pack()

rom_label = tk.Label(root, text='ROM:')
rom_label.pack()
rom_entry = tk.Entry(root)
rom_entry.pack()

battery_label = tk.Label(root, text='Battery (mAh):')
battery_label.pack()
battery_entry = tk.Entry(root)
battery_entry.pack()

submit_button = tk.Button(root, text='Submit', command=submit)
submit_button.pack()

root.mainloop()

#user_input = pd.DataFrame(abcd)
print(abcd)
df = pd.read_csv(r"C:\Users\Praveen\Desktop\ASSIGNMENTSEM-III\DS\pro\mainDataset.csv",encoding = "ISO-8859-1")
label_encoder = LabelEncoder()
# Select relevant features for recommendation
features = ['Name', 'RAM Gb', 'ROM Gb', 'Battery Mah']

# Preprocess the dataset
df_processed = df[features]

# Extract the brand from the 'Name' feature
df_processed['Brand'] = df_processed['Name'].str.split().str[0]

df_processed['Brand_encoded'] = label_encoder.fit_transform(df_processed['Brand'])

# Fill missing values
df_processed.fillna(0, inplace=True)

# Standardize the numerical features
scaler = StandardScaler()
df_processed[['RAM Gb', 'ROM Gb', 'Battery Mah']] = scaler.fit_transform(df_processed[['RAM Gb', 'ROM Gb', 'Battery Mah']])

# User input
user_input = pd.DataFrame({
    
    'RAM Gb': [6],
    'ROM Gb': [128],
    'Battery Mah': [6000],
    'Brand' : 'Samsung'
})


# Extract the brand from the user input


df_processed = df_processed.drop('Name', axis=1)
df_processed = df_processed.drop('Brand', axis=1)


# Standardize the user input
user_input[['RAM Gb', 'ROM Gb', 'Battery Mah']] = scaler.transform(user_input[['RAM Gb', 'ROM Gb', 'Battery Mah']])
user_input[['Brand_encoded']] = label_encoder.fit_transform(user_input[['Brand']])
user_input = user_input.drop('Brand', axis=1)
# Create NearestNeighbors model
k = 10  # Number of similar items to recommend

knn_model = NearestNeighbors(n_neighbors=k, metric='euclidean')

knn_model.fit(df_processed)

# Find the k nearest neighbors


distances, indices = knn_model.kneighbors(user_input)

# Display the recommended mobiles
print('Recommended Mobiles:')
for index in indices[0]:
    print(df.loc[index, 'Name'], df.loc[index, 'RAM Gb'], df.loc[index, 'ROM Gb'], df.loc[index, 'Battery Mah'])
