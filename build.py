#!/usr/bin/env python3
"""Génère le site bilingue de Carinne Leibovici : français à la racine, anglais dans /en/.

Chaque texte s'écrit t("français", "English"). Lancer : python3 build.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
W = "https://static.wixstatic.com/media/"
OLD = "https://www.carinneleibovici.com"
SITE = "https://www.carinneleibovici.com"
EMAIL = "carinne.leibovici@icloud.com"
WHATSAPP = "+33 6 24 90 33 25"
WA_LINK = "https://wa.me/33624903325"
FB = "https://www.facebook.com/carinnepsychologue/"
IG = "https://www.instagram.com/carinne.leibovici/"
YT = "https://www.youtube.com/channel/UCy7ONifkKb8_cWLWgjub7Mg"

LANG = "fr"


def t(fr, en):
    return fr if LANG == "fr" else en


def out_dir():
    return ROOT if LANG == "fr" else ROOT / "en"


def nav():
    return [
        ("index.html", t("Accueil", "Home")),
        ("qui-suis-je.html", t("Qui suis-je ?", "About")),
        ("therapies.html", t("Thérapies", "Therapies")),
        ("presse.html", t("TV & articles", "TV & articles")),
        ("faq.html", "FAQ"),
    ]


# Motifs : 1 cercle = une personne, 2 = un couple, 3 = une famille, globe = en ligne
MOTIFS = {
    "individuelle": '<svg class="motif" viewBox="0 0 72 44" aria-hidden="true"><circle class="fill" cx="36" cy="22" r="17"/><circle cx="36" cy="22" r="17"/></svg>',
    "couple": '<svg class="motif" viewBox="0 0 72 44" aria-hidden="true"><circle class="fill" cx="28" cy="22" r="16"/><circle cx="28" cy="22" r="16"/><circle cx="44" cy="22" r="16"/></svg>',
    "familiale": '<svg class="motif" viewBox="0 0 72 44" aria-hidden="true"><circle class="fill" cx="22" cy="24" r="14"/><circle cx="22" cy="24" r="14"/><circle cx="50" cy="24" r="14"/><circle cx="36" cy="18" r="12"/></svg>',
    "en-ligne": '<svg class="motif" viewBox="0 0 72 44" aria-hidden="true"><circle class="fill" cx="36" cy="22" r="18"/><circle cx="36" cy="22" r="18"/><ellipse cx="36" cy="22" rx="8" ry="18" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M18 22h36" stroke="currentColor" stroke-width="1.6"/></svg>',
}


def therapies():
    return [
        ("therapie-individuelle.html", "individuelle", t("Thérapie individuelle", "Individual therapy"),
         t("Un espace rien que pour vous, pour comprendre et surmonter vos difficultés émotionnelles et psychologiques.",
           "A space just for you, to understand and overcome your emotional and psychological difficulties.")),
        ("therapie-de-couple.html", "couple", t("Thérapie de couple", "Couples therapy"),
         t("Un cadre sécurisé pour vous et votre partenaire : renouer le dialogue, traverser les conflits, renforcer la relation.",
           "A safe space for you and your partner to talk again, work through conflict and strengthen your relationship.")),
        ("therapie-familiale.html", "familiale", t("Thérapie familiale", "Family therapy"),
         t("Un lieu pour améliorer la communication, mieux se comprendre et apaiser les tensions au sein de la famille.",
           "A place to improve communication, understand each other better and ease tension within the family.")),
        ("therapie-en-ligne.html", "en-ligne", t("Thérapie en ligne", "Online therapy"),
         t("Toutes les séances ont lieu en ligne, par vidéo ou par téléphone, où que vous soyez.",
           "All sessions take place online, by video or phone, wherever you are.")),
    ]


def articles():
    return [
        (t("Se sentir seul en couple : causes et solutions concrètes", "Feeling lonely in a relationship: causes and practical solutions"),
         "se-sentir-seul-en-couple-causes-et-solutions-concrètes", "local:article-seul-en-couple.jpg",
         t("Vivre à deux et se sentir seul : comprendre d'où vient ce sentiment et comment en sortir.",
           "Living together yet feeling alone: where this feeling comes from and how to move past it.")),
        (t("Estime de soi faible : 7 signes et pistes pour agir", "Low self-esteem: 7 signs and ways to act"),
         "estime-de-soi-faible-7-signes-et-pistes-pour-agir", "local:article-estime-de-soi.jpg",
         t("L'estime de soi peut s'éroder sans bruit. Sept signes pour la repérer, et des pistes pour la reconstruire.",
           "Self-esteem can wear away quietly. Seven signs to look for, and ways to rebuild it.")),
        (t("Amour ou dépendance affective : comment faire la différence ?", "Love or emotional dependency: how to tell the difference?"),
         "amour-ou-dépendance-affective-comment-faire-la-différence-concrètement", "local:article-dependance-affective.jpg",
         t("Confondre amour et dépendance affective peut faire beaucoup de mal. Quelques repères concrets.",
           "Mistaking emotional dependency for love can hurt. A few concrete markers.")),
        (t("Thérapie en ligne ou en cabinet : est-ce aussi efficace ?", "Online or in-person therapy: is it as effective?"),
         "thérapie-en-ligne-ou-en-cabinet-est-ce-aussi-efficace-ce-que-dit-la-science", "local:article-therapie-en-ligne.jpg",
         t("Ce que disent plus de quinze ans de recherche sur l'efficacité des consultations à distance.",
           "What more than fifteen years of research say about the effectiveness of remote therapy.")),
        (t("Quand la communication devient impossible dans le couple", "When communication breaks down in a couple"),
         "quand-la-communication-devient-impossible-dans-le-couple-signaux-d-alerte-et-solutions", "local:article-communication-couple.jpg",
         t("Ne plus réussir à se parler fait peur. Les signaux d'alerte, et ce qui peut aider.",
           "Not being able to talk anymore is frightening. Warning signs, and what can help.")),
        (t("Pourquoi je rumine sans arrêt ? Comprendre le mécanisme", "Why do I keep ruminating? Understanding the mechanism"),
         "pourquoi-je-rumine-sans-arrêt-comprendre-le-mécanisme-et-comment-l-arrêter", "local:article-rumination.jpg",
         t("Conversations, échecs, décisions qui tournent en boucle : comment fonctionne la rumination, et comment l'arrêter.",
           "Conversations, failures and decisions on a loop: how rumination works, and how to stop it.")),
    ]


def img(src, alt, cls=""):
    c = f' class="{cls}"' if cls else ""
    if src.startswith("local:"):
        url = ("" if LANG == "fr" else "../") + "assets/" + src[6:]
    else:
        url = W + src
    return f'<img{c} src="{url}" alt="{alt}" loading="lazy" onerror="this.remove()">'


def page(filename, title, description, body, current=None):
    pre = "" if LANG == "fr" else "../"
    assets = f"{pre}assets/style.css"
    other_href = (f"en/{filename}" if LANG == "fr" else f"../{filename}")
    other_label, other_lang = ("EN", "en") if LANG == "fr" else ("FR", "fr")
    fr_url = f"{SITE}/{'' if filename == 'index.html' else filename[:-5]}"
    en_url = f"{SITE}/en/{'' if filename == 'index.html' else filename[:-5]}"
    links = "\n".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == (current or filename) else ""}>{label}</a>'
        for href, label in nav()
    )
    therapy_links = "\n".join(f'<li><a href="{h}">{ti}</a></li>' for h, _, ti, _ in therapies())
    html = f"""<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{description}">
