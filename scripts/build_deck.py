import csv
import html
from pathlib import Path

import genanki


ROOT = Path(__file__).resolve().parents[1]

MODEL = genanki.Model(
    1846359201,
    "Pareto LeetCode Recall",
    fields=[
        {"name": "Order"},
        {"name": "Problem"},
        {"name": "Category"},
        {"name": "Difficulty"},
        {"name": "URL"},
        {"name": "Pattern"},
        {"name": "RecognitionTrigger"},
        {"name": "Invariant"},
        {"name": "Complexity"},
        {"name": "MistakeAndFix"},
        {"name": "EdgeCase"},
    ],
    templates=[
        {
            "name": "Solve and Recall",
            "qfmt": """
<div class="eyebrow">PARETO {{Order}} / 49</div>
<div class="meta"><span>{{Category}}</span><span class="{{Difficulty}}">{{Difficulty}}</span></div>
<h1>{{Problem}}</h1>
<a class="button" href="{{URL}}">Open problem on LeetCode</a>

<section class="mission">
  <h2>Do this now</h2>
  <ol>
    <li>Open the problem. Do not open old submissions or notes.</li>
    <li>Say the brute force approach and its complexity out loud.</li>
    <li>Identify the likely pattern and the invariant that makes it work.</li>
    <li>Implement and test in LeetCode.</li>
  </ol>
</section>

<div class="timers">
  <div><b>First attempt</b><br>Easy: 20 min<br>Medium: 35 min</div>
  <div><b>Review</b><br>Easy: 10 min<br>Medium: 15 min</div>
</div>

<p class="rule"><b>If stuck:</b> get only the smallest hint needed. After reading help, close it and implement again from a blank editor.</p>
<p class="footer">Do not reveal the back until the attempt is finished.</p>
""",
            "afmt": """
<div class="eyebrow">RECALL SHEET</div>
<h1>{{Problem}}</h1>
<p class="edit"><b>After your first solve:</b> press <kbd>E</kbd> and fill every field below in your own words. Keep each answer to one sentence. Never paste full code.</p>

<section class="notes">
  <h3>1. Pattern / data structure</h3>
  {{#Pattern}}<div>{{Pattern}}</div>{{/Pattern}}
  {{^Pattern}}<div class="missing">What reusable technique did you use?</div>{{/Pattern}}

  <h3>2. Recognition trigger</h3>
  {{#RecognitionTrigger}}<div>{{RecognitionTrigger}}</div>{{/RecognitionTrigger}}
  {{^RecognitionTrigger}}<div class="missing">Which clues in a new problem should make you consider this pattern?</div>{{/RecognitionTrigger}}

  <h3>3. Invariant / why it works</h3>
  {{#Invariant}}<div>{{Invariant}}</div>{{/Invariant}}
  {{^Invariant}}<div class="missing">What remains true as the algorithm runs?</div>{{/Invariant}}

  <h3>4. Complexity</h3>
  {{#Complexity}}<div>{{Complexity}}</div>{{/Complexity}}
  {{^Complexity}}<div class="missing">Write time and space complexity, including what each variable means.</div>{{/Complexity}}

  <h3>5. Mistake and prevention rule</h3>
  {{#MistakeAndFix}}<div>{{MistakeAndFix}}</div>{{/MistakeAndFix}}
  {{^MistakeAndFix}}<div class="missing">What specifically went wrong, and what rule will prevent it next time?</div>{{/MistakeAndFix}}

  <h3>6. Important edge case</h3>
  {{#EdgeCase}}<div>{{EdgeCase}}</div>{{/EdgeCase}}
  {{^EdgeCase}}<div class="missing">Name one input that could break a careless implementation.</div>{{/EdgeCase}}
</section>

<section class="grading">
  <h2>Grade this attempt</h2>
  <div><b>Again</b> Could not find the approach, used help, or did not finish.</div>
  <div><b>Hard</b> Correct without help, but over time or with a substantial bug.</div>
  <div><b>Good</b> Correct without help, within time, and explained why it works.</div>
  <div><b>Easy</b> Immediate, clean, correct, and clearly explained. Use rarely.</div>
</section>
<p class="footer">If you forgot, use Again, not Hard. FSRS treats Hard as successful recall.</p>
""",
        }
    ],
    css="""
.card {
  background: #0c1424;
  color: #e9eef8;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 17px;
  line-height: 1.5;
  margin: 0 auto;
  max-width: 720px;
  padding: 28px 22px 48px;
  text-align: left;
}
.eyebrow { color: #35bdf3; font-size: 13px; font-weight: 800; letter-spacing: .14em; }
.meta { display: flex; gap: 8px; margin-top: 14px; }
.meta span { background: #1a263b; border-radius: 999px; color: #b9c7dc; font-size: 13px; padding: 5px 10px; }
.meta .Easy { color: #75dc9a; }
.meta .Medium { color: #ffb85c; }
h1 { font-size: 32px; line-height: 1.12; margin: 14px 0 22px; }
h2 { font-size: 20px; margin: 0 0 10px; }
h3 { color: #9eabc0; font-size: 13px; letter-spacing: .04em; margin: 22px 0 6px; text-transform: uppercase; }
.button { background: #20aee9; border-radius: 8px; color: #07111d !important; display: inline-block; font-weight: 800; padding: 11px 16px; text-decoration: none; }
.mission, .grading { background: #121f33; border: 1px solid #263753; border-radius: 12px; margin-top: 24px; padding: 18px 20px; }
ol { margin: 0; padding-left: 23px; }
li { margin: 8px 0; }
.timers { display: grid; gap: 10px; grid-template-columns: 1fr 1fr; margin-top: 12px; }
.timers div { background: #18283e; border-radius: 10px; padding: 14px; }
.rule, .edit { background: #332714; border-left: 4px solid #ffb34c; margin-top: 18px; padding: 12px 14px; }
.notes { background: #111c2e; border-radius: 12px; margin-top: 18px; padding: 4px 20px 24px; }
.missing { color: #ffbd68; font-style: italic; }
.grading div { border-top: 1px solid #2b3a51; padding: 9px 0; }
.grading div:first-of-type { border-top: 0; }
.footer { color: #8795aa; font-size: 14px; margin-top: 20px; text-align: center; }
kbd { background: #e7edf7; border-radius: 4px; color: #152033; font-size: 14px; padding: 2px 6px; }
@media (max-width: 480px) {
  .card { font-size: 16px; padding: 20px 14px 40px; }
  h1 { font-size: 27px; }
  .timers { grid-template-columns: 1fr; }
}
""",
)

DECK = genanki.Deck(
    1764205839,
    "Pareto LeetCode",
    description=(
        "One ordered problem per day plus FSRS-scheduled reviews. "
        "Solve using the LeetCode link, record six short recall notes, and grade honestly."
    ),
)

with (ROOT / "data" / "problems.csv").open(newline="", encoding="utf-8") as source:
    for row in csv.DictReader(source):
        order = int(row["Order"])
        note = genanki.Note(
            model=MODEL,
            fields=[
                f"{order:02d}",
                html.escape(row["Problem"]),
                html.escape(row["Category"]),
                row["Difficulty"],
                row["LeetCode_URL"],
                "",
                "",
                "",
                "",
                "",
                "",
            ],
            tags=[
                "pareto",
                row["Category"].lower().replace(" & ", "_").replace(" / ", "_").replace(" ", "_"),
                row["Difficulty"].lower(),
                f"p{order:02d}",
            ],
            guid=genanki.guid_for("pareto-leetcode", str(order)),
            due=order,
        )
        DECK.add_note(note)

genanki.Package(DECK).write_to_file(ROOT / "Pareto-LeetCode.apkg")
