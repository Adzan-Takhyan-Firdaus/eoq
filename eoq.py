import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# 🌟 Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator EOQ Profesional",
    layout="centered"
)

# 🌟 Header
st.markdown(
    """
    <h1 style='text-align: center; color: #2c3e50;'>📦 EOQ (Economic Order Quantity)</h1>
    <p style='text-align: center; font-size:18px;'>Visualisasi Grafik Profesional: Ordering Cost, Holding Cost, dan Total Cost</p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# 🌟 Input Data
col1, col2, col3 = st.columns(3)

with col1:
    D = st.number_input("📈 Permintaan Tahunan (D)", min_value=1.0, format="%.2f")
with col2:
    S = st.number_input("💰 Biaya Pemesanan (S)", min_value=1.0, format="%.2f")
with col3:
    H = st.number_input("🏬 Biaya Penyimpanan per Unit (H)", min_value=1.0, format="%.2f")

if st.button("🚀 Hitung EOQ"):
    EOQ = np.sqrt((2 * D * S) / H)
    N = D / EOQ
    TC = (D / EOQ) * S + (EOQ / 2) * H

    st.success("✅ Perhitungan Selesai!")
    st.markdown(f"""
    - 📦 **EOQ:** `{EOQ:.2f}` unit  
    - 🔁 **Jumlah Pesanan/Tahun:** `{N:.2f}` kali  
    - 💸 **Total Biaya:** `Rp {TC:,.2f}`
    """)
    st.markdown("---")

    # 🌟 Simulasi Animasi
    st.subheader("🎬 Simulasi Pemesanan")
    progress = st.progress(0)
    info = st.empty()
    steps = min(10, int(N))
    for i in range(steps):
        info.text(f"Pemesanan ke-{i+1} sedang diproses...")
        progress.progress((i+1)/steps)
        time.sleep(0.3)
    info.text("✅ Semua pemesanan diproses!")
    st.markdown("---")

    # 🌟 Grafik EOQ Profesional
    st.subheader("📈 Grafik EOQ Profesional")

    Q = np.linspace(1, EOQ * 2, 200)
    ordering_cost = (D / Q) * S
    holding_cost = (Q / 2) * H
    total_cost = ordering_cost + holding_cost

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(Q, ordering_cost, color="dodgerblue", linewidth=2, label="Ordering Costs")
    ax.plot(Q, holding_cost, color="black", linewidth=2, label="Holding Costs")
    ax.plot(Q, total_cost, color="red", linewidth=2, label="Total Cost")

    # EOQ vertical line & point
    ax.axvline(EOQ, color="gray", linestyle="--", linewidth=1)
    ax.scatter([EOQ], [TC], color="gold", edgecolor="black", s=100, zorder=5)

    # Labeling
    ax.set_title("EOQ vs Cost Components", fontsize=14, fontweight='bold')
    ax.set_xlabel("Re-Order Quantity (Q)")
    ax.set_ylabel("Annual Cost")
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.5)

    st.pyplot(fig)
    st.info("📌 EOQ optimal dicapai saat Total Cost minimum (titik kuning).")
else:
    st.info("Masukkan nilai D, S, dan H lalu klik 'Hitung EOQ'.")

