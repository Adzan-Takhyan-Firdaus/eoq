import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# 🟢 Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator EOQ Lengkap",
    layout="centered",
    initial_sidebar_state="auto"
)

# 🟢 HEADER
st.markdown(
    """
    <h1 style='text-align: center; color: #336699;'>📦 Kalkulator EOQ Lengkap</h1>
    <p style='text-align: center; font-size:18px;'>Hitung jumlah pemesanan optimal dan visualisasi biaya persediaan</p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# 🟢 Input Data dalam Kolom
col1, col2, col3 = st.columns(3)

with col1:
    D = st.number_input("📈 Permintaan Tahunan (D)", min_value=0.0, format="%.2f")
with col2:
    S = st.number_input("💰 Biaya Pemesanan per Pesanan (S)", min_value=0.0, format="%.2f")
with col3:
    H = st.number_input("🏬 Biaya Penyimpanan per Unit per Tahun (H)", min_value=0.0, format="%.2f")

# 🟢 Tombol Hitung
if st.button("🚀 Hitung EOQ"):
    if D > 0 and S > 0 and H > 0:
        # 🧮 Hitung EOQ
        EOQ = np.sqrt((2 * D * S) / H)
        N = D / EOQ
        TC = (D / EOQ) * S + (EOQ / 2) * H

        # 🟢 Hasil
        st.success("✅ **Hasil Perhitungan Selesai!**")
        st.markdown(
            f"""
            - 📦 **EOQ:** `{EOQ:.2f}` unit
            - 🔄 **Jumlah Pesanan per Tahun:** `{N:.2f}` kali
            - 💸 **Total Biaya Persediaan:** `Rp {TC:,.2f}`
            """
        )

        st.markdown("---")

        # 🟢 Simulasi Animasi Pemesanan
        st.subheader("🎬 Simulasi Animasi Pemesanan:")
        total_steps = int(N) if N < 10 else 10
        progress = st.progress(0)
        status_text = st.empty()
        for i in range(total_steps):
            status_text.text(f"📦 Pemesanan ke-{i+1} sedang diproses...")
            time.sleep(0.5)
            progress.progress((i+1) / total_steps)
        status_text.text("✅ Semua pemesanan selesai diproses!")

        st.markdown("---")

        # 🟢 Grafik EOQ Lengkap
        st.subheader("📈 Grafik Ordering Cost, Holding Cost, dan Total Cost")

        Q_range = np.linspace(1, EOQ * 2, 200)
        Ordering_Cost = (D / Q_range) * S
        Holding_Cost = (Q_range / 2) * H
        Total_Cost = Ordering_Cost + Holding_Cost

        plt.style.use("seaborn-v0_8")
        fig, ax = plt.subplots(figsize=(9,6))

        # Garis Ordering Cost
        ax.plot(Q_range, Ordering_Cost, label="Ordering Cost", color="blue", linewidth=2)
        # Garis Holding Cost
        ax.plot(Q_range, Holding_Cost, label="Holding Cost", color="black", linewidth=2)
        # Garis Total Cost
        ax.plot(Q_range, Total_Cost, label="Total Cost", color="red", linewidth=2)

        # Garis vertikal EOQ
        ax.axvline(EOQ, color="gray", linestyle="--", linewidth=1)
        # Titik EOQ
        ax.scatter([EOQ], [TC], color="green", s=80, zorder=5)

        # Label
        ax.set_xlabel("Re-Order Quantity (Q)")
        ax.set_ylabel("Annual Cost")
        ax.set_title("EOQ Components: Ordering, Holding, and Total Cost")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.7)

        st.pyplot(fig)

        st.markdown("---")
        st.info("Aplikasi ini dibuat dengan ❤️ menggunakan Python dan Streamlit.\n\n© 2025 EOQ Project.")
    else:
        st.error("Semua input harus lebih dari 0.")
else:
    st.info("Masukkan data dan klik **Hitung EOQ** untuk memulai.")
