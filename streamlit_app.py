import streamlit as st
import sympy as sp
import pandas as pd

st.set_page_config(page_title="Metode Bisection - SPNL", layout="centered")

st.title("🔢 Aplikasi Web SPNL")
st.subheader("Metode Bisection")

st.write("Mencari akar persamaan non-linear menggunakan metode **Bisection**")

# Input persamaan
fungsi_input = st.text_input("Masukkan fungsi f(x):", "x**3 - x - 2")

# Input interval dan toleransi
a = st.number_input("Nilai a", value=1.0)
b = st.number_input("Nilai b", value=2.0)
toleransi = st.number_input("Toleransi Error", value=0.0001, format="%.5f")
maks_iterasi = st.number_input("Maksimum Iterasi", value=50, step=1)

if st.button("Hitung Akar"):
    x = sp.symbols('x')
    try:
        fungsi = sp.sympify(fungsi_input)
        f = sp.lambdify(x, fungsi)

        if f(a) * f(b) >= 0:
            st.error("❌ Syarat tidak terpenuhi: f(a) × f(b) harus < 0")
        else:
            data = []
            iterasi = 0
            error = abs(b - a)

            while error > toleransi and iterasi < maks_iterasi:
                c = (a + b) / 2
                fa = f(a)
                fb = f(b)
                fc = f(c)

                data.append([iterasi+1, a, b, c, fc, error])

                if fa * fc < 0:
                    b = c
                else:
                    a = c

                error = abs(b - a)
                iterasi += 1

            df = pd.DataFrame(data, columns=[
                "Iterasi", "a", "b", "c (Akar)", "f(c)", "Error"
            ])

            st.success(f"✅ Akar persamaan ≈ {c}")
            st.dataframe(df)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
