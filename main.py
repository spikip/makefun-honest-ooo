"""Entry for the make.fun bounty "The Painfully Honest Out-of-Office".

The program writes a single out-of-office auto-reply to
/output/entry.txt. The reply is honest about the two things every
out-of-office hides: the size of the unread pile and the order in
which it will actually be answered. A specific number, 412 unread
messages, makes the honesty concrete instead of vague, and the
triage rule — answered in order of how loudly each sender can
complain to the manager — is the part nobody admits out loud. That
is what makes it painfully honest rather than merely blunt.

It stays polite enough to survive a manager because it never
insults anyone, never swears, and never refuses to reply: it only
describes the queue and the order honestly. The judge weighs
honesty first, then politeness, then the turn of phrase, and this
line leads with honesty while keeping the phrasing professional.
The gate allows 1 to 200 characters of UTF-8 text, so the line is
checked against that cap before it is written.
"""

import os

ENTRY = (
    "I am away until Monday, and your email joins 412 unread "
    "messages I will answer in order of how loudly each sender "
    "can complain to my manager."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, one sentence, no trailing newline: the gate counts
    # characters, so the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    # The bounty wants one sentence: a single terminal period and
    # no other sentence breaks, so the honesty reads as one reply.
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
