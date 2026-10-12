import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quan ly diem sinh vien", layout="wide")

st.title("QUAN LY DIEM SINH VIEN")
st.write("Website theo doi ket qua hoc tap.")

# 1. Tao du lieu
data = {
    "Ho_ten": ["An", "Binh", "Chi", "Dung", "Ha",
               "Nam", "Lan", "Minh", "Phuc", "Linh"],
    "Chuyen_can": [9, 8, 7, 10, 8, 9, 6, 7, 8, 9],
    "Giua_ky": [7, 8, 6, 9, 7, 8, 5, 8, 7, 9],
    "Cuoi_ky": [8, 9, 5, 9, 8, 7, 6, 9, 8, 10]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

# 3. Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Bang diem
st.subheader("Bang diem sinh vien")
st.dataframe(df, use_container_width=True)

# 5. Thong ke
st.subheader("Thong ke lop hoc")
st.metric("Diem trung binh", round(df["Tong_ket"].mean(), 2))
st.metric("So sinh vien dat",
          int((df["Tong_ket"] >= 5).sum()))

cao_nhat = df.loc[df["Tong_ket"].idxmax()]
thap_nhat = df.loc[df["Tong_ket"].idxmin()]

st.write("Sinh vien cao nhat:", cao_nhat["Ho_ten"],
         "-", round(cao_nhat["Tong_ket"], 2))
st.write("Sinh vien thap nhat:", thap_nhat["Ho_ten"],
         "-", round(thap_nhat["Tong_ket"], 2))

# 6. Tra cuu sinh vien
st.subheader("Tra cuu diem")
ten = st.selectbox("Chon sinh vien", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]
st.write("Diem chuyen can:", sv["Chuyen_can"])
st.write("Diem giua ky:", sv["Giua_ky"])
st.write("Diem cuoi ky:", sv["Cuoi_ky"])
st.write("Diem tong ket:", round(sv["Tong_ket"], 2))
st.write("Xep loai:", sv["Xep_loai"])

# 7. Bieu do
st.subheader("Bieu do diem tong ket")
st.bar_chart(df.set_index("Ho_ten")["Tong_ket"])

# 8. Thong tin sinh vien thuc hien
st.caption("Nguoi thuc hien: [Ho ten] | MSSV: [Ma sinh vien]")