<link rel="alternate" hreflang="fr" href="{fr_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{W}097dac_71495018115849c1a142e2731f6c6c40~mv2.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Spectral:ital,wght@0,400;0,500;1,400&display=swap">
<link rel="stylesheet" href="{assets}">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><strong>Carinne Leibovici</strong><span>{t("Psychologue clinicienne", "Clinical psychologist")}</span></a>
    <button class="menu-toggle" id="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="{t("Navigation principale", "Main navigation")}">
{links}
<a class="lang" href="{other_href}" hreflang="{other_lang}" lang="{other_lang}" title="{t("English version", "Version française")}">{other_label}</a>
<a class="btn" href="contact.html">{t("Prendre rendez-vous", "Book a session")}</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <p class="brand"><strong>Carinne Leibovici</strong><span>{t("Psychologue clinicienne · Thérapie en ligne", "Clinical psychologist · Online therapy")}</span></p>
        <p class="muted" style="margin-top:14px;max-width:38ch">{t("Thérapies individuelle, de couple et familiale, uniquement en ligne, en français et en anglais.", "Individual, couples and family therapy, online only, in French and English.")}</p>
      </div>
      <div>
        <h3>{t("Thérapies", "Therapies")}</h3>
        <ul>{therapy_links}</ul>
      </div>
      <div>
        <h3>{t("Me suivre", "Follow me")}</h3>
        <ul>
          <li><a href="{FB}" rel="noopener">Facebook</a></li>
          <li><a href="{IG}" rel="noopener">Instagram</a></li>
          <li><a href="{YT}" rel="noopener">YouTube</a></li>
          <li><a href="{WA_LINK}" rel="noopener">WhatsApp</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© 2016 – 2026 Carinne Leibovici</span>
      <a href="confidentialite.html">{t("Politique de confidentialité", "Privacy policy")}</a>
    </div>
  </div>
</footer>
<script>
(function () {{
  var b = document.getElementById('menu-toggle'), n = document.getElementById('nav');
  if (b && n) b.addEventListener('click', function () {{
    var o = n.classList.toggle('open'); b.setAttribute('aria-expanded', o ? 'true' : 'false');
  }});
  document.querySelectorAll('[data-copy]').forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      var done = function () {{ btn.textContent = btn.getAttribute('data-done'); }};
      if (navigator.clipboard) navigator.clipboard.writeText(btn.getAttribute('data-copy')).then(done, function () {{}});
    }});
  }});
}})();
</script>
</body>
</html>
"""
    d = out_dir()
    d.mkdir(exist_ok=True)
    (d / filename).write_text(html, encoding="utf-8")


def cta(title=None, text=None):
    title = title or t("Faire le premier pas", "Take the first step")
    text = text or t("Écrivez-moi quelques lignes sur ce qui vous amène. Je vous réponds pour fixer un premier rendez-vous en ligne.",
                     "Write me a few lines about what brings you here. I will reply to arrange a first online session.")
    return f"""<section class="cta"><div class="wrap">
  <div style="display:grid;gap:12px"><h2>{title}</h2><p style="max-width:46ch">{text}</p></div>
  <a class="btn" href="contact.html">{t("Prendre rendez-vous", "Book a session")}</a>
</div></section>"""


def therapy_cards():
    more = t("En savoir plus", "Learn more")
    return "\n".join(
        f'<a class="card" href="{h}">{MOTIFS[k]}<h3>{ti}</h3><p class="muted">{d}</p><span class="more">{more}</span></a>'
        for h, k, ti, d in therapies()
    )


def posts(items):
    note = t("", '<p class="muted" style="font-size:.85rem">Article in French</p>')
    return "\n".join(
        f'<a class="post" href="{OLD}/single-post/{slug}" rel="noopener"><div class="thumb">{img(pic, "")}</div>'
        f'<div class="body"><h3>{ti}</h3><p class="muted">{d}</p>{note}</div></a>'
        for ti, slug, pic, d in items
    )


def head(crumb, h1, lead):
    return f"""<section class="page-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">{t("Accueil", "Home")}</a> / {crumb}</p>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
</div></section>"""


def sub_crumb(label):
    return f'<a href="therapies.html">{t("Thérapies", "Therapies")}</a> / {label}'


def ul(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def build():
    # ------------------------------------------------------------ Accueil
    motifs = [
        t("Anxiété", "Anxiety"), t("Stress", "Stress"), t("Stress post-traumatique", "Post-traumatic stress"),
        t("Dépression", "Depression"), t("Troubles de l'humeur, bipolarité", "Mood disorders, bipolar disorder"),
        t("Troubles du sommeil", "Sleep problems"), t("Difficultés relationnelles", "Relationship difficulties"),
        t("Troubles du développement", "Developmental disorders"), t("Troubles du comportement", "Behavioural disorders"),
        t("Sexualité et identité", "Sexuality and identity"), t("Maternité, infertilité", "Motherhood, infertility"),
        t("Addictions", "Addictions"), t("Difficultés professionnelles", "Work difficulties"),
        t("Intégration, Alyah", "Settling abroad, Aliyah"),
    ]
    tags = "".join(f"<li>{m}</li>" for m in motifs)
    page("index.html",
         t("Carinne Leibovici · Psychologue clinicienne en ligne", "Carinne Leibovici · Online clinical psychologist"),
         t("Carinne Leibovici, psychologue clinicienne. Thérapies individuelle, de couple et familiale, uniquement en ligne, en français et en anglais.",
           "Carinne Leibovici, clinical psychologist. Individual, couples and family therapy, online only, in French and English."),
         f"""
<section class="hero"><div class="wrap">
  <div class="hero-text">
    <p class="eyebrow">{t("Psychologue clinicienne · Séances en ligne", "Clinical psychologist · Online sessions")}</p>
    <h1>{t("Un espace pour comprendre ce qui vous pèse, <em>où que vous soyez.</em>", "A space to understand what weighs on you, <em>wherever you are.</em>")}</h1>
    <p class="lead">{t("Thérapie individuelle, de couple et familiale, uniquement en ligne, en français ou en anglais.", "Individual, couples and family therapy, online only, in French or English.")}</p>
    <div class="actions"><a class="btn" href="contact.html">{t("Prendre rendez-vous", "Book a session")}</a><a class="btn ghost" href="therapies.html">{t("Découvrir les thérapies", "Explore the therapies")}</a></div>
    <ul class="facts"><li>{t("Plus de 15 ans d'expérience", "Over 15 years of experience")}</li><li>{t("TCC, psychodynamique, systémique", "CBT, psychodynamic, systemic")}</li><li>{t("Séances de 50 min à 1 h 30", "Sessions of 50 min to 1 h 30")}</li></ul>
  </div>
  <div class="hero-photo"><img src="{"" if LANG == "fr" else "../"}assets/accueil.jpg" alt="{t("Une patiente chez elle, en séance de thérapie en ligne avec sa psychologue sur un ordinateur portable", "A client at home in an online therapy session with her psychologist on a laptop")}" width="1536" height="1024"></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">{t("Quelle thérapie pour vous ?", "Which therapy is right for you?")}</p><h2>{t("Seul, à deux ou en famille", "On your own, as a couple or as a family")}</h2></div>
  <div class="grid four">{therapy_cards()}</div>
