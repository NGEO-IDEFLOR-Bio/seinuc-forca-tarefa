import os

html_content = '''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEINUC/PA — Dossiê Técnico-Normativo de Regulamentação</title>
    <meta name="description" content="Dossiê Técnico-Normativo Executivo do SEINUC/PA — Regulamentação da Lei Estadual nº 10.306/2023, Schema de Dados, Manual de Auditoria e ICMS Ecológico.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    
    <!-- Font Awesome Icons CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"IBM Plex Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    },
                    colors: {
                        govNavy: '#041E42',
                        govGreen: '#005A36',
                        govGold: '#C59B27',
                        govDark: '#0B131F',
                    }
                }
            }
        }
    </script>

    <style>
        :root {
            --stack-top: 80px;
        }

        body {
            background-color: #070D14;
            color: #E2E8F0;
            font-family: 'IBM Plex Sans', sans-serif;
            overflow-x: hidden;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #070D14;
        }
        ::-webkit-scrollbar-thumb {
            background: #1E293B;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #334155;
        }

        /* Hero Background */
        .hero-bg {
            background: radial-gradient(ellipse at 50% 20%, #0c2340 0%, #070D14 75%);
        }

        /* Drawer Folder Container */
        .drawer-container {
            max-width: 1280px;
            width: 95%;
            margin: 0 auto;
            position: relative;
            padding-bottom: 30vh;
        }

        .folder {
            position: sticky;
            min-height: 620px;
            max-height: 88vh;
            background: transparent;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            filter: drop-shadow(0 -15px 35px rgba(0, 0, 0, 0.85));
            transition: top 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.3s ease;
        }

        /* Folder Stacking Top Positions */
        .folder:nth-child(1) { top: calc(var(--stack-top) + 0px); z-index: 1; --folder-theme: #0A2540; --tab-accent: #38BDF8; }
        .folder:nth-child(2) { top: calc(var(--stack-top) + 48px); z-index: 2; --folder-theme: #04382C; --tab-accent: #34D399; }
        .folder:nth-child(3) { top: calc(var(--stack-top) + 96px); z-index: 3; --folder-theme: #451A03; --tab-accent: #FB923C; }
        .folder:nth-child(4) { top: calc(var(--stack-top) + 144px); z-index: 4; --folder-theme: #1E1B4B; --tab-accent: #A78BFA; }
        .folder:nth-child(5) { top: calc(var(--stack-top) + 192px); z-index: 5; --folder-theme: #064E3B; --tab-accent: #4ADE80; }
        .folder:nth-child(6) { top: calc(var(--stack-top) + 240px); z-index: 6; --folder-theme: #1E293B; --tab-accent: #FBBF24; }

        .drawer-container.collapsed .folder {
            top: var(--stack-top) !important;
        }

        .folder-tab {
            height: 48px;
            min-width: 320px;
            max-width: 100%;
            padding: 0 28px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.08em;
            border-radius: 12px 12px 0 0;
            margin-bottom: -2px;
            z-index: 2;
            position: relative;
            color: #FFFFFF;
            background-color: var(--folder-theme);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-bottom: none;
            box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.4);
        }

        .folder-tab-badge {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: var(--tab-accent);
            box-shadow: 0 0 10px var(--tab-accent);
        }

        .folder-body {
            width: 100%;
            background: #0F172A;
            padding: 36px;
            border-radius: 0 16px 16px 16px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-top: 2px solid var(--tab-accent);
            flex-grow: 1;
            position: relative;
            z-index: 1;
            overflow-y: auto;
            max-height: calc(88vh - 48px);
            box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.4);
        }

        /* Legislative Text Style */
        .law-quote {
            background-color: #090E17;
            border-left: 4px solid var(--tab-accent);
            padding: 16px 20px;
            font-family: 'IBM Plex Sans', serif;
            font-size: 0.92rem;
            line-height: 1.6;
            color: #CBD5E1;
            border-radius: 0 8px 8px 0;
        }

        /* Code Block Styling */
        .code-container {
            background-color: #070C14;
            border: 1px solid #1E293B;
            border-radius: 10px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            line-height: 1.5;
            color: #38BDF8;
            overflow-x: auto;
        }
    </style>
</head>
<body>

    <!-- TOP EXECUTIVE HEADER -->
    <header class="sticky top-0 z-50 bg-[#070D14]/90 backdrop-blur-md border-b border-slate-800 shadow-lg">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <div class="flex items-center space-x-4">
                <img src="assets/img/logo_ideflor.png" alt="IDEFLOR-Bio" class="h-10 object-contain">
                <div class="h-8 w-px bg-slate-700 hidden sm:block"></div>
                <img src="assets/img/logo_governo_para.png" alt="Governo do Pará" class="h-9 object-contain hidden sm:block">
                <div class="h-8 w-px bg-slate-700 hidden md:block"></div>
                <img src="assets/img/logo_ngeo.png" alt="NGEO" class="h-8 object-contain hidden md:block">
            </div>

            <div class="hidden lg:flex items-center space-x-2 text-xs font-semibold tracking-wider text-slate-300 uppercase">
                <span class="px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-amber-400">
                    <i class="fa-solid fa-file-signature mr-1.5"></i> Lei Estadual nº 10.306/2023
                </span>
                <span class="px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-emerald-400">
                    <i class="fa-solid fa-shield-halved mr-1.5"></i> PGE/PA & FAMEP
                </span>
            </div>

            <a href="https://github.com/NGEO-IDEFLOR-Bio/seinuc-forca-tarefa" target="_blank" class="inline-flex items-center space-x-2 bg-slate-800 hover:bg-slate-700 text-slate-200 px-4 py-2 rounded-lg text-xs font-semibold transition-all border border-slate-700 shadow-sm">
                <i class="fa-brands fa-github text-sm"></i>
                <span class="hidden sm:inline">Repositório Oficial</span>
            </a>
        </div>
    </header>

    <!-- HERO SECTION -->
    <section class="hero-bg py-16 lg:py-20 border-b border-slate-800 text-center relative overflow-hidden">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="inline-flex items-center space-x-2 bg-emerald-950/80 border border-emerald-500/30 px-4 py-1.5 rounded-full text-xs font-semibold uppercase tracking-widest text-emerald-400 mb-6">
                <i class="fa-solid fa-scroll"></i>
                <span>Dossiê Técnico-Normativo • Parecer Executivo</span>
            </div>
            
            <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight mb-6">
                SEINUC / PA
            </h1>
            <h2 class="text-xl sm:text-2xl font-medium text-slate-300 max-w-3xl mx-auto mb-6">
                Sistema Estadual de Informações sobre Unidades de Conservação do Pará
            </h2>

            <p class="text-base sm:text-lg text-slate-400 max-w-3xl mx-auto leading-relaxed mb-8">
                Instrução normativa e estruturação tecnológica para regulamentação da <strong class="text-slate-200">Lei Estadual nº 10.306/2023</strong>. Consolidação dos arcabouços legal, cadastral, geográfico e financeiro para submissão à <strong class="text-slate-200">Procuradoria-Geral do Estado (PGE/PA)</strong> e consulta municipal.
            </p>

            <!-- Executive Context Box -->
            <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 text-left max-w-4xl mx-auto backdrop-blur-md shadow-2xl">
                <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
                    <div class="flex items-center space-x-3">
                        <i class="fa-solid fa-building-columns text-amber-400 text-lg"></i>
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-300">Sumário de Encaminhamento Institucional</span>
                    </div>
                    <span class="text-xs font-mono bg-emerald-950 text-emerald-300 px-2.5 py-1 rounded border border-emerald-800">Status: ✅ APROVADO</span>
                </div>
                <div class="grid md:grid-cols-3 gap-4 text-xs text-slate-300">
                    <div>
                        <span class="text-slate-500 block font-semibold uppercase">Órgão Central</span>
                        <strong class="text-slate-200">SEMAS/PA</strong> (Art. 68 da Lei 10.306)
                    </div>
                    <div>
                        <span class="text-slate-500 block font-semibold uppercase">Órgão Executor</span>
                        <strong class="text-slate-200">IDEFLOR-Bio</strong> (Gestão Operacional)
                    </div>
                    <div>
                        <span class="text-slate-500 block font-semibold uppercase">Rito Recursal Unificado</span>
                        <strong class="text-slate-200">15 Dias Úteis</strong> (Lei nº 8.972/2020 - LEPA)
                    </div>
                </div>
            </div>

            <div class="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4 text-xs font-semibold text-slate-400">
                <span><i class="fa-solid fa-arrow-down-long text-emerald-400 mr-2 animate-bounce"></i> Role a página para abrir as pastas do dossiê técnico</span>
            </div>
        </div>
    </section>

    <!-- DRAWER FOLDERS STACK CONTAINER -->
    <main class="py-12">
        <div class="drawer-container" id="drawer">
            
            <!-- PASTA 1: MINUTA DO DECRETO ESTADUAL -->
            <div class="folder" id="pasta-decreto">
                <div class="folder-tab">
                    <span class="folder-tab-badge"></span>
                    <span>PASTA I • MINUTA DO DECRETO ESTADUAL (EIXO LEGAL)</span>
                </div>
                <div class="folder-body">
                    <div class="flex flex-col lg:flex-row lg:items-center justify-between border-b border-slate-800 pb-4 mb-6 gap-4">
                        <div>
                            <span class="text-xs font-mono uppercase text-sky-400 tracking-wider">Regulamentação da Lei Estadual nº 10.306/2023</span>
                            <h2 class="text-2xl font-bold text-white mt-1">Dispositivos Regulamentares & Segurança Jurídica</h2>
                        </div>
                        <a href="producao/docs/docx/minuta-decreto-seinuc.docx" class="inline-flex items-center space-x-2 bg-sky-600 hover:bg-sky-500 text-white px-4 py-2 rounded-lg text-xs font-bold transition-all shadow-md">
                            <i class="fa-solid fa-file-word"></i>
                            <span>Baixar Minuta Oficial (.docx ABNT)</span>
                        </a>
                    </div>

                    <div class="grid lg:grid-cols-2 gap-6 mb-6">
                        <div class="space-y-4">
                            <h3 class="text-sm font-bold uppercase text-slate-300 tracking-wider flex items-center">
                                <i class="fa-solid fa-gavel text-sky-400 mr-2"></i> Pilares da Minuta Regulamentar
                            </h3>
                            <ul class="space-y-3 text-xs text-slate-300">
                                <li class="bg-slate-900/80 p-3 rounded-lg border border-slate-800">
                                    <strong class="text-sky-300 block mb-1">1. Pacificação de Terminologia (Art. 2º, XXII)</strong>
                                    Fica estabelecida a equivalência jurídica absoluta entre o termo federal "Plano de Manejo" e o termo legal estadual <strong class="text-white">"Plano de Gestão"</strong>, eliminando dupla exigência técnica.
                                </li>
                                <li class="bg-slate-900/80 p-3 rounded-lg border border-slate-800">
                                    <strong class="text-sky-300 block mb-1">2. Rito Recursal da LEPA/PA (Lei Estadual nº 8.972/2020)</strong>
                                    Fixação do prazo de <strong class="text-white">15 (quinze) dias úteis</strong> para interposição de recurso administrativo (Art. 83 da LEPA), garantidos a ampla defesa e o efeito suspensivo.
                                </li>
                                <li class="bg-slate-900/80 p-3 rounded-lg border border-slate-800">
                                    <strong class="text-sky-300 block mb-1">3. Minuta Aberta & Flexibilidade Executiva</strong>
                                    Adoção da técnica legislativa padrão <strong class="text-white">[NOME DO(A) GOVERNADOR(A)]</strong>, garantindo perenidade técnica independente de transição de mandato.
                                </li>
                            </ul>
                        </div>

                        <div>
                            <h3 class="text-sm font-bold uppercase text-slate-300 tracking-wider mb-3 flex items-center">
                                <i class="fa-solid fa-quote-left text-sky-400 mr-2"></i> Excerto Normativo do Decreto
                            </h3>
                            <div class="law-quote space-y-3">
                                <p class="font-semibold text-slate-200">
                                    "DECRETO Nº [NÚMERO], DE [DIA] DE [MÊS] DE [ANO]
                                </p>
                                <p class="italic">
                                    Regulamenta o Sistema Estadual de Informações sobre Unidades de Conservação do Pará (SEINUC/PA), previsto no Art. 68 da Lei Estadual nº 10.306, de 3 de janeiro de 2023, institui o Portal Público de Transparência e estabelece os procedimentos para apuração dos indicadores do ICMS Ecológico."
                                </p>
                                <p class="text-xs text-slate-400 border-t border-slate-800 pt-2">
                                    <strong>Art. 4º.</strong> O SEINUC/PA integrará as informações das UCs estaduais, municipais e RPPNs em quatro módulos estruturados de dados cadastrais, geográficos, de gestão e de repasse financeiro.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PASTA 2: ARQUITETURA DE DADOS & SCHEMA JSON -->
            <div class="folder" id="pasta-schema">
                <div class="folder-tab">
                    <span class="folder-tab-badge"></span>
                    <span>PASTA II • ARQUITETURA DE DADOS & SCHEMA JSON (EIXO TECNOLÓGICO)</span>
                </div>
                <div class="folder-body">
                    <div class="flex flex-col lg:flex-row lg:items-center justify-between border-b border-slate-800 pb-4 mb-6 gap-4">
                        <div>
                            <span class="text-xs font-mono uppercase text-emerald-400 tracking-wider">Especificação Técnica de Dados v1.0.0-final</span>
                            <h2 class="text-2xl font-bold text-white mt-1">Validação Estruturada & Regras Condicionais (allOf/if-then)</h2>
                        </div>
                        <a href="producao/docs/docx/especificacao-modulos-dados-seinuc.docx" class="inline-flex items-center space-x-2 bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-lg text-xs font-bold transition-all shadow-md">
                            <i class="fa-solid fa-file-word"></i>
                            <span>Baixar Especificação de Dados (.docx)</span>
                        </a>
                    </div>

                    <div class="grid lg:grid-cols-2 gap-6">
                        <div class="space-y-4">
                            <p class="text-xs text-slate-300 leading-relaxed">
                                O schema JSON do SEINUC/PA (Draft-07) unifica os 4 Módulos de Dados. Para evitar inconsistências de preenchimento pelos órgãos gestores e prefeituras, inclui validações rigorosas de tipos, padrões REGEX, enumerações fechadas e estruturas de dependência lógica.
                            </p>

                            <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-3">
                                <h4 class="text-xs font-bold uppercase text-emerald-400 flex items-center">
                                    <i class="fa-solid fa-code-branch mr-2"></i> Regra de Validação do Conselho Gestor (Refinamento R1)
                                </h4>
                                <p class="text-xs text-slate-300">
                                    Se o campo <code class="text-emerald-300">conselho_gestor_existente</code> for <code class="text-emerald-300">true</code>, o bloco <code class="text-emerald-300">then</code> exige obrigatoriamente a presença de <code class="text-emerald-300">conselho_reunioes_qtd</code>, impedindo omissão total do quantitativo de reuniões.
                                </p>
                            </div>

                            <div class="grid grid-cols-2 gap-3 text-xs">
                                <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                                    <span class="text-slate-500 block uppercase font-mono">Datum Cartográfico</span>
                                    <strong class="text-emerald-400">SIRGAS 2000 (EPSG:4674)</strong>
                                </div>
                                <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                                    <span class="text-slate-500 block uppercase font-mono">Formato Espacial</span>
                                    <strong class="text-emerald-400">GeoJSON / OGC Shapefile</strong>
                                </div>
                            </div>
                        </div>

                        <!-- Code Viewer -->
                        <div>
                            <div class="flex items-center justify-between bg-slate-900 px-4 py-2 rounded-t-lg border border-slate-800 border-b-0">
                                <span class="text-xs font-mono text-emerald-400">schema-seinuc.json [Trecho if-then]</span>
                                <span class="text-[10px] bg-slate-800 text-slate-400 px-2 py-0.5 rounded">JSON Schema Draft-07</span>
                            </div>
                            <div class="code-container p-4 rounded-b-lg max-h-64 overflow-y-auto">
<pre><code>{
  <span class="text-emerald-400">"allOf"</span>: [
    {
      <span class="text-emerald-400">"if"</span>: {
        <span class="text-emerald-400">"properties"</span>: {
          <span class="text-emerald-400">"conselho_gestor_existente"</span>: { <span class="text-amber-400">"const"</span>: <span class="text-sky-300">true</span> }
        }
      },
      <span class="text-emerald-400">"then"</span>: {
        <span class="text-emerald-400">"required"</span>: [
          <span class="text-sky-300">"conselho_ato_criacao"</span>,
          <span class="text-sky-300">"conselho_reunioes_qtd"</span>
        ],
        <span class="text-emerald-400">"properties"</span>: {
          <span class="text-emerald-400">"conselho_reunioes_qtd"</span>: {
            <span class="text-amber-400">"type"</span>: <span class="text-sky-300">"integer"</span>,
            <span class="text-amber-400">"minimum"</span>: <span class="text-sky-300">0</span>
          }
        }
      }
    }
  ]
}</code></pre>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PASTA 3: MANUAL OPERACIONAL DE AUDITORIA -->
            <div class="folder" id="pasta-manual">
                <div class="folder-tab">
                    <span class="folder-tab-badge"></span>
                    <span>PASTA III • MANUAL OPERACIONAL DE AUDITORIA (EIXO DE VÍCIOS)</span>
                </div>
                <div class="folder-body">
                    <div class="flex flex-col lg:flex-row lg:items-center justify-between border-b border-slate-800 pb-4 mb-6 gap-4">
                        <div>
                            <span class="text-xs font-mono uppercase text-amber-400 tracking-wider">Protocolo de Triagem e Qualificação Cadastral</span>
                            <h2 class="text-2xl font-bold text-white mt-1">Catálogo de Vícios Sanáveis vs. Insanáveis</h2>
                        </div>
                        <a href="producao/docs/docx/manual-fluxo-envio-e-triagem.docx" class="inline-flex items-center space-x-2 bg-amber-600 hover:bg-amber-500 text-white px-4 py-2 rounded-lg text-xs font-bold transition-all shadow-md">
                            <i class="fa-solid fa-file-word"></i>
                            <span>Baixar Manual Operacional (.docx)</span>
                        </a>
                    </div>

                    <div class="grid lg:grid-cols-2 gap-6">
                        <!-- Vícios Sanáveis -->
                        <div class="bg-slate-900/90 p-5 rounded-xl border border-amber-500/20">
                            <div class="flex items-center space-x-2 text-amber-400 font-bold text-sm uppercase mb-3">
                                <i class="fa-solid fa-wrench"></i>
                                <span>Vícios Sanáveis (Prazo Recursal de 15 Dias Úteis)</span>
                            </div>
                            <p class="text-xs text-slate-300 mb-4 leading-relaxed">
                                Irregularidades formais que admitem correção tempestiva sem perda de habilitação no ciclo de repasse:
                            </p>
                            <ul class="space-y-2 text-xs text-slate-300">
                                <li class="flex items-start space-x-2">
                                    <i class="fa-solid fa-check text-amber-400 mt-0.5"></i>
                                    <span>Erro de digitação em nomes de conselheiros ou número da ata.</span>
                                </li>
                                <li class="flex items-start space-x-2">
                                    <i class="fa-solid fa-check text-amber-400 mt-0.5"></i>
                                    <span>Falta temporária de cópia digitalizada de ata quando houver declaração formal do órgão gestor.</span>
                                </li>
                                <li class="flex items-start space-x-2">
                                    <i class="fa-solid fa-check text-amber-400 mt-0.5"></i>
                                    <span>Nomenclatura legada (ex: envio do arquivo com o nome oficial estipulado <code class="text-amber-300">PLANO_GESTAO.pdf</code> em substituição ao termo anterior).</span>
                                </li>
                            </ul>
                        </div>

                        <!-- Vícios Insanáveis -->
                        <div class="bg-slate-900/90 p-5 rounded-xl border border-red-500/20">
                            <div class="flex items-center space-x-2 text-red-400 font-bold text-sm uppercase mb-3">
                                <i class="fa-solid fa-circle-xmark"></i>
                                <span>Vícios Insanáveis / Eliminatórios</span>
                            </div>
                            <p class="text-xs text-slate-300 mb-4 leading-relaxed">
                                Inconformidades graves de natureza jurídica ou cartográfica que resultam no indeferimento imediato:
                            </p>
                            <ul class="space-y-2 text-xs text-slate-300">
                                <li class="flex items-start space-x-2">
                                    <i class="fa-solid fa-xmark text-red-400 mt-0.5"></i>
                                    <span><strong>Inconformidades Cartográficas Topológicas:</strong> Sobreposição indevida sobre Terras Indígenas ou Quilombolas sem amparo legal.</span>
                                </li>
                                <li class="flex items-start space-x-2">
                                    <i class="fa-solid fa-xmark text-red-400 mt-0.5"></i>
                                    <span><strong>Ausência do Ato Legal de Criação:</strong> Falta de publicação do Decreto de Criação no Diário Oficial.</span>
                                </li>
                                <li class="flex items-start space-x-2">
                                    <i class="fa-solid fa-xmark text-red-400 mt-0.5"></i>
                                    <span><strong>Incompatibilidade de Datum:</strong> Arquivos shapefile gravados fora do Datum oficial SIRGAS 2000.</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PASTA 4: ICMS ECOLÓGICO & REPASSE MUNICIPAL -->
            <div class="folder" id="pasta-icms">
                <div class="folder-tab">
                    <span class="folder-tab-badge"></span>
                    <span>PASTA IV • ICMS ECOLÓGICO & METODOLOGIA DE CÁLCULO (EIXO FINANCEIRO)</span>
                </div>
                <div class="folder-body">
                    <div class="flex flex-col lg:flex-row lg:items-center justify-between border-b border-slate-800 pb-4 mb-6 gap-4">
                        <div>
                            <span class="text-xs font-mono uppercase text-purple-400 tracking-wider">Cota-Parte Municipal & Decreto Estadual nº 1.064/2020</span>
                            <h2 class="text-2xl font-bold text-white mt-1">Linha do Tempo & Ciclo Anual de Apuração</h2>
                        </div>
                        <a href="producao/docs/docx/minuta-portaria-diretrizes-tecnicas.docx" class="inline-flex items-center space-x-2 bg-purple-600 hover:bg-purple-500 text-white px-4 py-2 rounded-lg text-xs font-bold transition-all shadow-md">
                            <i class="fa-solid fa-file-word"></i>
                            <span>Baixar Portaria de Diretrizes (.docx)</span>
                        </a>
                    </div>

                    <!-- Timeline Flow -->
                    <div class="grid md:grid-cols-4 gap-4 mb-6">
                        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 relative">
                            <span class="text-xs font-mono text-purple-400 block font-bold mb-1">FASE 1 • ATÉ 31/01</span>
                            <h4 class="text-xs font-bold text-white mb-1">Envio pelos Municípios</h4>
                            <p class="text-[11px] text-slate-400 leading-snug">Submissão dos dados anuais das UCs municipais no Portal SEINUC.</p>
                        </div>
                        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 relative">
                            <span class="text-xs font-mono text-purple-400 block font-bold mb-1">FASE 2 • FEVEREIRO</span>
                            <h4 class="text-xs font-bold text-white mb-1">Auditoria & Triagem</h4>
                            <p class="text-[11px] text-slate-400 leading-snug">Processamento sintático via Schema JSON e análise cartográfica OGC.</p>
                        </div>
                        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 relative">
                            <span class="text-xs font-mono text-purple-400 block font-bold mb-1">FASE 3 • MARÇO (15 D.U.)</span>
                            <h4 class="text-xs font-bold text-white mb-1">Janela de Recursos (LEPA)</h4>
                            <p class="text-[11px] text-slate-400 leading-snug">Notificação dos municípios com vícios sanáveis e prazo de 15 dias úteis.</p>
                        </div>
                        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 relative">
                            <span class="text-xs font-mono text-purple-400 block font-bold mb-1">FASE 4 • ATÉ 31/05</span>
                            <h4 class="text-xs font-bold text-white mb-1">Homologação Final</h4>
                            <p class="text-[11px] text-slate-400 leading-snug">Publicação do índice definitivo do IGUC para repasse no exercício seguinte.</p>
                        </div>
                    </div>

                    <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 text-xs text-slate-300">
                        <strong class="text-purple-300 block mb-1">Princípio da Atualização Contínua Intra-Ciclo</strong>
                        Enquanto os índices do ICMS Verde seguem o ciclo anual com trava em 31/05, os dados de geoprocessamento e polígonos de novas UCs no Portal Público possuem <strong class="text-white">atualização contínua e em tempo real</strong>.
                    </div>
                </div>
            </div>

            <!-- PASTA 5: GEOTECNOLOGIAS & INTEROPERABILIDADE OGC -->
            <div class="folder" id="pasta-ogc">
                <div class="folder-tab">
                    <span class="folder-tab-badge"></span>
                    <span>PASTA V • GEOSERVIÇOS OGC & ZONA DE AMORTECIMENTO (EIXO ESPACIAL)</span>
                </div>
                <div class="folder-body">
                    <div class="flex flex-col lg:flex-row lg:items-center justify-between border-b border-slate-800 pb-4 mb-6 gap-4">
                        <div>
                            <span class="text-xs font-mono uppercase text-emerald-400 tracking-wider">WebGIS Interativo & Serviços de Mapas WMS/WFS</span>
                            <h2 class="text-2xl font-bold text-white mt-1">Interoperabilidade Espacial & Transparência Activa</h2>
                        </div>
                        <a href="producao/docs/docx/especificacao-portal-transparencia-ogc.docx" class="inline-flex items-center space-x-2 bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-lg text-xs font-bold transition-all shadow-md">
                            <i class="fa-solid fa-file-word"></i>
                            <span>Baixar Especificação OGC (.docx)</span>
                        </a>
                    </div>

                    <div class="grid lg:grid-cols-3 gap-6">
                        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800">
                            <div class="text-emerald-400 font-bold text-xs uppercase mb-2 flex items-center">
                                <i class="fa-solid fa-layer-group mr-2"></i> Módulo A — WebGIS
                            </div>
                            <p class="text-xs text-slate-300 leading-relaxed">
                                Visualizador geográfico de UCs estaduais, municipais, RPPNs e Zonas de Amortecimento (ZA) com suporte a downloads diretos em KML, GeoJSON e Shapefile.
                            </p>
                        </div>

                        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800">
                            <div class="text-emerald-400 font-bold text-xs uppercase mb-2 flex items-center">
                                <i class="fa-solid fa-folder-tree mr-2"></i> Módulo B — Documental
                            </div>
                            <p class="text-xs text-slate-300 leading-relaxed">
                                Repositório unificado dos Planos de Gestão (equivalentes aos planos de manejo), Atos de Criação, Atas dos Conselhos e Estudos Antropológicos.
                            </p>
                        </div>

                        <div class="bg-slate-900 p-4 rounded-xl border border-slate-800">
                            <div class="text-emerald-400 font-bold text-xs uppercase mb-2 flex items-center">
                                <i class="fa-solid fa-chart-pie mr-2"></i> Módulo C — Painel ICMS
                            </div>
                            <p class="text-xs text-slate-300 leading-relaxed">
                                Consulta pública aos índices de efetividade de gestão das UCs por município com demonstrativos de repasse financeiro do ICMS Verde.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PASTA 6: CERTIFICAÇÃO DE APROVAÇÃO & PARECER FINAL -->
            <div class="folder" id="pasta-certificacao">
                <div class="folder-tab">
                    <span class="folder-tab-badge"></span>
                    <span>PASTA VI • CERTIFICAÇÃO DE APROVAÇÃO & ENCAMINHAMENTO PGE/PA</span>
                </div>
                <div class="folder-body">
                    <div class="flex flex-col lg:flex-row lg:items-center justify-between border-b border-slate-800 pb-4 mb-6 gap-4">
                        <div>
                            <span class="text-xs font-mono uppercase text-amber-400 tracking-wider">Conclusão da 4ª Rodada de Auditoria</span>
                            <h2 class="text-2xl font-bold text-white mt-1">Veredito: APROVADO PARA ENCAMINHAMENTO</h2>
                        </div>
                        <span class="inline-flex items-center space-x-2 bg-emerald-950 text-emerald-300 border border-emerald-700 px-4 py-2 rounded-lg text-xs font-bold">
                            <i class="fa-solid fa-circle-check text-emerald-400"></i>
                            <span>NULIDADE ZERO CERTIFICADA</span>
                        </span>
                    </div>

                    <div class="bg-slate-900/90 p-5 rounded-xl border border-slate-800 mb-6">
                        <h3 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-3">Matriz Final de Conformidade Por Eixo</h3>
                        <div class="grid md:grid-cols-5 gap-3 text-xs">
                            <div class="bg-slate-950 p-3 rounded border border-slate-800 text-center">
                                <span class="text-slate-400 block mb-1 font-semibold">1. Eixo Legal</span>
                                <strong class="text-emerald-400 font-bold">✅ 100% Aprovado</strong>
                            </div>
                            <div class="bg-slate-950 p-3 rounded border border-slate-800 text-center">
                                <span class="text-slate-400 block mb-1 font-semibold">2. Eixo Dados</span>
                                <strong class="text-emerald-400 font-bold">✅ 100% Aprovado</strong>
                            </div>
                            <div class="bg-slate-950 p-3 rounded border border-slate-800 text-center">
                                <span class="text-slate-400 block mb-1 font-semibold">3. Eixo Operacional</span>
                                <strong class="text-emerald-400 font-bold">✅ 100% Aprovado</strong>
                            </div>
                            <div class="bg-slate-950 p-3 rounded border border-slate-800 text-center">
                                <span class="text-slate-400 block mb-1 font-semibold">4. Eixo Geográfico</span>
                                <strong class="text-emerald-400 font-bold">✅ 100% Aprovado</strong>
                            </div>
                            <div class="bg-slate-950 p-3 rounded border border-slate-800 text-center">
                                <span class="text-slate-400 block mb-1 font-semibold">5. Eixo ABNT</span>
                                <strong class="text-emerald-400 font-bold">✅ 100% Aprovado</strong>
                            </div>
                        </div>
                    </div>

                    <p class="text-xs text-slate-300 leading-relaxed">
                        O pacote normativo-tecnológico do SEINUC/PA encerrou todas as etapas de revisão jurídica e técnica. O dossiê encontra-se pronto para emissão do parecer conclusivo da <strong class="text-white">Procuradoria-Geral do Estado do Pará (PGE/PA)</strong> e abertura de consulta pública junto à <strong class="text-white">FAMEP</strong>.
                    </p>
                </div>
            </div>

        </div>
    </main>

    <!-- CENTRAL DE DOWNLOADS DOCX (ABNT) & FOOTER -->
    <footer class="bg-[#04080F] border-t border-slate-800 py-16 text-slate-400 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-2xl mx-auto mb-10">
                <h3 class="text-lg font-bold text-white uppercase tracking-wider mb-2">Central de Documentos de Gabinete (.docx)</h3>
                <p class="text-slate-400">Arquivos oficiais formatados rigorosamente conforme a Norma ABNT NBR 14724:2023 e a Lei Complementar nº 95/1998.</p>
            </div>

            <!-- Grid de Downloads -->
            <div class="grid md:grid-cols-3 lg:grid-cols-5 gap-4 mb-12">
                <a href="producao/docs/docx/minuta-decreto-seinuc.docx" class="bg-slate-900 p-4 rounded-xl border border-slate-800 hover:border-sky-500/50 transition-all text-left block group">
                    <i class="fa-solid fa-file-word text-sky-400 text-2xl mb-2 group-hover:scale-110 transition-transform"></i>
                    <strong class="text-white block text-xs mb-1">Minuta de Decreto</strong>
                    <span class="text-[10px] text-slate-500 block">Regulamentação da Lei 10.306/23</span>
                </a>

                <a href="producao/docs/docx/especificacao-modulos-dados-seinuc.docx" class="bg-slate-900 p-4 rounded-xl border border-slate-800 hover:border-emerald-500/50 transition-all text-left block group">
                    <i class="fa-solid fa-file-word text-emerald-400 text-2xl mb-2 group-hover:scale-110 transition-transform"></i>
                    <strong class="text-white block text-xs mb-1">Especificação de Dados</strong>
                    <span class="text-[10px] text-slate-500 block">Schema JSON & Módulos</span>
                </a>

                <a href="producao/docs/docx/minuta-portaria-diretrizes-tecnicas.docx" class="bg-slate-900 p-4 rounded-xl border border-slate-800 hover:border-purple-500/50 transition-all text-left block group">
                    <i class="fa-solid fa-file-word text-purple-400 text-2xl mb-2 group-hover:scale-110 transition-transform"></i>
                    <strong class="text-white block text-xs mb-1">Portaria de Diretrizes</strong>
                    <span class="text-[10px] text-slate-500 block">Diretrizes SEMAS / IDEFLOR</span>
                </a>

                <a href="producao/docs/docx/manual-fluxo-envio-e-triagem.docx" class="bg-slate-900 p-4 rounded-xl border border-slate-800 hover:border-amber-500/50 transition-all text-left block group">
                    <i class="fa-solid fa-file-word text-amber-400 text-2xl mb-2 group-hover:scale-110 transition-transform"></i>
                    <strong class="text-white block text-xs mb-1">Manual de Triagem</strong>
                    <span class="text-[10px] text-slate-500 block">Catálogo de Vícios & LEPA</span>
                </a>

                <a href="producao/docs/docx/especificacao-portal-transparencia-ogc.docx" class="bg-slate-900 p-4 rounded-xl border border-slate-800 hover:border-teal-500/50 transition-all text-left block group">
                    <i class="fa-solid fa-file-word text-teal-400 text-2xl mb-2 group-hover:scale-110 transition-transform"></i>
                    <strong class="text-white block text-xs mb-1">Especificação WebGIS</strong>
                    <span class="text-[10px] text-slate-500 block">Portal Transparência & OGC</span>
                </a>
            </div>

            <div class="border-t border-slate-900 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
                <div class="flex items-center space-x-3">
                    <img src="assets/img/logo_ideflor.png" alt="IDEFLOR-Bio" class="h-6 object-contain opacity-70">
                    <span class="text-slate-600">•</span>
                    <span class="text-[11px] text-slate-500">Governo do Estado do Pará • SEINUC/PA 2026</span>
                </div>
                <div class="text-[11px] text-slate-500">
                    Desenvolvido pela Força-Tarefa de Geotecnologias (NGEO/IDEFLOR-Bio)
                </div>
            </div>
        </div>
    </footer>

    <!-- STACK SCROLL SCRIPT -->
    <script>
        const drawer = document.getElementById('drawer');
        const folders = document.querySelectorAll('.folder');

        function handleScroll() {
            const scrollTop = window.scrollY;
            const triggerPoint = 100;

            folders.forEach((folder, index) => {
                const rect = folder.getBoundingClientRect();
                // Check relative position to apply subtle scale / shadow effect
                if (rect.top <= (100 + index * 48) && rect.top > 50) {
                    folder.style.transform = 'scale(1)';
                } else if (rect.top < 50) {
                    folder.style.transform = 'scale(0.98)';
                } else {
                    folder.style.transform = 'scale(1)';
                }
            });
        }

        window.addEventListener('scroll', handleScroll);
        handleScroll();
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html created successfully.")
