TypeScript Representation

**shared components** 
**shared sections**
**forms**




**Group A-specific components** 
separate so the names don’t get mixed together.







```ts
// components.ts

export const coreComponents = [
  "Button",
  "Card",
  "Badge",
  "Form",
  "Header",
  "Footer",
  "MobileEmergencyCTA",
] as const;

export const coreForms = [
  "EmergencyQuickForm",
  "ContactForm",
  "QuoteForm",
] as const;

export const coreSections = [
  "Hero",
  "TrustStrip",
  "WarningSigns",
  "DiagnosticPlate",
  "Services",
  "FeaturedProject",
  "Process",
  "BeforeAfter",
  "Reviews",
  "ServiceArea",
  "FinalCTA",
] as const;

export const groupAComponents = [
  "EmergencyHero",
  "MobileEmergencyCTA",
  "FastFieldEmergencyForm",
  "EmergencyServiceCards",
  "LocalTrustSignals",
  "ServiceAreaBlock",
  "EmergencyProcess",
  "ReviewBlock",
  "EmergencyFAQ",
  "FinalEmergencyCTA",
] as const;

export const groupAOptionalComponents = [
  "EmergencyTypeSelector",
  "SafetyUrgencyDisclaimer",
  "BeforeAfterProofBlock",
  "InsuranceSupportBlock",
  "DispatchProcess",
] as const;

export const restorationComponents = [
  "RestorationDamageTypes",
  "RestorationTrustChecklist",
  "InsuranceSupportBlock",
  "WrittenEstimateBlock",
] as const;


// --------------------------------------------------
// TYPES
// --------------------------------------------------

export type CoreComponent =
  (typeof coreComponents)[number];

export type CoreForm =
  (typeof coreForms)[number];

export type CoreSection =
  (typeof coreSections)[number];

export type GroupAComponent =
  (typeof groupAComponents)[number];

export type GroupAOptionalComponent =
  (typeof groupAOptionalComponents)[number];

export type RestorationComponent =
  (typeof restorationComponents)[number];


// --------------------------------------------------
// COMPLETE REGISTRY
// --------------------------------------------------

export const componentRegistry = {
  core: {
    components: coreComponents,
    forms: coreForms,
    sections: coreSections,
  },

  groups: {
    groupA: {
      required: groupAComponents,
      optional: groupAOptionalComponents,
      restoration: restorationComponents,
    },
  },
} as const;

export type ComponentRegistry = typeof componentRegistry;
```

And this matches the folder logic we established:

```text
core/
├── components/
│   ├── Button.tsx
│   ├── Card.tsx
│   ├── Badge.tsx
│   ├── Form.tsx
│   ├── Header.tsx
│   ├── Footer.tsx
│   └── MobileEmergencyCTA.tsx
│
├── forms/
│   ├── EmergencyQuickForm.tsx
│   ├── ContactForm.tsx
│   └── QuoteForm.tsx
│
└── sections/
    ├── Hero.tsx
    ├── TrustStrip.tsx
    ├── WarningSigns.tsx
    ├── DiagnosticPlate.tsx
    ├── Services.tsx
    ├── FeaturedProject.tsx
    ├── Process.tsx
    ├── BeforeAfter.tsx
    ├── Reviews.tsx
    ├── ServiceArea.tsx
    └── FinalCTA.tsx

templates/
└── group-a/
    ├── EmergencyHero.tsx
    ├── MobileEmergencyCTA.tsx
    ├── FastFieldEmergencyForm.tsx
    ├── EmergencyServiceCards.tsx
    ├── LocalTrustSignals.tsx
    ├── ServiceAreaBlock.tsx
    ├── EmergencyProcess.tsx
    ├── ReviewBlock.tsx
    ├── EmergencyFAQ.tsx
    └── FinalEmergencyCTA.tsx
```

The naming rule stays consistent across the system:

```ts
// Component
EmergencyServiceCards

// File
EmergencyServiceCards.tsx

// React prop
serviceCards

// JSON field
service_cards

// CSS token
--service-card-gap
```

So **TypeScript/React components = PascalCase**, while the industry JSON stays `snake_case`. That separation is important because the JSON supplies the content; it should not dictate React naming.