</div></section>

<section><div class="wrap split">
  <div class="section-head" style="margin:0"><p class="eyebrow">{t("Ce qui peut amener à consulter", "Reasons people come to therapy")}</p><h2>{t("Des difficultés de tous les jours, et d'autres plus lourdes", "Everyday struggles, and heavier ones")}</h2>
  <p class="muted">{t("Il n'est pas nécessaire d'aller « très mal » pour consulter. Une période difficile, un sentiment de débordement ou une relation qui s'abîme suffisent.", "You don't need to be in crisis to see a psychologist. A hard period, feeling overwhelmed or a relationship that is wearing down are reason enough.")}</p></div>
  <ul class="tags">{tags}</ul>
</div></section>

<section class="band"><div class="wrap split">
  <div class="figure" style="aspect-ratio:1108/1419;max-width:440px"><img src="{"" if LANG == "fr" else "../"}assets/portrait.jpg" alt="Carinne Leibovici, {t("psychologue clinicienne", "clinical psychologist")}" width="1108" height="1419" loading="lazy"></div>
  <div class="prose">
    <p class="eyebrow">{t("Votre thérapeute", "Your therapist")}</p>
    <h2>Carinne Leibovici</h2>
    <p>{t("Psychologue clinicienne et psycholinguiste, j'accompagne depuis plus de quinze ans des enfants, des adolescents et des adultes, seuls, en couple ou en famille.", "I am a clinical psychologist and psycholinguist. For more than fifteen years I have worked with children, teenagers and adults, individually, as couples and as families.")}</p>
    <p>{t("Je m'appuie sur plusieurs approches, thérapies cognitivo-comportementales, psychodynamique et systémique, choisies selon votre situation. Je propose aussi un accompagnement en coaching personnel et professionnel.", "I draw on several approaches, cognitive behavioural, psychodynamic and systemic, chosen to suit your situation. I also offer personal and professional coaching.")}</p>
    <p>{t("Toutes mes séances ont lieu en ligne : vous consultez depuis l'endroit de votre choix.", "All my sessions take place online, so you can attend from wherever you choose.")}</p>
    <p><a href="qui-suis-je.html">{t("Mon parcours", "My background")}</a></p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><p class="eyebrow">{t("Comment ça se passe", "How it works")}</p><h2>{t("Du premier message à la première séance", "From your first message to your first session")}</h2></div>
  <ol class="steps" data-step="{t("Étape", "Step")}">
    <li><h3>{t("Vous m'écrivez", "You write to me")}</h3><p class="muted">{t("Écrivez-moi en quelques lignes ce qui vous amène, pour qui est la démarche, et ce que vous aimeriez savoir avant de commencer.", "Please tell me what brings you, who the sessions are for and what you would like to know before starting.")}</p></li>
    <li><h3>{t("Nous fixons un rendez-vous", "We set a time")}</h3><p class="muted">{t("Je vous réponds pour convenir d'un créneau et du format : vidéo ou téléphone.", "We agree on the date, time and format: video or audio.")}</p></li>
    <li><h3>{t("La première séance en ligne", "Your first online session")}</h3><p class="muted">{t("Nous faisons connaissance : vous m'expliquez les difficultés que vous rencontrez, puis nous décidons ensemble de la fréquence et de la durée de la thérapie.", "We get to know each other: you tell me about the issues you are facing, and together we decide on the frequency and length of therapy.")}</p></li>
  </ol>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">{t("TV, presse et articles", "TV, press and articles")}</p><h2>{t("À lire", "Reading")}</h2></div>
  <div class="grid three">{posts(articles()[:3])}</div>
  <p style="margin-top:28px"><a href="presse.html">{t("Tous les articles et passages TV", "All articles and TV appearances")}</a></p>
</div></section>
{cta()}
""")

    # ------------------------------------------------------------ Qui suis-je
    page("qui-suis-je.html",
         t("Qui suis-je ? · Carinne Leibovici", "About · Carinne Leibovici"),
         t("Parcours de Carinne Leibovici, psychologue clinicienne et psycholinguiste : formation, expérience clinique, télévision, coaching.",
           "Background of Carinne Leibovici, clinical psychologist and psycholinguist: education, clinical experience, television, coaching."),
         f"""
{head(t("Qui suis-je ?", "About"), t("Qui suis-je ?", "About me"), t("Psychologue clinicienne et psycholinguiste, j'accompagne enfants, adolescents et adultes dans leurs difficultés psychologiques et relationnelles.", "Clinical psychologist and psycholinguist, I support children, teenagers and adults with psychological and relationship difficulties."))}
<section style="padding-top:0"><div class="wrap split">
  <div class="portrait" style="max-width:380px;aspect-ratio:1108/1419"><img src="{"" if LANG == "fr" else "../"}assets/portrait.jpg" alt="Carinne Leibovici, {t("psychologue clinicienne", "clinical psychologist")}" width="1108" height="1419"></div>
  <div class="blocks">
    <div class="prose">
      <h2>{t("Formation", "Education")}</h2>
      {ul([t("Études doctorales en psychologie, Université Paris 5 Descartes", "Doctoral studies in psychology, Université Paris 5 Descartes"),
           t("Master professionnel en psychologie clinique et psychopathologie", "Professional Master's in clinical psychology and psychopathology"),
           t("Master recherche en psycholinguistique, Université Paris 5 Descartes", "Research Master's in psycholinguistics, Université Paris 5 Descartes"),
           t("Master en gestion et management, Université Paris 9 Dauphine", "Master's in business management, Université Paris 9 Dauphine")])}
    </div>
    <div class="prose">
      <h2>{t("Expérience clinique", "Clinical experience")}</h2>
      <p>{t("J'ai exercé plusieurs années dans des structures spécialisées dans les troubles du développement et de la communication chez l'enfant.", "I spent several years in clinics specialising in developmental and communication disorders in children.")}</p>
      <p>{t("Depuis 2009, je consulte en libéral. Aujourd'hui, toutes mes séances ont lieu en ligne, auprès d'enfants, d'adolescents, d'adultes, de couples et de familles.", "I have been in private practice since 2009. Today all my sessions take place online, with children, teenagers, adults, couples and families.")}</p>
      <p>{t("Je travaille en lien avec des médecins et des professionnels paramédicaux lorsque la situation le demande.", "When needed, I work alongside doctors and other health professionals.")}</p>
    </div>
    <div class="prose">
      <h2>{t("À la télévision", "On television")}</h2>
      <p>{t("De 2014 à 2018, j'ai participé à l'émission <em>SOS ma famille a besoin d'aide</em> (NRJ12), consacrée à l'accompagnement de familles en difficulté.", "From 2014 to 2018, I took part in the French TV show <em>SOS ma famille a besoin d'aide</em> (NRJ12), which supported families going through hard times.")}</p>
      <p><a href="presse.html">{t("Voir les émissions", "Watch the episodes")}</a></p>
    </div>
    <div class="prose">
      <h2>Coaching</h2>
      <p>{t("Avant la psychologie, j'ai mené une carrière dans le management et la stratégie des organisations. Cette expérience nourrit aujourd'hui mon accompagnement en développement personnel et professionnel, en orientation de carrière et en bilan de compétences.", "Before psychology, I had a career in management and organisational strategy. That experience now informs my coaching in personal and professional development, career guidance and skills assessment.")}</p>
    </div>
    <div class="prose">
      <h2>{t("Langues", "Languages")}</h2>
      <p>{t("Les séances se déroulent en français ou en anglais.", "Sessions are held in French or English.")}</p>
    </div>
  </div>
