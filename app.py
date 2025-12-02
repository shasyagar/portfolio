import streamlit as st

# ----- SIDEBAR NAVIGATION -----
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["Home", "Experience", "Projects", "Publications", "Skills", "Achievements", "Gallery"]
)

# ----- COMMON STYLES -----
st.markdown("""
<style>
h1, h2, h3 {
    color: #C76C84; /* blush heading */
}
</style>
""", unsafe_allow_html=True)

# ============================================
# HOME PAGE
# ============================================
if page == "Home":
    st.title("Sanjana Varada Hasyagar")
    st.subheader("Aspiring Bioinformatics Researcher")
    st.write("Driven to advance cancer research through collaborative discovery.")

    # Image placeholder
    st.markdown("### 📸 Profile Image")
    st.info("Upload your photo into `assets/profile.jpg` and replace this placeholder.")
    st.image("assets/profile.jpg", caption="Your Profile Image", use_column_width=True)

    st.markdown("---")
    st.header("Education")

    st.write("""
    **Boston University, MA (2024–2025)**  
    Master of Science – Bioinformatics (GPA 3.96)

    **PES University, Bangalore (2017–2021)**  
    B.Tech Biotechnology Engineering (GPA 3.86)  
    Minor: Computer Science (GPA 3.90)
    """)

# ============================================
# EXPERIENCE PAGE
# ============================================
elif page == "Experience":
    st.title("Experience")

    st.subheader("Data Scientist — Tata Consultancy Services (July 2025 – Present)")
    st.write("""
    - Developing a precision medicine model using LLMs to be offered as a service.
    """)

    st.subheader("Intern — Dries Lab (Feb 2025 – May 2025)")
    st.write("""
    - Processed spatial ATAC-seq using ArchR; integrated multimodal outputs using Giotto Suite.
    - Contributed `runIterativeLSI` to Giotto.
    - Built MAGIC-style imputation module; validated workflows with high-resolution Xenium data.
    """)

    st.subheader("Teaching Assistant — Boston University (Sept 2024 – Dec 2024)")
    st.write("""
    - Assisted in graduate-level bioinformatics: computational linguistics, Linux, Python.
    - Supported lab sessions and HPC usage.
    """)

    st.subheader("MS Student Researcher — BUSM (Mar 2024 – Sept 2024)")
    st.write("""
    - Used LLMs to predict gene expression & chromatin states.
    - Extracted TF & CRE embeddings and applied transfer learning approaches.
    """)

    st.subheader("Researcher — Tata Consultancy Services (June 2021 – Dec 2023)")
    st.write("""
    - Protein stability prediction using AI.
    - Built thermal stability datasets.
    - Developed ML/DL models using ProtBERT and ESM encodings.
    """)

    st.subheader("Research Intern — Eurofins Genomics (Jan 2021 – May 2021)")
    st.write("""
    - Worked on SARS-CoV-2 mutation prediction using supervised ML.
    """)

# ============================================
# PROJECTS PAGE
# ============================================
elif page == "Projects":
    st.title("Projects")

    st.subheader("R Shiny App: Huntington's Disease RNA-Seq (Dec 2024)")
    st.write("""
    - Built an R Shiny tool to explore differential expression datasets.
    """)

    st.subheader("ATAC-Seq Pipeline for Human Samples (Apr–May 2024)")
    st.write("""
    - Built a full pipeline using BowTie2, samtools, and MACS3 for chromatin accessibility analysis.
    """)

    st.subheader("APOE4 Genotype Web App (Mar–May 2024)")
    st.write("""
    - Created an interactive visualization tool using JS, HTML, CSS, AJAX, Python.
    """)

    st.subheader("ChIP-Seq Analysis of Runx1 (Mar 2024)")
    st.write("""
    - Analyzed Runx1 ChIP-Seq pipeline from reads to peaks using Bowtie2, HOMER.
    """)

    st.subheader("Protein Stability Prediction (2021–2023)")
    st.write("""
    - Used NLP models (ESM, ProtBERT) to predict ΔΔG changes in protein stability.
    """)

    st.subheader("SARS-CoV-2 Mutation Prediction (2021)")
    st.write("""
    - Random forest classifier predicted 38 missense mutations in S gene.
    """)

# ============================================
# PUBLICATIONS PAGE
# ============================================
elif page == "Publications":
    st.title("Publications")

    st.write("""
    **Giotto Suite: Spatial Multi-omics Ecosystem**  
    Accepted by Nature Methods.

    **Network Pharmacology Study (2021)**  
    Jethalia, V., Hasyagar, S., et al. Neuroscience Research Notes.
    """)

# ============================================
# SKILLS PAGE
# ============================================
elif page == "Skills":
    st.title("Skills")

    st.write("""
    **Technical:** Python, R, Shiny, Scikit-learn, PyTorch, Snakemake, Scanpy, Giotto, Cytoscape  
    **Bioinformatics:** RNA-Seq, ChIP-Seq, ATAC-Seq, Spatial ATAC-Seq  
    **Tools:** GitHub, VSCode, Linux, HPC clusters  
    **Web:** HTML, CSS, JS, AJAX  
    """)

# ============================================
# ACHIEVEMENTS PAGE
# ============================================
elif page == "Achievements":
    st.title("Achievements & Extracurriculars")

    st.write("""
    - Future Promise Scholarship, BU ($15,000)  
    - Distinction Awards (PES University)  
    - Head of University Dance Team (Sanskrithi)  
    - Distinction in Bharatanatyam  
    """)

    st.markdown("### 📸 Extracurricular Image")
    st.info("Place your image at `assets/extracurricular.jpg`.")
    st.image("assets/extracurricular.jpg", caption="Dance / Extracurriculars", use_column_width=True)

# ============================================
# GALLERY PAGE
# ============================================
elif page == "Gallery":
    st.title("Gallery")
    st.write("Add any images you want displayed here.")

    st.info("Upload your gallery images into the `assets/` folder.")
    st.image("assets/gallery1.jpg", caption="Gallery Image 1", use_column_width=True)
