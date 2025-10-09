import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="Certificados de Calibração",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Ocultar TODOS os elementos do Streamlit */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .viewerBadge_container__1QSob {display: none !important;}
    .styles_viewerBadge__1yB5_ {display: none !important;}
    .stApp [data-testid="stToolbar"] {display: none !important;}
    div[data-testid="stDecoration"] {display: none !important;}
    div[data-testid="stStatusWidget"] {display: none !important;}
    button[kind="header"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    section[data-testid="stSidebar"] {display: none !important;}
    .css-1dp5vir {display: none !important;}
    .css-18e3th9 {padding-top: 0 !important;}
    .block-container {padding-top: 2rem !important;}
    
    /* Ocultar "Created by" e "Hosted with Streamlit" */
    footer {display: none !important;}
    footer * {display: none !important;}
    .viewerBadge_container__r5tak {display: none !important;}
    .viewerBadge_link__qRIco {display: none !important;}
    footer::before {display: none !important;}
    footer::after {display: none !important;}
    a[href*="streamlit.io"] {display: none !important;}
    [data-testid="stToolbarActions"] {display: none !important;}
    .viewerBadge_link__1S137 {display: none !important;}
    .viewerBadge_text__1JaDK {display: none !important;}
    div[class*="viewerBadge"] {display: none !important;}
    div[class*="ViewerBadge"] {display: none !important;}
    header[data-testid="stHeader"] {display: none !important;}
    section[data-testid="stHeader"] {display: none !important;}
    div[data-testid="stHeader"] {display: none !important;}
    
    /* Forçar esconder footer completamente */
    footer, footer *, .main footer, .main footer * {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        position: absolute !important;
        left: -9999px !important;
    }
    
    /* Ocultar ícones do canto superior direito */
    button[kind="headerNoPadding"] {display: none !important;}
    button[data-testid="baseButton-header"] {display: none !important;}
    button[data-testid="baseButton-headerNoPadding"] {display: none !important;}
    div[data-testid="stActionButtonIcon"] {display: none !important;}
    .stApp > header {display: none !important;}
    .stApp header[data-testid="stHeader"] > div {display: none !important;}
    section[data-testid="stSidebarNav"] {display: none !important;}
    
    /* Ocultar qualquer botão no header */
    header button {display: none !important;}
    header svg {display: none !important;}
    .stApp > header > div {display: none !important;}
    
    [data-testid="column"] {
        padding: 0 4px !important;
    }
    
    .card {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 12px;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.06);
        height: 450px;
        display: flex;
        flex-direction: column;
        margin-bottom: 8px;
    }
    
    .card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    
    .card-img {
        width: 100%;
        height: 140px;
        object-fit: contain;
        background: #f9fafb;
        border-radius: 8px;
        margin-bottom: 8px;
    }
    
    .card-title {
        font-size: 13px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }
    
    .card-body {
        flex: 1;
        overflow-y: auto;
        font-size: 10px;
        color: #4b5563;
    }
    
    .card-body::-webkit-scrollbar {
        width: 4px;
    }
    
    .card-body::-webkit-scrollbar-thumb {
        background: #d1d5db;
        border-radius: 2px;
    }
    
    .field {
        margin: 3px 0;
        padding: 2px 0;
        border-bottom: 1px solid #f3f4f6;
        line-height: 1.3;
    }
    
    .field strong {
        color: #1f2937;
        font-weight: 600;
    }
    
    .link {
        color: #2563eb;
        text-decoration: none;
        font-weight: 600;
    }
    
    .link:hover {
        text-decoration: underline;
    }
    
    h1 {
        font-size: 24px !important;
        margin-bottom: 16px !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def normalize_text(text: str) -> str:
    if pd.isna(text):
        return ""
    text = str(text).lower()
    replacements = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c', 'ñ': 'n'
    }
    for accented, normal in replacements.items():
        text = text.replace(accented, normal)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return ' '.join(text.split())

def load_data() -> pd.DataFrame:
    try:
        df = pd.read_excel("PMJA-INSTRUMENTOS CERTIFICADOS.xlsx")
        for col in df.columns:
            if df[col].dtype == 'datetime64[ns]':
                df[col] = df[col].dt.strftime('%d/%m/%Y')
            elif 'data' in col.lower() or 'date' in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                    df[col] = df[col].dt.strftime('%d/%m/%Y')
                except:
                    pass
        return df
    except Exception as e:
        st.error(f"Erro: {str(e)}")
        st.stop()