</div></section>
{cta()}
""")

    # ------------------------------------------------------------ Thérapies
    approaches = [
        (t("Thérapie d'orientation psychanalytique", "Psychoanalytic therapy"),
         t("Comprendre ce qui se joue de façon inconsciente pour apaiser les symptômes et trouver d'autres manières de faire face.", "Understanding what is happening unconsciously, to ease symptoms and find new ways of coping.")),
        (t("Thérapie cognitivo-comportementale (TCC)", "Cognitive behavioural therapy (CBT)"),
         t("Une approche brève et structurée : analyse des situations, repérage des déclencheurs et des comportements, exercices concrets entre les séances.", "A short, structured approach: analysing situations, spotting triggers and behaviours, and practical exercises between sessions.")),
        (t("Thérapie systémique", "Systemic therapy"),
         t("Regarder le couple ou la famille comme un ensemble, où chacun influence les autres, pour remettre la communication en mouvement.", "Looking at the couple or family as a whole, where each person affects the others, to get communication moving again.")),
        (t("Coaching et développement", "Coaching and development"),
         t("Développement personnel et professionnel, orientation de carrière, bilan de compétences.", "Personal and professional development, career guidance, skills assessment.")),
    ]
    appr = "\n".join(f'<div class="block"><h3>{a}</h3><p>{b}</p></div>' for a, b in approaches)
    page("therapies.html",
         t("Thérapies · Carinne Leibovici", "Therapies · Carinne Leibovici"),
         t("Thérapies individuelle, de couple et familiale en ligne : approches TCC, psychodynamique et systémique, séances d'orientation, coaching.",
           "Online individual, couples and family therapy: CBT, psychodynamic and systemic approaches, guidance sessions, coaching."),
         f"""
{head(t("Thérapies", "Therapies"), t("Des thérapies adaptées à chacun", "Therapy shaped around you"), t("Des psychothérapies structurées, construites selon votre situation, toutes menées en ligne.", "Structured psychotherapy built around your situation, all held online."))}
<section style="padding-top:0"><div class="wrap"><div class="grid four">{therapy_cards()}</div></div></section>
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">{t("Le cadre", "The setting")}</p><h2>{t("Repères pratiques", "Practical details")}</h2></div>
  <dl class="dl">
    <div><dt>{t("Durée d'une séance", "Session length")}</dt><dd>{t("50 min à 1 h 30", "50 min to 1 h 30")}</dd></div>
    <div><dt>{t("Fréquence", "Frequency")}</dt><dd>{t("Définie ensemble", "Agreed together")}</dd></div>
    <div><dt>{t("Lieu", "Where")}</dt><dd>{t("En ligne uniquement", "Online only")}</dd></div>
    <div><dt>{t("Langues", "Languages")}</dt><dd>{t("Français, anglais", "French, English")}</dd></div>
  </dl>
</div></section>
<section><div class="wrap">
  <div class="section-head"><p class="eyebrow">{t("Approches", "Approaches")}</p><h2>{t("Plusieurs outils, choisis pour vous", "Several tools, chosen for you")}</h2></div>
  <div class="blocks">{appr}</div>
</div></section>
<section class="band"><div class="wrap split">
  <div class="section-head" style="margin:0"><p class="eyebrow">{t("Sans engager une thérapie", "Without starting full therapy")}</p><h2>{t("Séances d'orientation et de bilan", "Guidance and assessment sessions")}</h2></div>
  <div class="prose">
    <p>{t("Vous souhaitez un avis, un éclairage ou une orientation sans entamer une thérapie complète ? Je propose des séances d'orientation et de bilan, limitées à cinq séances au maximum.", "Would you like an opinion, some insight or guidance without starting full therapy? I offer guidance and assessment sessions, up to five at most.")}</p>
    <p>{t("Leur durée et leur tarif sont les mêmes que ceux d'une séance de thérapie.", "They have the same length and fee as a therapy session.")}</p>
  </div>
</div></section>
{cta()}
""")

    # ------------------------------------------------------------ Individuelle
    indiv = [
        t("Troubles anxieux", "Anxiety disorders"), t("Stress et stress post-traumatique", "Stress and post-traumatic stress"),
        t("Troubles de l'humeur", "Mood disorders"), t("Troubles du sommeil", "Sleep problems"),
        t("Difficultés relationnelles", "Relationship difficulties"),
        t("Troubles du développement (spectre autistique)", "Developmental disorders (autism spectrum)"),
        t("Troubles du comportement (hyperactivité, TOC)", "Behavioural disorders (ADHD, OCD)"),
        t("Sexualité et questions d'identité", "Sexuality and identity"), t("Maternité et infertilité", "Motherhood and infertility"),
        t("Addictions (substances, jeux, écrans)", "Addictions (substances, gambling, screens)"),
        t("Plaintes somatiques et hypocondrie", "Somatic complaints and health anxiety"), t("Troubles alimentaires", "Eating disorders"),
        t("Difficultés professionnelles et d'intégration (Alyah)", "Work difficulties and settling abroad (Aliyah)"),
    ]
    page("therapie-individuelle.html",
         t("Thérapie individuelle · Carinne Leibovici", "Individual therapy · Carinne Leibovici"),
         t("Thérapie individuelle en ligne : anxiété, stress, dépression, sommeil, addictions, troubles alimentaires. Approches psychanalytique et TCC.",
           "Online individual therapy: anxiety, stress, depression, sleep, addictions, eating disorders. Psychoanalytic and CBT approaches."),
         f"""
{head(sub_crumb(t("Individuelle", "Individual")), t("Thérapie individuelle", "Individual therapy"), therapies()[0][3])}
<section style="padding-top:0"><div class="wrap" style="display:grid;gap:48px">
  <div class="hero-photo" style="aspect-ratio:1092/390"><img src="{"" if LANG == "fr" else "../"}assets/therapie-individuelle.jpg" alt="{t("Une psychologue prend des notes pendant une séance de thérapie individuelle", "A psychologist taking notes during an individual therapy session")}" width="1092" height="390"></div>
  <div style="display:grid;gap:24px"><h2>{t("Pour quelles difficultés ?", "What can it help with?")}</h2><ul class="tags">{"".join(f"<li>{x}</li>" for x in indiv)}</ul></div>
