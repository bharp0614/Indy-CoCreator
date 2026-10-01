import os

def write_html_page(family, filename, title, hero_h1, hero_p, body_html, hide_nav=False):
    rel_path = "../../"
    
    header_html = "" if hide_nav else f"""
  <header>
    <div class="container header-container">
      <a href="{rel_path}index.html" class="logo">
        <span data-token="business.name">Redeveloper</span>
      </a>
      <nav>
        <ul class="nav-links">
          <li><a href="{rel_path}index.html">Home</a></li>
          <li><a href="{rel_path}use-cases.html">Sell a Property</a></li>
          <li><a href="{rel_path}projects.html">Projects</a></li>
          <li><a href="{rel_path}contact.html">Contact</a></li>
        </ul>
      </nav>
      <div class="header-cta">
        <a href="tel:+13175550199" class="phone-link" data-token="business.phone">+1 (317) 555-0199</a>
        <a href="{rel_path}contact.html" class="btn btn-primary">Submit a Property</a>
      </div>
    </div>
  </header>
"""

    footer_html = "" if hide_nav else f"""
  <footer>
    <div class="container footer-grid">
      <div class="footer-brand">
        <h3 data-token="business.name">Redeveloper</h3>
        <p>Direct property buyers backed by 30 years of construction-management experience. No high-pressure sales, no fabricated calculators.</p>
      </div>
      <div class="footer-nav">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="{rel_path}index.html">Home</a></li>
          <li><a href="{rel_path}use-cases.html">Sell a Property</a></li>
          <li><a href="{rel_path}projects.html">Projects</a></li>
          <li><a href="{rel_path}contact.html">Contact Us</a></li>
        </ul>
      </div>
      <div class="footer-contact">
        <h4>Contact & Area</h4>
        <p style="color: rgba(255, 255, 255, 0.7); line-height: 1.8;">
          <strong>Email:</strong> <a href="mailto:operations@example.com" data-token="business.email">operations@example.com</a><br>
          <strong>Phone:</strong> <a href="tel:+13175550199" data-token="business.phone">+1 (317) 555-0199</a><br>
          <strong>Service Area:</strong> <span data-token="business.service_area">Central Indiana</span><br>
          <strong>Primary Service:</strong> <span data-token="business.primary_service">Residential Redevelopment</span>
        </p>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; <span id="footer-year">2026</span> <span data-token="business.fullName">Residential Redevelopment Company</span>. All verified rights reserved.</p>
    </div>
  </footer>
"""

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Redeveloper</title>
  <link rel="stylesheet" href="{rel_path}css/global.css">
</head>
<body>

  {header_html}

  <!-- Page Hero -->
  <section class="hero" style="padding: var(--space-12) 0; background: linear-gradient(135deg, var(--color-primary-700) 0%, var(--color-primary-500) 100%);">
    <div class="container">
      <ul class="breadcrumbs">
        <li><a href="{rel_path}index.html" style="color: rgba(255, 255, 255, 0.7);">Home</a></li>
        <li><a href="#" style="color: rgba(255, 255, 255, 0.7);">{family.replace('-', ' ').title()}</a></li>
        <li style="color: white;" aria-current="page">{title}</li>
      </ul>
      <h1 style="color: var(--color-text-inverse); margin-bottom: var(--space-2);">{hero_h1}</h1>
      <p style="color: rgba(255, 255, 255, 0.85); margin-bottom: 0;">{hero_p}</p>
    </div>
  </section>

  {body_html}

  {footer_html}

  <script>
    document.addEventListener("DOMContentLoaded", () => {{
      // Set copyright year automatically
      const yearEl = document.getElementById('footer-year');
      if (yearEl) yearEl.textContent = new Date().getFullYear();

      // Load client data dynamically
      loadClientData();
    }});

    async function loadClientData() {{
      try {{
        const response = await fetch('{rel_path}data/client.json');
        if (!response.ok) return;
        const data = await response.json();
        
        // Bind simple key-value tokens
        document.querySelectorAll('[data-token]').forEach(el => {{
          const tokenName = el.getAttribute('data-token');
          const keys = tokenName.split('.');
          let val = data;
          for (const key of keys) {{
            if (val) val = val[key];
          }}
          if (val) {{
            if (el.tagName === 'A' && tokenName === 'business.phone') {{
              el.href = 'tel:' + val.replace(/\\D/g, '');
            }} else if (el.tagName === 'A' && tokenName === 'business.email') {{
              el.href = 'mailto:' + val;
            }}
            el.textContent = val;
          }}
        }});
      }} catch (e) {{
        console.warn("Could not dynamically load client.json.", e);
      }}
    }}
  </script>
