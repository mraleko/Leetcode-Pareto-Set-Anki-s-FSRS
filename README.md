# Pareto LeetCode Study System

This folder gives you one source of truth for progress and one scheduler for reviews:

- `pareto-tracker.csv`: the 49 problems from the image, in order, with direct LeetCode links.
- `anki-import.tsv`: recall cards for Anki's FSRS scheduler.
- Anki decides **when** to review. The tracker records **what happened**. Do not manually schedule review dates in the tracker.

No system can guarantee that you will "never forget" a solution. FSRS estimates when recall is becoming less likely and schedules retrieval practice before too much is lost. A 90% target deliberately permits some forgetting because trying to force 100% creates an unmanageable number of reviews.

## One-Time Setup

### 1. Tracker

Open `pareto-tracker.csv` in Google Sheets, Excel, or Numbers. In Google Sheets, use **File > Import > Upload > Replace spreadsheet**. Freeze row 1 and turn on a filter.

Use these exact status values:

- `Not Started`: no serious attempt yet.
- `Learning`: attempted but needed a hint, editorial, or solution.
- `Review`: accepted once and added to Anki.
- `Interview Ready`: independently accepted from scratch on two separate days, with a clear explanation of complexity and edge cases.

`Solved_Independently` means no hints, notes, old submissions, or autocomplete from a previous solution. An accepted result after reading a solution is useful learning, but it is not independent.

### 2. Anki and FSRS

1. Install [Anki Desktop](https://apps.ankiweb.net/). Use a current release with FSRS support.
2. In Anki, choose **File > Import** and select `anki-import.tsv`.
3. Confirm note type `Basic`, deck `Pareto LeetCode`, HTML enabled, and columns mapped to `Front`, `Back`, and `Tags`.
4. Open **Browse**, select the new `Pareto LeetCode` deck, select all cards, and choose **Cards > Toggle Suspend**. All 49 should initially appear yellow/suspended.
5. Open the deck's **Options**. Enable FSRS if it is not already enabled, set desired retention to `0.90`, and leave the FSRS parameters at their defaults until you have substantial review history.
6. Set new cards/day high enough that it is not a bottleneck; suspended cards will still keep unseen problems out of reviews.

Only unsuspend a card after the corresponding problem has an accepted submission and you understand the solution. This prevents Anki from treating an unseen problem as a failed memory.

After the first accepted solve, edit that card's `Back` and replace the placeholder with your own 2-5 bullets:

```text
Pattern/data structure:
Key invariant or decision:
Edge case I missed:
Time: O(...), Space: O(...)
```

Do not paste full solution code. The goal is to remember a reusable idea and reconstruct an implementation, not memorize lines.

## Daily Workflow

Do all due Anki reviews **before** learning a new problem. Reviews are the commitment; new problems are optional when the review queue is not clear.

For each new problem, work in the order listed in the tracker:

1. Open its `LeetCode_URL`; code only in LeetCode.
2. Spend 3-5 minutes restating inputs, outputs, constraints, and examples.
3. Attempt without help: up to 20 minutes for Easy or 35 minutes for Medium.
4. If stuck, seek the smallest useful hint first: pattern, then invariant/pseudocode, then editorial. Avoid passively watching a complete solution.
5. After using help, close it and produce an accepted solution again from a blank LeetCode editor.
6. Fill the tracker while the mistake is fresh. `Key_Insight` and `Mistake_or_Gap` should each be one specific sentence.
7. Change status to `Review`, update the card's Back, and unsuspend it in Anki.

Stop after 75-90 focused minutes. Consistency and honest review grades beat high problem counts.

## How to Review a Card

Before revealing the back:

1. Open the linked LeetCode problem without opening an old submission.
2. State the pattern, invariant, complexity, and important edge cases.
3. Implement from the provided signature in a blank editor. Use a 10-minute cap for Easy and 15 minutes for Medium during reviews.
4. Reveal your card, compare with your tracker/accepted submission, and grade the attempt honestly.

Use Anki's buttons this way:

- **Again**: could not identify the approach, used notes/hints, or produced a fundamentally wrong solution.
- **Hard**: right approach but needed more than the time cap, had a significant bug, or missed an important edge case/complexity.
- **Good**: independently implemented a correct solution within the cap and explained why it works.
- **Easy**: immediate, clean, correct implementation and explanation with substantial time left. Use this rarely.

If you press **Again** or **Hard**, update `Mistake_or_Gap` with the new failure mode. Do not reset or manually reschedule the card; FSRS adapts from your grade.

## Seven-Week Ramp

Aim for seven new problems per week while keeping every due review current. This completes the set in seven weeks:

| Week | Problems | Topics |
| --- | --- | --- |
| 1 | 1-7 | Arrays & Hashing |
| 2 | 8-14 | Arrays, Two Pointers, Sliding Window |
| 3 | 15-21 | Sliding Window, Stack, Binary Search |
| 4 | 22-28 | Linked Lists, first Tree problem |
| 5 | 29-35 | Trees |
| 6 | 36-42 | Trees, Heap / Priority Queue |
| 7 | 43-49 | Graphs |

A sustainable week is five learning days with one new problem each, one weekend session with two new problems, and one catch-up/rest day. If due reviews exceed about 45 minutes for three days in a row, stop adding new cards until the queue settles.

## Interview Phase

After all 49 are introduced, keep doing FSRS reviews and add two 45-minute mock sessions per week:

- Pick an unseen or forgotten Easy/Medium rather than a card that is already due.
- Spend 5 minutes clarifying, 25-30 minutes coding, and 10 minutes testing/explaining.
- Practice narrating tradeoffs and tests; interview performance is broader than recalling these 49 solutions.

Two weeks before an interview, raise desired retention from `0.90` to `0.93` if the projected workload in Anki remains manageable. Do not use `1.00`.