</div></section>
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">{t("Les approches", "Approaches")}</p><h2>{t("Trois manières de travailler", "Three ways of working")}</h2></div>
  <div class="blocks">
    <div class="block"><h3>{t("Psychothérapie d'inspiration analytique", "Psychodynamic psychotherapy")}</h3><div class="prose"><p>{t("Elle s'appuie sur ce qui se joue de façon inconsciente pour soulager les symptômes et construire de meilleures façons de faire face. Elle peut être brève, pour une difficulté ponctuelle, ou plus longue, pour reconstruire la confiance en soi.", "It works with what is happening unconsciously to relieve symptoms and build better ways of coping. It can be short, for a specific difficulty, or longer, to rebuild self-confidence.")}</p></div></div>
    <div class="block"><h3>{t("Cure psychanalytique", "Psychoanalysis")}</h3><div class="prose"><p>{t("Un travail au long cours, à raison de plusieurs séances par semaine, pour explorer les conflits inconscients. Elle ne convient pas à tout le monde, et nous en parlons ensemble avant de l'envisager.", "Long-term work, with several sessions a week, exploring unconscious conflicts. It is not right for everyone, and we discuss it together before considering it.")}</p></div></div>
    <div class="block"><h3>{t("Thérapie cognitivo-comportementale", "Cognitive behavioural therapy")}</h3><div class="prose"><p>{t("Une approche brève et structurée : analyse fonctionnelle des situations, repérage des déclencheurs et des comportements compulsifs, objectifs et exercices concrets. Elle convient à toute personne en souffrance.", "A short, structured approach: analysing situations, identifying triggers and compulsive behaviours, setting concrete goals and exercises. It suits anyone who is struggling.")}</p></div></div>
  </div>
</div></section>
{cta()}
""", current="therapies.html")

    # ------------------------------------------------------------ Couple
    couple = [
        t("Communication rompue", "Communication has broken down"), t("Perte de confiance", "Loss of trust"),
        t("Infidélité", "Infidelity"), t("Jalousie excessive", "Excessive jealousy"), t("Manque d'attention", "Lack of attention"),
        t("Absences répétées", "Frequent absences"), t("Insatisfaction sexuelle", "Sexual dissatisfaction"),
        t("Pression de la belle-famille ou de la famille", "Pressure from in-laws or family"),
        t("Attentes différentes", "Different expectations"), t("Relation trop fusionnelle avec les enfants", "An overly close bond with the children"),
        t("Problème de santé psychique ou physique d'un partenaire", "A partner's mental or physical health problem"),
        t("Séparation ou divorce envisagé", "Considering separation or divorce"),
    ]
    page("therapie-de-couple.html",
         t("Thérapie de couple · Carinne Leibovici", "Couples therapy · Carinne Leibovici"),
         t("Thérapie de couple en ligne : communication, confiance, infidélité, jalousie, séparation. Séances d'environ 1 h 30.",
           "Online couples therapy: communication, trust, infidelity, jealousy, separation. Sessions of about 1 h 30."),
         f"""
{head(sub_crumb(t("Couple", "Couples")), t("Thérapie de couple", "Couples therapy"), therapies()[1][3])}
<section style="padding-top:0"><div class="wrap" style="display:grid;gap:48px">
  <div class="hero-photo" style="aspect-ratio:1092/390"><img src="{"" if LANG == "fr" else "../"}assets/therapie-de-couple.jpg" alt="{t("Un couple en difficulté, chacun perdu dans ses pensées", "A couple in difficulty, each lost in their own thoughts")}" width="1092" height="390"></div>
  <div style="display:grid;gap:24px"><h2>{t("Quand consulter ?", "When to seek help")}</h2><ul class="tags">{"".join(f"<li>{x}</li>" for x in couple)}</ul></div>
</div></section>
<section class="band"><div class="wrap">
  <div class="blocks">
    <div class="block"><h3>{t("À qui s'adresse-t-elle ?", "Who is it for?")}</h3><div class="prose"><p>{t("À tous les couples, mariés ou non, qui sentent leur relation se dégrader. Mieux vaut consulter avant d'atteindre un point de rupture.", "Any couple, married or not, who feel their relationship is deteriorating. It is better to come before reaching breaking point.")}</p><p>{t("Le thérapeute reste neutre. Son rôle est de rétablir la communication, en tenant compte de l'histoire familiale de chacun des partenaires.", "The therapist stays neutral. The aim is to restore communication, taking each partner's family history into account.")}</p></div></div>
    <div class="block"><h3>{t("Comment se déroulent les séances ?", "How do sessions work?")}</h3><div class="prose"><p>{t("Le cadre est défini avec vous. En général : une première séance à deux, puis une séance individuelle pour chaque partenaire, puis un retour aux séances communes.", "We set the format together. Usually: a first joint session, then one individual session for each partner, then back to joint sessions.")}</p><p>{t("Il ne faut pas perdre espoir : beaucoup de couples retrouvent un équilibre.", "Don't lose hope: many couples find their balance again.")}</p></div></div>
  </div>
  <dl class="dl" style="margin-top:48px">
    <div><dt>{t("Durée moyenne", "Average length")}</dt><dd>1 h 30</dd></div>
    <div><dt>{t("Rythme conseillé", "Suggested rhythm")}</dt><dd>{t("Tous les 10 à 15 jours", "Every 10 to 15 days")}</dd></div>
  </dl>
</div></section>
{cta()}
""", current="therapies.html")

    # ------------------------------------------------------------ Famille
    page("therapie-familiale.html",
         t("Thérapie familiale · Carinne Leibovici", "Family therapy · Carinne Leibovici"),
         t("Thérapie familiale en ligne : conflits, difficultés d'un enfant, troubles alimentaires, séparation et garde. Approches systémique et psychanalytique.",
           "Online family therapy: conflict, a child's difficulties, eating disorders, separation and custody. Systemic and psychoanalytic approaches."),
         f"""
{head(sub_crumb(t("Famille", "Family")), t("Thérapie familiale", "Family therapy"), therapies()[2][3])}
<section style="padding-top:0"><div class="wrap" style="display:grid;gap:48px">
  <div class="hero-photo" style="aspect-ratio:1600/572"><img src="{"" if LANG == "fr" else "../"}assets/therapie-familiale.jpg" alt="{t("Un adolescent s'exprime, écouté par ses deux parents", "A teenager speaking while both parents listen")}" width="1600" height="572"></div>
  <div class="prose">
    <h2>{t("À qui s'adresse-t-elle ?", "Who is it for?")}</h2>
    <p>{t("Aux familles traversant des tensions, des conflits ou des événements difficiles. Notamment lorsqu'un enfant présente des difficultés d'interaction ou de comportement, ou des troubles alimentaires importants.", "Families facing tension, conflict or difficult events. In particular when a child has difficulties with behaviour or relating to others, or a serious eating disorder.")}</p>
    <p>{t("Elle peut aussi être conseillée lors d'une séparation ou d'un divorce, et pour les questions de garde.", "It can also help during a separation or divorce, and with custody questions.")}</p>
    <p>{t("Un enfant en difficulté est souvent le reflet d'un déséquilibre plus large : tout changement chez l'un des membres agit sur l'ensemble du groupe.", "A struggling child often reflects a wider imbalance: any change in one family member affects the whole group.")}</p>
  </div>
