# Figures of the S2 course (cartographie, risques, diagnostic), drawn in two modules.
FIGS = {}
for _mod in ('cours_figures_s2_a', 'cours_figures_s2_b'):
    try:
        FIGS.update(__import__(_mod).FIGS)
    except ImportError:
        pass
