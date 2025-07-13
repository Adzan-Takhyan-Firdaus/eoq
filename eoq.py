import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# 🟢 Konfigurasi Halaman
st.set_page_config(
    page_title="Kalkulator EOQ Jedag Jedug",
    layout="centered",
    initial_sidebar_state="auto"
)

# 🟢 HEADER Custom
st.markdown(
    """
    <h1 style='text-align: center; color: #336699;'>📦 Kalkulator EOQ Jedag Jedug</h1>
    <p style='text-align: center; font-size:18px;'>Optimalkan jumlah pesanan dan minimalkan biaya persediaan dengan visual interaktif</p>
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

        # 🟢 Hasil Perhitungan
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

        # 🟢 Grafik Total Cost vs Q
        st.subheader("📈 Grafik Total Biaya vs Kuantitas Pesanan")
        Q_range = np.linspace(1, EOQ * 2, 200)
        TC_range = (D / Q_range) * S + (Q_range / 2) * H

        plt.style.use("seaborn-v0_8")
        fig, ax = plt.subplots(figsize=(9,6))
        ax.plot(Q_range, TC_range, color="#1f77b4", linewidth=2, label="Total Biaya Persediaan")
        ax.axvline(EOQ, color="red", linestyle="--", linewidth=2, label=f"EOQ = {EOQ:.2f}")
        ax.scatter([EOQ], [TC], color="red", s=50)
        ax.set_xlabel("Kuantitas Pesanan (Q)")
        ax.set_ylabel("Total Biaya Persediaan")
        ax.set_title("Grafik Total Biaya Persediaan terhadap Kuantitas Pesanan")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.7)
        st.pyplot(fig)

        st.markdown("---")

        # 🟢 Info Footer
        st.info("Aplikasi ini dibuat dengan ❤️ menggunakan Python dan Streamlit.\n\n© 2025 EOQ Jedag Jedug Project.")
    else:
        st.error("Semua input harus lebih dari 0.")
else:
    st.info("Masukkan data kemudian klik **Hitung EOQ** untuk memulai.")
