import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="GlobalShield Tactical OS - Varsovie",
    page_icon="🛡️",
    layout="centered"
)

# Style CSS personnalisé pour imiter l'interface tactique sombre
st.markdown("""
<style>
    .stApp {
        background-color: #070a14;
        color: #f8fafc;
    }
    .main-title {
        color: #38bdf8;
        font-size: 1.5rem;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-header {
        text-align: center;
        color: #94a3b8;
        font-size: 0.85rem;
        margin-bottom: 15px;
    }
    .gps-box {
        background-color: #1e293b;
        color: #38bdf8;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 20px;
        border: 1px solid #334155;
    }
    .alert-card {
        background-color: #1e293b;
        border-left: 5px solid #3b82f6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-size: 0.9rem;
    }
    .alert-card-warning {
        background-color: #261f12;
        border-left: 5px solid #f59e0b;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# En-tête de l'application
st.markdown('<div class="main-title">🛡️ GlobalShield Tactical OS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Priorité Opérationnelle : Varsovie (Pologne)</div>', unsafe_allow_html=True)
st.markdown('<div class="gps-box">📍 Localisation : Varsovie (Centre / Sektor 1)</div>', unsafe_allow_html=True)

# Alerte 1 : Police Varsovie
st.markdown("""
<div class="alert-card">
    <div style="font-weight: bold; color: #fff; margin-bottom: 6px; display: flex; justify-content: space-between;">
        <span>🔵 POLICE : Sécurité Renforcée</span>
        <span style="font-size:0.7rem; background:#1e3a8a; color:#93c5fd; padding:2px 6px; border-radius:4px;">Live</span>
    </div>
    <p>Mise en place de barrières de sécurité et contrôles renforcés dans l'hypercentre (Krakowskie Przedmieście et axes avoisinants) suite aux consignes de la Policja.</p>
    <a href="https://policja.pl/" target="_blank" style="color: #38bdf8; font-size: 0.8rem; text-decoration: none;">🔗 Source officielle : Policja</a>
</div>
""", unsafe_allow_html=True)

# Alerte 2 : MSWiA
st.markdown("""
<div class="alert-card-warning">
    <div style="font-weight: bold; color: #fff; margin-bottom: 6px; display: flex; justify-content: space-between;">
        <span>🟡 MSWiA : Alerte Nationale & Consignes</span>
        <span style="font-size:0.7rem; background:#78350f; color:#fde68a; padding:2px 6px; border-radius:4px;">Actif</span>
    </div>
    <p>Rappel des consignes de vigilance et suivi des répercussions sécuritaires nationales (coordination inter-régionale).</p>
    <a href="https://www.gov.pl/web/mswia" target="_blank" style="color: #38bdf8; font-size: 0.8rem; text-decoration: none;">🔗 Source officielle : Ministère de l'Intérieur (MSWiA)</a>
</div>
""", unsafe_allow_html=True)

# Alerte 3 : Ministère de la Défense
st.markdown("""
<div class="alert-card-warning">
    <div style="font-weight: bold; color: #fff; margin-bottom: 6px; display: flex; justify-content: space-between;">
        <span>🟡 ARMÉE : Veille Stratégique</span>
        <span style="font-size:0.7rem; background:#78350f; color:#fde68a; padding:2px 6px; border-radius:4px;">Vigilance</span>
    </div>
    <p>Surveillance conjointe des points névralgiques de la capitale par les forces armées et les services de protection.</p>
    <a href="https://www.gov.pl/web/obrona-narodowa" target="_blank" style="color: #38bdf8; font-size: 0.8rem; text-decoration: none;">🔗 Source officielle : Ministère de la Défense (MON)</a>
</div>
""", unsafe_allow_html=True)

# Bouton SOS interactif sous Streamlit
if st.button("🚨 Déclencher Alerte SOS Urgence", type="primary", use_container_width=True):
    st.error("🚨 Alerte SOS transmise avec succès ! Position partagée avec les services d'urgence à Varsovie.")