</body>
</html>
"""

    family_dir = os.path.join("website", "pages", family)
    os.makedirs(family_dir, exist_ok=True)
    filepath = os.path.join(family_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated {filepath} successfully.")

def generate_all():
    # 1. SHARED PAGES
    write_html_page("shared", "home.html", "Home Entry Page", "Central Indiana Residential Redevelopment", 
                    "Direct property acquisitions and code-compliant construction management.",
                    """<section class="section-padding"><div class="container"><h2>Welcome to Redeveloper</h2><p>Please navigate using the menu above to explore our solutions, recent projects, or submit your property for evaluation.</p></div></section>""")
    
    write_html_page("shared", "contact.html", "General Contact", "Get in Touch With Us", 
                    "Reach out directly for general inquiries, referrals, or trade opportunities.",
                    """<section class="section-padding"><div class="container"><h2>General Contacts</h2><p>Email operations directly at <strong>operations@example.com</strong> or call our line.</p></div></section>""")
    
    write_html_page("shared", "reviews.html", "Customer Reviews", "Verified Customer Testimonials", 
                    "Read feedback from homeowners we have worked with across local communities.",
                    """<section class="section-padding"><div class="container"><h2>Testimonials</h2><div class="grid grid-3"><div class="card"><h4>Jane D., Indianapolis</h4><p>"The process was incredibly smooth. They handled all structural repairs and finished closing in less than 2 weeks."</p></div><div class="card"><h4>Mark S., Broad Ripple</h4><p>"Very professional crew. They bought my father's house directly and let us leave behind unwanted furniture."</p></div></div></div></section>""")
    
    write_html_page("shared", "faq.html", "Frequently Asked Questions", "Property Acquisition FAQ", 
                    "Common answers about our direct buying, inspection, and closing procedures.",
                    """<section class="section-padding"><div class="container"><h2>FAQ</h2><div class="faq-item"><details><summary>Do I need to pay any real estate agent commissions?</summary><p>No. We buy your property directly from you. There are no commissions or hidden transaction broker fees.</p></details></div><div class="faq-item"><details><summary>How fast can you close?</summary><p>We typically close through a local reputable title company within 10 to 14 days, depending on title clearance.</p></details></div></div></section>""")
    
    write_html_page("shared", "now-hiring.html", "Careers & Hiring", "Join Our Renovation Crews", 
                    "We are always looking for skilled carpenters, code leads, and licensed sub-trades.",
                    """<section class="section-padding"><div class="container"><h2>We are Hiring</h2><p>We keep an active bench of talent. Check out our Careers Index to see open roles.</p></div></section>""")

    # 2. SERVICE-BASED PAGES
    write_html_page("service-based", "services-index.html", "Services Overview", "Service & Repair Capabilities", 
                    "Comprehensive list of repair, renovation, and management services.",
                    """<section class="section-padding"><div class="container"><h2>Renovation Capabilities</h2><p>Explore our single services below.</p></div></section>""")
    
    write_html_page("service-based", "service-single.html", "Service Details", "Detailed Service Breakdown", 
                    "Granular overview of a specific trades task or structural repair standard.",
                    """<section class="section-padding"><div class="container"><h2>Service Outline</h2><p>Structural inspections, framing modifications, and mechanical upgrade stubs.</p></div></section>""")
    
    write_html_page("service-based", "emergency-service.html", "Emergency Dispatch", "24/7 Urgent Repair Response", 
                    "Immediate response dispatch team for priority water, electrical, or structural safety failures.",
                    """<section class="section-padding" style="border-left: 6px solid var(--color-error-700);"><div class="container"><h2>Emergency Dispatch Form</h2><p>Submit details for active system failures.</p></div></section>""")
    
    write_html_page("service-based", "pricing.html", "Cost Guidance", "Cost & Estimate Standards", 
                    "Transparent guidelines on material costs, labor rates, and project variables.",
                    """<section class="section-padding"><div class="container"><h2>Renovation Estimating Guides</h2><p>Learn how pricing is calculated.</p></div></section>""")
    
    write_html_page("service-based", "financing.html", "Financing & Terms", "Project Funding Assistance", 
                    "Information about flexible payment terms or structured financing partnerships.",
                    """<section class="section-padding"><div class="container"><h2>Payment Terms</h2><p>Options for deferred payments or home improvement credit.</p></div></section>""")

    # 3. PROJECT-BASED PAGES
    write_html_page("project-based", "use-cases-index.html", "Solutions Index", "Acquisition Use Cases", 
                    "Pathways for transitioning inherited properties, distressed rentals, or major rehabs.",
                    """<section class="section-padding"><div class="container"><h2>Transition Situations</h2><p>Find the scenario that matches your needs.</p></div></section>""")
    
    write_html_page("project-based", "use-case-single.html", "Solution Focus", "Situation Scenario Detail", 
                    "In-depth guidance on structural repairs, estate settlements, or tenant challenges.",
                    """<section class="section-padding"><div class="container"><h2>Resolution Steps</h2><p>Technical guidance for this use case.</p></div></section>""")
    
    write_html_page("project-based", "projects-index.html", "Acquisitions & Case Studies", "Completed Redevelopments", 
                    "List of residential acquisitions completed in our target sub-markets.",
                    """<section class="section-padding"><div class="container"><h2>Case Studies</h2><p>Explore recent projects.</p></div></section>""")
    
    write_html_page("project-based", "project-single.html", "Case Study Detail", "Structural & Finish Case Study", 
                    "Full technical scope, holding timelines, comparable values, and completed photo stubs.",
                    """<section class="section-padding"><div class="container"><h2>Case Study Scope</h2><p>Renovation details and structural scope outline.</p></div></section>""")
    
    write_html_page("project-based", "before-after-index.html", "Transformations Gallery", "Before & After Transformations", 
                    "Visual proofs of completed cosmetic and structural redevelopments.",
                    """<section class="section-padding"><div class="container"><h2>Renovation Comparisons</h2><p>Browse our transformation gallery.</p></div></section>""")
    
    write_html_page("project-based", "before-after-single.html", "Before & After Showcase", "Transformation Case Detail", 
                    "Visual study of a structural and layout overhaul showing phase-by-phase updates.",
                    """<section class="section-padding"><div class="container"><h2>Transformation Showcase</h2><p>Compare photos and scopes.</p></div></section>""")

    # 4. CONTENT PAGES
    write_html_page("content", "blog-index.html", "Education & Guides", "Homeowner Educational Articles", 
                    "Resources on local code compliance, inheritance, and real estate market updates.",
                    """<section class="section-padding"><div class="container"><h2>Articles List</h2><p>Read our local homeowner guides.</p></div></section>""")
    
    write_html_page("content", "blog-single.html", "Guide Article", "Understanding Property Code Violations", 
                    "How to handle city citations, deferred maintenance notices, and structural structural demands.",
                    """<section class="section-padding"><div class="container"><h2>Article Content</h2><p>Detailed analysis of local codes and guidelines.</p></div></section>""")

    # 5. RECRUITING PAGES
    write_html_page("recruiting", "careers-index.html", "Careers Overview", "Careers at Redeveloper", 
                    "Build a stable career with competitive daily rates and professional safety codes.",
                    """<section class="section-padding"><div class="container"><h2>Working With Us</h2><p>Available career opportunities.</p></div></section>""")
    
    write_html_page("recruiting", "job-single.html", "Job Details", "Lead Finish Carpenter", 
                    "Detailed posting for sub-crew project lead including requirements and rates.",
                    """<section class="section-padding"><div class="container"><h2>Job Description</h2><p>Apply for this role by sending details.</p></div></section>""")

    # 6. CAMPAIGNS
    write_html_page("campaigns", "landing-page.html", "Special Acquisition Campaign", "Get a Cash Offer Today", 
                    "Enter your property details below for an accelerated 48-hour cash offer review.",
                    """<section class="section-padding"><div class="container"><h2>Campaign Form</h2><p>Accelerated evaluation page.</p></div></section>""", hide_nav=True)
    
    write_html_page("campaigns", "lead-funnel.html", "Multi-Step Property Intake", "Submit Property Details", 
                    "Guided multi-step questionnaire for estate and rental portfolio submissions.",
                    """<section class="section-padding"><div class="container"><h2>Multi-Step Form</h2><p>Guided step-by-step submission.</p></div></section>""")
    
    write_html_page("campaigns", "promotions-index.html", "Promo Offers", "Active Partner Promotions", 
                    "Seasonal incentives and local partner referral bonuses.",
                    """<section class="section-padding"><div class="container"><h2>Offers</h2><p>Referral and promotion stubs.</p></div></section>""")
    
    write_html_page("campaigns", "promotion-single.html", "Special Offer Details", "Professional Referral Bonus", 
                    "Earn a referral bonus for submitting verified distressed properties.",
                    """<section class="section-padding"><div class="container"><h2>Promotion Outline</h2><p>Detailed promotion terms.</p></div></section>""")
    
    write_html_page("campaigns", "thank-you.html", "Submission Confirmed", "Property Details Captured", 
                    "Thank you. Our acquisitions manager is evaluating your neighborhood comparable sales.",
                    """<section class="section-padding"><div class="container"><h2>Thank You</h2><p>We will contact you within 24 hours.</p><a href="../../index.html" class="btn btn-primary">Return to Home</a></div></section>""")

    # 7. LOCAL GEOGRAPHIC PAGES
    write_html_page("local", "locations-index.html", "Locations Served", "Central Indiana Communities", 
                    "List of municipalities, cities, and neighborhoods we buy and redevelop in.",
                    """<section class="section-padding"><div class="container"><h2>Geographic Index</h2><p>Communities we service.</p></div></section>""")
    
    write_html_page("local", "location-single.html", "Indianapolis", "Indianapolis Property Buying", 
                    "Local property buyers focusing on Marion County and adjacent neighborhoods.",
                    """<section class="section-padding"><div class="container"><h2>Marion County Focus</h2><p>Local neighborhood comparable reports.</p></div></section>""")
    
    write_html_page("local", "service-location.html", "Indianapolis Structural Rehab", "Indianapolis Structural Renovation", 
                    "Code-compliant structural renovations and framing overhauls in Indianapolis.",
                    """<section class="section-padding"><div class="container"><h2>Indianapolis Service</h2><p>Structural services in this area.</p></div></section>""")
    
    write_html_page("local", "partners-index.html", "Community Partners", "Local Business Connections", 
                    "Directories of local estate lawyers, title companies, and code officials we collaborate with.",
                    """<section class="section-padding"><div class="container"><h2>Community Connections</h2><p>Partner listings.</p></div></section>""")
    
    write_html_page("local", "partner-single.html", "Partner Showcase", "Indiana Title & Trust Co.", 
                    "Highlighting our collaboration with reputable local title companies for clean closings.",
                    """<section class="section-padding"><div class="container"><h2>Partner Focus</h2><p>Partner details and resources.</p></div></section>""")

    # 8. LEGAL PAGES
    write_html_page("legal", "privacy-policy.html", "Privacy Policy", "Data Privacy & Protection Policy", 
                    "How we secure and handle your contact information and property details.",
                    """<section class="section-padding"><div class="container"><h2>Privacy Policy</h2><p>Detailed privacy policies and compliance parameters.</p></div></section>""")
    
    write_html_page("legal", "terms.html", "Terms of Service", "Website Terms & Use Conditions", 
                    "Operating standards, trademark compliance, and dispute resolution guidelines.",
                    """<section class="section-padding"><div class="container"><h2>Terms of Use</h2><p>Terms guidelines.</p></div></section>""")
    
    write_html_page("legal", "accessibility.html", "Accessibility Statement", "Web Accessibility Commitment", 
                    "Compliance guidelines and adjustments implemented to ensure WCAG 2.1 AA benchmarks.",
                    """<section class="section-padding"><div class="container"><h2>Accessibility</h2><p>Accessibility reports and contacts.</p></div></section>""")
    
    write_html_page("legal", "sms-terms.html", "SMS Terms & Conditions", "SMS Messaging Disclosures", 
                    "Opt-in disclosures, message frequencies, and carrier rates details.",
                    """<section class="section-padding"><div class="container"><h2>SMS Policy</h2><p>SMS terms guidelines.</p></div></section>""")

    # 9. SYSTEM PAGES
    write_html_page("system", "sitemap.html", "HTML Sitemap", "Sitemap Page Directory", 
                    "Human-readable directory index of every page template available in the system.",
                    """<section class="section-padding"><div class="container"><h2>Sitemap</h2><p>Full template link tree index.</p></div></section>""")
    
    write_html_page("system", "404.html", "Page Not Found", "404 - Template Not Found", 
                    "The page template you are searching for does not exist or has been moved.",
                    """<section class="section-padding"><div class="container"><h2>404 Error</h2><p>Use the main menu navigation above to return to a valid page.</p></div></section>""")

if __name__ == "__main__":
    generate_all()
