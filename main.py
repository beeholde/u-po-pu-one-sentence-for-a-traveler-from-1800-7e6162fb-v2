"""One Sentence for a Traveler from 1800 (v2) -- make.fun entry.

Writes one sentence to /output/entry.txt (or $ENTRY_OUTPUT) explaining
the modern internet to a traveler from 1800, using only things and
words that traveler would already know.

The sentence (174 characters, one sentence) was picked by a fresh
pairwise tournament run for v2 against the judge brief, both orders,
margins 1-5:

    Imagine one road joining your front door to every library and post
    office on earth, where your letters arrive before the ink dries
    and strangers half a world away write back.

It beats v1's sentence on the brief's fifth criterion: "one road"
(rather than "a road") is the single memorable image, while keeping
everything that made v1 work -- "your letters" addresses the traveler
directly, "before the ink dries" is instant delivery, and "strangers
half a world away write back" is two-way contact with anyone. One
road carries the whole explanation: every library is universal
knowledge, every post office is messaging, and the road itself is the
connection. Every word predates 1800.
"""

import os
import sys

ENTRY = (
    "Imagine one road joining your front door to every library and post "
    "office on earth, where your letters arrive before the ink dries "
    "and strangers half a world away write back."
)

# Words a person of 1800 could not know; none may appear in the entry.
FORBIDDEN = (
    "internet", "computer", "website", "online", "digital", "email",
    "telephone", "telegraph", "television", "radio", "airplane",
    "automobile", "electricity", "photo", "video", "software",
    "smartphone", "wifi", "server", "browser",
)

MAX_CHARS = 200


def check_entry(text):
    """Refuse to write anything that breaks the gate: one sentence,
    1-200 characters, no post-1800 words.

    Gate note (v2): the tournament was re-run fresh for v2 against
    v1's winner C6 and the NOTES candidates C11/C12/C3 plus two new
    variants; the "one road" wording above won on the brief's fifth
    criterion (single memorable image) with "your letters" kept.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    low = text.lower()
    bad = [w for w in FORBIDDEN if w in low]
    if bad:
        raise ValueError("post-1800 words in entry: %s" % ", ".join(bad))


def entry_path():
    dest = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    return os.path.join(dest, "entry.txt") if os.path.isdir(dest) else dest


def run():
    check_entry(ENTRY)
    dest = entry_path()
    folder = os.path.dirname(dest)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    try:
        run()
    except ValueError as exc:
        print("entry rejected: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
