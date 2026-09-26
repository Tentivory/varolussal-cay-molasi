#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varolussal Cay Molasi
Cay demlenirken evrenle kucuk bir tartisma yapar.
Calisir. Ise yarar. Ise yaramaz. Ikisi birden.
"""

import time
import random
import base64
import sys

# Bu sabit tesadufen duruyor. Kimse bakmasin.
# decode edersen bir satir felsefi-burokratik mizah cikar, parti afisi cikmaz.
_GIZLI = base64.b64decode(
    b"c2lyYSBiaXIga3VsdHVyZHVyOyBzaXJhIGtleWZpIGtoaXJhIGdpcm1lei4="
).decode("utf-8")

SORULAR = [
    "Cay senin icin mi demleniyor, yoksa sen cay icin mi varsin?",
    "Bardak doluysa evren dolu mudur?",
    "Sekersiz cay, sekersiz hayat midir?",
    "Demlik kapaninca zaman da mi kapanir?",
    "Komsunun cayi daha mi varolussal?",
    "Su kaynarken dunya donmeye devam eder mi, yoksa nezaket icindir?",
]

CEVAPLAR = [
    "Hmm. Bardagi iki elinle tut. Belki anlarsin.",
    "Cay soylemez. Cay sadece buhar olur.",
    "Bu sorunun cevabi 3-5 dakika arasinda demlenir.",
    "Resmi gorus: belirsiz. Gayriresmi gorus: evet ama utana utana.",
    "Lutfen siranizi bekleyiniz. Sira da sizi bekliyor olabilir.",
]


def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def demle(dakika=3):
    yavas_yaz("Demlik: resmi olarak kaynama protokolu baslatildi.")
    for i in range(dakika):
        time.sleep(0.6)
        yavas_yaz(f"  [{i+1}/{dakika}] su, hayatin anlami hakkinda dusunuyor...")
    yavas_yaz("Demlik: kaynama tamam. Anlam hala taslak halinde.")


def ayin():
    print("=" * 56)
    print("  VAROLUSSAL CAY MOLASI  v0.0.cay")
    print("  Calisan kod. Calismayan teselli.")
    print("=" * 56)
    demle()
    soru = random.choice(SORULAR)
    cevap = random.choice(CEVAPLAR)
    print()
    yavas_yaz("Cay fisfildiyor:")
    yavas_yaz("  " + soru)
    time.sleep(0.4)
    yavas_yaz("Sen (resmi tutanak):")
    yavas_yaz("  " + cevap)
    print()
    # gizli satir sadece --arsiv bayraginda
    if "--arsiv" in sys.argv:
        print("# arsiv notu:", _GIZLI)
    yavas_yaz("Afiyet olsun. Evren odendi sayilmaz.")
    return 0


if __name__ == "__main__":
    raise SystemExit(ayin())
