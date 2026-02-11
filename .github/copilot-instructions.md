# Copilot Instructions for YALI IT Website

## Project Overview
This is a static HTML website for YALI IT, a managed IT and cybersecurity services company. The site consists of multiple standalone HTML pages with shared CSS and JavaScript assets.

## Architecture
- **Structure**: Each page (index.html, about.html, services.html, contact.html, privacy.html, terms.html) is a separate HTML file in the root directory.
- **Assets**: Shared styles in `assets/style.css` and scripts in `assets/script.js`.
- **Navigation**: Consistent header navigation across all pages linking to each other.

## Key Patterns
- **Styling**: Uses CSS custom properties (variables) defined in `:root` for colors like `--accent`, `--bg`, `--muted`, `--surface`.
- **Layout**: `.container` class for max-width centering (1100px), padding 28px.
- **Logo**: "YALI<span class="dot">IT</span>" with `.dot` class for accent color on "IT".
- **Forms**: Contact form in `contact.html` uses `onsubmit="return submitForm(event)"` which prevents default and shows a thank you message.
- **Responsive**: Media query at 800px breakpoint for mobile adjustments.

## Development Workflow
- No build process required; edit HTML/CSS/JS directly.
- View changes by opening HTML files in a browser.
- No dependencies or package managers.

## Conventions
- Class names: Use kebab-case (e.g., `site-header`, `contact-form`).
- HTML structure: `<header>`, `<main>`, `<footer>` with `.container` inside.
- Links: Relative paths for navigation (e.g., `href="services.html"`).

## Examples
- Adding a new page: Copy structure from `about.html`, update title, content, and nav links.
- Styling: Define new colors in `:root` and use variables in selectors.