# Data Analysis with Spreadsheet Program - Course Website

This is the GitHub Pages website for the **Data Analysis with Spreadsheet Program** course at National Economics University, Faculty of Data Science and Artificial Intelligence.

## Overview

This website presents the complete course syllabus in a modern, accessible format. The site is built using Jekyll and is designed to be deployed on GitHub Pages.

**Live Website:** https://nghianguyen7171.github.io/excel_course/

## Features

- **Modern Design:** Clean, academic aesthetic inspired by MIT and Coursera course pages
- **Responsive Layout:** Works seamlessly on desktop, tablet, and mobile devices
- **Easy Navigation:** Sticky header with smooth scrolling to sections
- **Visual Design:** Alternating section backgrounds, instructor profile with image, styled tables
- **Accessible:** WCAG compliant with proper semantic HTML
- **Fast Loading:** Optimized images and minimal JavaScript
- **Background Image:** Custom background with transparent overlays for visual appeal

## Site Structure

```
excel_course_site/
├── _config.yml          # Jekyll configuration
├── _layouts/            # Page layouts
│   └── default.html     # Main layout template
├── _includes/           # Reusable components
│   ├── header.html      # Site header with navigation and logos
│   └── footer.html      # Site footer
├── assets/              # Static assets
│   ├── css/            # Stylesheets
│   │   └── main.scss   # Main styles (compiled to main.css)
│   ├── js/             # JavaScript files
│   │   └── main.js     # Site interactivity (smooth scroll, mobile menu)
│   └── images/         # Images
│       ├── bg_img.png  # Background image
│       ├── NEU logo.png
│       ├── FDA logo.png
│       ├── bai.png
│       └── instructor_profile.png
├── index.md            # Main course page
├── BACKUP-CONTEXT.md   # Detailed project documentation and context
├── .gitignore          # Git ignore rules
├── Gemfile             # Ruby gem dependencies
└── README.md           # This file
```

## Quick Start

### Local Development

1. **Install Jekyll and dependencies:**
   ```bash
   gem install bundler jekyll
   ```

2. **Navigate to project directory:**
   ```bash
   cd excel_course_site
   ```

3. **Install dependencies:**
   ```bash
   bundle install
   ```

4. **Run the development server:**
   ```bash
   bundle exec jekyll serve
   ```

5. **View the site:**
   Open [http://localhost:4000/excel_course/](http://localhost:4000/excel_course/) in your browser

**Note:** The base URL `/excel_course` is important for local testing to match production.

### View Lab 2 Instructions locally (standalone HTML)

The **Lab-2-Dataset** folder (see `student desk/Lab-2-Dataset/`) contains:

- **Lab-2-Instructions-WithKeys.html** — instructions with answer keys (for instructors / self-check).
- **Lab-2-Instructions-NoKeys.html** — student version without answer keys.

Open either HTML file in your browser. The page loads CSS from the deployed site; use the dataset files in the same folder for offline work.

## Deployment to GitHub Pages

This site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

### Repository Information

- **Repository:** https://github.com/nghianguyen7171/excel_course.git
- **Live URL:** https://nghianguyen7171.github.io/excel_course/
- **Branch:** main

### Manual Deployment Steps

1. **Push changes to GitHub:**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. **Wait for GitHub Pages build** (usually 1-2 minutes)

3. **Verify deployment:**
   - Check repository Settings > Pages for build status
   - Visit the live website URL

## Configuration

### Key Settings (_config.yml)

- **Base URL:** `/excel_course` (required for GitHub Pages subfolder)
- **Markdown Processor:** Kramdown with HTML block parsing enabled
- **Theme:** None (using custom layouts)
- **Plugins:** jekyll-feed, jekyll-sitemap, jekyll-relative-links

### Important Notes

- All asset paths use `{{ site.baseurl }}` for correct GitHub Pages deployment
- Background image uses relative path in SCSS (compiled by Jekyll)
- HTML blocks in markdown are processed correctly with `parse_block_html: true`

## Customization

### Updating Content

Edit `index.md` to update course content. The file uses Markdown syntax with Jekyll front matter.

### Changing Styles

Edit `assets/css/main.scss` to modify:
- Colors (defined as SCSS variables at the top)
- Typography
- Spacing and layout
- Responsive breakpoints

### Adding Images

Place images in `assets/images/` and reference them using:
```markdown
![Alt text]({{ site.baseurl }}/assets/images/your-image.png)
```

Or in HTML:
```html
<img src="{{ site.baseurl }}/assets/images/your-image.png" alt="Description">
```

### Adding Sections

1. Add content to `index.md` within a `<section id="section-name">` tag
2. Update navigation in `_includes/header.html` if needed
3. Section backgrounds automatically alternate (odd/even)

## Course Information

- **Course:** Data Analysis with Spreadsheet Program
- **Instructor:** Dr. Trong-Nghia Nguyen
- **Email:** nghiant@neu.edu.vn
- **Website:** https://nghianguyen7171.github.io/
- **Office:** Room 1613, Building A1, National Economics University
- **Department:** Faculty of Data Science and Artificial Intelligence, College of Technology, National Economics University

## Design Features

### Visual Elements

- **Background Image:** Custom background with transparent overlays
- **Section Alternation:** Light and dark alternating backgrounds
- **Hero Section:** Gradient blue header with course title
- **Instructor Profile:** Circular image with contact details
- **Table Wrappers:** Horizontal scrolling for wide schedule tables
- **Navigation:** Sticky header with smooth scroll links

### Responsive Design

- Mobile-first approach
- Breakpoints at 640px, 768px, 1024px, 1280px
- Responsive navigation (hamburger menu on mobile)
- Flexible layouts that adapt to screen size

## Technical Details

### Dependencies

- Jekyll (GitHub Pages compatible version)
- Kramdown (markdown processor)
- SCSS (CSS preprocessor)

### Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge (modern versions)

## Troubleshooting

### Assets Not Loading

- Verify `baseurl: "/excel_course"` in `_config.yml`
- Check that asset paths use `{{ site.baseurl }}`
- Ensure GitHub Pages build completed successfully

### Tables Overflowing

- Wide tables are wrapped in `<div class="table-wrapper">` for horizontal scrolling
- Check that wrapper CSS is applied correctly

### Background Image Not Visible

- Overlay opacity is set to 0.4 for body, 0.5 for page wrapper
- Adjust opacity values in `main.scss` if needed

### Markdown Not Rendering

- Ensure `layout: default` is in page front matter
- Check that `parse_block_html: true` is set in `_config.yml`

## Documentation

For detailed technical documentation, configuration details, and backup information, see:
- **BACKUP-CONTEXT.md** - Comprehensive project documentation

## Support

For issues or questions about the website:
- **Course Instructor:** Dr. Trong-Nghia Nguyen (nghiant@neu.edu.vn)
- **Technical Issues:** Check GitHub repository issues

## License

This course website is for educational purposes at National Economics University.

---

**Last Updated:** November 2025  
**Version:** 1.0  
**Maintained by:** Dr. Trong-Nghia Nguyen
