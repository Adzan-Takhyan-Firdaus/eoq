import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="Simulasi Antrian M/M/1", layout="centered")

st.title("📈 Simulasi Antrian M/M/1")

st.write("""
Aplikasi ini menghitung parameter sistem antrian dengan model M/M/1 serta menampilkan grafik dan simulasi animasi.
""")

# Input
lambd = st.number_input("λ (arrival rate)", min_value=0.0, format="%.2f")
mu = st.number_input("μ (service rate)", min_value=0.0, format="%.2f")

if lambd > 0 and mu > 0:
    if lambd >= mu:
        st.error("λ harus lebih kecil dari μ agar sistem stabil.")
    else:
        # Perhitungan parameter
        rho = lambd / mu
        L = rho / (1 - rho)
        Lq = rho**2 / (1 - rho)
        W = 1 / (mu - lambd)
        Wq = rho / (mu - lambd)

        st.subheader("📊 Hasil Perhitungan:")
        st.write(f"**Utilisasi (ρ):** {rho:.4f}")
        st.write(f"**Rata-rata pelanggan di sistem (L):** {L:.4f}")
        st.write(f"**Rata-rata pelanggan di antrian (Lq):** {Lq:.4f}")
        st.write(f"**Rata-rata waktu dalam sistem (W):** {W:.4f}")
        st.write(f"**Rata-rata waktu dalam antrian (Wq):** {Wq:.4f}")

        # 🕒 SIMULASI ANIMASI PELANGGAN (DITAMPILKAN SEBELUM GRAFIK)
        st.subheader("🕒 Simulasi Animasi Kedatangan Pelanggan:")

        total_customers = 5
        queue_slots = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
        status_text = st.empty()
        queue_display = st.empty()

        for i in range(total_customers):
            # Update slot
            queue_slots[i] = "[👤]"
            queue_display.text("Antrian: " + " ".join(queue_slots))
            status_text.text(f"Pelanggan {i+1} sedang dilayani...")
            time.sleep(1)

            # Kosongkan slot setelah dilayani
            queue_slots[i] = "[✔️]"
            queue_display.text("Antrian: " + " ".join(queue_slots))
            time.sleep(0.5)

        status_text.text("✅ Semua pelanggan telah dilayani.")

        # 📊 GRAFIK BATANG PARAMETER
        st.subheader("📊 Grafik Parameter:")
        fig, ax = plt.subplots()
        param_names = ["Utilisasi (ρ)", "L", "Lq"]
        param_values = [rho, L, Lq]
        ax.bar(param_names, param_values, color=["skyblue", "lightgreen", "salmon"])
        ax.set_ylabel("Nilai")
        st.pyplot(fig)

        # 📈 GRAFIK UTILISASI TERHADAP λ
        st.subheader("📈 Grafik Utilisasi vs Arrival Rate:")
        lambd_range = np.linspace(0, mu*0.99, 100)
        rho_range = lambd_range / mu
        fig2, ax2 = plt.subplots()
        ax2.plot(lambd_range, rho_range, color="purple")
        ax2.set_xlabel("λ (arrival rate)")
        ax2.set_ylabel("Utilisasi (ρ)")
        ax2.set_title("Utilisasi terhadap λ")
        st.pyplot(fig2)
else:
    st.info("Masukkan λ dan μ > 0 untuk memulai perhitungan.")
