from pathlib import Path
from textwrap import dedent

root = Path(__file__).resolve().parent

pages = [
    ("course-visual-testing.html", "Visual Testing (VT)", "NDT & Inspection"),
    ("course-liquid-penetrant-testing.html", "Liquid Penetrant Testing (PT/LPT)", "NDT & Inspection"),
    ("course-magnetic-particle-testing.html", "Magnetic Particle Testing (MT/MPT)", "NDT & Inspection"),
    ("course-ultrasonic-testing.html", "Ultrasonic Testing (UT)", "NDT & Inspection"),
    ("course-radiographic-testing.html", "Radiographic Testing (RT)", "NDT & Inspection"),
    ("course-eddy-current-testing.html", "Eddy Current Testing (ET)", "NDT & Inspection"),
    ("course-phased-array-ut.html", "Phased Array Ultrasonic Testing (PAUT)", "NDT & Inspection"),
    ("course-tofd.html", "Time of Flight Diffraction (TOFD)", "NDT & Inspection"),
    ("course-magnetic-flux-leakage.html", "Magnetic Flux Leakage (MFL)", "NDT & Inspection"),
    ("course-iris.html", "IRIS", "NDT & Inspection"),
    ("course-guided-wave-testing.html", "Guided Wave Testing (GWT)", "NDT & Inspection"),
    ("course-acoustic-emission-testing.html", "Acoustic Emission Testing (AET)", "NDT & Inspection"),
    ("course-infrared-thermography.html", "Infrared Thermography (IRT)", "NDT & Inspection"),
    ("course-leak-testing.html", "Leak Testing (LT)", "NDT & Inspection"),
    ("course-rope-access-ndt.html", "Rope Access NDT", "NDT & Inspection"),
    ("course-asnt-level-1.html", "ASNT Level I", "NDT & Inspection"),
    ("course-asnt-level-2.html", "ASNT Level II", "NDT & Inspection"),
    ("course-asnt-level-3.html", "ASNT Level III", "NDT & Inspection"),
    ("course-iso-9712-level-1.html", "ISO 9712 Level I", "NDT & Inspection"),
    ("course-iso-9712-level-2.html", "ISO 9712 Level II", "NDT & Inspection"),
    ("course-iso-9712-level-3.html", "ISO 9712 Level III", "NDT & Inspection"),
    ("course-asnt-certification-services.html", "ASNT Certification Services", "NDT & Inspection"),
    ("course-cswip-3-1.html", "CSWIP 3.1 Welding Inspector", "International Certification"),
    ("course-cswip-3-2.html", "CSWIP 3.2 Senior Welding Inspector", "International Certification"),
    ("course-bgas-grade-1.html", "BGAS Grade I", "International Certification"),
    ("course-bgas-grade-2.html", "BGAS Grade II", "International Certification"),
    ("course-api-510.html", "API 510", "International Certification"),
    ("course-api-570.html", "API 570", "International Certification"),
    ("course-api-653.html", "API 653", "International Certification"),
    ("course-api-936.html", "API 936", "International Certification"),
    ("course-aws-cwi.html", "AWS Certified Welding Inspector (CWI)", "International Certification"),
    ("course-asme-code-training.html", "ASME Code Training", "International Certification"),
    ("course-nace-cip-1.html", "NACE CIP Level 1", "International Certification"),
    ("course-nace-cip-2.html", "NACE CIP Level 2", "International Certification"),
    ("course-nace-cip-3.html", "NACE CIP Level 3", "International Certification"),
    ("course-frosio-coating-inspector.html", "FROSIO Coating Inspector", "International Certification"),
    ("course-iso-9001-lead-auditor.html", "ISO 9001 Lead Auditor", "International Certification"),
    ("course-iso-14001-lead-auditor.html", "ISO 14001 Lead Auditor", "International Certification"),
    ("course-iso-45001-lead-auditor.html", "ISO 45001 Lead Auditor", "International Certification"),
    ("course-nebosh-igc.html", "NEBOSH IGC", "International Certification"),
    ("course-iosh-managing-safely.html", "IOSH Managing Safely", "International Certification"),
    ("course-mechanical.html", "Mechanical", "National Programs"),
    ("course-qa-qc-engineer.html", "QA/QC Engineer", "National Programs"),
    ("course-welding-inspector.html", "Welding Inspector", "National Programs"),
    ("course-piping-qa-qc.html", "Piping QA/QC", "National Programs"),
    ("course-pressure-vessel-inspection.html", "Pressure Vessel Inspection", "National Programs"),
    ("course-pwht-technician.html", "PWHT Technician", "National Programs"),
    ("course-welding-technology.html", "Welding Technology", "National Programs"),
    ("course-boiler-inspection.html", "Boiler Inspection", "National Programs"),
    ("course-plant-maintenance.html", "Plant Maintenance", "National Programs"),
    ("course-material-testing.html", "Material Testing", "National Programs"),
    ("course-ndt-technician.html", "NDT Technician", "National Programs"),
    ("course-electrical.html", "Electrical", "National Programs"),
    ("course-electrical-qa-qc-engineer.html", "Electrical QA/QC Engineer", "National Programs"),
    ("course-electrical-safety.html", "Electrical Safety", "National Programs"),
    ("course-ht-lt-switchgear.html", "HT/LT Switchgear", "National Programs"),
    ("course-transformer-testing.html", "Transformer Testing", "National Programs"),
    ("course-relay-testing.html", "Relay Testing", "National Programs"),
    ("course-cable-testing.html", "Cable Testing", "National Programs"),
    ("course-earthing-lightning-protection.html", "Earthing & Lightning Protection", "National Programs"),
    ("course-solar-pv-installation.html", "Solar PV Installation", "National Programs"),
    ("course-plc-scada.html", "PLC & SCADA", "National Programs"),
    ("course-substation-testing-commissioning.html", "Substation Testing & Commissioning", "National Programs"),
    ("course-civil.html", "Civil", "National Programs"),
    ("course-civil-qa-qc-engineer.html", "Civil QA/QC Engineer", "National Programs"),
    ("course-concrete-technology.html", "Concrete Technology", "National Programs"),
    ("course-soil-testing.html", "Soil Testing", "National Programs"),
    ("course-highway-qa-qc.html", "Highway QA/QC", "National Programs"),
    ("course-bridge-inspection.html", "Bridge Inspection", "National Programs"),
    ("course-quantity-surveying.html", "Quantity Surveying", "National Programs"),
    ("course-autocad-civil.html", "AutoCAD Civil", "National Programs"),
    ("course-staad-pro.html", "STAAD Pro", "National Programs"),
    ("course-etabs.html", "ETABS", "National Programs"),
    ("course-primavera-p6.html", "Primavera P6", "National Programs"),
    ("course-piping-engineering.html", "Piping Engineering", "Refinery & Power Plant"),
    ("course-pipeline-inspection.html", "Pipeline Inspection", "Refinery & Power Plant"),
    ("course-shutdown-turnaround-management.html", "Shutdown & Turnaround Management", "Refinery & Power Plant"),
    ("course-static-equipment-inspection.html", "Static Equipment Inspection", "Refinery & Power Plant"),
    ("course-rotating-equipment-maintenance.html", "Rotating Equipment Maintenance", "Refinery & Power Plant"),
    ("course-heat-exchanger-inspection.html", "Heat Exchanger Inspection", "Refinery & Power Plant"),
    ("course-boiler-turbine-maintenance.html", "Boiler & Turbine Maintenance", "Refinery & Power Plant"),
    ("course-valve-inspection.html", "Valve Inspection", "Refinery & Power Plant"),
    ("course-corrosion-engineering.html", "Corrosion Engineering", "Refinery & Power Plant"),
    ("course-rbi.html", "Risk-Based Inspection (RBI)", "Refinery & Power Plant"),
    ("course-ffs.html", "Fitness For Service (FFS)", "Refinery & Power Plant"),
    ("course-plant-commissioning.html", "Plant Commissioning", "Refinery & Power Plant"),
    ("course-material-reconciliation.html", "Material Reconciliation", "Refinery & Power Plant"),
    ("course-hydrotest-pneumatic-test.html", "Hydrotest & Pneumatic Test", "Refinery & Power Plant"),
    ("course-wps.html", "WPS", "Refinery & Power Plant"),
    ("course-pqr.html", "PQR", "Refinery & Power Plant"),
    ("course-wqt.html", "WQT", "Refinery & Power Plant"),
]

for filename, title, badge in pages:
    target = root / filename
    if target.exists():
        continue
    content = dedent(f'''\
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | Narayan Technological Institution</title>
        <link rel="stylesheet" href="style.css">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="navbar-container">
            <div class="header">
                <h1>NARAYAN TECHNOLOGICAL INSTITUTION</h1>
            </div>
            <div class="menu">
                <nav>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="course.html">Programs & Courses</a></li>
                        <li><a href="affiliation.html">Affiliation</a></li>
                        <li><a href="index.html#contact">Contact Us</a></li>
                        <li><a href="verification.html">Student Verification</a></li>
                    </ul>
                </nav>
            </div>
        </div>

        <section class="course-detail-page">
            <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1400&q=80" alt="{title}" class="course-detail-hero">
            <div class="course-detail-card">
                <span class="course-detail-badge">{badge}</span>
                <h1>{title}</h1>
                <h2>About Course</h2>
                <p>This professional learning pathway introduces the principles, workflow, and industrial relevance of {title}. It is designed to help learners acquire practical knowledge and a strong foundation for quality, inspection, engineering, operations, or leadership responsibilities.</p>
                <h2>What is this Course?</h2>
                <p>It is a structured academic and professional program that supports practical understanding, certification readiness, and career growth in real-world industry settings.</p>
                <h2>Eligibility</h2>
                <p>Open to students, diploma holders, graduate learners, technicians, and professionals seeking specialized skill development.</p>
                <h2>Course Duration</h2>
                <p>4 to 8 weeks with guided instruction, practical exercises, and assessment support.</p>
                <h2>Certification</h2>
                <p>Institutional certification support and professional training aligned with modern industry expectations.</p>
                <h2>Career Opportunities</h2>
                <p>Inspection roles, technical support positions, quality-focused job profiles, engineering operations, and senior specialist career pathways.</p>
                <h2>Industries</h2>
                <p>Manufacturing, construction, energy, utilities, infrastructure, oil & gas, power, and process industries.</p>
                <h2>Course Fees</h2>
                <p>Contact Institute for Latest Fees.</p>
                <a href="apply.html?owner=1" class="know-btn">Apply Now</a>
            </div>
        </section>

        <footer id="contact" class="footer">
            <div class="footer-container">
                <div class="footer-box"><h2>Narayan Technological Institution</h2><p>Committed to industry-aligned professional training.</p></div>
                <div class="footer-box"><h2>Quick Links</h2><a href="index.html">Home</a><a href="course.html">Courses</a><a href="affiliation.html">Affiliation</a><a href="verification.html">Student Verification</a></div>
                <div class="footer-box"><h2>Contact Us</h2><div class="footer-contact-list"><div class="footer-contact-item">📍 <span>Jamnagar, Gujarat, India</span></div><div class="footer-contact-item">✉️ <span>admissions@nti.ac.in</span></div><div class="footer-contact-item">📞 <span>+91 98765 43210</span></div></div></div>
            </div>
            <hr>
            <p class="copyright">© 2026 Narayan Technological Institution. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    ''')
    target.write_text(content, encoding='utf-8')
    print(f'created {filename}')

print('finished creating course page files')
