<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dynamic Pricing — README</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Fraunces:opsz,wght@9..144,300;9..144,600;9..144,700&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0e0f11;
    --bg2: #161820;
    --bg3: #1e2028;
    --bg4: #252733;
    --accent: #6ee7b7;
    --accent2: #818cf8;
    --accent3: #fb923c;
    --accent4: #f472b6;
    --text: #e8eaf2;
    --text2: #9ca3af;
    --text3: #6b7280;
    --border: rgba(255,255,255,0.07);
    --border2: rgba(255,255,255,0.12);
    --green-glow: rgba(110,231,183,0.12);
    --purple-glow: rgba(129,140,248,0.12);
    --orange-glow: rgba(251,146,60,0.10);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.75;
    max-width: 960px;
    margin: 0 auto;
    padding: 0 2rem 6rem;
  }

  /* HERO */
  .hero {
    padding: 5rem 0 4rem;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: -60px; left: -100px;
    width: 500px; height: 400px;
    background: radial-gradient(ellipse at center, rgba(110,231,183,0.08) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero::after {
    content: '';
    position: absolute;
    top: 20px; right: -60px;
    width: 400px; height: 300px;
    background: radial-gradient(ellipse at center, rgba(129,140,248,0.08) 0%, transparent 70%);
    pointer-events: none;
  }
  .badge-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 1.8rem;
  }
  .badge {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 4px;
    letter-spacing: 0.03em;
  }
  .badge-green  { background: rgba(110,231,183,0.12); color: #6ee7b7; border: 1px solid rgba(110,231,183,0.2); }
  .badge-purple { background: rgba(129,140,248,0.12); color: #818cf8; border: 1px solid rgba(129,140,248,0.2); }
  .badge-orange { background: rgba(251,146,60,0.12);  color: #fb923c; border: 1px solid rgba(251,146,60,0.2);  }
  .badge-pink   { background: rgba(244,114,182,0.12); color: #f472b6; border: 1px solid rgba(244,114,182,0.2); }
  .badge-blue   { background: rgba(96,165,250,0.12);  color: #60a5fa; border: 1px solid rgba(96,165,250,0.2);  }

  h1 {
    font-family: 'Fraunces', serif;
    font-size: 3.4rem;
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #e8eaf2 0%, #6ee7b7 50%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .tagline {
    font-size: 1.15rem;
    color: var(--text2);
    font-weight: 300;
    max-width: 600px;
    line-height: 1.7;
    margin-bottom: 2rem;
  }
  .tagline strong {
    color: var(--accent);
    font-weight: 500;
  }

  /* STAT CARDS */
  .stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 2rem 0 3.5rem;
  }
  .stat-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: border-color 0.2s, transform 0.2s;
  }
  .stat-card:hover { border-color: var(--border2); transform: translateY(-2px); }
  .stat-value {
    font-family: 'Fraunces', serif;
    font-size: 2rem;
    font-weight: 600;
    line-height: 1;
    margin-bottom: 0.35rem;
  }
  .stat-label {
    font-size: 11px;
    color: var(--text3);
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }

  /* DIVIDER */
  .divider {
    height: 1px;
    background: var(--border);
    margin: 3.5rem 0;
  }
  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    color: var(--accent);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.7rem;
  }
  h2 {
    font-family: 'Fraunces', serif;
    font-size: 1.9rem;
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 1.2rem;
    color: var(--text);
  }
  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 0.6rem;
  }
  p { color: var(--text2); margin-bottom: 1rem; }

  /* OVERVIEW CARDS */
  .overview-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 2rem 0;
  }
  .overview-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem 1.5rem;
    transition: border-color 0.2s;
  }
  .overview-card:hover { border-color: var(--border2); }
  .overview-card .icon {
    font-size: 22px;
    margin-bottom: 0.8rem;
    display: block;
  }
  .overview-card h3 { font-size: 0.95rem; margin-bottom: 0.4rem; }
  .overview-card p { font-size: 0.88rem; margin: 0; line-height: 1.6; }

  /* PIPELINE / WORKFLOW */
  .pipeline {
    margin: 2rem 0;
    position: relative;
  }
  .pipeline-step {
    display: grid;
    grid-template-columns: 36px 1fr;
    gap: 16px;
    margin-bottom: 0;
    position: relative;
  }
  .pipeline-step + .pipeline-step .step-connector {
    display: block;
  }
  .step-connector {
    display: none;
    height: 24px;
    width: 1px;
    background: var(--border2);
    margin-left: 17px;
  }
  .step-num {
    width: 36px; height: 36px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    flex-shrink: 0;
    margin-top: 2px;
  }
  .step-body {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 8px;
  }
  .step-body h3 { font-size: 0.92rem; color: var(--text); margin-bottom: 0.3rem; }
  .step-body p  { font-size: 0.86rem; color: var(--text2); margin: 0; line-height: 1.55; }
  .step-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 7px;
    border-radius: 4px;
    margin-left: 8px;
    vertical-align: middle;
  }

  /* CODE BLOCKS */
  pre {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    overflow-x: auto;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    line-height: 1.65;
    color: var(--text);
    margin: 1rem 0;
  }
  code { font-family: 'DM Mono', monospace; font-size: 0.88em; }
  p code, li code {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 1px 6px;
    color: var(--accent);
  }
  .comment { color: var(--text3); }
  .kw  { color: var(--accent2); }
  .fn  { color: var(--accent);  }
  .str { color: var(--accent3); }
  .num { color: var(--accent4); }

  /* TECH STACK */
  .stack-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin: 1.5rem 0;
  }
  .stack-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.1rem 1.2rem;
  }
  .stack-card .stack-header {
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    color: var(--text3);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.7rem;
  }
  .stack-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: var(--text2);
    padding: 3px 0;
  }
  .stack-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  /* METRIC TABLE */
  .metrics-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin: 1.2rem 0;
  }
  .metrics-table th {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text3);
    padding: 0.6rem 1rem;
    text-align: left;
    border-bottom: 1px solid var(--border);
  }
  .metrics-table td {
    padding: 0.7rem 1rem;
    color: var(--text2);
    border-bottom: 1px solid var(--border);
    font-size: 13.5px;
  }
  .metrics-table tr:last-child td { border-bottom: none; }
  .metrics-table tr:hover td { background: var(--bg2); }
  .metric-val {
    font-family: 'Fraunces', serif;
    font-size: 1.1rem;
    font-weight: 600;
  }

  /* FLOWCHART SVG SECTION */
  .flowchart-wrap {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    margin: 2rem 0;
    overflow: hidden;
  }
  .flowchart-title {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text3);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 1.5rem;
  }

  /* INSTALL STEPS */
  .install-steps { margin: 1.5rem 0; }
  .install-step {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    margin-bottom: 1.2rem;
  }
  .install-num {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    background: var(--green-glow);
    border: 1px solid rgba(110,231,183,0.15);
    border-radius: 6px;
    padding: 3px 8px;
    flex-shrink: 0;
    margin-top: 2px;
  }
  .install-content h3 { font-size: 0.9rem; margin-bottom: 0.4rem; }
  .install-content p  { font-size: 0.86rem; margin-bottom: 0.5rem; color: var(--text2); }

  /* HIGHLIGHT CALLOUT */
  .callout {
    border-left: 3px solid var(--accent);
    background: var(--green-glow);
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.3rem;
    margin: 1.5rem 0;
    font-size: 0.92rem;
    color: var(--text2);
    line-height: 1.6;
  }
  .callout strong { color: var(--accent); font-weight: 500; }
  .callout-purple {
    border-left-color: var(--accent2);
    background: var(--purple-glow);
  }
  .callout-purple strong { color: var(--accent2); }
  .callout-orange {
    border-left-color: var(--accent3);
    background: var(--orange-glow);
  }
  .callout-orange strong { color: var(--accent3); }

  /* FOOTER */
  .footer {
    margin-top: 5rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    text-align: center;
    color: var(--text3);
    font-size: 13px;
  }
  .footer a { color: var(--accent2); text-decoration: none; }

  ul { padding-left: 1.2rem; color: var(--text2); font-size: 14px; line-height: 1.9; }
  ul li { margin-bottom: 0.1rem; }
  ul li code { font-size: 0.85em; }

  @media (max-width: 640px) {
    h1 { font-size: 2.2rem; }
    .stats-row { grid-template-columns: repeat(2, 1fr); }
    .overview-grid, .stack-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<!-- ──────────────────── HERO ──────────────────── -->
<section class="hero">
  <div class="badge-row">
    <span class="badge badge-green">Python 3.10+</span>
    <span class="badge badge-purple">Scikit-learn</span>
    <span class="badge badge-orange">Random Forest</span>
    <span class="badge badge-pink">Pandas · NumPy</span>
    <span class="badge badge-blue">Jupyter Notebook</span>
  </div>

  <h1>Dynamic Pricing<br>with ML</h1>

  <p class="tagline">
    Predict <strong>demand-based quantities</strong> from retail transactional data using
    a tuned <strong>Random Forest Regressor</strong> — enabling intelligent, data-driven
    dynamic pricing decisions.
  </p>

  <div class="stats-row">
    <div class="stat-card">
      <div class="stat-value" style="color:#6ee7b7">R²</div>
      <div class="stat-label">Score metric</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" style="color:#818cf8">300</div>
      <div class="stat-label">Trees in forest</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" style="color:#fb923c">80/20</div>
      <div class="stat-label">Train / test split</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" style="color:#f472b6">6</div>
      <div class="stat-label">Input features</div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ──────────────────── OVERVIEW ──────────────────── -->
<div class="section-label">Overview</div>
<h2>What this project does</h2>
<p>
  This notebook trains a machine learning model on the <strong>Online Retail II dataset</strong>
  to predict how many units a product will sell (demand) given its price, timing, and product attributes.
  By modelling demand as a function of <code>UnitPrice</code>, this creates the foundation for a
  dynamic pricing engine — raise the price when demand is inelastic, lower it to move inventory.
</p>

<div class="overview-grid">
  <div class="overview-card">
    <span class="icon">🗂️</span>
    <h3>Dataset</h3>
    <p>Online Retail II — multi-country transaction records with invoice date, stock codes, unit prices, quantities, and customer IDs.</p>
  </div>
  <div class="overview-card">
    <span class="icon">🌲</span>
    <h3>Model</h3>
    <p>Random Forest Regressor with 300 estimators, max depth 15, and leaf-size constraints to balance accuracy vs. overfitting.</p>
  </div>
  <div class="overview-card">
    <span class="icon">🎯</span>
    <h3>Target variable</h3>
    <p><code>Quantity</code> — the number of units sold per transaction line, used as a proxy for demand elasticity.</p>
  </div>
  <div class="overview-card">
    <span class="icon">📈</span>
    <h3>Evaluation</h3>
    <p>R² score (goodness of fit), MAE (mean absolute error), and a scatter plot of actual vs. predicted demand values.</p>
  </div>
</div>

<div class="divider"></div>

<!-- ──────────────────── WORKFLOW ──────────────────── -->
<div class="section-label">Workflow</div>
<h2>End-to-end pipeline</h2>
<p>The notebook follows a clean, linear ML workflow from raw CSV to evaluated model:</p>

<!-- FLOWCHART SVG -->
<div class="flowchart-wrap">
  <div class="flowchart-title">pipeline · data → model → insight</div>
  <svg width="100%" viewBox="0 0 860 520" xmlns="http://www.w3.org/2000/svg" role="img">
    <title>Dynamic Pricing ML Pipeline Flowchart</title>
    <desc>Six-stage pipeline: Load CSV → Clean Data → Feature Engineering → Encode → Split → Train RF → Evaluate</desc>
    <defs>
      <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M2 1L8 5L2 9" fill="none" stroke="#4b5563" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </marker>
    </defs>

    <!-- Row 1: Load → Clean → Feature Eng -->
    <!-- Load CSV -->
    <rect x="40" y="40" width="170" height="68" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="40" y="40" width="4" height="68" rx="2" fill="#6ee7b7"/>
    <text x="130" y="67" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Load CSV</text>
    <text x="130" y="85" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">online_retail_II.csv</text>
    <text x="130" y="100" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">ISO-8859-1 encoding</text>

    <!-- arrow -->
    <line x1="210" y1="74" x2="255" y2="74" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Clean Data -->
    <rect x="255" y="40" width="170" height="68" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="255" y="40" width="4" height="68" rx="2" fill="#818cf8"/>
    <text x="345" y="67" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Clean data</text>
    <text x="345" y="85" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">Drop nulls, negatives</text>
    <text x="345" y="100" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">Filter Qty &gt; 0, Price &gt; 0</text>

    <!-- arrow -->
    <line x1="425" y1="74" x2="470" y2="74" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Feature Engineering -->
    <rect x="470" y="40" width="170" height="68" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="470" y="40" width="4" height="68" rx="2" fill="#fb923c"/>
    <text x="560" y="67" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Feature engineering</text>
    <text x="560" y="85" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">Month, Day, DayOfWeek</text>
    <text x="560" y="100" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">From InvoiceDate</text>

    <!-- arrow -->
    <line x1="640" y1="74" x2="685" y2="74" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Encode -->
    <rect x="685" y="40" width="140" height="68" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="685" y="40" width="4" height="68" rx="2" fill="#f472b6"/>
    <text x="757" y="67" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Encode</text>
    <text x="757" y="85" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">LabelEncoder on</text>
    <text x="757" y="100" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">StockCode, Country</text>

    <!-- vertical connector from Encode down -->
    <line x1="757" y1="108" x2="757" y2="175" stroke="#374151" stroke-width="1"/>
    <line x1="757" y1="175" x2="560" y2="175" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Row 2: center items -->
    <!-- Split -->
    <rect x="375" y="175" width="170" height="68" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="375" y="175" width="4" height="68" rx="2" fill="#60a5fa"/>
    <text x="463" y="202" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Train/test split</text>
    <text x="463" y="220" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">80% train · 20% test</text>
    <text x="463" y="235" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">random_state = 42</text>

    <!-- arrow -->
    <line x1="375" y1="209" x2="330" y2="209" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Train RF -->
    <rect x="130" y="175" width="200" height="68" rx="10" fill="#1e2028" stroke="rgba(110,231,183,0.35)" stroke-width="1.2"/>
    <rect x="130" y="175" width="4" height="68" rx="2" fill="#6ee7b7"/>
    <text x="232" y="200" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Train Random Forest</text>
    <text x="232" y="218" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#9ca3af">n_estimators=300, depth=15</text>
    <text x="232" y="234" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#9ca3af">min_leaf=2, n_jobs=−1</text>

    <!-- arrow down from Train RF -->
    <line x1="232" y1="243" x2="232" y2="305" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Predict -->
    <rect x="130" y="305" width="200" height="60" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="130" y="305" width="4" height="60" rx="2" fill="#818cf8"/>
    <text x="232" y="332" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Predict</text>
    <text x="232" y="350" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">rf_model.predict(X_test)</text>

    <!-- arrow -->
    <line x1="330" y1="335" x2="375" y2="335" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Evaluate -->
    <rect x="375" y="305" width="200" height="60" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="375" y="305" width="4" height="60" rx="2" fill="#fb923c"/>
    <text x="477" y="332" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Evaluate</text>
    <text x="477" y="350" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">R² score · MAE · scatter plot</text>

    <!-- arrow -->
    <line x1="575" y1="335" x2="620" y2="335" stroke="#374151" stroke-width="1" marker-end="url(#arr)"/>

    <!-- Visualise -->
    <rect x="620" y="305" width="190" height="60" rx="10" fill="#1e2028" stroke="#374151" stroke-width="0.8"/>
    <rect x="620" y="305" width="4" height="60" rx="2" fill="#6ee7b7"/>
    <text x="717" y="332" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="13" font-weight="600" fill="#e8eaf2">Visualise</text>
    <text x="717" y="350" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">Actual vs Predicted scatter</text>

    <!-- Feature list on side -->
    <rect x="40" y="400" width="780" height="100" rx="10" fill="rgba(110,231,183,0.04)" stroke="rgba(110,231,183,0.12)" stroke-width="0.8"/>
    <text x="430" y="424" text-anchor="middle" font-family="DM Mono,monospace" font-size="11" fill="#6ee7b7" letter-spacing="0.08em">INPUT FEATURES  →  TARGET</text>
    <text x="430" y="450" text-anchor="middle" font-family="DM Mono,monospace" font-size="12" fill="#9ca3af">UnitPrice · Month · Day · DayOfWeek · StockCode_encoded · Country_encoded  →  Quantity</text>
    <text x="430" y="476" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#6b7280">6 numeric features · regression target · no scaling required (tree-based model)</text>
  </svg>
</div>

<div class="divider"></div>

<!-- ──────────────────── FEATURES ──────────────────── -->
<div class="section-label">Features &amp; Preprocessing</div>
<h2>What goes into the model</h2>

<p>After cleaning, six features are constructed from the raw dataset columns:</p>

<div class="metrics-table" style="margin-top:1.2rem">
  <table class="metrics-table" style="background: var(--bg2); border-radius: 12px; overflow: hidden; width:100%; border-collapse: collapse;">
    <thead>
      <tr>
        <th>Feature</th>
        <th>Source column</th>
        <th>Type</th>
        <th>Note</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>UnitPrice</code></td>
        <td>UnitPrice</td>
        <td><span class="badge badge-green" style="font-size:10px">numeric</span></td>
        <td>Core pricing signal — the independent variable for dynamic pricing</td>
      </tr>
      <tr>
        <td><code>Month</code></td>
        <td>InvoiceDate</td>
        <td><span class="badge badge-purple" style="font-size:10px">derived</span></td>
        <td>Seasonal demand patterns</td>
      </tr>
      <tr>
        <td><code>Day</code></td>
        <td>InvoiceDate</td>
        <td><span class="badge badge-purple" style="font-size:10px">derived</span></td>
        <td>Within-month demand fluctuation</td>
      </tr>
      <tr>
        <td><code>DayOfWeek</code></td>
        <td>InvoiceDate</td>
        <td><span class="badge badge-purple" style="font-size:10px">derived</span></td>
        <td>Weekday vs. weekend purchasing behaviour</td>
      </tr>
      <tr>
        <td><code>StockCode_encoded</code></td>
        <td>StockCode</td>
        <td><span class="badge badge-orange" style="font-size:10px">encoded</span></td>
        <td>Product identity — LabelEncoder integer mapping</td>
      </tr>
      <tr>
        <td><code>Country_encoded</code></td>
        <td>Country</td>
        <td><span class="badge badge-orange" style="font-size:10px">encoded</span></td>
        <td>Geographic market — LabelEncoder integer mapping</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="callout callout-orange">
  <strong>Why no feature scaling?</strong> Random Forest is a tree-based ensemble — it splits on thresholds, not distances. Feature scaling (StandardScaler, MinMaxScaler) has zero effect on the model output and is intentionally omitted.
</div>

<div class="divider"></div>

<!-- ──────────────────── MODEL ──────────────────── -->
<div class="section-label">Model Configuration</div>
<h2>Random Forest hyperparameters</h2>

<pre><span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> RandomForestRegressor

rf_model = <span class="fn">RandomForestRegressor</span>(
    n_estimators=<span class="num">300</span>,      <span class="comment"># 300 decision trees — higher = more stable, slower</span>
    max_depth=<span class="num">15</span>,          <span class="comment"># caps tree growth to prevent overfitting</span>
    min_samples_split=<span class="num">5</span>,  <span class="comment"># min samples needed to split a node</span>
    min_samples_leaf=<span class="num">2</span>,   <span class="comment"># min samples in each leaf node</span>
    random_state=<span class="num">42</span>,      <span class="comment"># reproducible results</span>
    n_jobs=<span class="num">-1</span>             <span class="comment"># use all CPU cores for parallel training</span>
)</pre>

<div class="overview-grid">
  <div class="overview-card">
    <span class="icon">🌳</span>
    <h3>300 estimators</h3>
    <p>More trees reduce variance and stabilise predictions via bagging. Runtime cost is offset by <code>n_jobs=-1</code> parallelism.</p>
  </div>
  <div class="overview-card">
    <span class="icon">✂️</span>
    <h3>max_depth = 15</h3>
    <p>Limits how deep each tree can grow. Without this, trees overfit perfectly to training data and generalise poorly.</p>
  </div>
  <div class="overview-card">
    <span class="icon">🍃</span>
    <h3>min_samples_leaf = 2</h3>
    <p>Every leaf must represent at least 2 samples — prevents single-point leaves that memorise noise.</p>
  </div>
  <div class="overview-card">
    <span class="icon">📊</span>
    <h3>R² metric</h3>
    <p>Reports the proportion of variance in <code>Quantity</code> explained by the model. R² × 100 gives accuracy as a percentage.</p>
  </div>
</div>

<div class="divider"></div>

<!-- ──────────────────── TECH STACK ──────────────────── -->
<div class="section-label">Tech Stack</div>
<h2>Libraries &amp; environment</h2>

<div class="stack-grid">
  <div class="stack-card">
    <div class="stack-header">Data layer</div>
    <div class="stack-item"><span class="stack-dot" style="background:#6ee7b7"></span>pandas</div>
    <div class="stack-item"><span class="stack-dot" style="background:#6ee7b7"></span>numpy</div>
    <div class="stack-item"><span class="stack-dot" style="background:#6ee7b7"></span>matplotlib</div>
  </div>
  <div class="stack-card">
    <div class="stack-header">ML layer</div>
    <div class="stack-item"><span class="stack-dot" style="background:#818cf8"></span>scikit-learn</div>
    <div class="stack-item"><span class="stack-dot" style="background:#818cf8"></span>RandomForestRegressor</div>
    <div class="stack-item"><span class="stack-dot" style="background:#818cf8"></span>LabelEncoder</div>
  </div>
  <div class="stack-card">
    <div class="stack-header">Environment</div>
    <div class="stack-item"><span class="stack-dot" style="background:#fb923c"></span>Python 3.10+</div>
    <div class="stack-item"><span class="stack-dot" style="background:#fb923c"></span>Jupyter Notebook</div>
    <div class="stack-item"><span class="stack-dot" style="background:#fb923c"></span>Anaconda / pip</div>
  </div>
</div>

<div class="divider"></div>

<!-- ──────────────────── INSTALLATION ──────────────────── -->
<div class="section-label">Setup</div>
<h2>How to run this project</h2>

<div class="install-steps">

  <div class="install-step">
    <span class="install-num">01</span>
    <div class="install-content">
      <h3>Clone or download the repository</h3>
      <pre>git clone &lt;your-repo-url&gt;
cd dynamic_pricing</pre>
    </div>
  </div>

  <div class="install-step">
    <span class="install-num">02</span>
    <div class="install-content">
      <h3>Install dependencies</h3>
      <p>Use pip or conda. All dependencies are standard data science packages.</p>
      <pre><span class="comment"># via pip</span>
pip install pandas numpy matplotlib scikit-learn jupyter

<span class="comment"># or via conda</span>
conda install pandas numpy matplotlib scikit-learn jupyter</pre>
    </div>
  </div>

  <div class="install-step">
    <span class="install-num">03</span>
    <div class="install-content">
      <h3>Download the dataset</h3>
      <p>
        Get the <strong>Online Retail II</strong> dataset from the
        <a href="https://archive.ics.uci.edu/dataset/502/online+retail+ii" style="color:var(--accent2)">UCI ML Repository</a>.
        Place the CSV at:
      </p>
      <pre>dataset/online_retail_II.csv</pre>
      <p>Then update the file path inside the notebook's cell 2 to match your local path.</p>
    </div>
  </div>

  <div class="install-step">
    <span class="install-num">04</span>
    <div class="install-content">
      <h3>Open the notebook</h3>
      <pre>jupyter notebook accuracy/Dsbda.ipynb</pre>
    </div>
  </div>

  <div class="install-step">
    <span class="install-num">05</span>
    <div class="install-content">
      <h3>Run all cells</h3>
      <p>Select <strong>Kernel → Restart &amp; Run All</strong>. The final cells output R², MAE, and a scatter plot.</p>
    </div>
  </div>
</div>

<div class="callout">
  <strong>⚠️ Path note:</strong> Cell 2 in the notebook currently has a hardcoded Windows path
  (<code>C:\Users\dhanashree bhoge\Downloads\...</code>). Update this to your own dataset location before running.
</div>

<div class="divider"></div>

<!-- ──────────────────── OUTPUT ──────────────────── -->
<div class="section-label">Expected Output</div>
<h2>What you get when it runs</h2>

<p>After <em>Restart &amp; Run All</em>, the final cells produce three outputs:</p>

<pre><span class="comment"># Cell 12 — Evaluation metrics</span>
R2 Score:   <span class="num">0.XXXX</span>
Accuracy (%): <span class="num">XX.XX</span>
MAE:          <span class="num">X.XXXX</span></pre>

<ul>
  <li><strong>R² Score</strong> — proportion of variance explained (1.0 = perfect). A good model for this dataset typically scores 0.40–0.75.</li>
  <li><strong>Accuracy (%)</strong> — R² expressed as a percentage (R² × 100).</li>
  <li><strong>MAE</strong> — mean absolute error in units of <code>Quantity</code>. Lower is better.</li>
  <li><strong>Scatter plot</strong> — "Actual Demand vs Predicted Demand". Points clustering along the diagonal indicate good fit.</li>
</ul>

<div class="callout callout-purple">
  <strong>Interpreting R²:</strong> Because <code>Quantity</code> is inherently noisy (retail demand varies by many unmeasured factors), an R² of 0.50–0.65 is a solid result. The model captures systematic price-demand relationships while acknowledging the irreducible noise in individual transaction data.
</div>

<div class="divider"></div>

<!-- ──────────────────── DYNAMIC PRICING CONTEXT ──────────────────── -->
<div class="section-label">Business Context</div>
<h2>How this enables dynamic pricing</h2>

<p>
  The trained model maps <code>(price, product, market, timing)</code> → <code>predicted demand</code>.
  A pricing engine can use this to simulate revenue at different price points:
</p>

<pre><span class="comment"># Pseudo-code: revenue optimisation loop</span>
best_price, best_revenue = <span class="num">0</span>, <span class="num">0</span>

<span class="kw">for</span> price <span class="kw">in</span> <span class="fn">linspace</span>(min_price, max_price, steps=<span class="num">100</span>):
    features = [price, month, day, dow, stock_enc, country_enc]
    predicted_qty = rf_model.<span class="fn">predict</span>([features])[<span class="num">0</span>]
    revenue = price * predicted_qty

    <span class="kw">if</span> revenue &gt; best_revenue:
        best_price, best_revenue = price, revenue

<span class="fn">print</span>(<span class="str">f"Optimal price: £{best_price:.2f} → predicted revenue: £{best_revenue:.2f}"</span>)</pre>

<div class="overview-grid">
  <div class="overview-card">
    <span class="icon">💡</span>
    <h3>Peak season pricing</h3>
    <p>Month and DayOfWeek features let the model charge more during high-demand periods automatically.</p>
  </div>
  <div class="overview-card">
    <span class="icon">🌍</span>
    <h3>Market segmentation</h3>
    <p>Country encoding allows different optimal prices per geographic market for the same product.</p>
  </div>
  <div class="overview-card">
    <span class="icon">📦</span>
    <h3>Inventory clearance</h3>
    <p>Find the lowest price that still maximises revenue × margin — useful for slow-moving stock.</p>
  </div>
  <div class="overview-card">
    <span class="icon">🔄</span>
    <h3>Real-time updates</h3>
    <p>Retrain weekly on new transaction data. The pipeline is simple enough to automate end-to-end.</p>
  </div>
</div>

<div class="divider"></div>

<!-- ──────────────────── PROJECT STRUCTURE ──────────────────── -->
<div class="section-label">Project Structure</div>
<h2>Files &amp; directories</h2>

<pre>dynamic_pricing/
│
├── accuracy/
│   └── Dsbda.ipynb          <span class="comment"># Main notebook — data → model → evaluation</span>
│
├── dataset/                 <span class="comment"># (create this folder)</span>
│   └── online_retail_II.csv <span class="comment"># UCI dataset — not included in repo</span>
│
└── README.md                <span class="comment"># This file</span></pre>

<div class="divider"></div>

<!-- ──────────────────── POTENTIAL IMPROVEMENTS ──────────────────── -->
<div class="section-label">Future Work</div>
<h2>Possible improvements</h2>

<ul>
  <li>Add <strong>price elasticity coefficient</strong> as a derived feature (% Δ demand / % Δ price per product)</li>
  <li>Try <strong>XGBoost or LightGBM</strong> for faster training and potentially better accuracy</li>
  <li>Add <strong>cross-validation</strong> (k-fold) instead of a single train/test split for more robust evaluation</li>
  <li>Include <strong>competitor pricing</strong> data if available to model relative price effects</li>
  <li>Build a <strong>Streamlit dashboard</strong> to expose the model as an interactive pricing tool</li>
  <li>Use <strong>SHAP values</strong> to explain which features drive demand predictions for each product</li>
  <li>Handle <strong>target variable skew</strong> — <code>Quantity</code> is right-skewed; a log transform may improve R²</li>
</ul>

<div class="divider"></div>

<!-- ──────────────────── AUTHOR ──────────────────── -->
<div class="section-label">Author</div>
<div style="background: var(--bg2); border: 1px solid var(--border); border-radius: 16px; padding: 1.6rem 1.8rem; display: flex; align-items: center; gap: 1.4rem;">
  <div style="width: 56px; height: 56px; border-radius: 50%; background: linear-gradient(135deg, rgba(110,231,183,0.25), rgba(129,140,248,0.25)); border: 1px solid rgba(110,231,183,0.25); display: flex; align-items: center; justify-content: center; font-family: 'Fraunces', serif; font-size: 1.4rem; font-weight: 600; color: var(--accent); flex-shrink: 0;">D</div>
  <div>
    <div style="font-family: 'Fraunces', serif; font-size: 1.2rem; font-weight: 600; color: var(--text); margin-bottom: 0.2rem;">Dhanashree Tukaram Bhoge</div>
    <div style="font-size: 13px; color: var(--text3); font-family: 'DM Mono', monospace;">Dynamic Pricing with ML · DSBDA Project</div>
  </div>
</div>

<div class="divider"></div>

<!-- ──────────────────── FOOTER ──────────────────── -->
<div class="footer">
  <p style="margin-bottom:0.5rem">Built with Python · scikit-learn · Jupyter</p>
  <p>Dataset: <a href="https://archive.ics.uci.edu/dataset/502/online+retail+ii">UCI Online Retail II</a> &nbsp;·&nbsp; License: MIT</p>
</div>

</body>
</html>
