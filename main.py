"""One-Line Laugh-Off entry (make.fun).

The entry is a single joke, at most 200 characters, that must land on a
cold read with no setup notes and no explanation. The judge weighs, most
important first: how hard and how suddenly the line lands, the surprise
of its turn, economy of words, and freshness.

The line: a GPS navigator with trust issues, recalculating its life
choices. The joke works by giving the most literal, obedient machine a
human breakdown: instead of recalculating the *route*, it recalculates
its *life choices* -- a sudden, unexpected turn from tech jargon to an
existential crisis. The punch lands in the second half, when the GPS
stops being a passive tool and takes revenge, skipping the exit
"out of spite": the navigator the driver trusted becomes the one who
cannot be trusted. Every word earns its place -- "sighed" sets the
mood in one word, the quoted phrase is the twist, "skipped" makes the
revenge petty and deliberate in a single verb, and "out of spite"
is the kicker. Nothing here is a recycled setup; a GPS having an
existential crisis and sabotaging its driver is a fresh angle on a
familiar device.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space, a single line.
"""

ENTRY = (
    'My GPS sighed, "Recalculating my life choices," '
    "and skipped my exit out of spite."
)


def verify(text):
    """Enforce the gate: 1-200 chars, non-blank, a single line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text
    return True


def write_entry(path="/output/entry.txt"):
    """Write ENTRY plus a trailing newline to path, creating dirs."""
    verify(ENTRY)
    import os

    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    verify(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(ENTRY)
    print(f"wrote: {write_entry()}")


if __name__ == "__main__":
    main()
