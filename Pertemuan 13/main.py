import streamlit as st

# Inisialisasi daftar tugas
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Fungsi untuk menambahkan tugas
def add_task():
    if st.session_state.new_task:
        st.session_state.tasks.append(st.session_state.new_task)
        st.session_state.new_task = ""  # Reset input field

# Fungsi untuk menghapus tugas
def delete_task(index):
    st.session_state.tasks.pop(index)

# Halaman Navigasi
menu = ["Home", "Task", "About"]
choice = st.sidebar.selectbox("Navigasi", menu)

# Halaman Home
if choice == "Home":
    st.title("🏠 Selamat Datang di Aplikasi To-Do List")
    st.write("""
        Aplikasi To-Do List membantu Anda mengatur tugas harian dengan mudah.
        Pilih menu **Task** untuk mulai menambahkan tugas Anda.
    """)
    st.image(
        "https://source.unsplash.com/800x400/?productivity,work", 
        caption="Tingkatkan produktivitas Anda!",
        use_column_width=True,
    )

# Halaman Task
elif choice == "Task":
    st.title("📝 Task Management")

    # Input untuk menambahkan tugas baru
    st.text_input(
        "Tambah tugas baru:",
        key="new_task",
        on_change=add_task,
        placeholder="Masukkan tugas Anda"
    )

    # Daftar tugas
    st.subheader("Daftar Tugas Anda")
    if st.session_state.tasks:
        for index, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(f"- {task}")
            with col2:
                if st.button("Hapus", key=f"delete_{index}"):
                    delete_task(index)
    else:
        st.write("✅ Tidak ada tugas saat ini!")

# Halaman About
elif choice == "About":
    st.title("ℹ️ Tentang Aplikasi")
    st.write("""
        **To-Do List App** dibuat menggunakan Streamlit untuk membantu Anda
        mengatur dan mengelola tugas harian dengan mudah dan efisien.

        ### Fitur
        - Tambahkan tugas baru
        - Lihat daftar tugas
        - Hapus tugas yang telah selesai

        ### Teknologi
        - Python
        - Streamlit

        Dikembangkan dengan ❤️ oleh [Wahyu Ahmad Yassin](https://github.com).
    """)
    st.image(
        "https://source.unsplash.com/800x400/?coding,developer",
        caption="Selalu ada waktu untuk belajar dan produktivitas.",
        use_column_width=True,
    )