</div></section>
<section class="band"><div class="wrap">
  <div class="blocks">
    <div class="block"><h3>{t("Deux approches", "Two approaches")}</h3><div class="prose"><p>{t("<strong>La thérapie systémique</strong> considère la famille comme un système et travaille sur la communication entre ses membres.", "<strong>Systemic therapy</strong> sees the family as a system and works on communication between its members.")}</p><p>{t("<strong>La thérapie familiale psychanalytique</strong> s'intéresse aux conflits parentaux et transgénérationnels non résolus.", "<strong>Psychoanalytic family therapy</strong> looks at unresolved parental and intergenerational conflicts.")}</p></div></div>
    <div class="block"><h3>{t("Qui participe ?", "Who takes part?")}</h3><div class="prose"><p>{t("Idéalement toute la famille au départ : parents, frères et sœurs, parfois grands-parents. Les séances suivantes réunissent en général les membres clés.", "Ideally the whole family at first: parents, siblings, sometimes grandparents. Later sessions usually bring together the key members.")}</p></div></div>
    <div class="block"><h3>{t("Déroulement", "How sessions run")}</h3><div class="prose"><p>{t("Des séances structurées, en visioconférence, où chacun prend la parole à son tour.", "Structured video sessions where everyone speaks in turn.")}</p></div></div>
  </div>
  <dl class="dl" style="margin-top:48px">
    <div><dt>{t("Durée", "Length")}</dt><dd>{t("Environ 1 h 30", "About 1 h 30")}</dd></div>
    <div><dt>{t("Rythme", "Rhythm")}</dt><dd>{t("1 à 2 fois par mois", "Once or twice a month")}</dd></div>
  </dl>
</div></section>
{cta()}
""", current="therapies.html")

    # ------------------------------------------------------------ En ligne
    benefits = [
        (t("Accessible", "Accessible"), t("Aucune contrainte géographique.", "No geographical limits.")),
        (t("Gain de temps", "Saves time"), t("Pas de trajet.", "No commute.")),
        (t("Confort", "Comfort"), t("Un cadre familier et rassurant.", "A familiar, reassuring setting.")),
        (t("Flexibilité", "Flexibility"), t("Plus simple à concilier avec le travail et la vie personnelle.", "Easier to fit around work and personal life.")),
        (t("Discrétion", "Discretion"), t("Personne ne vous voit entrer chez un psy.", "Nobody sees you walk into a therapist's office.")),
        (t("Continuité", "Continuity"), t("Le suivi continue, même en voyage.", "Therapy continues even when you travel.")),
    ]
    page("therapie-en-ligne.html",
         t("Thérapie en ligne · Carinne Leibovici", "Online therapy · Carinne Leibovici"),
         t("Toutes les séances ont lieu en ligne : Zoom, Teams, FaceTime, WhatsApp ou téléphone, de 50 min à 1 h 30, en français ou en anglais.",
           "All sessions are online: Zoom, Teams, FaceTime, WhatsApp or phone, 50 min to 1 h 30, in French or English."),
         f"""
{head(sub_crumb(t("En ligne", "Online")), t("Thérapie en ligne", "Online therapy"), t("Toutes mes séances ont lieu en ligne, par vidéo ou par téléphone. Où que vous viviez, le lieu n'est plus une contrainte.", "All my sessions take place online, by video or phone. Wherever you live, location is no longer a barrier."))}
<section style="padding-top:0"><div class="wrap" style="display:grid;gap:40px">
  <div class="hero-photo" style="aspect-ratio:1536/1024"><img src="{"" if LANG == "fr" else "../"}assets/therapie-en-ligne.jpg" alt="{t("Un patient en séance de thérapie en ligne avec sa psychologue, par visioconférence", "A client in an online therapy session with his psychologist by video call")}" width="1536" height="1024" loading="lazy"></div>
  <dl class="dl">
    <div><dt>{t("Outils", "Tools")}</dt><dd>{t("Zoom, Skype, Teams, FaceTime, WhatsApp, téléphone", "Zoom, Skype, Teams, FaceTime, WhatsApp, phone")}</dd></div>
    <div><dt>{t("Durée", "Length")}</dt><dd>{t("50 min à 1 h 30", "50 min to 1 h 30")}</dd></div>
    <div><dt>{t("Paiement", "Payment")}</dt><dd>{t("À l'avance : virement, Wise, Wero, Revolut ou PayPal", "In advance: bank transfer, Wise, Wero, Revolut or PayPal")}</dd></div>
    <div><dt>{t("Annulation", "Cancellation")}</dt><dd>{t("Remboursement si 48 h avant", "Refund if 48 h ahead")}</dd></div>
  </dl>
</div></section>
<section class="band"><div class="wrap split">
  <div class="section-head" style="margin:0"><p class="eyebrow">{t("Un cadre structuré", "A structured setting")}</p><h2>{t("Pourquoi consulter en ligne ?", "Why online therapy?")}</h2><p class="muted">{t("Les séances en ligne suivent une structure claire, définie dès la première rencontre. La recherche montre qu'elles sont aussi efficaces que les séances en présentiel. Certaines mutuelles les remboursent en partie ou en totalité.", "Online sessions follow a clear structure, agreed at our first meeting. Research shows they are as effective as in-person therapy. Some insurers cover them in part or in full.")}</p></div>
  <div class="grid two">{"".join(f'<div class="card"><h3>{a}</h3><p class="muted">{b}</p></div>' for a, b in benefits)}</div>
</div></section>
{cta()}
""", current="therapies.html")

    # ------------------------------------------------------------ Presse
    page("presse.html",
         t("TV, presse et articles · Carinne Leibovici", "TV, press and articles · Carinne Leibovici"),
         t("Passages TV de Carinne Leibovici dans SOS ma famille a besoin d'aide (NRJ12) et articles sur le couple, l'estime de soi, l'anxiété et la thérapie en ligne.",
           "Carinne Leibovici on TV in SOS ma famille a besoin d'aide (NRJ12), and articles on relationships, self-esteem, anxiety and online therapy."),
         f"""
{head(t("TV & articles", "TV & articles"), t("TV, presse et articles", "TV, press and articles"), t("Émissions de télévision et articles pour mieux comprendre ce que l'on traverse.", "TV programmes and articles to help make sense of what you are going through."))}
<section style="padding-top:0"><div class="wrap split">
  <div class="figure" style="aspect-ratio:16/10">{img("097dac_39ec2334fc864df1b6d78bc92afb6b68.png", "SOS ma famille a besoin d'aide")}</div>
  <div class="prose">
    <p class="eyebrow">{t("Télévision · NRJ12", "Television · NRJ12 (France)")}</p>
    <h2>SOS ma famille a besoin d'aide</h2>
    <p>{t("De 2014 à 2018, j'ai accompagné des familles en difficulté dans cette émission diffusée sur NRJ12, disponible en replay et sur la chaîne YouTube de l'émission.", "From 2014 to 2018, I supported families in difficulty on this French TV show, broadcast on NRJ12 and available on the show's YouTube channel (in French).")}</p>
    <div class="actions">
      <a class="btn" href="https://www.youtube.com/watch?v=eWGoerPkZNs" rel="noopener">{t("Voir l'épisode Laetitia et Liliana", "Watch the Laetitia and Liliana episode")}</a>
      <a class="btn ghost" href="https://www.youtube.com/@sosmafamilleabesoindaide" rel="noopener">{t("La chaîne de l'émission", "The show's channel")}</a>
    </div>
  </div>
