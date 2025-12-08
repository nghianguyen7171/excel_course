# Backup Context - Data Analysis with Spreadsheet Program Course Website

This file documents the current state, configuration, and important information about the Jekyll-based GitHub Pages website for the Data Analysis with Spreadsheet Program course.

## Project Overview

**Course:** Data Analysis with Spreadsheet Program  
**Institution:** National Economics University  
**Faculty:** Faculty of Data Science and Artificial Intelligence, College of Technology  
**Instructor:** Dr. Trong-Nghia Nguyen  
**Website URL:** https://nghianguyen7171.github.io/excel_course/  
**Repository:** https://github.com/nghianguyen7171/excel_course.git

## Technical Stack

- **Static Site Generator:** Jekyll
- **Hosting:** GitHub Pages
- **Markdown Processor:** Kramdown
- **CSS Preprocessor:** SCSS (Sass)
- **Base URL:** `/excel_course`
- **Full URL:** `https://nghianguyen7171.github.io`

## File Structure

```
excel_course_site/
├── _config.yml                 # Jekyll configuration
├── _layouts/
│   └── default.html            # Main page layout
├── _includes/
│   ├── header.html             # Site header with navigation and logos
│   └── footer.html             # Site footer
├── assets/
│   ├── css/
│   │   └── main.scss           # Main stylesheet (compiled to main.css)
│   ├── js/
│   │   └── main.js             # JavaScript for interactivity
│   └── images/
│       ├── bg_img.png          # Background image
│       ├── NEU logo.png        # National Economics University logo
│       ├── FDA logo.png        # Faculty of Data Science and AI logo
│       ├── bai.png             # BAI Lab logo
│       └── instructor_profile.png  # Instructor profile picture
├── index.md                    # Main course page content
├── .gitignore                  # Git ignore rules
├── Gemfile                     # Ruby gem dependencies
└── README.md                   # Project documentation
```

## Key Configuration Settings

### Jekyll Configuration (_config.yml)

- **Base URL:** `/excel_course` (important for GitHub Pages subfolder deployment)
- **Markdown:** Kramdown with GFM input
- **HTML Parsing:** `parse_block_html: true`, `parse_span_html: true`
- **Plugins:** jekyll-feed, jekyll-sitemap, jekyll-relative-links, jekyll-default-layout, jekyll-optional-front-matter, jekyll-titles-from-headings
- **No Theme:** Using custom layouts

### Important Paths

- **CSS:** `{{ site.baseurl }}/assets/css/main.css`
- **JavaScript:** `{{ site.baseurl }}/assets/js/main.js`
- **Images:** `{{ site.baseurl }}/assets/images/`
- **Background Image:** `url('../images/bg_img.png')` (relative path in SCSS)

## Design Features

### Color Scheme
- Primary Blue: `#1e3a8a`
- Secondary Blue: `#3b82f6`
- Background overlays with transparency to show background image
- Alternating section backgrounds (light/dark)

### Typography
- Headings: Crimson Text (serif)
- Body: Inter (sans-serif)

### Layout Features
- Hero section with gradient background
- Sticky navigation header
- Responsive design (mobile-first)
- Table wrapper with horizontal scrolling for wide schedule tables
- Instructor profile section with circular image
- Alternating section backgrounds

## Critical Fixes Applied

### 1. Base URL Configuration
- Set `baseurl: "/excel_course"` in `_config.yml`
- Updated all asset paths to use `{{ site.baseurl }}`
- Fixed background image path in SCSS (relative path)

### 2. Markdown Processing
- Removed `minima` theme to prevent conflicts
- Enabled HTML block parsing in Kramdown
- Used `parse_block_html: true` for HTML in markdown

### 3. Table Overflow Fixes
- Wrapped wide schedule tables in `.table-wrapper` divs
- Added horizontal scrolling with styled scrollbar
- Set overflow controls on containers

### 4. Background Image Visibility
- Reduced overlay opacity: `rgba(255, 255, 255, 0.4)` for body
- Reduced page wrapper opacity: `rgba(255, 255, 255, 0.5)`
- Added backdrop-filter for glass effect

## Content Structure

### Main Sections (index.md)
1. General Information
2. Department and Instructors (with instructor profile image)
3. Course Description
4. Learning Resources (with online links)
5. Course Goals & Learning Outcomes
6. Course Assessment
7. Three-Phase Course Structure & 15-Week Schedule
8. Weekly Schedule & Contact Hours
9. Course Policies
10. Learning Support & Resources
11. Required Technical Setup
12. Final Project Overview
13. Key Learning Competencies by Phase
14. Course Contacts & Resources
15. Syllabus Policies & Disclaimers

## Deployment Information

### GitHub Pages Setup
- **Repository:** https://github.com/nghianguyen7171/excel_course.git
- **Branch:** main
- **Deployment:** Automatic via GitHub Pages
- **Build Time:** ~1-2 minutes after push

### Local Development
```bash
cd excel_course_site
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000/excel_course/
```

## Image Assets

### Logos (Priority Order)
1. NEU logo.png (55px height desktop, 45px mobile)
2. FDA logo.png (50px height desktop, 40px mobile)
3. bai.png (65px height desktop, 55px mobile)

### Background
- bg_img.png - Used as page background with overlay

### Instructor Profile
- instructor_profile.png - Circular profile picture (200px desktop, 150px mobile)
- Object position: `center top` for better framing

## CSS Key Features

### Responsive Breakpoints
- Small: 640px
- Medium: 768px
- Large: 1024px
- XL: 1280px

### Important Styles
- Alternating section backgrounds using `nth-of-type(odd/even)`
- Table wrapper with horizontal scroll
- Instructor profile flex layout
- Navigation with `white-space: nowrap` to prevent text wrapping

## Known Issues & Solutions

### Issue: Tables Overflowing
**Solution:** Wrapped tables in `.table-wrapper` div with horizontal scrolling

### Issue: Background Image Not Visible
**Solution:** Reduced overlay opacity and added backdrop-filter

### Issue: HTML Not Rendering in Markdown
**Solution:** Enabled `parse_block_html: true` in Kramdown config

### Issue: CSS/Images Not Loading
**Solution:** Fixed `baseurl` configuration and asset paths

## Maintenance Notes

- SCSS is compiled to CSS by Jekyll automatically
- Images should be placed in `assets/images/`
- All links use `{{ site.baseurl }}` for correct GitHub Pages paths
- Section IDs are used for navigation anchor links
- Tables with many columns use `.table-wrapper` for scrolling

## Contact Information

**Instructor:** Dr. Trong-Nghia Nguyen  
**Email:** nghiant@neu.edu.vn  
**Website:** https://nghianguyen7171.github.io/  
**Office:** Room 1613, Building A1, National Economics University  
**Department:** Faculty of Data Science and Artificial Intelligence, College of Technology, National Economics University

---

**Last Updated:** November 2025  
**Jekyll Version:** GitHub Pages compatible  
**Browser Compatibility:** Chrome, Firefox, Safari, Edge (modern versions)

