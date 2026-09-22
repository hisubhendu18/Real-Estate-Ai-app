import streamlit as st
import google.generativeai as genai

# ১. গুগল জেমিনি এপিআই কনফিগারেশন (Streamlit Secrets থেকে সুরক্ষিতভাবে রিড)
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "YOUR_GEMINI_API_KEY_HERE"

if API_KEY != "YOUR_GEMINI_API_KEY_HERE" and API_KEY != "":
    genai.configure(api_key=API_KEY)

# ২. পেজ কনফিগারেশন ও কাস্টম সিএসএস (UI Styling)
st.set_page_config(page_title="PropAI - Real Estate Content Generator", page_icon="🏠", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 16px;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 15px rgba(0,0,0,0.15); }
    .card-box {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        border-left: 5px solid #1e3c72;
    }
    .title-text { color: #1e3c72; font-weight: 800; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# ৩. 🌐 গ্লোবাল ল্যাঙ্গুয়েজ ডিকশনারি (UI Translate Only)
ui_strings = {
    "Bengali (বাংলা)": {
        "title": "🏠 PropAI: রিয়েল এস্টেট কন্টেন্ট জেনারেটর",
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
        "info_text": "বাঁদিকের ঘরে প্রপার্টির তথ্য দিয়ে বাটনে ক্লিক করলেই এখানে আপনার চমৎকার বিজ্ঞাপনটি ভেসে উঠবে।",
        "warning_text": "⚠️ দয়া করে লোকেশন এবং সুবিধাসমূহের ঘর দুটি পূরণ করুন。"
    },
    "English": {
        "title": "🏠 PropAI: Real Estate Content Generator",
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
        "info_text": "Enter property details on the left and click the button to see your amazing ad here.",
        "warning_text": "⚠️ Please fill in both Location and Amenities fields."
    },
    "Spanish (Español)": {
        "title": "🏠 PropAI: Generador de Contenido Inmobiliario",
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
        "info_text": "Ingrese los detalles a la izquierda y haga clic en el botón para ver su anuncio aquí.",
        "warning_text": "⚠️ Por favor complete los campos de Ubicación y Amenidades."
    },
    "French (Français)": {
        "title": "🏠 PropAI: Générateur de Contenu Immobilier",
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
        "info_text": "Entrez los détails à gauche et cliquez sur le bouton pour voir votre annonce ici.",
        "warning_text": "⚠️ Veuillez remplir los champs Emplacement et Équipements."
    }
}

# ৪. সাইডবার ল্যাঙ্গুয়েজ কন্ট্রোল (দুটি আলাদা ড্রপডাউন)
st.sidebar.markdown("### 🌐 Language Settings")

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
st.markdown(f"<p style='text-align: center; color: #666;'>{ui['subtitle']}</p>", unsafe_allow_html=True)
st.write("---")

st.sidebar.markdown(f"### {ui['sidebar_title']}")
property_type = st.sidebar.selectbox(
    ui['prop_type'], 
    ["1 BHK Flat", "2 BHK Apartment", "3 BHK Luxury Flat", "4 BHK Penthouse", "Duplex House", "Commercial Office/Shop", "Plot/Land"]
)

# মূল স্ক্রিন লেআউট (ডাবল কলাম)
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown(f"<div class='card-box'><h4>{ui['input_title']}</h4>", unsafe_allow_html=True)
    location = st.text_input(ui['loc_label'], placeholder=ui['loc_placeholder'])
    amenities = st.text_area(ui['amenities_label'], placeholder=ui['amenities_placeholder'], height=120)
    st.write("")
    generate_btn = st.button(ui['btn_text'])
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='card-box' style='min-height: 380px;'><h4>{ui['output_title']}</h4>", unsafe_allow_html=True)
    
    if generate_btn:
        if not location or not amenities:
            st.warning(ui['warning_text'])
        else:
            with st.spinner("AI Generating..."):
                try:
                    # প্রম্পটে এআই আউটপুট ল্যাঙ্গুয়েজকে আলাদাভাবে পাঠানো হলো
                    prompt = f"""
                    You are a world-class real estate copywriter. 
                    Based on these details, write a highly engaging social media ad and property description.
                    Property Type: {property_type}
                    Location: {location}
                    Amenities: {amenities}
                    Strict Instruction: Write the entire marketing ad and description output in {selected_output_lang} language. Include emojis and hashtags.
                    """
                    
                    model = genai.GenerativeModel("gemini-3.5-flash-lite")
                    response = model.generate_content(prompt)
                    
                    st.markdown(response.text)
                    st.write("---")
                    st.text_area("📋 Copy text:", value=response.text, height=150)
                    
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.info(ui['info_text'])
        
    st.markdown("</div>", unsafe_allow_html=True)
