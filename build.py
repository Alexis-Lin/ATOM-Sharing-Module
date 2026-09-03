#!/usr/bin/env python3
"""Build the four root-level deliverables from sources/.

Rule: 根目录 = 给人看的（生成物）· sources/ = 给人改的（源文件）
Run after editing anything in sources/:

    python3 build.py
"""
import html, pathlib

SRC = pathlib.Path('sources')

DOCS = [
    {
        'out': '00-启动会-讨论文档.html',
        'title': '启动会 · 分享模块讨论',
        'emoji': '🎤',
        'who': '会议演示',
        'sub': '幻灯片式讨论文档：13 页，← → 翻页、M 开目录，内嵌可点 demo。已决策与待拍板分开标注。',
        'parts': [('启动会讨论文档', '启动会-讨论文档.html')],
        'raw': True,   # 幻灯片需要整屏，不套 iframe 外壳，源文件直接复制
    },
    {
        'out': '01-总览-分享体系.html',
        'title': '总览 · ATOM 分享体系',
        'emoji': '🎯',
        'who': '全员 · 对外介绍',
        'sub': '从这里开始读：体系怎么做 · 分享路径与四大载体 · 报告与洞察 · 分享样式。多处可点击交互。',
        'parts': [('分享体系总览', '总览-分享体系解释.html')],
    },
    {
        'out': '02-PRD-P0课后报告分享.html',
        'title': 'PRD · P0 课后报告分享',
        'emoji': '📋',
        'who': 'PM · 评审',
        'sub': '第一个可上线切片的需求单：FR 清单、边界 case、埋点、排期，含可交互逻辑图与分享编辑器模拟。',
        'parts': [('需求与交互设计', 'PRD-需求与交互设计.html')],
    },
    {
        'out': '03-规范-网格与模板.html',
        'title': '规范 · 网格与模板',
        'emoji': '📏',
        'who': '设计 · 工程',
        'sub': '画布网格标准（尺寸/预算/间距/字阶/出血权）+ 8 张成图样例 + 23+4 个模板的原子账本。',
        'parts': [
            ('网格标准与成图样例', '规范-网格标准与成图样例.html'),
            ('分享模板总目录', '规范-分享模板总目录.html'),
        ],
    },
    {
        'out': '04-设计-原子与报告.html',
        'title': '设计 · 原子与报告',
        'emoji': '📐',
        'who': '设计',
        'sub': '24+7 个原子的低保真线框 · 单原子深钻规格 · 课后报告与洞察引擎的设计讨论稿。',
        'parts': [
            ('原子低保真线框总板', '原子-低保真线框总板.html'),
            ('原子规格 · B2 肌肉热力图', '原子-B2肌肉热力图规格.html'),
            ('深钻 · 课后报告与洞察设计 ★', '深钻-课后报告与洞察设计.html'),
        ],
    },
    {
        'out': '05-推荐-邀请分享与归因.html',
        'title': '推荐 · 邀请分享与归因',
        'emoji': '🔗',
        'who': 'PM · 增长 · 工程',
        'sub': '邀请好友买硬件：电商优先的归因五级阶梯、图片+H5 两种分享形式、CN/GLOBAL 双 Profile，含可交互链路模拟器。',
        'parts': [('邀请分享与归因设计', '推荐-邀请分享与归因设计.html')],
    },
    {
        'out': '06-Demo-邀请页交互.html',
        'title': 'Demo · 邀请页交互',
        'emoji': '📱',
        'who': 'PM · 设计',
        'sub': '低保真可点 Demo：邀请页一屏三事（怎么做 / 一键分享 / 数据与权益），可模拟好友点击、下单、激活、退货看数字与权益怎么动。',
        'parts': [('邀请页交互 Demo', 'Demo-邀请页交互.html')],
    },
    {
        'out': '07-原型-邀请全链路线框.html',
        'title': '原型 · 邀请全链路线框',
        'emoji': '🧩',
        'who': '设计 · PM · 硬件',
        'sub': '可交互低保真线框：邀请人手机 / 好友手机 / Atom 466×466 圆屏三条泳道，二十个界面全部可点走通，含每屏要素与去向。',
        'parts': [('邀请全链路线框原型', '原型-邀请全链路线框.html')],
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
    display:flex;align-items:center;gap:12px;padding:9px 20px;flex-wrap:wrap;}}
  .topbar .bd{{font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.1em;}}
  .topbar .bd em{{font-style:normal;color:var(--acc-ink);}}
  .topbar .who{{font-family:var(--mono);font-size:10.5px;color:var(--on-acc);background:var(--acc);
    border-radius:2px;padding:2px 8px;font-weight:700;}}
  .topbar nav{{display:flex;gap:6px;margin-left:auto;flex-wrap:wrap;}}
  .topbar a{{font-family:var(--mono);font-size:11.5px;color:var(--muted);text-decoration:none;
    border:1px solid var(--line);border-radius:2px;padding:4px 10px;}}
  .topbar a:hover{{border-color:var(--acc);color:var(--ink);}}
  .subnote{{max-width:1160px;margin:0 auto;padding:14px 20px 0;color:var(--muted);font-size:13.5px;line-height:1.65;}}
  .srcnote{{max-width:1160px;margin:0 auto;padding:6px 20px 0;color:var(--faint);font-family:var(--mono);font-size:11px;}}
  .sechead{{max-width:1160px;margin:0 auto;padding:26px 20px 0;}}
  .sechead .kicker{{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
    color:var(--acc-ink);font-weight:700;display:flex;align-items:center;gap:10px;}}
  .sechead .kicker::before{{content:"";width:22px;height:2px;background:var(--acc);}}
  iframe{{display:block;width:100%;border:0;}}
  footer{{max-width:1160px;margin:0 auto;padding:22px 20px 48px;border-top:1px solid var(--line);
    color:var(--faint);font-family:var(--mono);font-size:11px;line-height:1.9;}}
  footer b{{color:var(--muted);}}
