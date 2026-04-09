import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚀 My Portfolio")
page = st.sidebar.radio("Navigation", ["Home", "Projects", "Skills", "Contact"])

st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ using Streamlit")

# ---------------- HOME ----------------
if page == "Home":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("👋 Hi, I'm Ajay Nikam")
        st.subheader("Python Developer | Streamlit Expert")

        st.write("""
        I build interactive web applications using Python.
        Passionate about automation, data, and clean UI.
        """)

        st.download_button(
            label="📄 Download Resume",
            data="Your resume content here",
            file_name="resume.txt"
        )

    with col2:
        st.image("https://via.placeholder.com/250", caption="Your Photo")

    st.divider()

    st.subheader("🔥 Highlights")

    col1, col2, col3 = st.columns(3)

    col1.metric("Projects", "10+")
    col2.metric("Experience", "2 Years")
    col3.metric("Clients", "5+")


# ---------------- PROJECTS ----------------
elif page == "Projects":
    st.title("💼 My Projects")

    projects = [
        {
            "title": "Portfolio App",
            "desc": "Personal portfolio built with Streamlit",
            "link": "https://example.com"
        },
        {
            "title": "Data Dashboard",
            "desc": "Interactive dashboard using Python",
            "link": "https://example.com"
        }
    ]

    for project in projects:
        with st.container():
            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(project["title"])
                st.write(project["desc"])

            with col2:
                st.link_button("🔗 View", project["link"])

            st.divider()


# ---------------- SKILLS ----------------
elif page == "Skills":
    st.title("🧠 Skills")

    skills = {
        "Programming": ["Python", "SQL"],
        "Frameworks": ["Streamlit", "Flask"],
        "Tools": ["Git", "Docker"],
    }

    for category, items in skills.items():
        st.subheader(category)
        st.write(", ".join(items))

    st.divider()

    st.subheader("📊 Skill Level")

    st.progress(90, text="Python")
    st.progress(80, text="Streamlit")
    st.progress(70, text="SQL")


# ---------------- CONTACT ----------------
elif page == "Contact":
    st.title("📬 Contact Me")

    st.write("Let's connect!")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")
        email = st.text_input("Email")

    message = st.text_area("Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("✅ Message sent successfully!")
        else:
            st.error("❌ Please fill all fields")

    st.divider()

    st.subheader("🌐 Social Links")
    st.link_button("GitHub", "https://github.com/")
    st.link_button("LinkedIn", "https://linkedin.com/")
