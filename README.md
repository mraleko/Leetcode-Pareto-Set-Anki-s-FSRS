# Pareto LeetCode: Anki-Only System

The spreadsheet is not required. Use **Anki as the single app** for your queue, notes, progress, and spaced-repetition schedule. You will still write and submit code on LeetCode through the link on each card.

The deck contains all 49 problems in order. Every card tells you what to do, how long to spend, exactly what to record, and how to grade the attempt. Anki's New, Learning, and Review counts are your progress tracker.

No system can literally guarantee that you never forget. FSRS schedules reviews around a target probability of recall; `0.90` is a practical balance rather than an impossible 100% promise.

## Set Up Once

1. Install the current [Anki Desktop](https://apps.ankiweb.net/).
2. Open `Pareto-LeetCode.apkg`. Anki will import a `Pareto LeetCode` deck with 49 cards.
3. Click the gear beside the deck, then **Options**.
4. Set **New cards/day** to `1` and **Maximum reviews/day** to `9999`.
5. Set **New card gather order** to `Ascending position` and **New/review order** to `Show after reviews`.
6. Enable **FSRS**, set **Desired retention** to `0.90`, and leave its parameters at the defaults for now.

Do not suspend the cards. One new card per day means Anki gives you the next problem automatically after all due reviews. Missing a day does not create a pile of new problems; continue when you return.

## Every Day

1. Open only the `Pareto LeetCode` deck.
2. Complete every due review Anki presents.
3. Complete the one new problem Anki presents.
4. Follow the instructions on the card and code through its LeetCode link.
5. On the back, press `E` and fill the six prompted note fields in your own words.
6. Choose `Again`, `Hard`, `Good`, or `Easy` using the rubric printed on the card.
7. Stop when Anki says the deck is finished for today.

If the session reaches 90 minutes, finish due reviews but postpone the new card. If reviews take more than 45 minutes for three consecutive days, temporarily set **New cards/day** to `0` until the review load settles.

## Record Only This

Each problem has six fields. Keep each to one sentence:

1. **Pattern / data structure:** the reusable technique, not a walkthrough.
2. **Recognition trigger:** clues that should make you consider that technique in a new problem.
3. **Invariant / why it works:** what remains true while the algorithm runs.
4. **Complexity:** time and space, including what variables mean.
5. **Mistake and prevention rule:** your specific failure and a rule that prevents it.
6. **Important edge case:** one concrete input that can break a careless implementation.

Do not paste solution code. Your accepted submissions already preserve code; these notes should help you reconstruct the idea.

## Grade Honestly

- **Again:** you could not find the approach, used any help, or did not finish.
- **Hard:** you solved without help but exceeded the review time limit or had a substantial bug.
- **Good:** you solved without help, within the limit, and explained why it works.
- **Easy:** the implementation and explanation were immediate and clean. Use rarely.

For FSRS, forgetting is always **Again**, never **Hard**. The Anki manual explicitly treats Hard as successful recall. After a failed review, update the mistake field before grading.

`pareto-tracker.csv` remains only as a readable backup list of links. You do not need to open or maintain it.