</style>
<div class="topbar"><span class="bd">{emoji} <em>BODY PARK ATOM</em> · {short}</span><span class="who">{who}</span>{nav}</div>
<div class="subnote">{sub}</div>
<div class="srcnote">源文件：{srcs} · 本文件由 build.py 生成，修改请编辑 sources/ 后重新构建</div>
{sections}
<footer><b>阅读顺序</b> — 01 总览（从这读起）· 02 PRD（P0 需求）· 03 规范（网格与模板）· 04 设计（原子与报告）· README.md（架构总纲 · 事实源）</footer>
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

for d in DOCS:
    if d.get('raw'):
        body = (SRC / d['parts'][0][1]).read_text(encoding='utf-8')
        pathlib.Path(d['out']).write_text(body, encoding='utf-8')
        print('built %-30s %4d KB  ← raw（整屏幻灯片，不套外壳）' % (d['out'], len(body) // 1024))
        continue
    multi = len(d['parts']) > 1
    nav, sections, srcs = [], [], []
    for i, (label, fname) in enumerate(d['parts']):
        doc = (SRC / fname).read_text(encoding='utf-8')
        anchor = 'part%d' % (i + 1)
        srcs.append('sources/' + fname)
        if multi:
            nav.append('<a href="#%s">%s</a>' % (anchor, label))
            sections.append('<div class="sechead" id="%s"><div class="kicker">0%d · %s</div></div>'
                            % (anchor, i + 1, label))
        sections.append('<iframe title="%s" srcdoc="%s"></iframe>'
                        % (label, html.escape(doc, quote=True)))
    out = SHELL.format(
        title=d['title'], short=d['title'].split('·')[-1].strip(), emoji=d['emoji'],
        who=d['who'], sub=d['sub'], srcs=' · '.join(srcs),
        nav=('<nav>' + ''.join(nav) + '</nav>') if multi else '',
        sections='\n'.join(sections))
    pathlib.Path(d['out']).write_text(out, encoding='utf-8')
    print('built %-30s %4d KB  ← %d part(s)' % (d['out'], len(out) // 1024, len(d['parts'])))
