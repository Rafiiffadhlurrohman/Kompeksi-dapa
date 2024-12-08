import os
import streamlit as st

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = file.read().splitlines()
    else:
        data = []
    return data

def save_data(data, filename):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def add_stock(data, name, size, quantity):
    for i, entry in enumerate(data):
        e_name, e_size, e_quantity = entry.split(',')
        if e_name == name and e_size == size:
            new_quantity = int(e_quantity) + quantity
            data[i] = f"{name},{size},{new_quantity}"
            return data
    data.append(f"{name},{size},{quantity}")
    return data

def subtract_stock(data, name, size, quantity):
    for i, entry in enumerate(data):
        e_name, e_size, e_quantity = entry.split(',')
        if e_name == name and e_size == size:
            new_quantity = int(e_quantity) - quantity
            if new_quantity < 0:
                st.error("Stok tidak mencukupi!")
                return data
            data[i] = f"{name},{size},{new_quantity}"
            return data
    st.error("Produk tidak ditemukan!")
    return data

# Streamlit app
def main():
    st.title(":rainbow[KONVEKSI DAVA]")

    filename = 'data_stok_kompeksi.txt'
    data = load_data(filename)

    menu = ["Tambah Stok", "Kurangi Stok", "Lihat Stok"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Tambah Stok":
        st.subheader("Tambah Stok")
        name = st.text_input("Nama Produk")
        size = st.selectbox("Ukuran", ["S", "M", "L", "XL", "XXL"])
        quantity = st.number_input("Jumlah", min_value=0, step=1)
        if st.button("Tambah"):
            if name and size and quantity > 0:
                data = add_stock(data, name, size, int(quantity))
                save_data(data, filename)
                st.success("Stok berhasil ditambahkan!")
            else:
                st.error("Silakan masukkan semua data dengan benar!")

    elif choice == "Kurangi Stok":
        st.subheader("Kurangi Stok")
        name = st.text_input("Nama Produk")
        size = st.selectbox("Ukuran", ["S", "M", "L", "XL", "XXL"])
        quantity = st.number_input("Jumlah", min_value=0, step=1)
        if st.button("Kurangi"):
            if name and size and quantity > 0:
                data = subtract_stock(data, name, size, int(quantity))
                save_data(data, filename)
                st.success("Stok berhasil dikurangi!")
            else:
                st.error("Silakan masukkan semua data dengan benar!")

    elif choice == "Lihat Stok":
        st.subheader("Data Stok")
        for entry in data:
            st.text(entry)

if __name__ == "__main__":
    main()
