# Exports the revision-card QCM (fiches_veille/fiches_*.md) to Moodle XML for the question bank.
# One sub-category per card under "Veille S1 - Fiches de revision", so a single Moodle quiz
# can draw every question (or N random per card) and give one grade.
# Usage: python build_moodle_qcm.py <out_dir> [entrainement|evaluation]
#   entrainement: QCM printed in the revision cards (fiches_veille/fiches_*.md)
#   evaluation:   separate graded bank, questions never shown to learners (qcm_eval/eval_*.md)
import glob, os, sys
from html import escape
from build_fiches import parse, inl, HERE

BANKS = {
    'entrainement': ('fiches_veille/fiches_*.md', 'Veille S1 - QCM des fiches de révision', 'veilleS1', '07_QCM_Veille_S1_Moodle.xml'),
    'evaluation': ('qcm_eval/eval_*.md', 'Veille S1 - Évaluation (questions inédites)', 'veilleS1-eval', '08_QCM_Evaluation_Veille_S1_Moodle.xml'),
    's2-entrainement': ('fiches_s2/fiches_*.md', 'SI cartographie risques S2 - QCM des fiches de cours', 'siS2', '12_QCM_SI_Cartographie_S2_Moodle.xml'),
    's2-evaluation': ('qcm_eval_s2/eval_*.md', 'SI cartographie risques S2 - Évaluation (questions inédites)', 'siS2-eval', '13_QCM_Evaluation_SI_Cartographie_S2_Moodle.xml'),
}


def cdata(s):
    return '<![CDATA[' + s.replace(']]>', ']]]]><![CDATA[>') + ']]>'


def category(path):
    return (f'  <question type="category">\n    <category><text>$course$/top/{escape(path)}</text></category>\n'
            f'    <info format="html"><text></text></info>\n  </question>\n')


def question(c, i, q, prefix):
    answers = ''.join(
        f'    <answer fraction="{100 if j == q["ok"] else 0}" format="html">\n'
        f'      <text>{cdata(inl(o))}</text>\n'
        f'      <feedback format="html"><text>{cdata("Bonne réponse." if j == q["ok"] else "Ce n’est pas la bonne réponse.")}</text></feedback>\n'
        f'    </answer>\n' for j, o in enumerate(q['opts']))
    why = f'<p>{inl(q["why"])}</p><p><em>À revoir : fiche {c["num"]}, {inl(c["title"])} (cours, chapitre {inl(c["chap"])}).</em></p>'
    return (f'  <question type="multichoice">\n'
            f'    <name><text>{escape(f"F{c["num"]}-Q{i} {q["q"][:60]}")}</text></name>\n'
            f'    <questiontext format="html"><text>{cdata("<p>" + inl(q["q"]) + "</p>")}</text></questiontext>\n'
            f'    <generalfeedback format="html"><text>{cdata(why)}</text></generalfeedback>\n'
            f'    <defaultgrade>1</defaultgrade>\n    <penalty>0</penalty>\n    <hidden>0</hidden>\n'
            + ('' if FLAT else f'    <idnumber>{prefix}-f{c["num"]}-q{i}</idnumber>\n') +
            f'    <single>true</single>\n    <shuffleanswers>true</shuffleanswers>\n    <answernumbering>ABCD</answernumbering>\n'
            f'    <showstandardinstruction>0</showstandardinstruction>\n'
            f'    <correctfeedback format="html"><text></text></correctfeedback>\n'
            f'    <partiallycorrectfeedback format="html"><text></text></partiallycorrectfeedback>\n'
            f'    <incorrectfeedback format="html"><text></text></incorrectfeedback>\n'
            f'{answers}  </question>\n')


def xml(cards, root, prefix):
    out = ['<?xml version="1.0" encoding="UTF-8"?>\n<quiz>\n']
    for c in cards:
        if not FLAT:  # S2 : aucune catégorie dans le fichier, l'import va dans la catégorie choisie dans Moodle
            out.append(category(f'{root}/Fiche {c["num"]} - {c["title"]}'))
        out += [question(c, i, q, prefix) for i, q in enumerate(c['qcm'], 1)]
    out.append('</quiz>\n')
    return ''.join(out)


FLAT = False


def build(out_dir, bank='entrainement'):
    global FLAT
    FLAT = bank.startswith('s2-')
    src, root, prefix, name = BANKS[bank]
    text = ''.join(open(f, encoding='utf8').read() + '\n' for f in sorted(glob.glob(os.path.join(HERE, src))))
    cards = parse(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, name)
    open(path, 'w', encoding='utf8').write(xml(cards, root, prefix))
    print(path, len(cards), 'catégories,', sum(len(c['qcm']) for c in cards), 'questions')


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..'), sys.argv[2] if len(sys.argv) > 2 else 'entrainement')
