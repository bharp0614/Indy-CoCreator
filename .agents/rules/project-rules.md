# Indy-CoCreator Project Rules

## Project Context
This workspace builds high-ticket home service landing pages for Indianapolis-area businesses: HVAC, plumbing, electrical, roofing, water damage restoration, garage door repair, and roadside assistance. These are lead-generation funnels targeting homeowners in emergency and routine service scenarios.

## Design Archetype: High-Ticket Home Services Funnel

### Page Structure (Follow This Order)
1. **Sticky Header** — Logo left, nav center, phone CTA right (always visible)
2. **Hero** — Photographic background + gradient overlay + bold headline + dual CTA (call + schedule)
3. **Trust Bar** — 4 icon badges (24/7, Licensed, Same-Day, 100% Guaranteed)
4. **Lead Capture Form** — Elevated floating card, white background, 3-5 fields max
5. **Services Grid** — Icon cards with service names, short descriptions, and "Learn More" links
6. **Process Timeline** — 3-5 step numbered flow (call → diagnose → fix → guarantee)
7. **About / Why Us** — Photo + text split, team credentials, years in business
8. **Seasonal Promotion** — Time-sensitive offer with pricing cards
9. **Reviews / Testimonials** — Real names, star ratings, service type mentioned
10. **Service Areas** — City cards with photos, or a simple map reference
11. **Footer** — Full nav, contact info, social links, legal

### Funnel Mechanics
- **Track A (High Intent):** Phone call CTA → sticky header → direct conversion
- **Track B (Consideration):** Form fill → nurture content (hardware comparison, process timeline, reviews) → consultation booking
- **Every section must drive toward one of these two tracks.**

### Brand Token Defaults
When no brand-specific tokens are provided, use these as the baseline:
```css
:root {
  --color-primary-base: #345D81;       /* Navy blue — trust, authority */
  --color-primary-dark: #1A3A5C;       /* Deep navy for overlays */
  --color-surface-light: #E9F3FF;      /* Ice blue tint for alternating sections */
  --color-cta-action: #F4B41A;         /* Gold/amber — urgency, warmth */
  --color-cta-hover: #E5A313;          /* Darkened gold for hover */
  --color-text-primary: hsl(220 15% 15%);
  --color-text-body: hsl(220 12% 30%);
  --color-text-muted: hsl(220 10% 50%);
  --color-surface-white: #FFFFFF;
  --color-surface-dark: hsl(215 50% 10%);
  
  --shadow-card-floating: 
    0 20px 45px -10px rgba(15, 23, 42, 0.15),
    0 8px 20px -8px rgba(15, 23, 42, 0.10);
  --shadow-card-hover:
    0 25px 50px -10px rgba(15, 23, 42, 0.20),
    0 12px 24px -8px rgba(15, 23, 42, 0.12);
  
  --radius-card: 12px;
  --radius-button: 8px;
  --radius-input: 6px;
  
  --font-heading: 'Montserrat', sans-serif;
  --font-body: 'Inter', sans-serif;
}
```

### Hero Overlay Standard
```css
.hero-overlay {
  background: linear-gradient(
    135deg,
    rgba(52, 93, 129, 0.92) 0%,
    rgba(20, 42, 61, 0.80) 100%
  );
}
```

### Copy Voice
- **Headline tone:** Direct, urgent, benefit-focused. "No Heat? No Cooling? No Wait."
- **Body tone:** Professional but approachable. Mention Indianapolis, specific neighborhoods, and Indiana-specific concerns (winter furnace failures, summer AC emergencies).
- **CTAs:** Action verbs + urgency. "Call Now", "Schedule Service", "Get Your Free Estimate", "Calculate My Savings".
- **Never generic:** Don't say "our team of professionals." Say "our licensed Indianapolis HVAC technicians" or "our EPA-certified restoration specialists."

### Emergency vs. Routine Pages
- **Emergency pages** lead with urgency: red/orange accents, "24/7" prominent, phone CTA above form CTA
- **Routine pages** lead with value: seasonal offers, maintenance plans, form CTA above phone CTA

### File Organization
- Service-specific JSON files in root contain structured data (copy blocks, pricing, service details)
- Brand token files in `group_a_emergency_restoration_brand_tokens/`
- Generated pages go in `pages/`
- Shared CSS in `css/`
- Section templates in `sections/`
