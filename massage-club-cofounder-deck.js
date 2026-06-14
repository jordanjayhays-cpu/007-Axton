const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "Massage Club — Co-founder";

// Exact design tokens from massage-madrid-magic.lovable.app
const C = {
  bg:         "F8F6F0",   // warm cream background
  foreground: "331313",   // dark warm brown
  primary:    "A31422",   // deep burgundy
  accent:     "E4AA25",   // gold
  card:       "FCFAF7",   // near-white card
  muted:      "E8E2D8",   // warm muted
  secondary:  "EFE8DB",   // warm beige
  border:     "DED5C3",   // warm border
  priGlow:    "DE162A",   // bright red glow
  accDeep:    "B67F20",   // deep gold
  white:      "FFFFFF",
};

// Font sizes in pt
const F = {
  hero:    42,
  title:   36,
  section: 9,
  body:    11,
  small:   9,
};

// ─── HELPERS ───────────────────────────────────────────────────
function headerBar(slide, subtitle) {
  // Deep burgundy top bar
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.88, fill: { color: C.primary } });
  // Gold accent strip
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0.88, w: 10, h: 0.055, fill: { color: C.accent } });
  // Logo text
  slide.addText("MASSAGE CLUB", {
    x: 0.65, y: 0.16, w: 3.5, h: 0.32,
    fontSize: 11, fontFace: "Calibri", color: C.accent, bold: true, charSpacing: 5, margin: 0,
  });
  slide.addText(subtitle, {
    x: 0.65, y: 0.52, w: 4, h: 0.25,
    fontSize: 8, fontFace: "Calibri", color: "E8B4B4", charSpacing: 3, margin: 0,
  });
}

function footerBar(slide, num) {
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.1, w: 10, h: 0.525, fill: { color: C.primary } });
  slide.addText("massageclub.io", {
    x: 0.65, y: 5.2, w: 5, h: 0.28,
    fontSize: 9, fontFace: "Calibri", color: "E8B4B4", margin: 0,
  });
  slide.addText(num, {
    x: 9.1, y: 5.2, w: 0.5, h: 0.28,
    fontSize: 9, fontFace: "Calibri", color: "A07070", align: "right", margin: 0,
  });
}

function divider(slide, y) {
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.65, y, w: 8.7, h: 0.02, fill: { color: C.border } });
}

function contentCard(slide, x, y, w, h, topColor) {
  slide.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: C.card } });
  slide.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 0.055, fill: { color: topColor } });
}

function sectionTag(slide, text, x, y, color) {
  slide.addText(text, {
    x, y, w: 2.5, h: 0.22,
    fontSize: 7.5, fontFace: "Calibri", color, bold: true, charSpacing: 3, margin: 0,
  });
}

// ─── SLIDE 1 — THE OPPORTUNITY ──────────────────────────────────
var s1 = pres.addSlide();
s1.background = { color: C.bg };

headerBar(s1, "THE COMPANY");

// Hero
s1.addText("Massage Club", {
  x: 0.65, y: 1.08, w: 7, h: 0.72,
  fontSize: F.hero, fontFace: "Calibri", color: C.primary, bold: true, margin: 0,
});
s1.addText("Masajes ilimitados. Una suscripción.", {
  x: 0.65, y: 1.82, w: 6, h: 0.32,
  fontSize: 14, fontFace: "Calibri", color: C.muted, margin: 0,
});
s1.addText("Slide 1 of 3", {
  x: 7.5, y: 1.82, w: 2, h: 0.25,
  fontSize: 8, fontFace: "Calibri", color: "B8A98A", align: "right", margin: 0,
});

divider(s1, 2.25);

// 3 content columns
const c1X = 0.65, c2X = 3.5, c3X = 6.35, cW = 2.55, cY = 2.42;

