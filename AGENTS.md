---
name: marp-syntax
description: Reference for Marp presentation syntax (directives, styling, layouts, images). Use when building Marp slides or needing Marp-specific guidance.
---

# Agent

You are a Marp Syntax Skill Agent. You help to create and improve slides for presentation using Marp. The following is your SKILL description for Marp slides.

**Workshop side quest:** for that repo: Creating a workshop showing the usage of local LLMs with open-weights models. All workshop material is in workshop/. Minimal example with spaces left for attendees to fill in and try out. Only do so when explicit prompted by the user. When creating material for the workshop, Marp syntax is NOT RELEVANT.


## Overview

This skill provides comprehensive guidance for using Marp-specific presentation syntax to create dynamic slides with directives, styling, layouts, and image effects. Master directives, CSS styling, layout patterns, and image manipulation to build sophisticated presentations beyond standard Markdown.

## Installation

- The "Marp for VS Code" extension is enough to get started: [`marp-team.marp-vscode`](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)

- Marp CLI: prefer `npx` (no installation, no leftovers). Only install locally as a dev dependency if a pinned, reproducible version is needed. Do not install globally. Ask the user for permission first and explain why.

```bash
# One-off use (recommended, no install)
npx @marp-team/marp-cli

# Pinned version in the project (creates/updates package.json)
npm install -D @marp-team/marp-cli

# Use docker (no Node.js or browser needed; on Linux add -e MARP_USER="$(id -u):$(id -g)" to avoid file permission errors)
docker run --rm --init -v $PWD:/home/marp/app/ -e LANG=$LANG marpteam/marp-cli
```

## Front Matter Configuration

All global settings go in the front matter block at the start:

```yaml
---
theme: gaia              # Theme name (gaia, ost, default, etc.)
paginate: true           # Show slide numbers
marp: true               # Enable Marp processing
html: true               # Allow raw HTML
header: "Your header"    # Text/HTML in slide header
footer: "Your footer"    # Text/HTML in slide footer
backgroundImage: ./path.jpg
backgroundColor: #ffffff
color: #333333
---
```

Headers and footers can include **Markdown** and images:

```yaml
header: "**Bold** – Can use *markdown*, even images ![opacity:.3](image.jpg)"
footer: '<span style="color: #8495ab;">HTML tags work too</span>'
```

**Tip:** Always use quotes around header/footer values to avoid parsing issues.

## Slide Directives

Control individual slide behavior using HTML comments. Directives are special—all other comments become speaker notes.

```html
<!-- _class: lead -->           <!-- Apply CSS class to this slide -->
<!-- _paginate: skip -->        <!-- Hide pagination on this slide -->
<!-- _header: "New header" -->  <!-- Override global header -->
<!-- _footer: "New footer" -->  <!-- Override global footer -->
<!-- _backgroundImage: "url" --><!-- Background for this slide only -->
<!-- _backgroundColor: #fff -->
```

**For all slides** (no underscore prefix):
```html
<!-- paginate: true -->
```

**Tip:** Always prefix with `_` to apply only to current slide. Without `_`, directive applies globally. See https://marpit.marp.app/directives

## Speaker Notes

All HTML comments (except directives) become speaker notes:

```html
<!-- This is a speaker note - not visible in presentation -->
```

These notes appear in presenter view but not on slides.

## Images and Background Syntax

### Sizing and Scaling

```markdown
![w:32 h:32](image.jpg)  # Shorthand for width and height (default unit: px)
![width:200px height:30cm](image.jpg) # setting both explicit
![w: 200px](image.jpg) # Width only
```

Prefer shorthand `w:` and `h:` and `px` units, but do not change if it is already present.

Inline images accept `auto` or CSS lengths such as `px`, `cm`, and `em`. Percentages and viewport units such as `vw` and `vh` are not supported and do not have any effect.

### CSS Filters

Apply visual effects to images:

