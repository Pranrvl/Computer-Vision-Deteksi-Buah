---
name: Fruit Freshness Soft UI
colors:
  surface: '#fbf8ff'
  surface-dim: '#d7d8f4'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f2ff'
  surface-container: '#edecff'
  surface-container-high: '#e6e6ff'
  surface-container-highest: '#e0e0fc'
  on-surface: '#181a2e'
  on-surface-variant: '#41474e'
  inverse-surface: '#2d2f44'
  inverse-on-surface: '#f1efff'
  outline: '#72787f'
  outline-variant: '#c1c7cf'
  surface-tint: '#30628a'
  primary: '#30628a'
  on-primary: '#ffffff'
  primary-container: '#a2d2ff'
  on-primary-container: '#275b82'
  inverse-primary: '#9bcbf8'
  secondary: '#006a62'
  on-secondary: '#ffffff'
  secondary-container: '#70f8e8'
  on-secondary-container: '#007168'
  tertiary: '#bb152c'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffbcba'
  on-tertiary-container: '#af0525'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cde5ff'
  primary-fixed-dim: '#9bcbf8'
  on-primary-fixed: '#001d32'
  on-primary-fixed-variant: '#104a70'
  secondary-fixed: '#70f8e8'
  secondary-fixed-dim: '#4fdbcc'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#005049'
  tertiary-fixed: '#ffdad8'
  tertiary-fixed-dim: '#ffb3b1'
  on-tertiary-fixed: '#410007'
  on-tertiary-fixed-variant: '#92001c'
  background: '#fbf8ff'
  on-background: '#181a2e'
  surface-variant: '#e0e0fc'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 30px
  title-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
  title-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 22px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  gutter: 1.5rem
  margin: 1.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system establishes an approachable, scientifically grounded computer vision interface. It balances laboratory-grade precision with soft organic warmth, reducing the anxiety often associated with quality inspection and automated decision-making. 

The aesthetic is clean, welcoming, and tactile—blending soft minimalism with subtle atmospheric depth. Crisp micro-copy, pastel surfaces, and pill-shaped interactive triggers create an inviting, human-centric machine learning utility. Interfaces built with this system feel light, airy, and trustworthy, avoiding the visual density and cold cynicism typical of enterprise analytical dashboards.

## Colors

The palette revolves around calming pastels reinforced by sharp diagnostic indicators:

- **Primary (`#a2d2ff`)**: Pastel sky blue. Applied to primary controls, interactive buttons, active selections, and neutral highlight states.
- **Secondary / Positive Status (`#2ec4b6`)**: Crisp organic teal-green. Used for successful inference, high freshness scores, verified batches, and positive quality badges. Secondary confirmation tone is supported by `#38b000` for pure green telemetry metrics.
- **Tertiary / Warning & Critical (`#e63946`)**: Balanced botanical scarlet. Signifies decay, low shelf-life warnings, spoiled/rotten status, and destructive operations. Paired with deep crimson `#d90429` for high-severity alerts.
- **Neutral Primary (`#2b2d42`)**: Deep slate. Delivers high contrast for primary data, titles, and key numeric outputs without the harshness of pure black.
- **Neutral Secondary (`#4a4e69`)**: Muted slate-plum. Used for supporting captions, metadata, unit indicators, and inactive states.
- **Canvas / Background (`#f8fafd`)**: Soft cool off-white that minimizes glare during prolonged visual review sessions.
- **Surface Elevation (`#ffffff`)**: Pure white base for floating inference cards and upload containers.

## Typography

Typography relies entirely on Plus Jakarta Sans to deliver an ergonomic blend of geometric structure and friendly rounded glyph terminals. 

Hierarchy is established via weight and value shifts rather than dramatic size differences. Numeric inference scores, confidence intervals, and condition ratings share the primary headline font with tabular figures enabled for baseline alignment across analytical cards. Labels utilize increased letter spacing with medium to bold weights to guarantee legibility against pastel containers.

## Layout & Spacing

The layout centers around a unified, card-focused single column for AI inspection workflows, scaling to a balanced dual-column display on larger screens:

- **Constraint**: Max-width of `840px` for centered operational tools; expands to `1140px` for split-view dashboards (original imagery alongside model feature maps).
- **Desktop (>= 1024px)**: Dual-column grid with `1.5rem` gutters. Left region anchors file upload and camera inputs; right region presents real-time classification readouts and confidence breakdowns.
- **Tablet (768px - 1023px)**: Single column with `1.5rem` margins and centered card modules.
- **Mobile (< 768px)**: Unified vertical stack with `1rem` margins and `0.75rem` card paddings to preserve vertical real estate.

## Elevation & Depth

Visual depth is achieved through ultra-diffuse ambient shadows paired with white structural planes against the `#f8fafd` canvas:

- **Level 0 (Flat)**: Transparent utility areas and structural spacers.
- **Level 1 (Card & Surface Base)**: Floating white modules utilize `box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0, 0, 0, 0.02)`.
- **Level 2 (Active & Dropzone Hover)**: Interactive components, active drag zones, and opened dialogs transition to `box-shadow: 4px 6px 16px rgba(43, 45, 66, 0.06), 0 2px 4px rgba(43, 45, 66, 0.03)`.
- **Level 3 (Modal / Floating Telemetry)**: Overlay elements use `box-shadow: 0 12px 28px rgba(43, 45, 66, 0.08), 0 4px 8px rgba(43, 45, 66, 0.03)`.

Borders are kept low-contrast: `1px solid rgba(74, 78, 105, 0.08)` to softly define boundaries without visual clutter.

## Shapes

The design language emphasizes organic rounded forms through pill-shaped profiles and generous card corners:

- **Buttons, Badges, and Pill Sliders**: Full pill shape (`border-radius: 9999px`) to create tactile, soft touch targets.
- **Content Cards & Media Panels**: Curved corners (`border-radius: 1.25rem` to `1.5rem`) to frame imagery and data panels with a gentle profile.
- **Form Inputs & Dropzones**: Pill or soft stadium silhouettes (`border-radius: 1rem`) to maintain structural continuity with primary action triggers.

## Components

### Buttons
- **Primary**: Background `#a2d2ff`, text `#2b2d42`, pill shape (`rounded-full`), padded `0.75rem 1.75rem`. Hover introduces a subtle translateY(-1px) and an ambient shadow enhancement (`0 4px 12px rgba(162, 210, 255, 0.45)`).
- **Secondary / Utility**: Surface `#ffffff` with subtle border `1px solid rgba(74, 78, 105, 0.12)`, text `#2b2d42`.

### Status Badges & Chips
- **Fresh Fruit Indicator**: Pastel mint pill (`#e8f8f5`), label `#2ec4b6`, accompanied by `#38b000` status dot. Font size `12px`, bold tracking.
- **Rotten / Defective Indicator**: Soft crimson pill (`#fdebec`), label `#e63946`, accompanied by `#d90429` status dot.
- **Confidence Meter**: Inline badge displaying percentage metrics inside a neutral light container (`#f0f4f8`) with `#4a4e69` typography.

### Inference Upload Cards
- Pure white surface (`#ffffff`), `rounded-2xl` (20px radius), border `2px dashed rgba(162, 210, 255, 0.6)`. 
- Drag-hover state fills with soft sky-blue wash (`rgba(162, 210, 255, 0.15)`).

### Input Fields & Controls
- **File Inputs & Dropdowns**: Background `#ffffff`, text `#2b2d42`, border `1px solid rgba(74, 78, 105, 0.15)`, radius `12px`. Focus state shifts border to `#a2d2ff` with a diffuse `0 0 0 3px rgba(162, 210, 255, 0.3)` focus ring.
- **Checkboxes & Radios**: Rounded pill checks with `#a2d2ff` filled selections and `#2b2d42` tick icons.

### Prediction Telemetry Bar
- Horizontal metric track with height `8px`, track background `#eef2f7`, `rounded-full`. 
- Progress fill uses `#2ec4b6` for high freshness ratings and transitions dynamically to `#e63946` when quality degradation thresholds are reached.