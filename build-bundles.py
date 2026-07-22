#!/usr/bin/env python3
"""Generate the three published artifact bundles from source docs.

Each bundle is a shell page embedding source docs as auto-resizing
seamless iframes (srcdoc), so per-doc styles and scripts stay isolated
and interactive demos keep working. Run after editing any source doc:

    python3 build-bundles.py
"""
import html

BUNDLES = [
    {
        'out': 'ATOM分享模块-产品与架构.html',
        'title': 'ATOM 分享模块 · 产品与架构',
        'emoji': '⚛',
        'sub': '架构设计框架（评审视觉版） + P0 PRD 与交互 Demo。源文件：架构-ATOM分享模块设计框架 · PRD-ATOM分享模块与交互设计',
        'parts': [
            ('01 · 架构设计框架', '架构-ATOM分享模块设计框架.html'),
            ('02 · PRD 与交互设计（P0）', 'PRD-ATOM分享模块与交互设计.html'),
        ],
    },
    {
        'out': 'ATOM分享模块-设计规范.html',
        'title': 'ATOM 分享模块 · 设计规范',
        'emoji': '📏',
        'sub': '网格标准与成图样例 + 分享模板总目录（19+4）。源文件：规范-网格标准与成图样例 · 规范-分享模板总目录',
        'parts': [
            ('01 · 网格标准与成图样例', '规范-网格标准与成图样例.html'),
            ('02 · 分享模板总目录', '规范-分享模板总目录.html'),
        ],
    },
    {
        'out': 'ATOM分享模块-原子库.html',
        'title': 'ATOM 分享模块 · 原子库',
        'emoji': '📐',
        'sub': '全原子低保真线框总板 + 逐个深钻的原子规格（当前：B2）。源文件：原子-低保真线框总板 · 原子-*规格',
        'parts': [
            ('01 · 低保真线框总板（22+7 原子）', '原子-低保真线框总板.html'),
            ('02 · 原子规格 · B2 肌肉热力图', '原子-B2肌肉热力图规格.html'),
        ],
    },
]

SHELL = '''<title>{title}</title>
<style>
  :root{{--bg:#F6F7F4;--surface:#FFFFFF;--ink:#141712;--muted:#5C645A;--faint:#939C8F;
    --line:#E4E8E1;--acc:#6FCC1B;--acc-ink:#47940B;--on-acc:#10240A;
    --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
    --cjk:"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;}}
  @media (prefers-color-scheme:dark){{:root{{--bg:#0F110E;--surface:#161A15;--ink:#E9ECE6;--muted:#9AA396;
    --faint:#707A6B;--line:#262B24;--acc:#A3E635;--acc-ink:#BEF264;--on-acc:#10240A;}}}}
  :root[data-theme="light"]{{--bg:#F6F7F4;--surface:#FFFFFF;--ink:#141712;--muted:#5C645A;--faint:#939C8F;--line:#E4E8E1;--acc:#6FCC1B;--acc-ink:#47940B;}}
  :root[data-theme="dark"]{{--bg:#0F110E;--surface:#161A15;--ink:#E9ECE6;--muted:#9AA396;--faint:#707A6B;--line:#262B24;--acc:#A3E635;--acc-ink:#BEF264;}}
  *{{box-sizing:border-box}}
  body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--cjk);}}
  .topbar{{position:sticky;top:0;z-index:20;background:var(--surface);border-bottom:1px solid var(--line);
    display:flex;align-items:center;gap:14px;padding:10px 20px;flex-wrap:wrap;}}
  .topbar .brand{{font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.1em;}}
  .topbar .brand em{{font-style:normal;color:var(--acc-ink);}}
  .topbar nav{{display:flex;gap:8px;margin-left:auto;flex-wrap:wrap;}}
  .topbar a{{font-family:var(--mono);font-size:11.5px;color:var(--muted);text-decoration:none;
    border:1px solid var(--line);border-radius:2px;padding:4px 10px;}}
  .topbar a:hover{{border-color:var(--acc);color:var(--ink);}}
  .sechead{{max-width:1160px;margin:0 auto;padding:26px 20px 0;}}
  .sechead .kicker{{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
    color:var(--acc-ink);font-weight:700;display:flex;align-items:center;gap:10px;}}
  .sechead .kicker::before{{content:"";width:22px;height:2px;background:var(--acc);}}
  .subnote{{max-width:1160px;margin:0 auto;padding:8px 20px 0;color:var(--faint);font-family:var(--mono);font-size:11px;}}
  iframe{{display:block;width:100%;border:0;}}
  footer{{max-width:1160px;margin:0 auto;padding:24px 20px 48px;color:var(--faint);font-family:var(--mono);font-size:11px;
    border-top:1px solid var(--line);}}
</style>
<div class="topbar"><span class="brand">{emoji} <em>BODY PARK ATOM</em> · {title_short}</span><nav>{nav}</nav></div>
<div class="subnote">{sub} · 合集由 build-bundles.py 生成，修改请编辑源文件</div>
{sections}
<footer>{title} · 单文件合集 · 内部各节交互均可用</footer>
<script>
function fit(f){{try{{var d=f.contentDocument;if(!d||!d.documentElement)return;
  f.style.height=Math.max(d.documentElement.scrollHeight,d.body?d.body.scrollHeight:0)+'px';}}catch(e){{}}}}
document.querySelectorAll('iframe').forEach(function(f){{
  f.addEventListener('load',function(){{fit(f);
    try{{new ResizeObserver(function(){{fit(f);}}).observe(f.contentDocument.documentElement);}}catch(e){{}}
    setTimeout(function(){{fit(f);}},600);setTimeout(function(){{fit(f);}},2000);}});
}});
</script>
'''

for b in BUNDLES:
    nav, sections = [], []
    for i, (label, path) in enumerate(b['parts']):
        doc = open(path, encoding='utf-8').read()
        anchor = 'part%d' % (i + 1)
        nav.append('<a href="#%s">%s</a>' % (anchor, label.split('·', 1)[1].strip() if '·' in label else label))
        sections.append(
            '<div class="sechead" id="%s"><div class="kicker">%s</div></div>\n'
            '<iframe title="%s" srcdoc="%s"></iframe>' % (anchor, label, label, html.escape(doc, quote=True))
        )
    out = SHELL.format(title=b['title'], title_short=b['title'].split('·')[-1].strip(),
                       emoji=b['emoji'], sub=b['sub'], nav=''.join(nav), sections='\n'.join(sections))
    open(b['out'], 'w', encoding='utf-8').write(out)
    print('built', b['out'], len(out) // 1024, 'KB')
