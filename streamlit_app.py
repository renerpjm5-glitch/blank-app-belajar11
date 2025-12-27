import streamlit as st
import sympy as sp
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="SPNL - Metode Bisection",
    layout="centered"
)

st.title("🔢 Aplikasi Web SPNL")
st.subheader("Metode Bisection")
st.write("Mencari akar persamaan non-linear menggunakan **Metode Bisection**")

# ================= INPUT =================
fungsi_input = st.text_input(
    "Masukkan fungsi f(x):",
    value="x**3 - x - 2"
)

a = st.number_input("Nilai batas bawah (a)", value=1.0)
b = st.number_input("Nilai batas atas (b)", value=2.0)
toleransi = st.number_input(
    "Toleransi Error",
    value=0.0001,
    format="%.6f"
)
maks_iterasi = st.number_input(
    "Maksimum Iterasi",
    value=50,
    step=1
)

# ================= PROSES =================
if st.button("🔍 Hitung Akar"):
    x = sp.symbols('x')

    try:
        # Konversi fungsi input ke fungsi Python
        fungsi = sp.sympify(fungsi_input)
        f = sp.lambdify(x, fungsi, "math")

        fa = f(a)
        fb = f(b)

        # Validasi syarat bisection
        if fa * fb >= 0:
            st.error("❌ Syarat tidak terpenuhi: f(a) × f(b) harus < 0")
        else:
            data = []
            iterasi = 1
            error = abs(b - a)
            c = 0

            while error > toleransi and iterasi <= maks_iterasi:
                c = (a + b) / 2
                fc = f(c)

                data.append([
                    iterasi,
                    round(a, 6),
                    round(b, 6),
                    round
