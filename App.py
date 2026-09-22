import streamlit as st
import google.generativeai as genai


if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "YOUR_GEMINI_API_KEY_HERE" 

if API_KEY != "YOUR_GEMINI_API_KEY_HERE":
    genai.configure(api_key=API_KEY)

# ২. পেজ কনফিগারেশন ও কাস্টম সিএসএস (UI Styling)
st.set_page_config(page_title="PropAI - Real Estate Content Generator", page_icon="🏠", layout="wide")

# প্রফেশনাল লুক দেওয়ার জন্য কাস্টম স্টাইল
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
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .card-box {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        border-left: 5px solid #1e3c72;
    }
    .title-text {
        color: #1e3c72;
        font-weight: 800;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True) # <-- এখানে ঠিক করা হয়েছে


st.markdown("<h1 class='title-text'>🏠 PropAI: Real Estate Content Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>এআই প্রযুক্তির মাধ্যমে মাত্র ৫ সেকেন্ডে প্রফেশনাল রিয়েল এস্টেট বিজ্ঞাপন তৈরি করুন।</p>", unsafe_allow_html=True)
st.write("---")

# বামদিকের সাইডবার (Sidebar) - ইনপুট ও কনফিগারেশন
st.sidebar.markdown("### ⚙️ প্রপার্টি কনফিগারেশন")

property_type = st.sidebar.selectbox(
    "🏢 প্রপার্টির ধরণ:", 
    ["1 BHK Flat", "2 BHK Apartment", "3 BHK Luxury Flat", "4 BHK Penthouse", "Duplex House", "Commercial Office/Shop", "Plot/Land"]
)

# পৃথিবীর প্রধান প্রধান ভাষাগুলোর একটি সুন্দর ড্রপডাউন লিস্ট
languages_list = [
    "Bengali (বাংলা)", "English", "Hindi (हिन्दी)", "Spanish (Español)", 
    "French (Français)", "Arabic (العربية)", "German (Deutsch)", 
    "Portuguese (Português)", "Japanese (日本語)", "Mix (Banglish/Hinglish)"
]

language = st.sidebar.selectbox("🌐 বিজ্ঞাপনের ভাষা (Select Language):", languages_list)

# মূল স্ক্রিন - ডাবল কলাম লেআউট
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("<div class='card-box'><h4>📝 প্রপার্টির বিবরণ দিন</h4>", unsafe_allow_html=True)
    location = st.text_input("📍 লোকেশন (যেমন: Salt Lake Sector 5, Kolkata):", placeholder="ঠিকানাটি এখানে লিখুন...")
    
    amenities = st.text_area(
        "✨ বিশেষ সুবিধাসমূহ (কমা দিয়ে লিখুন):", 
        placeholder="যেমন: Swimming Pool, Gym, 24/7 Security, Covered Parking, Near Metro Station",
        height=120
    )
    
    st.write("")
    generate_btn = st.button("🚀 ম্যাজিক কন্টেন্ট তৈরি করুন")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card-box' style='min-height: 380px;'><h4>🔥 আপনার রেডি-টু-পোস্ট বিজ্ঞাপন</h4>", unsafe_allow_html=True)
    
    if generate_btn:
        if not location or not amenities:
            st.warning("⚠️ দয়া করে লোকেশন এবং সুবিধাসমূহের ঘর দুটি পূরণ করুন।")
        elif API_KEY == "YOUR_GEMINI_API_KEY_HERE":
            st.error("🛑 আগে আপনার আসল Gemini API Key বসাতে হবে।")
        else:
            with st.spinner("AI আপনার জন্য কন্টেন্ট তৈরি করছে..."):
                try:
                    # প্রম্পট ইঞ্জিনিয়ারিং
                    prompt = f"""
                    You are a world-class real estate copywriter and digital marketer. 
                    Based on the following details, write a highly engaging Facebook/Instagram Ad and a detailed property description.
                    
                    Property Type: {property_type}
                    Location: {location}
                    Amenities: {amenities}
                    
                    Strict Instructions:
                    1. Write the entire output in {language} language. 
                    2. If the language is Bengali, keep the tone very professional yet welcoming.
                    3. Include an eye-catching headline, a clear list of premium features using emojis, and a strong Call to Action (e.g., Contact for site visit).
                    4. Add relevant real estate hashtags at the very end.
                    """
                    
                    model = genai.GenerativeModel("gemini-3.5-flash-lite")
                    response = model.generate_content(prompt)
                    
                    st.markdown(response.text)
                    
                    st.write("---")
                    st.text_area("📋 নিচে থেকে সহজে টেক্সট কপি করুন:", value=response.text, height=150)
                    
                except Exception as e:
                    st.error(f"একটি ত্রুটি ঘটেছে: {e}. আপনার API Key অথবা ইন্টারনেট কানেকশন চেক করুন।")
    else:
        st.info("বাঁদিকের ঘরে প্রপার্টির তথ্য দিয়ে বাটনে ক্লিক করলেই এখানে আপনার চমৎকার বিজ্ঞাপনটি ভেসে উঠবে।")
        
    st.markdown("</div>", unsafe_allow_html=True)
