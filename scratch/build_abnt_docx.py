"""
SEINUC/PA — ABNT & Legal Drafting DOCX Converter
Converte a documentação Markdown de producao/docs/ em arquivos .docx na pasta producao/docs/docx/
obedecendo rigorosamente às normas ABNT NBR 14724:2023, NBR 10520:2023 e Lei Complementar nº 95/1998.
"""

import os
import re
import docx
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement, parse_xml

# Color constants
COLOR_BLACK = RGBColor(0, 0, 0)
COLOR_GRAY = RGBColor(80, 80, 80)
BG_LIGHT_GRAY = "F4F6F8"
BORDER_GRAY = "CCCCCC"

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Define margens internas de uma célula da tabela"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    """Define cor de fundo para uma célula"""
    shading_elm = parse_xml(f'<w:shd xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_abnt_table_borders(table):
    """Aplica o padrão de bordas ABNT: apenas bordas horizontais (topo, cabeçalho e rodapé), sem bordas verticais."""
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
            f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
            f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'  <w:left w:val="none"/>'
            f'  <w:right w:val="none"/>'
            f'  <w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def set_code_block_borders(table):
    """Borda fina cinza e fundo cinza claro para blocos de código/schema"""
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{BORDER_GRAY}"/>'
            f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{BORDER_GRAY}"/>'
            f'  <w:left w:val="single" w:sz="12" w:space="0" w:color="003366"/>'
            f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="{BORDER_GRAY}"/>'
            f'  <w:insideH w:val="none"/>'
            f'  <w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_header_footer(doc, title_text):
    """Adiciona cabeçalho e rodapé institucionais ABNT"""
    section = doc.sections[0]
    section.header_distance = Cm(1.25)
    section.footer_distance = Cm(1.25)
    
    # Header
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("SEINUC/PA — GOVERNO DO ESTADO DO PARÁ / IDEFLOR-Bio")
    hrun.font.name = 'Times New Roman'
    hrun.font.size = Pt(8.5)
    hrun.font.italic = True
    hrun.font.color.rgb = RGBColor(120, 120, 120)
    
    # Footer
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run(f"Documento Oficial de Regulamentação e Especificação Técnica • {title_text}")
    frun.font.name = 'Times New Roman'
    frun.font.size = Pt(8.5)
    frun.font.italic = True
    frun.font.color.rgb = RGBColor(120, 120, 120)

def parse_markdown_formatting(paragraph, text, font_name='Times New Roman', font_size=Pt(12), is_bold=False, is_italic=False):
    """
    Processa marcações inline de markdown (**negrito**, *itálico*, `código inline`)
    e adiciona runs formatadas ao parágrafo.
    """
    pattern = re.compile(r'(\*\*.*?\*\*|\*.*?\*|`.*?`)')
    tokens = pattern.split(text)
    
    for token in tokens:
        if not token:
            continue
        
        run = paragraph.add_run()
        run.font.name = font_name
        run.font.size = font_size
        
        if token.startswith('**') and token.endswith('**'):
            run.text = token[2:-2]
            run.font.bold = True
            run.font.italic = is_italic
        elif token.startswith('*') and token.endswith('*'):
            run.text = token[1:-1]
            run.font.bold = is_bold
            run.font.italic = True
        elif token.startswith('`') and token.endswith('`'):
            run.text = token[1:-1]
            run.font.name = 'Consolas'
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(0, 51, 102)
        else:
            run.text = token
            run.font.bold = is_bold
            run.font.italic = is_italic

def create_abnt_document(title=""):
    """Cria um documento Word pré-configurado nas margens e estilos ABNT NBR 14724:2023"""
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Cm(3.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.0)
    
    # Configure Normal Style
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.font.color.rgb = COLOR_BLACK
    style.paragraph_format.line_spacing = 1.5
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.space_after = Pt(0)
    
    if title:
        add_header_footer(doc, title)
        
    return doc

def convert_md_to_abnt_docx(md_path, docx_path):
    """Converte um arquivo Markdown individual para DOCX ABNT com rigor técnico e legal"""
    print(f"Processando: {os.path.basename(md_path)} -> {os.path.basename(docx_path)}")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.splitlines()
    
    doc_title = os.path.basename(md_path).replace('.md', '').replace('-', ' ').title()
    doc = create_abnt_document(doc_title)
    
    is_legal_minuta = 'minuta' in os.path.basename(md_path).lower()
    in_code_block = False
    code_buffer = []
    in_table = False
    table_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 1. Bloco de Código / Schema
        if stripped.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_buffer = []
            else:
                in_code_block = False
                # Render Code Block as a shaded ABNT box
                code_text = "\n".join(code_buffer)
                tbl = doc.add_table(rows=1, cols=1)
                tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                set_code_block_borders(tbl)
                cell = tbl.rows[0].cells[0]
                set_cell_shading(cell, BG_LIGHT_GRAY)
                set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
                
                cp = cell.paragraphs[0]
                cp.paragraph_format.line_spacing = 1.0
                cp.paragraph_format.space_before = Pt(4)
                cp.paragraph_format.space_after = Pt(4)
                cp.paragraph_format.first_line_indent = Cm(0)
                
                crun = cp.add_run(code_text)
                crun.font.name = 'Consolas'
                crun.font.size = Pt(9.5)
                crun.font.color.rgb = RGBColor(30, 30, 30)
                
                # Spacer paragraph after table
                sp = doc.add_paragraph()
                sp.paragraph_format.space_after = Pt(6)
                sp.paragraph_format.line_spacing = 1.0
            i += 1
            continue
            
        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue
            
        # 2. Tabelas Markdown
        if '|' in stripped and not stripped.startswith('>'):
            if not in_table:
                in_table = True
                table_lines = [stripped]
            else:
                table_lines.append(stripped)
            i += 1
            continue
        else:
            if in_table:
                # Process accumulated table lines
                in_table = False
                render_markdown_table(doc, table_lines)
                table_lines = []
                
        # 3. Linha em branco
        if not stripped:
            i += 1
            continue
            
        # 4. Divisores / Linha horizontal
        if stripped in ['---', '***', '___']:
            i += 1
            continue
            
        # 5. Títulos (Headings)
        if stripped.startswith('#'):
            h_match = re.match(r'^(#+)\s+(.*)', stripped)
            if h_match:
                level = len(h_match.group(1))
                h_text = h_match.group(2).strip()
                
                p = doc.add_paragraph()
                p.paragraph_format.first_line_indent = Cm(0)
                p.paragraph_format.line_spacing = 1.5
                p.paragraph_format.space_before = Pt(12 if level <= 2 else 6)
                p.paragraph_format.space_after = Pt(6)
                
                if level == 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_legal_minuta and 'MINUTA' in h_text) else WD_ALIGN_PARAGRAPH.LEFT
                    parse_markdown_formatting(p, h_text.upper() if not is_legal_minuta else h_text, font_size=Pt(12), is_bold=True)
                elif level == 2:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    parse_markdown_formatting(p, h_text, font_size=Pt(12), is_bold=True)
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    parse_markdown_formatting(p, h_text, font_size=Pt(12), is_bold=True, is_italic=True)
                i += 1
                continue
                
        # 6. Ementa em Atos Normativos (linhas iniciando com `>`)
        if stripped.startswith('>'):
            e_text = re.sub(r'^>\s*', '', stripped).strip()
            
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(7.5)  # Ementa recuada à direita conforme LC 95/98
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.line_spacing = 1.0     # Espaçamento simples
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            parse_markdown_formatting(p, e_text, font_size=Pt(10), is_italic=True)
            i += 1
            continue

        # 7. Preâmbulo em Atos Normativos ("O GOVERNADOR...", "RESOLVEM:")
        if is_legal_minuta and (stripped.startswith('**O GOVERNADOR') or stripped.startswith('**O SECRETÁRIO') or stripped == '**DECRETA:**' or stripped == '**RESOLVEM:**' or stripped.startswith('PALÁCIO DO GOVERNO')):
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(12)
            
            if stripped in ['**DECRETA:**', '**RESOLVEM:**', 'PALÁCIO DO GOVERNO']:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.first_line_indent = Cm(0)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.first_line_indent = Cm(1.25)
                
            parse_markdown_formatting(p, stripped)
            i += 1
            continue

        # 8. Listas / Bullets
        if stripped.startswith('* ') or stripped.startswith('- ') or re.match(r'^\d+\.\s', stripped):
            is_num_list = bool(re.match(r'^\d+\.\s', stripped))
            item_text = re.sub(r'^(\*|-|\d+\.)\s*', '', stripped).strip()
            
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(1.25)
            p.paragraph_format.first_line_indent = Cm(-0.5)
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(2)
            
            bullet_prefix = "" if is_num_list else "• "
            parse_markdown_formatting(p, bullet_prefix + item_text)
            i += 1
            continue

        # 9. Parágrafo Padrão (ABNT Body Text)
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        
        # ABNT Recuo de Primeira Linha (1.25 cm)
        # Exceção: assinaturas e fechos no final do documento
        if stripped.startswith('**HELDER BARBALHO**') or stripped.startswith('_________________________________') or stripped.startswith('*Governador') or stripped.startswith('[NOME DO DECLARANTE]'):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(12)
        else:
            p.paragraph_format.first_line_indent = Cm(1.25)
            
        parse_markdown_formatting(p, stripped)
        i += 1

    # Final table flush if any
    if in_table and table_lines:
        render_markdown_table(doc, table_lines)
        
    doc.save(docx_path)
    print(f"[OK] Concluido: {docx_path}")

def render_markdown_table(doc, table_lines):
    """Renderiza tabelas do Markdown como tabelas ABNT NBR 14724"""
    parsed_rows = []
    for line in table_lines:
        # Ignore separator lines like |---|---|
        if re.match(r'^\|?\s*:?-+:?\s*\|', line):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if any(cells):
            parsed_rows.append(cells)
            
    if not parsed_rows:
        return
        
    num_cols = max(len(r) for r in parsed_rows)
    table = doc.add_table(rows=len(parsed_rows), cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_abnt_table_borders(table)
    
    for r_idx, row_data in enumerate(parsed_rows):
        is_header = (r_idx == 0)
        row = table.rows[r_idx]
        
        for c_idx in range(num_cols):
            cell = row.cells[c_idx]
            cell_text = row_data[c_idx] if c_idx < len(row_data) else ""
            
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            
            if is_header:
                set_cell_shading(cell, "F2F2F2")
                
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if is_header else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.first_line_indent = Cm(0)
            
            parse_markdown_formatting(p, cell_text, font_size=Pt(10), is_bold=is_header)

    # Add space after table
    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(6)
    sp.paragraph_format.line_spacing = 1.0

def convert_all_docs():
    docs_dir = r"H:\Meu Drive\IDEFLOR\SEINUC\producao\docs"
    docx_dir = r"H:\Meu Drive\IDEFLOR\SEINUC\producao\docs\docx"
    
    os.makedirs(docx_dir, exist_ok=True)
    
    files = [f for f in os.listdir(docs_dir) if f.endswith('.md')]
    
    print(f"Encontrados {len(files)} arquivos para conversão ABNT...")
    for filename in files:
        md_path = os.path.join(docs_dir, filename)
        docx_filename = filename.replace('.md', '.docx')
        docx_path = os.path.join(docx_dir, docx_filename)
        
        convert_md_to_abnt_docx(md_path, docx_path)

if __name__ == '__main__':
    convert_all_docs()
