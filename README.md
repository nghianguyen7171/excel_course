# Data Analysis with Excel - Course Website

This is the GitHub Pages website for the **Data Analysis with Excel** course at National Economics University, Faculty of Data Science and Artificial Intelligence.

## Overview

This website presents the complete course syllabus in a modern, accessible format. The site is built using Jekyll and is designed to be deployed on GitHub Pages.

## Features

- **Modern Design:** Clean, academic aesthetic inspired by MIT and Coursera course pages
- **Responsive Layout:** Works seamlessly on desktop, tablet, and mobile devices
- **Easy Navigation:** Sticky header with smooth scrolling to sections
- **Accessible:** WCAG compliant with proper semantic HTML
- **Fast Loading:** Optimized images and minimal JavaScript

## Site Structure

```
excel_course_site/
├── _config.yml          # Jekyll configuration
├── _layouts/            # Page layouts
│   └── default.html     # Main layout template
├── _includes/           # Reusable components
│   ├── header.html      # Site header with navigation
│   └── footer.html      # Site footer
├── assets/              # Static assets
│   ├── css/            # Stylesheets
│   │   ├── main.scss   # Main styles
│   │   └── variables.scss # CSS variables
│   ├── js/             # JavaScript files
│   │   └── main.js     # Site interactivity
│   └── images/         # Images
│       ├── bg_img.png  # Background image
│       ├── NEU logo.png
│       ├── FDA logo.png
│       └── bai.png
├── index.md            # Main course page
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Local Development

To run this site locally with Jekyll:

1. **Install Jekyll and dependencies:**
   ```bash
   gem install bundler jekyll
   ```

2. **Install dependencies:**
   ```bash
   bundle install
   ```

3. **Run the development server:**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site:**
   Open [http://localhost:4000](http://localhost:4000) in your browser

## Deployment to GitHub Pages

1. **Create a new repository** on GitHub (e.g., `excel_course`)

2. **Push the site files:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/nghianguyen7171/excel_course.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings
   - Navigate to Pages section
   - Select source branch (usually `main`)
   - Select folder (`/ (root)`)
   - Click Save

4. **Access your site:**
   The site will be available at: `https://nghianguyen7171.github.io/excel_course/`

## Customization

### Updating Content

Edit `index.md` to update course content. The file uses Markdown syntax with Jekyll front matter.

### Changing Colors/Theme

Edit `assets/css/variables.scss` to modify color scheme, fonts, and spacing.

### Adding Sections

Add new sections to `index.md` and update navigation in `_includes/header.html`.

## Course Information

- **Course:** Data Analysis with Excel
- **Instructor:** Dr. Trong-Nghia Nguyen
- **Email:** nghiant@neu.edu.vn
- **Website:** https://nghianguyen7171.github.io/
- **University:** National Economics University
- **Department:** Faculty of Data Science and Artificial Intelligence

## License

This course website is for educational purposes at National Economics University.

## Support

For issues or questions about the website, please contact the course instructor.

---

**Last Updated:** November 2025