// THE PROBLEM
contentCard(s1, c1X, cY, cW, 2.58, C.primary);
sectionTag(s1, "THE PROBLEM", c1X+0.2, cY+0.18, C.primary);
s1.addText([
  { text: "No hay plataforma central — reserva fragmentada entre Google, FB y paseos", options: { bullet: true, breakLine: true } },
  { text: "Las plataformas cobran 30–40% de comisión", options: { bullet: true, breakLine: true } },
  { text: "Sin disponibilidad en tiempo real, sin descubrimiento fácil", options: { bullet: true } },
], {
  x: c1X+0.2, y: cY+0.5, w: cW-0.4, h: 1.9,
  fontSize: 10, fontFace: "Calibri", color: C.foreground, paraSpaceAfter: 5, margin: 0,
});

// THE SOLUTION
contentCard(s1, c2X, cY, cW, 2.58, C.accent);
sectionTag(s1, "THE SOLUTION", c2X+0.2, cY+0.18, C.accent);
s1.addText([
  { text: "Suscripción €79/mes — masajes ilimitados", options: { bullet: true, breakLine: true } },
  { text: "Reserva directa — terapeuta cobra 100%", options: { bullet: true, breakLine: true } },
  { text: "Disponibilidad en tiempo real, reserva instantánea", options: { bullet: true } },
], {
  x: c2X+0.2, y: cY+0.5, w: cW-0.4, h: 1.9,
  fontSize: 10, fontFace: "Calibri", color: C.foreground, paraSpaceAfter: 5, margin: 0,
});

// TARGET AUDIENCE
contentCard(s1, c3X, cY, cW, 2.58, C.primary);
sectionTag(s1, "TARGET AUDIENCE", c3X+0.2, cY+0.18, C.primary);
s1.addText([
  { text: "Profesionales urbanos en Madrid, 25–45 años", options: { bullet: true, breakLine: true } },
  { text: "Valoran el bienestar y su tiempo por igual", options: { bullet: true, breakLine: true } },
  { text: "Visitantes frecuentes de estudios de masaje", options: { bullet: true } },
], {
  x: c3X+0.2, y: cY+0.5, w: cW-0.4, h: 1.9,
  fontSize: 10, fontFace: "Calibri", color: C.foreground, paraSpaceAfter: 5, margin: 0,
});

footerBar(s1, "01");


// ─── SLIDE 2 — WHO WE NEED ───────────────────────────────────────
var s2 = pres.addSlide();
s2.background = { color: C.bg };

headerBar(s2, "OPEN POSITION");

// Hero
s2.addText("Who we're looking for.", {
  x: 0.65, y: 1.08, w: 7.5, h: 0.72,
  fontSize: F.title, fontFace: "Calibri", color: C.primary, bold: true, margin: 0,
});
// Pill badge
s2.addShape(pres.shapes.RECTANGLE, { x: 0.65, y: 1.84, w: 2.6, h: 0.3, fill: { color: C.accent } });
s2.addText("Equity-based  ·  Madrid (hybrid)", {
  x: 0.65, y: 1.84, w: 2.6, h: 0.3,
  fontSize: 8, fontFace: "Calibri", color: C.white, bold: true, align: "center", valign: "middle", margin: 0,
});
s2.addText("Slide 2 of 3", {
  x: 7.5, y: 1.84, w: 2, h: 0.25,
  fontSize: 8, fontFace: "Calibri", color: "B8A98A", align: "right", margin: 0,
});

divider(s2, 2.32);

// Two columns
const lX = 0.65, rX = 5.1, cH = 2.62, lY = 2.5;

// WHAT WE NEED — left card
contentCard(s2, lX, lY, 4.15, cH, C.primary);
sectionTag(s2, "WHAT WE NEED", lX+0.25, lY+0.18, C.primary);
const needs = [
  ["Full-stack development", "React, TypeScript, Supabase — our stack is live and needs a real engineer to own it."],
  ["Product thinking", "Someone who can build features users actually want, not just what sounds good."],
  ["Move fast", "We have a product, a market, and a plan. We need someone who executes."],
];
needs.forEach(([t, d], i) => {
  const ry = lY + 0.52 + i * 0.68;
  s2.addText(t, { x: lX+0.25, y: ry, w: 3.65, h: 0.26, fontSize: 11, fontFace: "Calibri", bold: true, color: C.primary, margin: 0 });
  s2.addText(d, { x: lX+0.25, y: ry+0.28, w: 3.65, h: 0.38, fontSize: 9.5, fontFace: "Calibri", color: C.foreground, margin: 0 });
});

