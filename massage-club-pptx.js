const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "Massage Club — One Pager";

// Massage Pass / Vercel theme — near-black bg, green accent, minimal
const C = {
  bg: "0A0A0A",
  surface: "111111",
  surface2: "1A1A1A",
  border: "1A1A1A",
  text: "FFFFFF",
  muted: "888888",
  subtle: "555555",
  accent: "4ADE80",   // green from Vercel site
  accentDim: "0f1a14",
  white: "FFFFFF",
};

var s = pres.addSlide();
s.background = { color: C.bg };

// Top accent strip — green
s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.05, fill: { color: C.accent } });

// Nav-like top bar
s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0.05, w: 10, h: 0.5, fill: { color: C.surface } });
s.addText("MASSAGE CLUB", {
  x: 0.7, y: 0.12, w: 3, h: 0.3,
  fontSize: 9, color: C.accent, bold: true, charSpacing: 4, margin: 0,
});
s.addText("ONE PAGER", {
  x: 7.5, y: 0.12, w: 2, h: 0.3,
  fontSize: 9, color: C.subtle, align: "right", charSpacing: 4, margin: 0,
});

// Hero section
s.addText("Find the best massage\ntherapists in Madrid.", {
  x: 0.7, y: 0.7, w: 8.5, h: 1.1,
  fontSize: 40, color: C.white, bold: true, margin: 0,
});

// Green badge
s.addShape(pres.shapes.RECTANGLE, { x: 0.7, y: 1.88, w: 2.2, h: 0.3, fill: { color: C.accentDim }, line: { color: C.accent, width: 0.5 } });
s.addText("LAUNCHING APRIL 24, 2026", {
  x: 0.7, y: 1.88, w: 2.2, h: 0.3,
  fontSize: 7, color: C.accent, bold: true, align: "center", valign: "middle", margin: 0,
});

// Divider
s.addShape(pres.shapes.RECTANGLE, { x: 0.7, y: 2.35, w: 8.6, h: 0.01, fill: { color: C.border } });

// Three columns — Problem / Solution / Traction
const col1X = 0.7;
const col2X = 3.6;
const col3X = 6.5;

// Problem — orange accent
s.addText("THE PROBLEM", {
  x: col1X, y: 2.55, w: 2.6, h: 0.25,
  fontSize: 8, color: "FB923C", bold: true, charSpacing: 4, margin: 0,
});
s.addShape(pres.shapes.RECTANGLE, { x: col1X, y: 2.82, w: 0.6, h: 0.025, fill: { color: "FB923C" } });
s.addText([
  { text: "Booking a therapist means platform fees (30–40%)", options: { bullet: true, breakLine: true } },
  { text: "No direct channel for therapists to build their own clients", options: { bullet: true, breakLine: true } },
  { text: "Clients trust the app, not the therapist", options: { bullet: true, breakLine: true } },
  { text: "Discovery is fragmented — FB, Google, Walk-ins", options: { bullet: true } },
], {
  x: col1X, y: 2.93, w: 2.6, h: 2,
  fontSize: 10, color: "CBD5E1", paraSpaceAfter: 5, margin: 0,
});

// Solution — green accent
s.addText("THE SOLUTION", {
  x: col2X, y: 2.55, w: 2.6, h: 0.25,
  fontSize: 8, color: C.accent, bold: true, charSpacing: 4, margin: 0,
});
s.addShape(pres.shapes.RECTANGLE, { x: col2X, y: 2.82, w: 0.6, h: 0.025, fill: { color: C.accent } });
s.addText([
  { text: "Massage Club — subscription pass (€49/mo)", options: { bullet: true, breakLine: true } },
  { text: "Direct booking — therapist keeps 100%", options: { bullet: true, breakLine: true } },
  { text: "Partner studios onboarded via Supabase", options: { bullet: true, breakLine: true } },
  { text: "Whova/Eventbrite integration for B2B events", options: { bullet: true } },
], {
  x: col2X, y: 2.93, w: 2.6, h: 2,
  fontSize: 10, color: "CBD5E1", paraSpaceAfter: 5, margin: 0,
});

// Traction — blue accent
s.addText("TRACTON", {
  x: col3X, y: 2.55, w: 2.6, h: 0.25,
  fontSize: 8, color: "60A5FA", bold: true, charSpacing: 4, margin: 0,
});
s.addShape(pres.shapes.RECTANGLE, { x: col3X, y: 2.82, w: 0.6, h: 0.025, fill: { color: "60A5FA" } });
s.addText([
  { text: "Madrid leads cron running daily (job: 1bdcb5a0900e)", options: { bullet: true, breakLine: true } },
  { text: "FB groups + Spanish forums as sourcing channel", options: { bullet: true, breakLine: true } },
  { text: "Niah pipeline — event networking + B2B leads", options: { bullet: true, breakLine: true } },
  { text: "Vercel deployed, Supabase backend", options: { bullet: true } },
], {
  x: col3X, y: 2.93, w: 2.6, h: 2,
  fontSize: 10, color: "CBD5E1", paraSpaceAfter: 5, margin: 0,
});

// Bottom stats bar
s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.0, w: 10, h: 0.625, fill: { color: C.surface } });

const stats = [
  ["Madrid", "Primary market"],
  ["€49/mo", "Subscription model"],
  ["Niah + events", "B2B channel"],
  ["Direct booking", "100% to therapist"],
];
stats.forEach(([num, label], i) => {
  const sx = 0.7 + i * 2.35;
  s.addText(num, {
    x: sx, y: 5.04, w: 2, h: 0.3,
    fontSize: 13, bold: true, color: C.accent, margin: 0,
  });
  s.addText(label, {
    x: sx, y: 5.32, w: 2, h: 0.22,
    fontSize: 8, color: C.muted, margin: 0,
  });
});

// Slide number
s.addText("01", {
  x: 9.2, y: 5.12, w: 0.6, h: 0.28,
  fontSize: 9, color: C.subtle, align: "right", margin: 0,
});

// Save
pres.writeFile({ fileName: "/Users/jordan/workspace/007-Axton/massage-club/Massage-Club-One-Pager.pptx" })
  .then(() => console.log("Done"))
  .catch(e => console.error(e));