</div></section>
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">{t("Articles", "Articles")}</p><h2>{t("À lire", "Reading")}</h2></div>
  <div class="grid three">{posts(articles())}</div>
</div></section>
{cta()}
""")

    # ------------------------------------------------------------ FAQ
    faq = [
        (t("Qu'est-ce qu'une thérapie et comment fonctionne-t-elle ?", "What is therapy and how does it work?"),
         t("Une thérapie est un travail mené au fil de séances régulières avec un thérapeute, pour mieux comprendre ses pensées, ses émotions et ses comportements, et trouver des façons d'aller mieux.", "Therapy is work done over regular sessions with a therapist, to better understand your thoughts, feelings and behaviour, and find ways to feel better.")),
        (t("Comment savoir si j'ai besoin de consulter un psychologue ?", "How do I know if I need to see a psychologist?"),
         t("Vous pouvez consulter si vous traversez une période difficile, si vous vous sentez débordé, en cas d'anxiété, de tristesse persistante ou de difficultés relationnelles ou professionnelles.", "You can come if you are going through a hard time, feel overwhelmed, or are dealing with anxiety, lasting sadness, or difficulties in your relationships or at work.")),
        (t("Quelle est la différence entre un psychologue et un psychiatre ?", "What is the difference between a psychologist and a psychiatrist?"),
         t("Le psychologue accompagne par la parole et la thérapie. Le psychiatre est médecin et peut prescrire des médicaments. Les deux travaillent parfois ensemble.", "A psychologist helps through talking and therapy. A psychiatrist is a medical doctor and can prescribe medication. They sometimes work together.")),
        (t("Combien de temps dure une séance ?", "How long is a session?"),
         t("En général entre 50 minutes et 1 h 30, selon le type de thérapie et vos besoins.", "Usually between 50 minutes and 1 h 30, depending on the type of therapy and your needs.")),
        (t("À quelle fréquence dois-je consulter ?", "How often should I come?"),
         t("Nous fixons le rythme ensemble lors de la première séance. Certaines personnes consultent chaque semaine, d'autres espacent davantage.", "We agree on the rhythm at the first session. Some people come weekly, others less often.")),
        (t("Les consultations sont-elles confidentielles ?", "Are sessions confidential?"),
         t("Oui. Tout ce qui est dit en séance est strictement confidentiel, conformément au code de déontologie des psychologues.", "Yes. Everything said in session is strictly confidential, in line with the psychologists' code of ethics.")),
        (t("Comment se déroule une thérapie en ligne ?", "How does online therapy work?"),
         t("Toutes les séances ont lieu par vidéo ou par téléphone, sur une plateforme sécurisée, avec une structure claire. Voir la page <a href=\"therapie-en-ligne.html\">Thérapie en ligne</a>.", "All sessions take place by video or phone on a secure platform, with a clear structure. See <a href=\"therapie-en-ligne.html\">Online therapy</a>.")),
        (t("Proposez-vous des séances en cabinet ?", "Do you offer in-person sessions?"),
         t("Non. Toutes les séances ont lieu en ligne.", "No. All sessions take place online.")),
        (t("Comment se préparer à la première séance ?", "How should I prepare for the first session?"),
         t("Aucune préparation n'est nécessaire. Il peut être utile de réfléchir à ce qui vous amène et à ce que vous attendez. Prévoyez un endroit calme où vous ne serez pas dérangé.", "No preparation is needed. It can help to think about what brings you and what you hope for. Find a quiet place where you won't be disturbed.")),
        (t("Combien coûte une consultation et est-elle remboursée ?", "How much does a session cost, and is it covered?"),
         t("Le tarif horaire est le même pour les thérapies individuelle, de couple et familiale. Il vous est communiqué sur demande. Certaines mutuelles remboursent tout ou partie des séances : renseignez-vous auprès de la vôtre.", "The hourly fee is the same for individual, couples and family therapy, and is available on request. Some insurers cover part or all of the cost: check with yours.")),
        (t("Puis-je annuler ou reporter une séance ?", "Can I cancel or reschedule a session?"),
         t("Oui, en prévenant 24 à 48 heures à l'avance. Hors urgence, une annulation tardive peut être facturée.", "Yes, with 24 to 48 hours' notice. Except in an emergency, late cancellations may be charged.")),
        (t("Combien de temps dure une thérapie ?", "How long does therapy last?"),
         t("Cela dépend de vos difficultés et de vos objectifs : quelques semaines, quelques mois, parfois davantage.", "It depends on your difficulties and goals: a few weeks, a few months, sometimes longer.")),
        (t("Puis-je prendre rendez-vous pour quelqu'un d'autre ?", "Can I book for someone else?"),
         t("Oui, à condition que la personne souhaite elle-même être accompagnée : c'est ce qui rend la thérapie utile.", "Yes, as long as the person wants support themselves: that is what makes therapy work.")),
        (t("Comment se déroule une séance avec un mineur ?", "How do sessions with a child work?"),
         t("Je reçois d'abord les parents seuls. L'enfant est ensuite vu seul ou accompagné selon son âge. Ce qu'il dit reste confidentiel, sauf en cas de danger, et les parents sont tenus informés de l'évolution.", "I first meet the parents on their own. The child is then seen alone or with a parent, depending on age. What the child says stays confidential unless there is a risk of harm, and parents are kept informed of progress.")),
    ]
    page("faq.html",
         t("Questions fréquentes · Carinne Leibovici", "FAQ · Carinne Leibovici"),
         t("Questions fréquentes : durée et fréquence des séances, confidentialité, thérapie en ligne, tarifs et remboursement, annulation, consultation d'un mineur.",
           "Frequently asked questions: session length and frequency, confidentiality, online therapy, fees and insurance, cancellation, sessions with children."),
         f"""
{head("FAQ", t("Questions fréquentes", "Frequently asked questions"), t("Les réponses aux questions que l'on se pose avant de commencer.", "Answers to the questions people ask before starting."))}
<section style="padding-top:0"><div class="wrap"><div class="faq">
{"".join(f'<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>' for q, a in faq)}
</div></div></section>
{cta(t("Une autre question ?", "Another question?"), t("Écrivez-moi, je vous réponds personnellement.", "Write to me and I will reply personally."))}
""")

    # ------------------------------------------------------------ Contact
    subject = t("Demande%20de%20rendez-vous", "Session%20request")
    page("contact.html",
         t("Prendre rendez-vous · Carinne Leibovici", "Book a session · Carinne Leibovici"),
         t("Prendre rendez-vous en ligne avec Carinne Leibovici, psychologue clinicienne : contact par e-mail, horaires.",
           "Book an online session with Carinne Leibovici, clinical psychologist: email contact and hours."),
         f"""
{head(t("Rendez-vous", "Book"), t("Prendre rendez-vous", "Book a session"), t("Toutes les séances ont lieu en ligne. Écrivez-moi pour convenir d'un premier rendez-vous.", "All sessions take place online. Write to me to arrange a first appointment."))}
<section style="padding-top:0"><div class="wrap split">
  <div class="contact-card">
    <p class="eyebrow">{t("Écrivez-moi", "Write to me")}</p>
    <a class="email" href="mailto:{EMAIL}">{EMAIL}</a>
    <div class="actions"><a class="btn" href="mailto:{EMAIL}?subject={subject}">{t("Envoyer un e-mail", "Send an email")}</a><button class="copy" type="button" data-copy="{EMAIL}" data-done="{t("Adresse copiée", "Address copied")}">{t("Copier l'adresse", "Copy address")}</button></div>
    <p class="eyebrow">WhatsApp</p>
    <a class="email" href="{WA_LINK}" rel="noopener">{WHATSAPP}</a>
    <div class="actions"><a class="btn ghost" href="{WA_LINK}" rel="noopener">{t("Écrire sur WhatsApp", "Message on WhatsApp")}</a></div>
    <div style="display:flex;align-items:center;gap:18px;flex-wrap:wrap">
      <img src="{"" if LANG == "fr" else "../"}assets/whatsapp-qr.png" alt="{t("QR code WhatsApp de Carinne Leibovici", "Carinne Leibovici's WhatsApp QR code")}" width="152" height="150" style="border-radius:10px;border:1px solid var(--line)">
      <p class="muted" style="max-width:24ch;font-size:.95rem">{t("Scannez ce QR code avec l'appareil photo de votre téléphone pour m'écrire sur WhatsApp.", "Scan this QR code with your phone's camera to message me on WhatsApp.")}</p>
    </div>
    <p class="note">{t("Je ne réponds pas aux appels de numéros inconnus, mais vous pouvez m'écrire par e-mail ou sur WhatsApp : je vous réponds rapidement.", "I don't answer calls from unknown numbers, but you can write to me by email or on WhatsApp and I will reply quickly.")}</p>
    <div class="prose"><p class="muted">{t("Pour faciliter la réponse, indiquez qui consulte (vous, votre couple, votre famille, votre enfant), ce qui vous amène en quelques mots, votre langue (français ou anglais) et vos disponibilités.", "To help me reply, say who the sessions are for (you, your couple, your family, your child), what brings you in a few words, your language (French or English) and when you are available.")}</p></div>
  </div>
  <div class="blocks">
    <div class="prose">
      <h2>{t("Horaires", "Hours")}</h2>
      <table class="hours"><tbody>
        <tr><td>{t("Dimanche – jeudi", "Sunday – Thursday")}</td><td>9:00 – 20:00</td></tr>
        <tr><td>{t("Vendredi", "Friday")}</td><td>9:00 – 15:00</td></tr>
        <tr><td>{t("Samedi", "Saturday")}</td><td>{t("Fermé", "Closed")}</td></tr>
      </tbody></table>
    </div>
    <div class="prose">
      <h2>{t("Séance en ligne", "Online session")}</h2>
      <dl class="dl">
        <div><dt>{t("Durée", "Length")}</dt><dd>50 min</dd></div>
        <div><dt>{t("Tarif", "Fee")}</dt><dd>{t("Sur demande", "On request")}</dd></div>
        <div><dt>{t("Paiement", "Payment")}</dt><dd>{t("Virement bancaire, Wise, Wero, Revolut ou PayPal", "Bank transfer, Wise, Wero, Revolut or PayPal")}</dd></div>
      </dl>
      <p class="muted">{t("Toutes les séances ont lieu en ligne, par vidéo ou par téléphone.", "All sessions take place online, by video or phone.")}</p>
    </div>
  </div>
