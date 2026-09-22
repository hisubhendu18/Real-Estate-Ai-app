import streamlit as st
import google.generativeai as genai

# ১. গুগল জেমিনি এপিআই কনফিগারেশন (Streamlit Secrets থেকে সুরক্ষিতভাবে রিড)
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "YOUR_GEMINI_API_KEY_HERE"

if API_KEY != "YOUR_GEMINI_API_KEY_HERE" and API_KEY != "":
    genai.configure(api_key=API_KEY)

# ২. পেজ কনফিগারেশন ও কাস্টম সিএসএস (Ultra-Professional UI Styling)
st.set_page_config(page_title="PropAI Premium - Real Estate SaaS", page_icon="🏠", layout="wide")

# ইন্টারন্যাশনাল লাক্সারি কর্পোরেট থিম (Deep Navy, Slate Blue and Premium Shadows)
st.markdown("""
    <style>
    /* মেইন ব্যাকগ্রাউন্ড */
    .stApp {
        background-color: #f4f6f9;
    }
    
    /* সাইডবার কাস্টমাইজেশন */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        color: #f8fafc !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label {
        color: #f8fafc !important;
    }
    
    /* গ্লোবাল ফন্ট এবং হেডার স্টাইল */
    .title-text {
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
        font-size: 38px;
        margin-bottom: 5px;
        font-family: 'Inter', sans-serif;
    }
    .subtitle-text {
        text-align: center;
        color: #64748b;
        font-size: 16px;
        margin-bottom: 30px;
    }
    
    /* প্রিমিয়াম ইনপুট ও আউটপুট কার্ড বক্স */
    .card-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    .card-box:hover {
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        transform: translateY(-2px);
    }
    
    .card-header-in {
        color: #0f172a;
        font-weight: 700;
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .card-header-out {
        color: #0f172a;
        font-weight: 700;
        border-bottom: 2px solid #10b981;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    /* ইন্টারঅ্যাক্টিভ প্রিমিয়াম বাটন */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 14px 28px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        width: 100% !important;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #2563eb, #1e40af) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4) !important;
    }
    
    /* কাস্টম ইনপুট ফিল্ড বর্ডার কালার */
    div[data-baseweb="input"] {
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ৩. 🌐 গ্লোবাল ল্যাঙ্গুয়েজ ডিকশনারি (UI Localization)
ui_strings = {
    "Bengali (বাংলা)": {
        "title": "🏠 PropAI Premium",
        "subtitle": "এআই প্রযুক্তির মাধ্যমে মাত্র ৫ সেকেন্ডে প্রফেশনাল রিয়েল এস্টেট বিজ্ঞাপন তৈরি করুন।",
        "sidebar_ui_lang": "🌐 ওয়েবসাইটের ভাষা (UI Language):",
        "sidebar_out_lang": "📝 বিজ্ঞাপনের আউটপুট ভাষা (AI Output Language):",
        "sidebar_title": "⚙️ প্রপার্টি কনফিগারেশন",
        "prop_type": "🏢 প্রপার্টির ধরণ:",
        "input_title": "📝 প্রপার্টির বিবরণ দিন",
        "loc_label": "📍 লোকেশন (যেমন: Salt Lake Sector 5, Kolkata):",
        "loc_placeholder": "ঠিকানাটি এখানে লিখুন...",
        "amenities_label": "✨ বিশেষ সুবিধাসমূহ (কমা দিয়ে লিখুন):",
        "amenities_placeholder": "যেমন: Swimming Pool, Gym, 24/7 Security",
        "btn_text": "🚀 ম্যাজিক কন্টেন্ট তৈরি করুন",
        "output_title": "🔥 আপনার রেডি-টু-পোস্ট বিজ্ঞাপন",
        "info_text": "📄 বাঁদিকের ঘরে প্রপার্টির তথ্য দিয়ে বাটনে ক্লিক করলেই এখানে আপনার চমৎকার বিজ্ঞাপনটি ভেসে উঠবে।",
        "warning_text": "⚠️ দয়া করে লোকেশন এবং সুবিধাসমূহের ঘর দুটি পূরণ করুন।"
    },
    "English": {
        "title": "🏠 PropAI Premium",
        "subtitle": "Create professional real estate ads in just 5 seconds using AI technology.",
        "sidebar_ui_lang": "🌐 Website Language (UI Language):",
        "sidebar_out_lang": "📝 Ad Output Language (AI Output Language):",
        "sidebar_title": "⚙️ Property Configuration",
        "prop_type": "🏢 Property Type:",
        "input_title": "📝 Enter Property Details",
        "loc_label": "📍 Location (e.g., Salt Lake Sector 5, Kolkata):",
        "loc_placeholder": "Enter address here...",
        "amenities_label": "✨ Amenities (comma separated):",
        "amenities_placeholder": "e.g., Swimming Pool, Gym, 24/7 Security",
        "btn_text": "🚀 Generate Magic Content",
        "output_title": "🔥 Your Ready-to-Post Ad",
        "info_text": "📄 Enter property details on the left and click the button to see your amazing ad here.",
        "warning_text": "⚠️ Please fill in both Location and Amenities fields."
    },
    "Spanish (Español)": {
        "title": "🏠 PropAI Premium",
        "subtitle": "Cree anuncios inmobiliarios profesionales en solo 5 segundos con IA.",
        "sidebar_ui_lang": "🌐 Idioma del Sitio Web (Idioma de la IU):",
        "sidebar_out_lang": "📝 Idioma de Salida del Anuncio (Idioma de IA):",
        "sidebar_title": "⚙️ Configuración de la Propiedad",
        "prop_type": "🏢 Tipo de Propiedad:",
        "input_title": "📝 Ingrese Detalles de la Propiedad",
        "loc_label": "📍 Ubicación (ej., Salt Lake Sector 5, Kolkata):",
        "loc_placeholder": "Ingrese la dirección aquí...",
        "amenities_label": "✨ Amenidades (separadas por comas):",
        "amenities_placeholder": "ej., Piscina, Gimnasio, Seguridad 24/7",
        "btn_text": "🚀 Generar Contenido Mágico",
        "output_title": "🔥 Su Anuncio Listo para Publicar",
        "info_text": "📄 Ingrese los detalles a la izquierda y haga clic en el botón para ver su anuncio aquí.",
        "warning_text": "⚠️ Por favor complete los campos de Ubicación y Amenidades."
    },
    "French (Français)": {
        "title": "🏠 PropAI Premium",
        "subtitle": "Créez des annonces immobilières professionnelles en seulement 5 secondes grâce a l'IA.",
        "sidebar_ui_lang": "🌐 Langue du Site Web (Langue de l'IU):",
        "sidebar_out_lang": "📝 Langue de Sortie de l'Annonce (Langue de l'IA):",
        "sidebar_title": "⚙️ Configuration de la Propriété",
        "prop_type": "🏢 Type de Propriété:",
        "input_title": "📝 Entrez los Détails de la Propriété",
        "loc_label": "📍 Emplacement (ex., Salt Lake Sector 5, Kolkata):",
        "loc_placeholder": "Entrez l'adresse ici...",
        "amenities_label": "✨ Équipements (séparés par des virgules):",
        "amenities_placeholder": "ex., Piscine, Salle de sport, Sécurité 24/7",
        "btn_text": "🚀 Générer le Contenu Magique",
        "output_title": "🔥 Votre Annonce Prête à Publier",
        "info_text": "📄 Entrez los détails à gauche et cliquez sur le bouton pour voir votre annonce ici.",
        "warning_text": "⚠️ Veuillez remplir los champs Emplacement et Équipements."
    }
}

# ৪. সাইডবার ল্যাঙ্গুয়েজ কন্ট্রোল (প্রিমিয়াম ডার্ক থিম সাইডবার)
st.sidebar.markdown("## 🌐 Global Settings")

# ড্রপডাউন ১: পুরো ওয়েবসাইটের ইন্টারফেস ল্যাঙ্গুয়েজ কন্ট্রোল করবে
selected_ui_lang = st.sidebar.selectbox("Choose Website Language:", list(ui_strings.keys()))
ui = ui_strings[selected_ui_lang] # ইউজারের সিলেক্ট করা UI টেক্সট লোড

st.sidebar.write("---")

# ড্রপডাউন ২: এআই (AI) কোন ভাষায় কন্টেন্ট লিখবে তা কন্ট্রোল করবে
output_languages = [
    "Bengali (বাংলা)", "English", "Hindi (हिन्दी)", "Spanish (Español)", 
    "French (Français)", "Arabic (العربية)", "German (Deutsch)", 
    "Portuguese (Português)", "Japanese (日本語)", "Mix (Banglish/Hinglish)"
]
selected_output_lang = st.sidebar.selectbox(ui['sidebar_out_lang'], output_languages)

# ৫. অ্যাপ্লিকেশনের মূল ইন্টারফেস (ডাইনামিক UI টেক্সট)
st.markdown(f"<h1 class='title-text'>{ui['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle-text'>{ui['subtitle']}</p>", unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.markdown(f"### {ui['sidebar_title']}")
property_type = st.sidebar.selectbox(
    ui['prop_type'], 
    ["1 BHK Flat", "2 BHK Apartment", "3 BHK Luxury Flat", "4 BHK Penthouse", "Duplex House", "Commercial Office/Shop", "Plot/Land"]
)

col1, col2 = st.columns([1, 1.25])

with col1:
    st.markdown(f"<div class='card-box'><h3 class='card-header-in'>{ui['input_title']}</h3>", unsafe_allow_html=True)
    location = st.text_input(ui['loc_label'], placeholder=ui['loc_placeholder'])
    amenities = st.text_area(ui['amenities_label'], placeholder=ui['amenities_placeholder'], height=120)
    st.write("")
    generate_btn = st.button(ui['btn_text'])
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='card-box' style='min-height: 420px;'><h3 class='card-header-out'>{ui['output_title']}</h3>", unsafe_allow_html=True)
    
    if generate_btn:
        if not location or not amenities:
            st.warning(ui['warning_text'])
        else:
            with st.spinner("✨ PropAI Magic Generating..."):
                try:
