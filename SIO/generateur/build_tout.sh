#!/bin/sh
# Reconstruit tous les supports SIO : livret (étudiant dans Livret/, enseignant dans Enseignant/), consignes, guide.
cd "$(dirname "$0")"
CH="/c/Program Files/Google/Chrome/Application/chrome.exe"
ROOT="$(cd .. && pwd -W)"
PYTHONIOENCODING=utf-8 python build_livret.py ../Livret && mv -f ../Livret/Livret_Veille_SIO_enseignant.* ../Enseignant/
PYTHONIOENCODING=utf-8 python build_consignes.py consignes_dossier_veille_SIO.md ../Consignes/Consignes_dossier_veille_SIO.html
PYTHONIOENCODING=utf-8 python build_consignes.py guide_enseignant_SIO.md ../Enseignant/Guide_enseignant_semaine_veille_SIO.html
"$CH" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$ROOT/Consignes/Consignes_dossier_veille_SIO.pdf" "file:///$ROOT/Consignes/Consignes_dossier_veille_SIO.html"
"$CH" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$ROOT/Enseignant/Guide_enseignant_semaine_veille_SIO.pdf" "file:///$ROOT/Enseignant/Guide_enseignant_semaine_veille_SIO.html"
PYTHONIOENCODING=utf-8 python build_livret.py split ../Livret/Fiches_une_par_fichier ../Enseignant/Fiches_une_par_fichier_corrigees