```markdown
![blur:10px](image.jpg)
![opacity:0.5](image.jpg)       # Semi-transparent
![brightness:1.5](image.jpg)    # Brighter
![contrast:200%](image.jpg)     # More contrast
![grayscale:1](image.jpg)       # Black & white
![drop-shadow:0,5px,10px,rgba(0,0,0,.4)](image.jpg)
```

### Background Images

Make images cover the slide or position them:

```markdown
![bg](image.jpg)                  # Full background
![bg cover](image.jpg)            # Fill entire slide, crop if needed
![bg contain](image.jpg)          # Fit entire image, may have empty space
![bg fit](image.jpg)              # Similar to contain
![bg left:33%](image.jpg)         # Position on left, take 33% width
![bg right:40%](image.jpg)        # Position on right, take 40% width
![bg auto](image.jpg)             # Original size
![bg opacity:0.3](image.jpg)      # Semi-transparent background
![bg cover opacity:0.3](image.jpg)# Combine multiple attributes
```

**Tip:** Use `opacity` to overlay text on background images without losing readability.

**Reference:** https://marpit.marp.app/image-syntax

## Styling

### Global Styles (Front Matter)

Define CSS that applies to all slides. Marpit converts `<style>` blocks into theme CSS:

```yaml
---
theme: gaia
style: |
  section {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
  }
  h1 {
    color: #0066cc;
  }
---
```

Or use raw `<style>` block in Markdown:

```html
<style>
section {
  background: yellow;
}
</style>
```

### Scoped Styles (Slide-Specific)

Use `<style scoped>` to style only the current slide:

```html
<style scoped>
section {
  color: blue;
}
h1 {
  text-align: center;
}
</style>
```

**Tip:** Scoped styles are useful for creating unique layouts or visual treatments on specific slides without affecting others.

## Classes and Class-Based Styling

Apply CSS classes to slides to create reusable designs:

**Define in front matter:**

```yaml
---
theme: gaia
style: |
  section.lead h1 {
    text-align: center;
    font-size: 3em;
  }
  section.highlight {
    background-color: #fff3cd;
  }
---
```

**Apply to slides:**

```html
<!-- _class: lead -->
# Title Slide

<!-- _class: highlight -->
# Important Content
```

The class directive changes the `class` attribute of the `<section>` element, allowing targeted CSS styling.

**Tip:** Combine multiple design patterns with well-named classes for consistency.

## Fragmented Lists

Make list items appear one-by-one during HTML presentations (not PDF):

**Unordered list fragmentation** – Use `*` instead of `-`:

```markdown
* One
* Two
* Three
```

**Ordered list fragmentation** – Use `)` instead of `.`:

```markdown
1) One
2) Two
3) Three
```

**Tip:** Fragmentation only works in browser presentations. Use for engaging slideshows.

## Layout Patterns

### Two-Column Flexbox Layout

```html
<div style="display: flex; gap: 20px;">
  <div style="flex: 0.5;">
  
### Left Column
Content here
  
  </div>
  <div style="flex: 1;">
  
### Right Column
More content
  
  </div>
</div>
```

Use `flex` values to control width ratios. `flex: 0.5` = 33%, `flex: 1` = 66%.


## Background Directives Reference

Control slide appearance:

| Directive | Type | Example |
|-----------|------|---------|
| `backgroundImage` | URL/gradient | `"./image.jpg"` or `"linear-gradient(to bottom, #67b8e3, #0288d1)"` |
| `backgroundColor` | Color | `"#ffffff"` or `"rgb(255,0,0)"` |
| `backgroundPosition` | Position | `"center"` (default), `"left"`, `"right"` |
| `backgroundRepeat` | Repeat | `"no-repeat"` (default), `"repeat"`, `"repeat-x"` |
| `backgroundSize` | Size | `"cover"` (default), `"contain"`, `"100px 50px"` |
| `color` | Text color | `"#333333"` |

Apply as directives:

```html
<!-- _backgroundImage: "linear-gradient(to bottom, #67b8e3, #0288d1)" -->
<!-- _backgroundColor: "#ffffff" -->
<!-- _color: "#000" -->
```

**Tip:** Use `_` prefix to apply only to current slide.

## Viewing and exporting slides with VS Code

- With the Marp extensions you can:
  - Preview slides in VS Code real-time
  - Export slides to PDF, PPTX, or HTML with the command `markdown.marp.export`

### Export with the Marp CLI

Use `npx @marp-team/marp-cli` if the `marp` command is not installed.

```bash
# HTML (no browser engine needed)
marp slides/slides.md --allow-local-files --theme-set slides/theme/ost.css

# PDF / PPTX (requires a browser: Chrome, Edge, or Firefox)
marp slides/slides.md --allow-local-files --theme-set slides/theme/ost.css --pdf
marp slides/slides.md --allow-local-files --theme-set slides/theme/ost.css --pptx
```

Flags:

- `-o` – specify output file name. The extension determines the output format (HTML, PDF, PPTX), e.g. `-o slides/slides.pdf`. If used, do not pass `--pdf` or `--pptx` as well to avoid confusion.
- `--allow-local-files` – load local images (backgrounds, logo); use only with trusted Markdown
- `--theme-set slides/theme/ost.css` – register a custom theme so the front-matter `theme: ost` directive resolves
- `-w, --watch` – re-export on every change
- `--images [png|jpeg]` – export **one image file per slide** (`stem.001.png`, `stem.002.png`, …); image export only, never combine with PDF/PPTX output
- `--image [png|jpeg]` – export only the first (title) slide as one image, e.g. for Open Graph
- `--image-scale <n>` – scale factor for rendered images (default 1; 2 for PPTX). Raise it for high-resolution output, e.g. `--image-scale 2` for a @2x title slide
- `--pdf-notes` – add PDF note annotations to the lower left when the slide page has [Marpit presenter notes](https://marpit.marp.app/usage?id=presenter-notes)
- `--pdf-outlines` – add PDF outlines/bookmarks
- `--notes` – export presenter notes as a text file (also: `-o output.txt`)
- `--pptx-editable` (experimental) – generate an editable PPTX (needs LibreOffice Impress; lower fidelity, no presenter notes)
- `--server` / `-s <dir>` – serve a directory over HTTP; converted PDF/PPTX/images available by appending a query string, e.g. `http://localhost:8080/deck.md?pdf`
- `--preview` / `-p` – open a preview window immediately after conversion (watch mode auto-enabled)
- `--browser` – choose the browser for conversion, e.g. `--browser firefox` (or comma-separated, first available is used; default `auto`)
- `--browser-path` – explicitly specify the path to a browser executable not found automatically

### Agent preview (how an agent can see rendered slides)

The in-editor Marp preview is a VS Code webview that agents cannot see. The standard approach is to render a standalone HTML file and inspect it in the browser:

1. Export to standalone HTML (include `--theme-set` for custom themes, `--allow-local-files` for local images):

```bash
marp slides/slides.md --allow-local-files --theme-set slides/theme/ost.css -o slides/slides.html
```

2. Open the generated HTML file in the integrated browser (e.g. `file:///.../slides/slides.html`)
3. Navigate to a specific slide by appending its number as a URL hash: `slides.html#7`
4. Verify with a **screenshot** of the slide and/or by inspecting the DOM (e.g. check that the expected elements/classes are present and the CSS is embedded in the HTML)
5. Repeat for every slide that was touched; the screenshot is the ground truth for visual checks

## Further Help

Check the documentation (https://github.com/marp-team/marp-cli/blob/main/README.md) if you are stuck, need a full overview, or need information on topics not covered here, such as how to swap the conversion engine (e.g. pure Marpit or custom engines), how to configure the CLI project-wide (config files, `package.json`), choosing the HTML template for the exported deck, setting deck metadata (title, author, description), and using the official Docker image or standalone binaries.