def filter_data(df: pd.DataFrame, search: str) -> pd.DataFrame:
    if not search:
        return df
    normalized_search = normalize_text(search)
    mask = pd.Series([False] * len(df), index=df.index)
    for col in df.columns:
        normalized_col = df[col].apply(normalize_text)
        mask |= normalized_col.str.contains(normalized_search, na=False)
    return df[mask]

# JavaScript para remover elementos do Streamlit
st.markdown("""
<script>
    // Função para remover elementos
    function removeStreamlitElements() {
        // Remover footer
        const footer = window.parent.document.querySelector('footer');
        if (footer) footer.remove();
        
        // Remover todos os elementos com "streamlit" no texto
        const allElements = window.parent.document.querySelectorAll('*');
        allElements.forEach(el => {
            if (el.textContent && (el.textContent.includes('Streamlit') || 
                el.textContent.includes('Created by') || 
                el.textContent.includes('Hosted'))) {
                el.style.display = 'none';
                el.remove();
            }
        });
        
        // Remover header
        const header = window.parent.document.querySelector('header');
        if (header) header.remove();
        
        // Remover toolbar
        const toolbar = window.parent.document.querySelector('[data-testid="stToolbar"]');
        if (toolbar) toolbar.remove();
        
        // Remover badges
        const badges = window.parent.document.querySelectorAll('[class*="viewerBadge"]');
        badges.forEach(badge => badge.remove());
    }
    
    // Executar imediatamente
    removeStreamlitElements();
    
    // Executar periodicamente
    setInterval(removeStreamlitElements, 100);
    
    // Executar quando a página carregar
    window.addEventListener('load', removeStreamlitElements);
    document.addEventListener('DOMContentLoaded', removeStreamlitElements);
</script>
""", unsafe_allow_html=True)

st.title("PMJA - Gestão de Instrumentos Certificados")

df = load_data()
if 'Item' in df.columns:
    df = df.drop(columns=['Item'])

search = st.text_input("Buscar", placeholder="🔍 Buscar...", label_visibility="collapsed")
filtered_df = filter_data(df, search)

if not filtered_df.empty:
    cols = st.columns(4, gap="small")
    
    for idx, (_, row) in enumerate(filtered_df.iterrows()):
        with cols[idx % 4]:
            # Prioritize meaningful identifier columns
            preferred_identifier_cols = ['Cód. Material (Nº do Ativo)', 'Descrição do Instrumento', 'Nº de Série', 'Marca', 'Modelo']
            identifier_col = None
            for col in preferred_identifier_cols:
                if col in row.index:
                    identifier_col = col
                    break
            # If none of the preferred columns exist, use the first available column that's not 'item'
            if identifier_col is None:
                identifier_col = [col for col in row.index if col.lower() != 'item'][0]
            identifier = row[identifier_col] if not pd.isna(row[identifier_col]) else "Sem ID"
            
            link = row.get('LinkCertificado', '')
            imagem = row.get('ImagemLink', '')
            
            html = '<div class="card">'
            
            # Imagem
            if imagem and pd.notna(imagem) and str(imagem).strip():
                html += f'<img src="{imagem}" class="card-img">'
            else:
                html += f'<div class="card-img" style="display:flex;align-items:center;justify-content:center;font-size:11px;color:#9ca3af;">{identifier}</div>'
            
            # Título
            html += f'<div class="card-title">{identifier}</div>'
            
            # Campos
            html += '<div class="card-body">'
            for col in row.index:
                if col.lower() not in ['item', 'link', 'imagemlink', 'linkcertificado', 'click', 'imagem']:
                    value = row[col]
                    if pd.notna(value) and str(value).strip():
                        # Link no certificado
                        if col in ['Nº do Certificado', 'Certificate Number / Calibration Number', 'N do Certificado']:
                            if link and pd.notna(link) and str(link).strip() and str(link).strip() != '#':
                                html += f'<div class="field"><strong>{col}:</strong> <a href="{link}" target="_blank" class="link">{value}</a></div>'
                            else:
                                html += f'<div class="field"><strong>{col}:</strong> {value}</div>'
                        else:
                            html += f'<div class="field"><strong>{col}:</strong> {value}</div>'
            html += '</div></div>'
            
            st.markdown(html, unsafe_allow_html=True)
else:
    st.info("Nenhum resultado encontrado.")