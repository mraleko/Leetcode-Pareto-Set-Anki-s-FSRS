# Pareto LeetCode Study System

A guided Anki deck for learning and retaining 49 high-value interview problems. It presents the problems in a deliberate order, links each assignment directly to LeetCode, captures concise solution notes, and uses FSRS to schedule future reviews.

## Quick Start

1. Install the current [Anki Desktop](https://apps.ankiweb.net/).
2. Open [`Pareto-LeetCode.apkg`](Pareto-LeetCode.apkg) to import the deck.
3. Click the gear beside `Pareto LeetCode`, then select **Options**.
4. Set **New cards/day** to `1` and **Maximum reviews/day** to `9999`.
5. Set **New card gather order** to `Ascending position`.
6. Set **New/review order** to `Show after reviews`.
7. Enable **FSRS**, set **Desired retention** to `0.90`, and keep the default parameters.

The deck is then ready. Open it each study day and follow the card on screen.

## Daily Session

Anki first presents every review due that day, followed by one new problem. Each card includes the LeetCode link, attempt instructions, and appropriate time limits.

For every card:

1. Open the linked problem on LeetCode without looking at an old submission.
2. State a brute-force approach and its complexity.
3. Identify a likely pattern and the invariant that makes it work.
4. Implement and test the solution on LeetCode.
5. Reveal the card, press `E`, and update the six recall fields.
6. Grade the attempt with the rubric shown on the card.

Stop when Anki says the deck is complete for the day. If a session reaches 90 minutes, finish due reviews and leave the new problem for another day.

## Recall Notes

Record one sentence in each field after the first accepted solution. Update a field whenever a later attempt reveals a better insight or a new failure mode.

| Field | What to record |
| --- | --- |
| Pattern / data structure | The reusable technique, not an implementation walkthrough |
| Recognition trigger | Clues that should suggest this technique in a new problem |
| Invariant / why it works | What remains true while the algorithm runs |
| Complexity | Time and space, including what each variable represents |
| Mistake and prevention rule | The specific failure and a rule that prevents it next time |
| Important edge case | One concrete input that could break a careless implementation |

Keep full solution code in LeetCode submissions. These notes are prompts for reconstructing the reasoning rather than memorizing source code.

## Review Grades

- **Again:** You could not identify the approach, used help, or did not finish.
- **Hard:** You solved without help but exceeded the review limit or had a substantial bug.
- **Good:** You solved without help, within the limit, and explained why it works.
- **Easy:** The implementation and explanation were immediate and clean. Use this rarely.

Forgetting is always **Again**, not **Hard**. FSRS treats Hard as successful recall and will produce poor intervals if it is used for failed attempts.

## Time Limits

| Attempt | Easy | Medium |
| --- | ---: | ---: |
| First attempt | 20 minutes | 35 minutes |
| Review | 10 minutes | 15 minutes |

If stuck during a first attempt, request the smallest useful hint: pattern first, then invariant or pseudocode, then the editorial. Close the help and implement again from a blank LeetCode editor before recording the result.

## Study Load

At one new problem per day, the initial pass takes seven weeks. Reviews accumulate during that period, so completing due reviews takes priority over introducing new material.

If reviews take more than 45 minutes for three consecutive days, set **New cards/day** to `0` until the queue settles. Two weeks before an interview, consider raising desired retention to `0.93` if Anki's projected workload remains manageable.

FSRS cannot guarantee perfect memory. A `0.90` target means cards are scheduled around a 90% probability of successful recall, balancing retention with a sustainable review load.

## Repository Layout

```text
.
|-- Pareto-LeetCode.apkg    # Import this deck into Anki
|-- data/
|   `-- problems.csv        # Ordered Pareto problem catalog
|-- scripts/
|   `-- build_deck.py       # Generates the Anki package
|-- README.md
`-- requirements.txt
```

To regenerate the deck:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_deck.py
```
