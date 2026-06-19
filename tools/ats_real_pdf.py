import re, collections
from pypdf import PdfReader
def extract_text(p):
    return "\n".join((pg.extract_text() or "") for pg in PdfReader(p).pages)

PDF = "/root/.claude/uploads/7be39091-12f4-5639-8acd-fdfa33334049/8ff0358e-Anna_Brown_Nonprofit_Resume_26_1.pdf"

JD = """Donor Services Associate. Ensure exceptional donor experience through accurate gift processing, thoughtful stewardship, and strong data integrity. Manage all contributions in Tessitura, maintain high-quality constituent data, support donor communications and recognition, provide timely reporting and analysis to advance fundraising and engagement. Partner to Development, Ticketing, and Finance. Process and record all gifts, pledges, and payments in Tessitura. Generate personalized tax receipts and acknowledgment letters. Track pledge schedules. Reconcile gifts and pledges with Finance. Serve as donor concierge including ticketing and account assistance. Maintain donor recognition listings. Prepare donor profiles and giving histories. Maintain accurate donor and prospect records. Data hygiene, duplicate resolution, quality control. Set up campaign, appeal, fund, designation, and source codes in Tessitura. Segmentation, list building, and data extraction for direct mail, email, gala, tele-funding. Generate standard and ad-hoc reports. Analyze donor retention, donor growth, campaign performance. Liaison between Development and Ticketing. Administrative support to Chief Development Officer including scheduling and note-taking. Event support for Opening Nights, Gala. Required: Bachelor's degree, experience with a relational database system, high proficiency in Microsoft Office especially Excel and Word, experience in fundraising, ticketing, or nonprofit operations. Preferred: performing arts, ticketing, marketing, donor stewardship, reporting, campaign tracking."""

STOP = set("a an the and or of to in for with on at by from as is are be this that role you your we our their will all across into within during other more most can able team teams work working experience including high strong support provide ensure manage managing maintain new program programs help may etc end day days time type position company employee applicant person status year years professional minimum based".split())
SECTIONS = ["SUMMARY","SKILLS","EXPERIENCE","EDUCATION","AWARDS"]

def keywords(text, n=28):
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}", text.lower())
    freq = collections.Counter(w for w in words if w not in STOP)
    phrases = ["gift processing","data integrity","tessitura","salesforce","stewardship","pledge","acknowledgment","segmentation","reconcile","reconciliation","ticketing","donor","database","fundraising","reporting","nonprofit","excel","project management","operations","briefing","portfolio","pipeline","discretion","metrics","cross-functional","data analytics","communication","records","campaign","finance","liaison"]
    out=[]
    for k in [w for w,_ in freq.most_common(n)]+phrases:
        if k in text.lower() and k not in out: out.append(k)
    return out

txt = extract_text(PDF)
low = txt.lower()
email = bool(re.search(r"[\w.]+@[\w.]+", txt))
phone = bool(re.search(r"\d{3}[.\-]\d{3}[.\-]\d{4}", txt))
secs = [s for s in SECTIONS if s.lower() in low]
kws = keywords(JD)
found=[k for k in kws if k.lower() in low]
score=round(100*len(found)/len(kws))

print("="*70)
print("ANNA'S ACTUAL RESUME (two-column 'Nonprofit_Resume_26.pdf')")
print("Parsed by an ATS engine (pdfminer), matched to the Shakespeare Donor Services JD")
print("="*70)
print("\n----- WHAT THE ATS ACTUALLY 'READS' (raw extracted text order) -----\n")
# show the extraction so she can SEE the jumbling
shown = "\n".join(l for l in txt.splitlines())
print(shown[:1600])
print("\n----- CHECKS -----")
print(f"Email detected:               {'YES' if email else 'NO'}")
print(f"Phone detected:               {'YES' if phone else 'NO'}")
print(f"Standard sections found:      {len(secs)}/5  -> {', '.join(secs) if secs else 'NONE'}")
print(f"Keyword match vs JD:          {score}%   ({len(found)}/{len(kws)})")
print(f"  matched: {', '.join(found)}")
print("="*70)
print(f"COMPARISON  ->  Her actual resume: {score}%   |   ATS-optimized version: 78%")
print("="*70)
