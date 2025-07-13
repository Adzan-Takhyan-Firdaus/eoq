import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# 🌟 Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator EOQ Profesional",
    layout="centered"
)

# 🌟 Sidebar
st.sidebar.title("ℹ️ Tentang EOQ")

st.sidebar.markdown("""
**📘 Pengertian EOQ:**  
EOQ (*Economic Order Quantity*) adalah metode untuk menentukan jumlah pemesanan barang yang paling ekonomis sehingga biaya pemesanan dan biaya penyimpanan menjadi minimum.

**🎯 Fungsi EOQ:**  
✅ Menentukan kuantitas pemesanan optimal  
✅ Mengurangi biaya total persediaan  
✅ Meningkatkan efisiensi pengadaan barang  

**🛠️ Cara Menggunakan Aplikasi:**  
1️⃣ Masukkan *Permintaan Tahunan (D)*  
2️⃣ Masukkan *Biaya Pemesanan (S)*  
3️⃣ Masukkan *Biaya Penyimpanan (H)*  
4️⃣ Klik **Hitung EOQ**  
5️⃣ Lihat hasil, simulasi, dan grafik
""")

# 🌟 Header utama
st.markdown(
    """
    <h1 style='text-align: center; color: #2c3e50;'>📦 </h1>
    <p style='text-align: center; font-size:18px;'>Hitung kuantitas pemesanan optimal & visualisasi biaya persediaan</p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# 🌟 Input form
col1, col2, col3 = st.columns(3)
with col1:
    D = st.number_input("📈 Permintaan Tahunan (D)", min_value=1.0, format="%.2f")
with col2:
    S = st.number_input("💰 Biaya Pemesanan (S)", min_value=1.0, format="%.2f")
with col3:
    H = st.number_input("🏬 Biaya Penyimpanan per Unit (H)", min_value=1.0, format="%.2f")

# 🌟 Proses hitung EOQ
if st.button("🚀 Hitung EOQ"):
    EOQ = np.sqrt((2 * D * S) / H)
    N = D / EOQ
    ordering_cost = N * S
    holding_cost = (EOQ / 2) * H
    total_cost = ordering_cost + holding_cost

    # 🌟 Tampilkan hasil
    st.success("✅ Perhitungan Selesai!")
    st.markdown(f"""
    - 📦 **EOQ:** `{EOQ:.2f}` unit  
    - 🔁 **Jumlah Pesanan per Tahun:** `{N:.2f}` kali  
    - 💸 **Biaya Pemesanan Tahunan:** `Rp {ordering_cost:,.2f}`  
    - 💼 **Biaya Penyimpanan Tahunan:** `Rp {holding_cost:,.2f}`  
    - 🏷️ **Total Biaya Tahunan:** `Rp {total_cost:,.2f}`
    """)
    st.markdown("---")

    # 🌟 Simulasi animasi pemesanan
    st.subheader("🎬 Simulasi Proses Pemesanan")
    progress = st.progress(0)
    status = st.empty()
    steps = min(10, int(N))
    for i in range(steps):
        status.text(f"📦 Pemesanan ke-{i+1} sedang diproses...")
        time.sleep(0.3)
        progress.progress((i+1)/steps)
    status.text("✅ Semua pemesanan selesai diproses!")
    st.markdown("---")

    # 🌟 Grafik EOQ
    st.subheader("📈 Grafik EOQ")

    Q = np.linspace(5, EOQ * 2, 200)
    ordering_cost_curve = (D / Q) * S
    holding_cost_curve = (Q / 2) * H
    total_cost_curve = ordering_cost_curve + holding_cost_curve

    fig, ax = plt.subplots(figsize=(9,6))
    ax.plot(Q, ordering_cost_curve, label="Ordering Costs", color="dodgerblue", linewidth=2)
    ax.plot(Q, holding_cost_curve, label="Holding Costs", color="black", linewidth=2)
    ax.plot(Q, total_cost_curve, label="Total Cost", color="red", linewidth=2)

    ax.axvline(EOQ, color="gray", linestyle="--", linewidth=1)
    ax.scatter([EOQ], [total_cost], color="gold", edgecolor="black", s=100, zorder=5)

    ax.set_title("EOQ vs Komponen Biaya", fontsize=14, fontweight='bold')
    ax.set_xlabel("Re-Order Quantity (Q)")
    ax.set_ylabel("Annual Cost")
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.6)

    st.pyplot(fig)
    st.info("📌 Titik kuning menunjukkan EOQ optimal.")
else:
    st.info("Masukkan data di atas lalu klik **Hitung EOQ**.")