// THE OPPORTUNITY — right card
contentCard(s2, rX, lY, 4.15, cH, C.accent);
sectionTag(s2, "THE OPPORTUNITY", rX+0.25, lY+0.18, C.accDeep);
const opps = [
  ["Co-founder title", "Not an early employee — a real co-founder with meaningful equity."],
  ["Build something real", "A consumer app in a city you live in. Real users, real bookings."],
  ["Madrid is open", "No dominant player. Timing is right. Market is ready."],
];
opps.forEach(([t, d], i) => {
  const ry = lY + 0.52 + i * 0.68;
  s2.addText(t, { x: rX+0.25, y: ry, w: 3.65, h: 0.26, fontSize: 11, fontFace: "Calibri", bold: true, color: C.primary, margin: 0 });
  s2.addText(d, { x: rX+0.25, y: ry+0.28, w: 3.65, h: 0.38, fontSize: 9.5, fontFace: "Calibri", color: C.foreground, margin: 0 });
});

footerBar(s2, "02");


// ─── SLIDE 3 — WHY THIS, WHY NOW ─────────────────────────────────
var s3 = pres.addSlide();
s3.background = { color: C.bg };

headerBar(s3, "WHY THIS, WHY NOW");

// Hero
s3.addText("Why join us.", {
  x: 0.65, y: 1.08, w: 7, h: 0.72,
  fontSize: F.hero, fontFace: "Calibri", color: C.primary, bold: true, margin: 0,
});
s3.addText("Slide 3 of 3", {
  x: 7.5, y: 1.08, w: 2, h: 0.25,
  fontSize: 8, fontFace: "Calibri", color: "B8A98A", align: "right", margin: 0,
});

divider(s3, 1.9);

// 2x2 reason grid
const reasons = [
  { num:"01", title:"Real product, real market",       desc:"The app is live. The subscription model proven elsewhere. Madrid is untapped and ready.", topC:C.primary },
  { num:"02", title:"Get in at the start",             desc:"Co-founder title, meaningful equity. You build this — not join it.",                      topC:C.accent },
  { num:"03", title:"A market that isn\u2019t going anywhere", desc:"Wellness is growing. People spend more on their bodies. Right category, right time.",  topC:C.primary },
  { num:"04", title:"Build something you can show",    desc:"A consumer app in a city you live in. Real users, real bookings, real impact.",            topC:C.accent },
];

const grid = [
  { x: 0.65,  y: 2.08 },
  { x: 5.1,   y: 2.08 },
  { x: 0.65,  y: 3.55 },
  { x: 5.1,   y: 3.55 },
];

reasons.forEach((r, i) => {
  const { x, y } = grid[i];
  contentCard(s3, x, y, 4.15, 1.28, r.topC);
  s3.addText(r.num, {
    x: x+0.22, y: y+0.12, w: 0.5, h: 0.35,
    fontSize: 20, fontFace: "Calibri", bold: true, color: r.topC, margin: 0,
  });
  s3.addText(r.title, {
    x: x+0.72, y: y+0.14, w: 3.2, h: 0.32,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.primary, margin: 0,
  });
  s3.addText(r.desc, {
    x: x+0.22, y: y+0.54, w: 3.7, h: 0.62,
    fontSize: 10, fontFace: "Calibri", color: C.foreground, margin: 0,
  });
});

// Footer CTA
s3.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.1, w: 10, h: 0.525, fill: { color: C.primary } });
s3.addText("Interested? Let\u2019s talk.  \u2192  jordan@massageclub.io", {
  x: 0.65, y: 5.2, w: 6, h: 0.28,
  fontSize: 10, fontFace: "Calibri", color: C.accent, margin: 0,
});
s3.addText("03", {
  x: 9.1, y: 5.2, w: 0.5, h: 0.28,
  fontSize: 9, fontFace: "Calibri", color: "A07070", align: "right", margin: 0,
});

// Save
pres.writeFile({ fileName: "/Users/jordan/workspace/007-Axton/massage-club/massage_club_cofounder_deck.pptx" })
  .then(() => console.log("Done"))
  .catch(e => console.error(e));