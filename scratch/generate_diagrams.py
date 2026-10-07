"""
SEINUC/PA — Gerador de Diagramas Institucionais de Alta Resolução (IDEFLOR-Bio)
Gera imagens PNG estilizadas para inserção nos documentos ABNT e suporte aos diagramas Mermaid.
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Cores Institucionais
COLOR_NAVY = (0, 51, 102)        # #003366 - Azul Primário Executivo
COLOR_GREEN = (30, 77, 43)       # #1E4D2B - Verde Conservação
COLOR_AMBER = (217, 119, 6)      # #D97706 - Dourado / Alerta
COLOR_DARK = (45, 55, 72)        # #2D3748 - Grafite Texto
COLOR_BG_LIGHT = (248, 249, 250) # #F8F9FA - Fundo Card
COLOR_BORDER = (203, 213, 225)   # #CBD5E1 - Borda suave
COLOR_WHITE = (255, 255, 255)

def get_font(size=14, bold=False):
    font_path = "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf"
    if not os.path.exists(font_path):
        font_path = "C:\\Windows\\Fonts\\seguiemj.ttf"
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

def draw_card(draw, box, title, subtitle="", bg_color=COLOR_BG_LIGHT, border_color=COLOR_BORDER, text_color=COLOR_DARK, title_size=15, sub_size=12, radius=8):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=bg_color, outline=border_color, width=2)
    
    font_t = get_font(title_size, bold=True)
    font_s = get_font(sub_size, bold=False)
    
    if subtitle:
        # Title + Subtitle centered vertically
        draw.text(((x1+x2)/2, y1 + 14), title, fill=text_color, font=font_t, anchor="mm")
        draw.text(((x1+x2)/2, y1 + 36), subtitle, fill=text_color, font=font_s, anchor="mm")
    else:
        draw.text(((x1+x2)/2, (y1+y2)/2), title, fill=text_color, font=font_t, anchor="mm")

def draw_arrow(draw, start, end, color=COLOR_DARK, width=3):
    x1, y1 = start
    x2, y2 = end
    draw.line([x1, y1, x2, y2], fill=color, width=width)
    
    # Arrow head
    if x1 == x2: # Vertical arrow down
        draw.polygon([(x2-6, y2-8), (x2+6, y2-8), (x2, y2+2)], fill=color)
    elif y1 == y2: # Horizontal arrow right
        draw.polygon([(x2-8, y2-6), (x2-8, y2+6), (x2+2, y2)], fill=color)

# ---------------------------------------------------------
# 1. Diagrama: Portal Público de Transparência
# ---------------------------------------------------------
def generate_portal_diagram(output_path):
    w, h = 1000, 360
    img = Image.new("RGB", (w, h), COLOR_WHITE)
    draw = ImageDraw.Draw(img)
    
    # Root Box
    draw_card(draw, [250, 20, 750, 85], "PORTAL PÚBLICO SEINUC/PA", "(Transparência Ativa - LAI & Lei 10.306/2023)", bg_color=COLOR_NAVY, text_color=COLOR_WHITE, title_size=17, sub_size=12)
    
    # Connecting Lines
    draw.line([500, 85, 500, 130], fill=COLOR_NAVY, width=3)
    draw.line([175, 130, 825, 130], fill=COLOR_NAVY, width=3)
    
    draw_arrow(draw, (175, 130), (175, 160), color=COLOR_NAVY)
    draw_arrow(draw, (500, 130), (500, 160), color=COLOR_NAVY)
    draw_arrow(draw, (825, 130), (825, 160), color=COLOR_NAVY)
    
    # Child Boxes
    draw_card(draw, [20, 160, 330, 310], "MÓDULO A", "Visualizador WebGIS Interativo\n(WMS, WFS e Mapas de UCs)", bg_color=COLOR_GREEN, text_color=COLOR_WHITE, title_size=15, sub_size=12)
    draw_card(draw, [345, 160, 655, 310], "MÓDULO B", "Repositório Documental\n(Planos de Gestão e Atos)", bg_color=COLOR_GREEN, text_color=COLOR_WHITE, title_size=15, sub_size=12)
    draw_card(draw, [670, 160, 980, 310], "MÓDULO C", "Painel do ICMS Ecológico\n(Prestação de Contas e 20%)", bg_color=COLOR_AMBER, text_color=COLOR_WHITE, title_size=15, sub_size=12)
    
    img.save(output_path, dpi=(300, 300))
    print(f"[OK] Gerado: {output_path}")

# ---------------------------------------------------------
# 2. Diagrama: Arquitetura Canônica de Módulos
# ---------------------------------------------------------
def generate_modules_diagram(output_path):
    w, h = 1000, 400
    img = Image.new("RGB", (w, h), COLOR_WHITE)
    draw = ImageDraw.Draw(img)
    
    # Root Box
    draw_card(draw, [250, 15, 750, 75], "SEINUC/PA — BANCO DE DADOS OFICIAL", "(Estrutura Canônica de Módulos Temáticos)", bg_color=COLOR_NAVY, text_color=COLOR_WHITE, title_size=17, sub_size=12)
    
    # 4 Modules Cards
    boxes = [
        ([20, 120, 480, 240], "MÓDULO I — AMBIENTAL & CLIMA", "Fauna, Flora, Hidrografia, Solos, Relevo,\nClima e Espécies Ameaçadas/Exóticas", COLOR_GREEN),
        ([520, 120, 980, 240], "MÓDULO II — GEOTECNOLOGIAS & ZA", "SIRGAS 2000 (EPSG:4674), Perímetros,\nZoneamento e Zonas de Amortecimento", COLOR_GREEN),
        ([20, 260, 480, 380], "MÓDULO III — GESTÃO & UCS LEGADAS", "Conselhos, Planos de Gestão, UCs Legadas,\nAspectos Antropológicos e Repasse (20%)", COLOR_GREEN),
        ([520, 260, 980, 380], "MÓDULO IV — FUNDIÁRIO & RPPNS", "Situação Dominial, Regularização Fundiária,\nRPPNs e Averbação no RGI", COLOR_GREEN)
    ]
    
    # Lines
    draw.line([500, 75, 500, 100], fill=COLOR_NAVY, width=3)
    draw.line([250, 100, 750, 100], fill=COLOR_NAVY, width=3)
    draw_arrow(draw, (250, 100), (250, 120), color=COLOR_NAVY)
    draw_arrow(draw, (750, 100), (750, 120), color=COLOR_NAVY)
    
    for box, title, sub, color in boxes:
        draw_card(draw, box, title, sub, bg_color=color, text_color=COLOR_WHITE, title_size=14, sub_size=11)
        
    img.save(output_path, dpi=(300, 300))
    print(f"[OK] Gerado: {output_path}")

# ---------------------------------------------------------
# 3. Diagrama: Fluxo Operacional Anual (ICMS Ecológico)
# ---------------------------------------------------------
def generate_flow_diagram(output_path):
    w, h = 1000, 220
    img = Image.new("RGB", (w, h), COLOR_WHITE)
    draw = ImageDraw.Draw(img)
    
    steps = [
        ([15, 40, 195, 170], "1. TRANSMISSÃO", "Até 31/Jan\nFormulário / SFTP\nHash SHA-256"),
        ([210, 40, 390, 170], "2. TRIAGEM", "Até 28/Fev\nAdmissibilidade\nDiligência 5 dias"),
        ([405, 40, 585, 170], "3. ANÁLISE MÉRITO", "Março a Abril\nAvaliação Técnica\nPontuação Quesitos"),
        ([600, 40, 780, 170], "4. PROVISÓRIO", "Até 31/Maio\nDOE e Portal SEINUC\nRecurso 15 dias úteis"),
        ([795, 40, 985, 170], "5. DEFINITIVO", "Até 31/Julho\nHomologação SEMAS\nEnvio à SEFA/PA")
    ]
    
    for i, (box, title, sub) in enumerate(steps):
        bg = COLOR_NAVY if i in [0, 4] else (COLOR_AMBER if i == 3 else COLOR_GREEN)
        draw_card(draw, box, title, sub, bg_color=bg, text_color=COLOR_WHITE, title_size=13, sub_size=11)
        if i < len(steps) - 1:
            next_x1 = steps[i+1][0][0]
            draw_arrow(draw, (box[2], 105), (next_x1, 105), color=COLOR_DARK, width=3)
            
    img.save(output_path, dpi=(300, 300))
    print(f"[OK] Gerado: {output_path}")

# ---------------------------------------------------------
# 4. Diagrama: Estrutura de Diretórios do Pacote de Envio
# ---------------------------------------------------------
def generate_package_diagram(output_path):
    w, h = 900, 340
    img = Image.new("RGB", (w, h), COLOR_WHITE)
    draw = ImageDraw.Draw(img)
    
    draw_card(draw, [20, 20, 380, 70], "[PACOTE_ENVIO_ANO_BASE]/", "(Diretório Raiz Compactado .zip)", bg_color=COLOR_NAVY, text_color=COLOR_WHITE, title_size=14, sub_size=11)
    
    folders = [
        ([430, 20, 880, 70], "01_DOCUMENTOS_OBRIGATORIOS/", "Ofício de Encaminhamento e Declaração de Veracidade"),
        ([430, 80, 880, 130], "02_MODULO_I_AMBIENTAL/", "Ficha de Caracterização Ambiental e Biodiversidade (PDF)"),
        ([430, 140, 880, 190], "03_MODULO_II_GEOTECNOLOGIAS/", "Pacote Vetorial em SIRGAS 2000 (.zip / GeoPackage / KML)"),
        ([430, 200, 880, 250], "04_MODULO_III_GESTAO/", "Plano de Gestão, Atas do Conselho e Comprovantes"),
        ([430, 260, 880, 310], "05_MODULO_IV_FUNDIARIO_RPPN/", "Certidão do RGI e Matrícula Averbadora de RPPN")
    ]
    
    draw.line([200, 70, 200, 285], fill=COLOR_NAVY, width=3)
    
    for box, title, sub in folders:
        y_mid = (box[1] + box[3]) / 2
        draw_arrow(draw, (200, y_mid), (430, y_mid), color=COLOR_NAVY, width=2)
        draw_card(draw, box, title, sub, bg_color=COLOR_BG_LIGHT, border_color=COLOR_NAVY, text_color=COLOR_DARK, title_size=13, sub_size=11)
        
    img.save(output_path, dpi=(300, 300))
    print(f"[OK] Gerado: {output_path}")

# ---------------------------------------------------------
# 5. Diagrama: Fases do Roadmap
# ---------------------------------------------------------
def generate_roadmap_diagram(output_path):
    w, h = 1000, 180
    img = Image.new("RGB", (w, h), COLOR_WHITE)
    draw = ImageDraw.Draw(img)
    
    fases = [
        ([15, 30, 230, 150], "FASE 1 — 100%", "Arcabouço Normativo\nDecreto, Ciclo & LEPA"),
        ([260, 30, 475, 150], "FASE 2 — 100%", "Arquitetura de Dados\nMódulos I a IV & Schemas"),
        ([505, 30, 720, 150], "FASE 3 — 100%", "Esteira Operacional\nPortaria, Envio & Triagem"),
        ([750, 30, 980, 150], "FASE 4 — 100%", "Transparência & OGC\nPortal, WMS/WFS & CSW")
    ]
    
    for i, (box, title, sub) in enumerate(fases):
        draw_card(draw, box, title, sub, bg_color=COLOR_GREEN, text_color=COLOR_WHITE, title_size=13, sub_size=11)
        if i < len(fases) - 1:
            next_x1 = fases[i+1][0][0]
            draw_arrow(draw, (box[2], 90), (next_x1, 90), color=COLOR_DARK, width=3)
            
    img.save(output_path, dpi=(300, 300))
    print(f"[OK] Gerado: {output_path}")

if __name__ == '__main__':
    img_dir = r"H:\Meu Drive\IDEFLOR\SEINUC\producao\docs\img"
    os.makedirs(img_dir, exist_ok=True)
    
    generate_portal_diagram(os.path.join(img_dir, "diagrama_portal_transparencia.png"))
    generate_modules_diagram(os.path.join(img_dir, "diagrama_arquitetura_modulos.png"))
    generate_flow_diagram(os.path.join(img_dir, "diagrama_fluxo_operacional.png"))
    generate_package_diagram(os.path.join(img_dir, "diagrama_estrutura_pacote.png"))
    generate_roadmap_diagram(os.path.join(img_dir, "diagrama_fases_roadmap.png"))
