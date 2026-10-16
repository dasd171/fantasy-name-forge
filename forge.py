import random, argparse
STYLES = {
 "elf": (["Ae", "Ela", "Fae", "Lir", "Syl", "Thal", "Ari", "Cel"], ["dri", "wen", "ion", "riel", "ndor", "thas", "lith", "mir"]),
 "dwarf": (["Bal", "Dur", "Gim", "Thor", "Brom", "Kaz", "Dvar", "Grun"], ["in", "grim", "dek", "rak", "dun", "bor", "li", "mund"]),
 "orc": (["Gr", "Ur", "Mog", "Zug", "Krag", "Gash", "Rok", "Thr"], ["ash", "nak", "gul", "mash", "tok", "zog", "uk", "dush"])}
TITLES = ["of the Silver Moon", "the Unbroken", "Ironbeard", "Storm-Caller", "the Wanderer", "Bone-Crusher", "the Quiet"]
if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("style", nargs="?", default="elf", choices=STYLES); p.add_argument("-n", type=int, default=5)
    a = p.parse_args(); pre, suf = STYLES[a.style]
    for _ in range(a.n): print(f"⚔️  {random.choice(pre)}{random.choice(suf)} {random.choice(TITLES)}")