</div></section>
""")

    # ------------------------------------------------------------ Confidentialité
    privacy = [
        (t("Responsable du traitement", "Data controller"), t(f"Carinne Leibovici, psychologue. Pour toute question sur vos données, écrivez à {EMAIL}.", f"Carinne Leibovici, psychologist. For any question about your data, write to {EMAIL}.")),
        (t("Données collectées", "Data collected"), t("Votre identité et vos coordonnées, les informations de santé que vous choisissez de transmettre lors d'une prise de contact ou d'une téléconsultation, et des données de navigation (cookies, adresse IP, utilisation du site).", "Your identity and contact details, health information you choose to share when getting in touch or during an online session, and browsing data (cookies, IP address, site usage).")),
        (t("Finalités", "Purposes"), t("Répondre à vos demandes et à vos prises de rendez-vous, assurer les consultations, améliorer le site et respecter les obligations professionnelles.", "Answering your enquiries and bookings, providing sessions, improving the site and meeting professional obligations.")),
        (t("Données de santé", "Health data"), t("Elles sont strictement confidentielles, sauf obligation légale ou risque grave pour vous ou pour autrui.", "Strictly confidential, except where required by law or in case of serious risk to you or others.")),
        (t("Partage", "Sharing"), t("Vos données ne sont partagées avec aucun tiers, sauf consentement explicite de votre part, obligation légale ou demande d'une autorité judiciaire ou administrative.", "Your data is not shared with any third party, except with your explicit consent, where required by law, or at the request of a judicial or administrative authority.")),
        (t("Durée de conservation", "Retention"), t("Les données de contact sont conservées 2 ans après le dernier échange. Les données de santé sont conservées en général 5 ans après la dernière consultation.", "Contact data is kept for 2 years after our last exchange. Health data is generally kept for 5 years after the last session.")),
        (t("Sécurité", "Security"), t("Des mesures techniques et organisationnelles protègent vos données contre la perte, la modification ou l'accès non autorisé.", "Technical and organisational measures protect your data against loss, alteration or unauthorised access.")),
        (t("Vos droits", "Your rights"), t("Conformément au RGPD, vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité, que vous pouvez exercer par e-mail.", "Under the GDPR, you have the right to access, correct, erase, restrict, object to and port your data. You can exercise these rights by email.")),
        (t("Cookies", "Cookies"), t("Vous pouvez les paramétrer à tout moment dans votre navigateur.", "You can manage cookies at any time in your browser settings.")),
        (t("Modifications", "Changes"), t("Cette politique peut évoluer. La date de dernière mise à jour figure en haut de cette page.", "This policy may change. The date of the last update appears at the top of this page.")),
    ]
    page("confidentialite.html",
         t("Politique de confidentialité · Carinne Leibovici", "Privacy policy · Carinne Leibovici"),
         t("Politique de confidentialité et protection des données personnelles du site de Carinne Leibovici, psychologue clinicienne.",
           "Privacy policy and personal data protection for the website of Carinne Leibovici, clinical psychologist."),
         f"""
{head(t("Confidentialité", "Privacy"), t("Politique de confidentialité", "Privacy policy"), t("Dernière mise à jour : octobre 2026.", "Last updated: October 2026."))}
<section style="padding-top:0"><div class="wrap"><div class="blocks">
{"".join(f'<div class="block"><h3>{a}</h3><div class="prose"><p>{b}</p></div></div>' for a, b in privacy)}
</div></div></section>
""")


for LANG in ("fr", "en"):
    build()
print("ok", sorted(p.name for p in ROOT.glob("*.html")), sorted(p.name for p in (ROOT / "en").glob("*.html")))
