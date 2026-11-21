import sys, wave, subprocess, os
import numpy as np
from PIL import Image

out = sys.argv[1]

# ---------- sprites: original pixel art (half-grids, mirrored) ----------
def build(rows, palette, scale):
    full = [r + r[::-1] for r in rows]
    h, w = len(full), len(full[0])
    img = Image.new("RGBA", (w * scale, h * scale), (0, 0, 0, 0))
    px = img.load()
    for y, row in enumerate(full):
        for x, ch in enumerate(row):
            if ch in palette:
                for dy in range(scale):
                    for dx in range(scale):
                        px[x * scale + dx, y * scale + dy] = palette[ch]
    return img

CY = (64, 224, 255, 255); CYD = (20, 130, 190, 255)
MG = (255, 70, 200, 255); MGD = (160, 30, 120, 255)
LM = (150, 255, 90, 255); LMD = (60, 160, 50, 255)
OR = (255, 150, 40, 255); WH = (255, 255, 255, 255); DK = (20, 10, 40, 255)
PU = (150, 100, 255, 255); PUD = (80, 50, 170, 255); GD = (255, 220, 80, 255)

# jellyfish-orb (lowest score)
a1 = ["....aaaa",
      "..aaaaaa",
      ".abbbbbb",
      ".abwwbbb",
      ".abwkbbb",
      ".abbbbbb",
      "..a.a.a.",
      ".a.a.a.a",
      ".a..a..a"]
build(a1, {"a": LMD, "b": LM, "w": WH, "k": DK}, 3).save(f"{out}/Graphics/alien_1.png")

# bat-wing manta (mid)
a2 = ["aa......",
      ".aaa....",
      "..aabbbb",
      "abbbbbbb",
      "abbbwkbb",
      ".abbbbbb",
      "..a.abbb",
      "......ab"]
build(a2, {"a": MGD, "b": MG, "w": WH, "k": DK}, 3).save(f"{out}/Graphics/alien_2.png")

# crystal gem (highest)
a3 = ["......aa",
      ".....abb",
      "....abbw",
      "...abbwb",
      "..abbbbb",
      ".abbbbbb",
      "abbbbkkb",
      ".abbbbbb",
      "..abbbbb",
      "...abbbb",
      "....abbb",
      ".....abb",
      "......aa"]
build(a3, {"a": CYD, "b": CY, "w": WH, "k": DK}, 3).save(f"{out}/Graphics/alien_3.png")

# player fighter (arrow shape)
sp = ["........",
      "........",
      ".......a",
      "......ab",
      ".....abb",
      "...aabbw",
      "..abbbbb",
      "aabbobbb",
      "abbbbbbb",
      "ab.ab..a"]
sp = ["........",
      ".......a",
      ".......b",
      "......ab",
      "....aabb",
      "..aabbbw",
      ".abbbbbb",
      "abbbobbb",
      "abbbbbbb",
      "ab.abb.."]
build(sp, {"a": PUD, "b": PU, "w": WH, "o": OR}, 4).save(f"{out}/Graphics/spaceship.png")

# bonus ship (gold capsule)
my = ["........aaaa",
      ".....aabbbbb",
      "..aabbbbwbbb",
      ".abbkbbkbbkb",
      "aabbbbbbbbbb",
      "..aa.aa.aa.a"]
build(my, {"a": (170, 110, 20, 255), "b": GD, "w": WH, "k": (120, 60, 10, 255)}, 4).save(f"{out}/Graphics/mystery.png")

# ---------- sounds: synthesized from scratch ----------
SR = 22050
def save(name, data):
    data = np.clip(data, -1, 1)
    pcm = (data * 32767 * 0.8).astype(np.int16)
    wav = f"{out}/Sounds/{name}.wav"
    with wave.open(wav, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

def tone(freq, dur, shape="square", vol=1.0):
    t = np.arange(int(SR * dur)) / SR
    ph = 2 * np.pi * np.cumsum(np.broadcast_to(freq, t.shape)) / SR
    if shape == "square": s = np.sign(np.sin(ph))
    elif shape == "tri": s = 2 / np.pi * np.arcsin(np.sin(ph))
    else: s = np.sin(ph)
    return s * vol

# laser: quick downward "pew"
d = 0.22; t = np.arange(int(SR * d)) / SR
save("laser", tone(1400 * np.exp(-t * 9) + 250, d, "sine") * np.exp(-t * 10))

# explosion: filtered noise burst
rng = np.random.default_rng(7)
d = 0.55; n = int(SR * d); t = np.arange(n) / SR
noise = rng.uniform(-1, 1, n)
k = 24; noise = np.convolve(noise, np.ones(k) / k, mode="same")
save("explosion", (noise * 2.5 + tone(90 * np.exp(-t * 4) + 40, d, "sine") * 0.8) * np.exp(-t * 5))

# music: 8-bar loop, A minor, bass + arpeggio + soft pad
bpm = 112; beat = 60 / bpm; step = beat / 2
notes = {"A2": 110.0, "F2": 87.31, "C3": 130.81, "G2": 98.0}
prog = ["A2", "A2", "F2", "F2", "C3", "C3", "G2", "G2"]
arp_scale = {"A2": [220, 261.63, 329.63, 440], "F2": [174.61, 220, 261.63, 349.23],
             "C3": [261.63, 329.63, 392, 523.25], "G2": [196, 246.94, 293.66, 392]}
track = []
for root in prog:
    bar = np.zeros(int(SR * beat * 4))
    for i in range(8):
        f = arp_scale[root][[0, 1, 2, 3, 2, 1, 2, 3][i]]
        seg = tone(f, step, "tri", 0.22)
        env = np.exp(-np.arange(len(seg)) / SR * 6)
        a = int(i * step * SR); bar[a:a + len(seg)] += (seg * env)[:len(bar) - a]
    for b in range(4):
        seg = tone(notes[root], beat * 0.9, "square", 0.18)
        env = np.exp(-np.arange(len(seg)) / SR * 3)
        a = int(b * beat * SR); bar[a:a + len(seg)] += (seg * env)[:len(bar) - a]
    track.append(bar)
save("music", np.concatenate(track) * 0.9)
