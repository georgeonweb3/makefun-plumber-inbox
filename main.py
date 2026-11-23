"""The Plumber's Inbox: A 120-Word Cold Email — make.fun entry.

Writes one cold email of about 120 words, subject line included,
pitching a bookkeeping service to a busy plumber, to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    'Subject: Your invoices, done before your tea goes cold\n'
    "\n"
    "Hi — I know your day starts before six, the call-outs never stop, "
    "and the paperwork waits until night. I take that night pile off "
    "plumbers: invoices sent, receipts chased, VAT sorted, and your books "
    "ready for your accountant, every month.\n"
    "\n"
    "One fixed price: £95 a month, no hourly billing, no long contract. "
    "The first month is free while we tidy your last three months "
    "together. Most plumbers I work with save about four hours a week, "
    "and your evenings stay yours.\n"
    "\n"
    'If it sounds useful, reply "yes" and I will send a two-minute setup '
    "link. No call needed unless you would like one.\n"
    "\n"
    "Thanks for your time,\n"
    "Sarah — ClearBooks Bookkeeping"
)

# The brief asks for about 120 words, subject line included. Guard the
# count at runtime so a future wording tweak that drifts off-brief fails
# loudly instead of silently submitting a wrong-length email.
WORD_TARGET = 120
WORD_WINDOW = 10


def main() -> None:
    words = ENTRY.split()
    if not WORD_TARGET - WORD_WINDOW <= len(words) <= WORD_TARGET + WORD_WINDOW:
        raise ValueError(
            f"entry is {len(words)} words, expected about {WORD_TARGET}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
